from db_connection import get_connection

def create_loan_payment_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LoanPayment (
            loan_payment_id INT PRIMARY KEY,
            loan_id INT,
            amount DECIMAL(15,2),
            FOREIGN KEY (loan_id) REFERENCES Loan(loan_id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
