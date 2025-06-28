from db_connection import get_connection

def create_customer_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            customer_id INT PRIMARY KEY,
            customer_name VARCHAR(100),
            dob DATE,
            mobileno VARCHAR(15),
            account_id INT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
