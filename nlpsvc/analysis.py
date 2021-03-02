import time
import pymysql
import requests
from itertools import groupby
from multiprocessing import Process

# 提取待分析新闻id
# sql = 'SELECT id FROM nlp_news_feed x where tim >= %s and tim < %s and dupid is null'
# sql = "select distinct(oid) from news.nlp_news_event where upt >= %s and upt <= %s and event_code = ''"
# sql = "select a.id from news.nlp_news_feed a where txt_type = 1 and id >= 6282570 and id <= 9005088  order by a.id"
# sql = "select  f.id from nlp_news_feed  f inner join nlp_news_additional a on f.id = a.oid and a.is_stock_review = 0 and f.id >= 24175088  and f.id <= 24375088"
sql = "select distinct id from nlp_news_feed where txt_type  = 1 and dupid is null and id >=  24200186 and id <= 24400186;"
# sql = "select distinct id from nlp_news_feed where txt_type  = 1 and dupid is null and id >=  24400186 and id <= 24700186;"
# sql = "select distinct id from nlp_news_feed where txt_type  = 1 and dupid is null and id >=  24700186 and id <= 24900186;"
# sql = "select distinct id from nlp_news_feed where txt_type  = 1 and dupid is null and id >=  24900186 and id <= 25110250;"

# 分析接口地址
url_analysis = 'http://192.168.251.22:9081/csf/nlp-news/api/v1/nlp/analysis/'
url_re_analysis = 'http://192.168.251.22:9081/csf/nlp-news/api/v1/nlp/re-analysis/'
# 需分析的算法
# url_json = {"algoList": ["match_company_full"]}
url_json = {"algoList": ["match_event", "match_event_entity"]}
# 新闻数据库
# conn = pymysql.connect(host='192.168.250.200', user='news_user', passwd="chinascope1234", db='jl_news')
conn = pymysql.connect(host='192.168.251.95', user='read_only_user', passwd="read_only_user321@!", db='news')
# 进程数
process_size = 5
is_re_analysis = True
analysis_header = {'Content-Type': 'application/json',
                   'X-Company-Scope': 'full',
                   'Authorization': 'eyJhbGciOiJIUzI1NiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWyiwuVrJSSi5O083LKSguS1bSUcpMLFGyMjQzMDIxt7QwNtNRSq0ogApYGJuABEqLU4vyEnNTgTrzUsuL45OLEstzUoviC4ryU5RqASHVkJhVAAAA.zZ23DhFloJ-6GueW846nPuhwJ8e-8e67UDKenlWG-hU'
                   }


# 提取新闻id
def fetch_news_ids(df, dt):
    cur = conn.cursor()
    # cur.execute(sql, args=(df, dt))
    cur.execute(sql)
    try:
        return [i[0] for i in cur]
    except Exception as e:
        print(str(e))
    cur.close()


# 取余函数
def projection(val):
    return val % process_size


# 调用分析接口
def process(m, ids):
    print("process num [{}] ids size [{}], ids: [{}]".format(m, len(ids), ids))
    for news_id in ids:
        if is_re_analysis:
            rs = requests.post(url_re_analysis + str(news_id), json=url_json, headers=analysis_header)
            print(rs.text)
        else:
            rs = requests.post(url_analysis + str(news_id), headers=analysis_header)
            print(rs.text)


# 按日期提取新闻,再按进程数分组id列表
def analysis_by_dates(df, dt):
    ids = fetch_news_ids(df, dt)
    print("find news id size: ", len(ids))
    x_sorted = sorted(ids, key=projection)
    x_grouped = [list(it) for k, it in groupby(x_sorted, projection)]
    print('grouped size: ', len(x_grouped))
    processes = []
    for m in range(0, process_size):
        n = m + 1
        p = Process(target=process, args=(n, x_grouped[m]))
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


if __name__ == '__main__':
    # analysis_by_dates('2020-02-03', '2020-02-08')
    analysis_by_dates('2020-07-01 15:50:00', '2020-07-01 16:52:00')
    # analysis_by_year(2018)
    # process(0, [15888801])
    conn.close()
