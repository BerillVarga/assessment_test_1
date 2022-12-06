# Import module
import psycopg2

# Creating connection
def connection():
    conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="assessmentdb",
            user="postgres",
            password = '***'
            )
    return conn


def read_contact_list():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact_list;")
    rows = cur.fetchall()
    cur.close()
    return rows


