from getpass import getpass
from db_connection import get_connection

def login():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Username: ")
    password = getpass("Password: ")

    cursor.execute("""
        SELECT * FROM Login WHERE username = %s AND password = %s
    """, (username, password))

    result = cursor.fetchone()

    if result:
        print("✅ Login successful!")
    else:
        print("❌ Invalid credentials.")

    cursor.close()
    conn.close()
