import mysql.connector
import datetime
import demjson
import pykafka
import time
from mysql.connector import Error


try:
    connection = mysql.connector.connect(
        host='192.168.250.200',
        port=3306,
        user='readonly',
        password='chinascope1234',
        database='crawler_storage_government'
    )

    # topic_name = "qa_goverment_news_topic";
    cursor = connection.cursor()
    # print("Before Get Data : ", datetime.datetime.now())
    sql = "select title, author, content, cate, url, ct, dt, jobcode, id, createdate from crawler_news where createdate < '2020-08-25' and createdate > '2020-03-01' order by createdate limit {},{}"
    start_index = 10
    batch_size = 7000
    total_size = 429500
    total_count = 10

    while  start_index < total_size:
        print("start_index : {}, end_index : {}".format(start_index, start_index + batch_size))

        cursor.execute(sql.format(start_index, batch_size))
        result = cursor.fetchall()
        # print("After Get Data : {}, Size : {}".format(datetime.datetime.now(), len(result)))

        mqclient = pykafka.KafkaClient("192.168.250.203:9092,192.168.250.204:9092,192.168.250.205:9092")
        topic = mqclient.topics[b"qa_goverment_news_topic"]
        producer = topic.get_producer()
        count = 0

        for i in result:

            total_count += 1
            count += 1

            item = {}
            item['title'] = i[0]
            item['author'] = i[1]
            item['content'] = i[2]
            item['cate'] = i[3]
            item["url"] = str(i[4])
            item['ct'] = i[5]
            item['dt'] = i[6]
            item['jobCode'] = i[7]
            item['id'] = i[8]
            item['createdate'] = i[9].strftime("%Y-%m-%dT%H:%M:%S")

            # print(item)

            if count % 200 == 0:
                time.sleep(10)
                print("Current Count : {}, Time : {}".format(total_count, datetime.datetime.now()))

            producer.produce(demjson.encode([item], encoding="UTF-8"))
        start_index = start_index + batch_size

    print("Total Count : ", count)

except Error as e:
    print("Error reading data from Mysql.", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()

    producer.stop()
    print("Mysql Connection is closed. Time: ", datetime.datetime.now())



