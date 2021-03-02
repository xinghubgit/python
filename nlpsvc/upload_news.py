import datetime
import pandas as pd
import mysql
import requests
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='192.168.250.200',
        port=3306,
        user='news_user',
        password='chinascope1234',
        database='news'
    )

    df = pd.read_excel(r'D:\github\test.xlsx')  # place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    print(df)




except Error as e:
    print("Error reading data from Mysql.", e)
finally:
    if connection.is_connected():
        connection.close()
        # cursor.close()

    print("Mysql Connection is closed. Time: ", datetime.datetime.now())
