#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
This script connects to a MySQL database using credentials provided via command-line arguments and retrieves all records from the 'states' table, ordered by the 'id' column in ascending order.
"""


import sys
import MySQLdb



if __name__ == "__main__":
    """
    Main execution block:
    - Retrieves MySQL credentials from command line arguments.
    - Connects to the MySQL database.
    - Executes an SQL query to select all states.
    - Fetches and prints the query results.
    - Closes the cursor and database connection.
    """

    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the executed query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


