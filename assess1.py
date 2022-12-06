# Import module
import psycopg2

# Creating connection
def connection():
    conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="assessmentdb",
            user="postgres",
            password = 'dataLove'
            )
    return conn

# Showing the content of the contacts table
def read_contact_list():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# Inserting data into the contacts table
def insert_data(first_name, last_name, title, organization):
    conn = connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO contacts (first_name, last_name, title, organization) VALUES ('{first_name}', '{last_name}', '{title}', '{organization}');")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()

# Removing data (row) from the contacts table
def delete_data(first_name, last_name):
    conn = connection()
    cur = conn.cursor()
    cur.execute(f"SELECT id FROM contacts WHERE first_name = '{first_name}' AND last_name = '{last_name}';")
    id = cur.fetchall()
    cur.execute(f"DELETE FROM contacts WHERE id = '{id[0][0]}';")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()

# Savning the changes
def save_changes():
    conn = connection()
    cur = conn.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()
    conn.close()


def main():
    # Information about the program and what is does
    print('Hello and welcome to the this program, available commands:')
    print('  list   - list information about the contacts\n  insert - inserting new data')
    print('  delete - delete a person\n  quit   - quit the program')

    while True: 
        cmd = input("Command: ").strip().upper()
        if cmd == "LIST":
            c_list = read_contact_list()
            for item in c_list:
                print(item)
        elif cmd == "INSERT":
            first_name = input("  First name: ")
            last_name = input("  Last name: ")
            title =  input("  Title: ")
            organization = input("  Organization: ")
            insert_data(first_name, last_name, title, organization)
        elif cmd == "DELETE":
            first_name = input("  First name: ")
            last_name = input("  Last name: ")
            delete_data(first_name, last_name)
        elif cmd == "QUIT":
            save_changes()
            exit()
        else:
            print('  Unknown command:', cmd)

if __name__ == '__main__':
    main()


