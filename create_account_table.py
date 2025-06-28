from db_connection import get_connection

def create_account_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Account (
            account_id INT PRIMARY KEY,
            account_balance DECIMAL(15,2),
            account_type VARCHAR(50),
            branch_id INT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
