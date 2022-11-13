import pymysql

db = pymysql.connect(host="localhost",
                     user="testuser",
                     password="test123",
                     database="sakila")
cursor = db.cursor()
sql = "SELECT * FROM NEWTESTTABLE"
try:
    cursor.execute(sql)
    result_set = cursor.fetchall()
    print(type(result_set))
    for index, row in enumerate(result_set):
        fname  = row[0]
        lname  = row[1]
        age    = row[2]
        sex    = row[3]
        income = row[4]
        #print("--- Table row:", index, "---")
        #print("First name:", fname,
        #      "\nLast name:", lname,
        #      "\nAge:", age,
        #      "\nSex:", sex,
        #      "\nIncome:", income)
        print("%s, %s, %d, %s, %d" %(fname, lname, age, sex, income))
    print("Table records were fetched successfully.")
except:
    print("Table records were not fetched.")
    
db.close()
