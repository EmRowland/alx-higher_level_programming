#!/usr/bin/python3
"""
Lists all states from the database
 hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

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

    # Execute the SQL query to select states with names matching the user
    # input, ordered by id in ascending order
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Fetch all the rows from the executed query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
