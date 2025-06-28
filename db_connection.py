import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        username="your_username",        
        password="your_password",    
        database="bankingsystem" ,          
    )
def init_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS bankingsystem")
    conn.commit()
    cursor.close()
    conn.close()