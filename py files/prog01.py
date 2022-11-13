import pymysql

db = pymysql.connect(host="localhost",
                     user="testuser",
                     password="test123",
                     db="sakila")
cursor = db.cursor()

sql = "SELECT VERSION()"

cursor.execute(sql)

data = cursor.fetchone()

print("Database version: %s" % data)

db.close()
