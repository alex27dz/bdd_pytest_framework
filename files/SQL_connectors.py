import mysql.connector
import pyodbc


def mysql_connector():
    # Define the connection parameters
    host = "ltc-ist-08-cc-0019-sat-sql-ewc3a.database.windows.net"
    port = 1433      #  3306  # MySQL default port
    database = "CMS_QA"
    user = "CMSIstUser"
    password = "j22WaVeDPUM4S3K9"

    # Create the MySQL connection
    conn = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    # if conn.is_connected():
    print("Connected to the MySQL database")
    cursor = conn.cursor()  # Create a cursor object to interact with the database
    cursor.execute("SELECT * FROM TrainingProviderApplicantBusinesses")  # Execute a query to fetch data from a table
    rows = cursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)
    cursor.close()  # Close the cursor and connection when done
    conn.close()


def sql_microsoft_connector():
    # Define the connection string parameters
    server_name = "ltc-ist-08-cc-0019-sat-sql-ewc3a.database.windows.net,1433"  # Replace with your SQL Server's hostname
    database_name = "CMS_QA"  # Replace with your database name
    username = "CMSIstUser"  # Replace with your SQL Server username
    password = "j22WaVeDPUM4S3K9"  # Replace with your SQL Server password
    # Create a connection string
    connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server_name};Database={database_name};Uid={username};Pwd={password}"
    # Establish a connection to the database
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()  # Create a cursor to interact with the database
    cursor.execute("SELECT * FROM TrainingProviderApplicantBusinesses")  # Execute SQL queries
    rows = cursor.fetchall()
    for row in rows:  # Iterate through the results
        print(row)
    print(cursor)  # connection
    cursor.close()  # Close the cursor and connection when done
    connection.close()


