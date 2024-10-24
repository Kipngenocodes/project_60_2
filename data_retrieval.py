import psycopg2

try:
    # Connect to your postgres DB
    connection = psycopg2.connect(
        dbname="kipchep",
        user="duke",
        password="Baltimoreravens",
        host="localhost",  # or your database server
        port="5432"        # default port
    )

    # Open a cursor to perform database operations
    cursor = connection.cursor()

    # Retrieve data from the table
    select_query = "SELECT * FROM kipngenodata;"  # Fetch only the first 10 rows for now
    cursor.execute(select_query)

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the retrieved data
    print("\nRetrieved data:")
    for row in rows:
        print(row)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
