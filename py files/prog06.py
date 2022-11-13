import pymysql

db = pymysql.connect(host="localhost",
                     user="testuser",
                     password="test123",
                     database="sakila")
cursor = db.cursor()

sql1 = """INSERT INTO NEWTESTTABLE
          (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
           VALUES ('Dejan', 'Dichoski', '24', 'K', '1000')"""

sql2 = "DELETE FROM NEWTESTTABLE WHERE SEX = '%c'" % ('K')
#sql2 = "DELETE FROM NEWTESTTABLE" # deletes all entries

try:
    try:
        cursor.execute(sql1)
        db.commit()
        print('Table record inserted.')
    except:
        db.rollback()
        print('Table record not inserted.')      
    cursor.execute(sql2)
    db.commit()
    print("Table records were deleted successfully.")
except:
    db.rollback()
    print("No table records were deleted.")
    
db.close()
