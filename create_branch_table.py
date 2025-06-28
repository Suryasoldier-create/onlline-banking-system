from db_connection import get_connection

def create_branch_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Branch (
            branch_id INT PRIMARY KEY,
            banker_name VARCHAR(100),
            assets DECIMAL(20,2),
            branch_address VARCHAR(255)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
