import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='pi8643bb',
                             password='sailboat128',
                             db='pi8643bb_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# userInput = 'Kami'
userInput = input("Enter Name: ")

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = " SELECT * from Students WHERE fName =  " + "'" + userInput  + "'"
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
