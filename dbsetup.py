import mysql.connector

def setup_database():
    conn = mysql.connector.connect(host="localhost", user="root", password="Yvss@123")
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
    cursor.execute("USE student_db")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY,
            name VARCHAR(50),
            marks INT
        )
    """)
    
    return conn, cursor