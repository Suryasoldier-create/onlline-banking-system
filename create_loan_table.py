from db_connection import get_connection

def create_loan_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Loan (
            loan_id INT PRIMARY KEY,
            account_id INT,
            branch_id INT,
            issued_amount DECIMAL(15,2),
            remaining_amount DECIMAL(15,2),
            FOREIGN KEY (account_id) REFERENCES Account(account_id),
            FOREIGN KEY (branch_id) REFERENCES Branch(branch_id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
