import psycopg2

#connect to db
connection = psycopg2.connect(
    dbname="internsearch",
    user="paullieber",
    port=5432 #default port connection
)

cursor = connection.cursor() #returns cursor object so that we can fetch/execute queries





#close connection & cursor
connection.close()
cursor.close()
