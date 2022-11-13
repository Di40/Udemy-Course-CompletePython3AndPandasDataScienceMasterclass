import pymysql

db = pymysql.connect(host="localhost",
                     user="testuser",
                     password="test123",
                     db="sakila")
cursor = db.cursor()
try:
    sql = """CREATE TABLE NEWTESTTABLE (FIRST_NAME CHAR(20) NOT NULL,
                                        LAST_NAME  CHAR(20) NOT NULL,
                                        AGE INT,
                                        SEX CHAR(1),
                                        INCOME FLOAT)"""
    cursor.execute(sql)
    print("The table was created successfully.")
except:
    print("The table already exists in the database.")

db.close()
