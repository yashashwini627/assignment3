
import csv
from dbsetup import setup_database
from csvhandler import write_to_csv, append_to_csv, read_from_csv
from dbhandler import insert_data_from_csv, insert_additional_records, fetch_all_students

def main():

    conn, cursor = setup_database()

    csv_filename = "students.csv"
    data = [
        [1, "yash", 85],
        [2, "keerti", 90],
        [3, "shivaram", 78]
    ]
    
    write_to_csv(csv_filename, ["id", "name", "marks"], data)

    new_record = [4, "sunanda", 88]
    append_to_csv(csv_filename, new_record)

    
    csv_data = read_from_csv(csv_filename)
    insert_data_from_csv(cursor, csv_data)

    additional_records = [
        (5, "veeranna", 92),
        (6, "Abc", 80)
    ]
    insert_additional_records(cursor, additional_records)

    output_filename = "students_from_db.csv"
    data_from_db = fetch_all_students(cursor)
    write_to_csv(output_filename, ["id", "name", "marks"], data_from_db)

    print("Data from database:")
    for row in fetch_all_students(cursor):
        print(row)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
