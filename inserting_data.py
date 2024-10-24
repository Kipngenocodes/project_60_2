import psycopg2
import random
import string

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

    # Create a table with 5 columns
    create_table_query = """
    CREATE TABLE IF NOT EXISTS kipngenodata (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        address VARCHAR(100),
        salary DECIMAL(10, 2),
        department VARCHAR(50)
    );
    """
    # Execute the create table query
    cursor.execute(create_table_query)
    print("Table created successfully.")

    # Generate 100 rows of data
    data = []
    for i in range(100):
        name = ''.join(random.choices(string.ascii_uppercase, k=5))  # Random 5-letter name
        age = random.randint(20, 60)  # Random age between 20 and 60
        address = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))  # Random address
        salary = round(random.uniform(30000, 100000), 2)  # Random salary between 30k and 100k
        department = random.choice(['HR', 'Finance', 'IT', 'Marketing', 'Sales'])  # Random department
        data.append((name, age, address, salary, department))

    # Insert multiple rows using executemany
    insert_query = """
    INSERT INTO kipngenodata (name, age, address, salary, department)
    VALUES (%s, %s, %s, %s, %s);
    """
    cursor.executemany(insert_query, data)
    print("100 rows inserted successfully.")

    # Commit the changes
    connection.commit()

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
