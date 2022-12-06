# Import module
import psycopg2

# Creating connection
conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="assessmentdb",
        user="postgres",
        password="****"
        )