import mysql.connector
import datetime

from mysql.connector import Error

#pycharm

try:
    connection = mysql.connector.connect(
        host='192.168.251.170',
        port=3306,
        user='pandora',
        password='pandora!@#',
        database='jd_company'
    )

    start_day = datetime.date.today() - datetime.timedelta(days=30)

    cursor = connection.cursor()
    table_name = "t_company_sam_region"
    min_max_sql = "select csfid from t_company_sam_region limit 10 "
    print(min_max_sql)
    cursor.execute(min_max_sql)
    result = cursor.fetchone()
    print("Connect SQL Success.")

except Error as e:
    print("Error reading data from Mysql.", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()

    print("Mysql Connection is closed. Time: ", datetime.datetime.now())
