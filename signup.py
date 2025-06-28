from getpass import getpass
from db_connection import get_connection

def signup():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter your name: ")
    account_id = int(input("Enter your account number: "))
    password = getpass("Create password: ")
    confirm = getpass("Confirm password: ")

    if password != confirm:
        print("❌ Passwords do not match.")
        return

    try:
        # Insert into Signup
        cursor.execute("""
            INSERT INTO Signup (name, account_id, create_password, confirm_password)
            VALUES (%s, %s, %s, %s)
        """, (name, account_id, password, confirm))

        # Insert into Login
        cursor.execute("""
            INSERT INTO Login (username, password)
            VALUES (%s, %s)
        """, (name, password))

        conn.commit()
        print("✅ Signup successful!")

    except Exception as e:
        print(f"❌ Error during signup: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
