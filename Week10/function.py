import sqlite3

# Execute query with parameter support and error handling
def query_executor(cursor, query, params=()):
    try:
        print("---")
        print(f"Executing: {query}")

        cursor.execute(query, params)

        if query.strip().lower().startswith("select"):
            return cursor  # Return cursor for SELECT queries
        else:
            return cursor.rowcount  # Return number of affected rows for DELETE/INSERT/UPDATE

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


# Fetch query results based on fetch type
def query_responder(cursor, fetch_type="fetchall", fetch_amount=3):
    try:
        if fetch_type == "fetchall":
            all_rows = cursor.fetchall()
        elif fetch_type == "fetchone":
            all_rows = cursor.fetchone()
        elif fetch_type == "fetchmany":
            all_rows = cursor.fetchmany(fetch_amount)
        else:
            print("Invalid fetch type")
            return None

        if not all_rows:
            print("No results found.")
            return None

        # Print results
        if isinstance(all_rows, list):  # Multiple rows
            for row in all_rows:
                print(dict(row))
        else:  # Single row
            print(dict(all_rows))

        return all_rows

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
