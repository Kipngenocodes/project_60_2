import psycopg2

try:
    # Connect to your postgres DB
    connection = psycopg2.connect(
        dbname="kipchep",
        user="duke",a
        password="Baltimoreravens",
        host="localhost",  # or your database server
        port="5432"        # default port
    )

    # Open a cursor to perform database operations
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT version();")

    # Fetch and print the result
    db_version = cursor.fetchone()
    print(f"PostgreSQL version: {db_version[0]}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
