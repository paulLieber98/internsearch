import psycopg2

#connect to db
connection = psycopg2.connect(
    dbname="internsearch",
    user="paullieber",
    port=5432 #default port connection
)

cursor = connection.cursor() #returns cursor object so that we can fetch/execute queries

#selecting all columns from jobs table
cursor.execute("SELECT * FROM jobs;")

#fetching the columns that w/ the query we sent
results = cursor.fetchall()

print(results)



#close connection & cursor
connection.close()
cursor.close()
