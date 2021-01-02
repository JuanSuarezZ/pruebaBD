import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='sql10.freesqldatabase.com',
                                         user='sql10384747',
                                         passwd='cMluk7p3z6',
                                         db='sql10384747')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select * from proveedor;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)