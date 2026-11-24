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


def save_checkpoint(next_cursor):
    """
    saves checkpoint of where the pagination process stopped.
    """

    completed = next_cursor is None #boolean

    cursor.execute(
        """
        UPDATE ingestion_state
        SET next_cursor = %s, pages_processed = pages_processed + 1, completed = %s
        WHERE source = 'himalayas';
        """,
        (next_cursor, completed) #pass into %s 
    )

def load_checkpoint():
    """
    loads the last saved checkpoint to continue where pagination process stopped
    """
    cursor.execute(
        """
        SELECT next_cursor, completed
        FROM ingestion_state
        WHERE source = 'himalayas'
        """
    )

    last_saved_row = cursor.fetchone() #returning the last saved row with .fetchone() returning a single row
    return last_saved_row

# print(load_checkpoint())
