import mysql.connector
import datetime

from mysql.connector import Error


try:
    connection = mysql.connector.connect(
        host='192.168.250.200',
        port=3306,
        user='news_user',
        password='chinascope1234',
        database='news'
    )

    cursor = connection.cursor()
    table_name = "nlp_news_region"
    min_max = "select min(id), max(id), count(id) from {} where id <= 3407496 ".format(table_name)
    cursor.execute(min_max)
    result = cursor.fetchone()
    del_sql = "delete from " + table_name +" where id >= {} and id < {}"

    batch_size = 50000
    min_num = result[0]
    max_num = result[1]
    count = result[2]
    if min_num is None or max_num is None:
        print("Data has already deleted.")
    else:
        start_index = min_num
        end_index = start_index
        print("Min : {}, Max : {}, Count : {}".format(min_num, max_num, count))

        while True:
            if end_index > max_num:
                break
            else:
                end_index = start_index + batch_size
            print("Start_Index : {}, End_Index : {}, Time : {}".format(start_index, end_index, datetime.datetime.now()))

            cursor.execute(del_sql.format(start_index, end_index))
            print(cursor.rowcount)
            start_index = end_index


        connection.commit()

except Error as e:
    print("Error reading data from Mysql.", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()

    print("Mysql Connection is closed. Time: ", datetime.datetime.now())
