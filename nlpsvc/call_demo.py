# coding=utf-8

import json
import requests
from datetime import datetime


class SK:

    def __init__(self):
        self.token_url = "https://service.chinascope.com/csf/nlp-news/public/users/login?username=xxxxusernamexxx&password=xxxpasswordxxx"
        self.upload_url = "https://service.chinascope.com/csf/nlp-news/api/v1/news/"
        self.lookup_url = "https://service.chinascope.com/csf/nlp-news/api/v1/nlp/analysis/${newsId}"

    def get_token(self):
        response = requests.post(self.token_url)
        # print(response)
        print(response.text)
        self.token = response.text

    def upload(self, content, title="None", url="None", time=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")):
        body = {
            "newsTitle": title,
            "newsTs": time,
            "newsUrl": url,
            "newsContent": content
        }
        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token
        }
        response = requests.post(self.upload_url, headers=header, data=json.dumps(body))
        # print(response)
        print(response.text)
        return json.loads(response.text)["newsId"]

    def lookup(self, news_id):
        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token
        }
        # print(header)
        print(self.lookup_url.replace("${newsId}", str(news_id)))
        response = requests.post(self.lookup_url.replace("${newsId}", str(news_id)), headers=header)
        return response.text


if __name__ == "__main__":
    sk = SK()
    sk.get_token()
    title = "方大特钢被执行标的超1800万，欲打造工业旅游新标杆"
    content = '''
    今日16时30分许，方大特钢公司焦化分厂2号高炉在维修中发生气体泄漏，产生燃烧爆炸，造成1死9伤，伤员均已送医治疗。目前，现场救援处置和善后工作正在进行中。

启信宝显示，位于“江西省南昌市青山湖区东郊南钢路”的江西方大钢铁集团有限公司成立于1959年5月5日，法定代表人为黄智华，注册资本达10亿3533万人民币，隶属于辽宁方大集团实业有限公司。

江西方大钢铁集团有限公司投资有方大特钢科技股份有限公司，这是一家上市企业，成立于1999年9月16日，注册资本达14亿4987万人民币，法定代表人为谢飞鸣，并于2003年实现IPO。启信宝股权信息显示，方大特钢科技股份有限公司背后，还有国信证券、中国人寿保险、农业银行、鞍钢集团的持股。

近日，方大特钢宣布要走绿色发展转型升级之路，欲打造特色工业旅游新标杆，启信宝显示，今年1月29日，其经营范围新增“旅游资源开发和经营管理；旅游宣传策划；旅游商品开发销售；景区配套设施建设、运营；景区园林规划、设计及施工；景观游览服务、景区内客运及相关配套服务；旅游文化传播；餐饮服务；停车场服务”。

媒体还报道称方大特钢生产厂区的生态环境“赶上了南昌市艾溪湖湿地公园水平”。

5月13日，方大特钢成为被执行人，执行标的达1821万1908。
    '''
    url = "https://finance.sina.com.cn/roll/2019-05-29/doc-ihvhiqay2096677.shtml"
    news_id = sk.upload(content=content, title=title, url=url)
    # print(news_id)
    result = sk.lookup(news_id)
    jsonResult = json.loads(result)
    print(json.dumps(jsonResult, ensure_ascii=False, indent=4))
