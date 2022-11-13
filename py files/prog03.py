import pymysql

db = pymysql.connect(host="localhost",
                     user="testuser",
                     password="test123",
                     database="sakila")
cursor = db.cursor()
sql1 = """INSERT INTO NEWTESTTABLE
          (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
           VALUES ('Dejan', 'Dichoski', '24', 'M', '700')"""
sql2 = """INSERT INTO NEWTESTTABLE
          (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
          VALUES ('Emilija', 'Dichoska', '26', 'F', '3000')"""
try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    db.commit()
    print("Insert into table was successfull.")
except:
    db.rollback()
    print("Insert into table failed.")
    
db.close()
