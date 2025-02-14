import sqlite3

def view_database():
    conn = sqlite3.connect('./data/test.db')
    cursor = conn.cursor()
    
    # List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])
    
    # Query data from a specific table
    print("\nData from custom_fields table:")
    cursor.execute("SELECT * FROM custom_fields;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    print("\nData from email_cadences table:")
    cursor.execute("SELECT * FROM email_cadences;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    view_database()
