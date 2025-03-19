def insert_data_from_csv(cursor, csv_data):
    for row in csv_data:
        cursor.execute("""
            INSERT INTO students (id, name, marks) 
            VALUES (%s, %s, %s) 
            ON DUPLICATE KEY UPDATE name=%s, marks=%s
        """, (row[0], row[1], row[2], row[1], row[2]))

def insert_additional_records(cursor, records):
    cursor.executemany("""
        INSERT INTO students (id, name, marks) 
        VALUES (%s, %s, %s)
    """, records)

def fetch_all_students(cursor):
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()