from db_connection import init_database
from create_customer_table import create_customer_table
from create_account_table import create_account_table
from create_branch_table import create_branch_table
from create_banker_table import create_banker_table
from create_loan_table import create_loan_table
from create_loan_payment_table import create_loan_payment_table
from create_signup_table import create_signup_table
from create_login_table import create_login_table

def create_all_tables():
    init_database()
    create_customer_table()
    create_account_table()
    create_branch_table()
    create_banker_table()
    create_loan_table()
    create_loan_payment_table()
    create_signup_table()
    create_login_table()
    print("✅ All tables created successfully.")

if __name__ == "__main__":
    create_all_tables()
    
def main():
    while True:
        print("\n--- Bank System ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
    
    if __name__ == "__main__":
         main()
