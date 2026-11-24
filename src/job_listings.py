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
            company_name,
            title,
            employment_type,
            description,
            location,
            application_url
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (guid) DO NOTHING;
        """,

        (
            job['guid'],
            job['companyName'],
            job['title'],
            job['employmentType'],
            job['description'],
            ", ".join(job['locationRestrictions'] or []),
            job['applicationLink']
        )
    )



#close connection & cursor
# connection.close()
# cursor.close()
