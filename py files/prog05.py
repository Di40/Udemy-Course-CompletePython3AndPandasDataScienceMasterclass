import pymysql

db = pymysql.connect(host="localhost",
                     user="testuser",
                     password="test123",
                     database="sakila")
cursor = db.cursor()

sql = "UPDATE NEWTESTTABLE SET INCOME = INCOME + 500 WHERE SEX = '%c'" % ('M')
#sql = "UPDATE NEWTESTTABLE SET INCOME = INCOME + 500 WHERE SEX = 'F' OR SEX = 'M'"
try:
    cursor.execute(sql)
    db.commit()
    print("Table records were updated successfully.")
except:
    db.rollback()
    print("No table records were updated.")
    
db.close()
