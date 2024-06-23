#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa, safe from SQL injection.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials, database name, and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute the SQL query to select all cities of the given state, ordered by id in ascending order
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows from the executed query
    rows = cursor.fetchall()

    # Print the cities separated by commas
    print(", ".join(row[0] for row in rows))

    # Close the cursor and the database connection
    cursor.close()
    db.close()

