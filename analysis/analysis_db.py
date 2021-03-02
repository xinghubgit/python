import time
import pymysql
import requests
from itertools import groupby
from multiprocessing import Process
from datetime import datetime
from functools import wraps
import configparser

# 进程数
process_size = 2

class SK:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.token_url = "{url}/csf/nlp-news/public/users/login"
        self.upload_url = "{url}/csf/nlp-news/api/v1/news/"
        self.analysis_url = "{url}/csf/nlp-news/api/v1/nlp/analysis/{newsId}"
        self.re_analysis_url = "{url}/csf/nlp-news/api/v1/nlp/re-analysis/{newsId}"
        self.token = ""
        self.time_format = '%Y-%m-%d %H:%M:%S'

    def get_token(self):
        params = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(self.token_url.format(url=self.url), params)
        print("{time} token={token}".format(time=self.get_time(), token=response.text))
        self.token = response.text

    def upload(self, content, title="None", news_ts=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")):
        body = {
            "newsTitle": title,
            "newsTs": news_ts,
            "newsUrl": self.upload_url.format(url=self.url),
            "newsContent": content,
            "txtType": 1
        }
        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token
        }
        response = requests.post(self.upload_url, headers=header, data=json.dumps(body))
        if response.status_code == 401:
            self.get_token()
            response = requests.post(self.upload_url, headers=header, data=json.dumps(body))
        print(response.text)
        return json.loads(response.text)["newsId"]

    def analysis(self, news_id):
        header = {
            "Content-Type": "application/json",
            "X-Company-Scope": "full",
            "Authorization": "Bearer " + self.token
        }
        print("{time} start analysis newsId={newsId}".format(time=self.get_time(), newsId=news_id))
        response = requests.post(self.analysis_url.format(url=self.url, newsId=news_id), headers=header)
        if response.status_code == 401:
            self.get_token()
            response = requests.post(self.analysis_url.format(url=self.url, newsId=news_id), headers=header)

        if response.status_code == 200:
            print("{time} finish analysis success newsId={newsId}".format(time=self.get_time(), newsId=news_id))
        else:
            print("{time} finish analysis fail newsId={newsId}, statusCode={statusCode}".format(time=self.get_time(), newsId=news_id, statusCode=response.status_code))
        return response.text

    def re_analysis(self, news_id, data):
        header = {
            "Content-Type": "application/json",
            "X-Company-Scope": "full",
            "Authorization": "Bearer " + self.token
        }
        print("{time} start reanalysis newsId={newsId}".format(time=self.get_time(), newsId=news_id))
        response = requests.post(self.re_analysis_url.format(url=self.url, newsId=news_id), json=data, headers=header)
        if response.status_code == 401:
            self.get_token()
            response = requests.post(self.re_analysis_url.format(url=self.url, newsId=news_id), json=data, headers=header)

        if response.status_code == 200:
            print("{time} finish reanalysis success newsId={newsId}".format(time=self.get_time(), newsId=news_id))
        else:
            print("{time} finish reanalysis fail newsId={newsId}, statusCode={statusCode}".format(time=self.get_time(), newsId=news_id, statusCode=response.text))

        return response.text

    def get_time(self):
        return datetime.now().strftime(self.time_format)


class NewsProcess:

    def __init__(self, db_host, port, db_username, db_password, db_name):
        self.conn = pymysql.connect(host=db_host, port=port, user=db_username, passwd=db_password, db=db_name)

    def fetch_news_ids(self, news_sql):
        cur = self.conn.cursor()
        cur.execute(news_sql)
        try:
            return [i[0] for i in cur]
        except Exception as e:
            print(str(e))
        cur.close()


# 取余函数
def projection(val):
    return val % process_size


# 调用分析接口
def process(m, ids, sk, data, is_re_analysis):
    print("process num [{}] ids size [{}], ids: [{}]".format(m, len(ids), ids))
    for news_id in ids:
        if news_id == 20537951 or news_id == 20548427:
            continue
        if is_re_analysis:
            rs = sk.re_analysis(news_id, data)
        else:
            rs = sk.analysis(news_id)


# 按日期提取新闻,再按进程数分组id列表
def analysis_by_dates(ids, url, username, password, data, is_re_analsysis=False):
    print("find news id size: ", len(ids))
    x_sorted = sorted(ids, key=projection)
    x_grouped = [list(it) for k, it in groupby(x_sorted, projection)]
    size = len(x_grouped)
    print('grouped size: ', size)
    processes = []
    for m in range(0, size):
        n = m + 1
        sk = SK(url, username, password)
        sk.get_token()
        p = Process(target=process, args=(n, x_grouped[m], sk, data, is_re_analsysis))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


# 按年分析新闻 (1-12月)
def analysis_by_year(year):
    for y in range(1, 13):
        yy = str(y) if y >= 10 else '0' + str(y)
        ym = y + 1
        yym = str(ym) if ym >= 10 else '0' + str(ym)
        df = '%s-%s-01' % (year, yy)
        dt = '%s-%s-01' % (year, yym)
        print(df + " -- " + dt)
        analysis_by_dates(df, dt)


def read_conf():
    file = 'news.conf'
    cf = configparser.ConfigParser()
    cf.read(file)
    news_conf = {}
    news_conf['db_host'] = cf.get("db", "db_host")
    news_conf['db_port'] = int(cf.get('db', 'db_port'))
    news_conf['db_user'] = cf.get("db", "db_user")
    news_conf['db_pass'] = cf.get("db", "db_pass")
    news_conf['db_name'] = cf.get('db', 'db_name')
    news_conf['db_sql'] = cf.get('db', 'db_sql')
    news_conf['min_id'] = int(cf.get('db', 'min_id'))
    news_conf['db_limit'] = int(cf.get('db', 'db_limit'))
    news_conf['news_user'] = cf.get('news', 'db_user')
    news_conf['news_pass'] = cf.get('news', 'db_pass')
    news_conf['news_url'] = cf.get('news', 'analysis_url')
    news_conf['news_algo_list'] = cf.get('news', 'algo_list')
    return news_conf


if __name__ == '__main__':
    conf = read_conf()
    analaysis_url = conf['news_url']
    newsUsername = conf['news_user']
    # 新闻数据库
    newsPassword = conf['news_pass']
    dbHost = conf['db_host']
    dbPort = conf['db_port']
    dbUsername = conf['db_user']
    dbPassword = conf['db_pass']
    dbName = conf['db_name']
    sql = conf['db_sql']
    # 需分析的算法
    algoList = conf['news_algo_list'].split(",")
    url_json = {"algoList": algoList}
    # 是否是重分析
    isReAnalysis = False
    newsProcess = NewsProcess(db_host=dbHost, port=dbPort, db_username=dbUsername, db_password=dbPassword, db_name=dbName)
    # 提取待分析新闻id
    minId = conf['min_id']
    limit = conf['db_limit']
    batch = 0
    while True:
        batch = batch + 1
        new_sql = sql.format(minId=minId, limit=limit)
        print("batch={batch}, new_sql={new_sql}".format(batch=batch, new_sql=new_sql))
        newIds = newsProcess.fetch_news_ids(news_sql=new_sql)
        size = len(newIds)
        if size == 0:
            break
        print("minId={minId}, maxId={maxId}, size={size}".format(minId=newIds[0], maxId=newIds[-1], size=size))
        minId = newIds[-1]
        analysis_by_dates(ids=newIds, url=analaysis_url, username=newsUsername, password=newsPassword, data=url_json, is_re_analsysis=isReAnalysis)
        if size < limit:
            break

