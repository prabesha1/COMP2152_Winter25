import sqlite3
from contextlib import closing
from function import query_executor, query_responder

# Database path
db_path = "test.db"

try:
    # Open connection using context manager
    with closing(sqlite3.connect(db_path)) as db_con:
        db_con.row_factory = sqlite3.Row  # Enable dictionary-like row access
        
        with closing(db_con.cursor()) as cursor:
            # ✅ String Indexing - Get names of rows with ID > 14
            try:
                query_1 = "SELECT * FROM demo WHERE id > 14"
                cursor = query_executor(cursor, query_1)

                if cursor:
                    print("Names of rows with id > 14:")
                    rows = query_responder(cursor, fetch_type="fetchall")
                    if rows:
                        for row in rows:
                            print(row["name"])

            except Exception as e:
                print(f"Error executing query_1: {e}")

            # ✅ Delete Row - User input and confirmation
            try:
                del_row = int(input("Enter the row ID threshold for deletion: "))
                query_2 = "DELETE FROM demo WHERE id < ?"
                num_rows = query_executor(cursor, query_2, (del_row,))

                if num_rows is not None:
                    print(f"{num_rows} rows affected. Are you sure you want to continue? (y/n):")
                    confirm = input().strip().lower()
                    if confirm == 'y':
                        db_con.commit()
                        print("Deletion confirmed.")
                    else:
                        print("Deletion cancelled.")

            except Exception as e:
                print(f"Error executing query_2: {e}")

except sqlite3.Error as e:
    print(f"Database connection error: {e}")
