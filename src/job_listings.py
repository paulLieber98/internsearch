import psycopg2

#connect to db
connection = psycopg2.connect(
    dbname="internsearch",
    user="paullieber",
    port=5432 #default port connection
)

cursor = connection.cursor() #returns cursor object so that we can fetch/execute queries

#inserts job info as a row in "jobs" table inside db
#guid, company_name, title, employment_type, full_job_desc, location, application_url
def insert(job):
    cursor.execute(
        """
        INSERT INTO jobs (
            guid, 
            companyName, 
            title, 
            employmentType, 
            description, 
            applicationLink
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """,

        (
            job['guid'], 
            job['companyName'], 
            job['title'], 
            job['employmentType'], 
            job['description'], 
            job['applicationLink']
        )
    )



#selecting all columns from jobs table
cursor.execute("SELECT * FROM jobs;")

#fetching the columns that w/ the query we sent
results = cursor.fetchall()

print(results)



#close connection & cursor
# connection.close()
cursor.close()
