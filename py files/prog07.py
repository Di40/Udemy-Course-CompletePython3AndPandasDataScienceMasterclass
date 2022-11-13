import pymysql

db = pymysql.connect(host="localhost",
                     user="testuser",
                     password="test123",
                     database="sakila")
cursor = db.cursor()

sql = "DROP TABLE TESTTABLE"

try:
    cursor.execute(sql)
    print("Table was dropped/deleted.")
except:
    print("Table could not be dropped/deleted. The object doesn't exist.")
    
db.close()
