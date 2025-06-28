from db_connection import get_connection

def create_banker_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Banker (
            banker_name VARCHAR(100),
            branch_id INT,
            PRIMARY KEY (banker_name, branch_id),
            FOREIGN KEY (branch_id) REFERENCES Branch(branch_id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
