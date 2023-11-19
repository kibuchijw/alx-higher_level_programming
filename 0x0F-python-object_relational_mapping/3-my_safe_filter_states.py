#!/usr/bin/python3
"""
Lists all states where name matches argument passed,
from the  database hbtn_0e_0_usa
(Improved to handle SQL injection)
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            )

    # Get a cursor object
    cursor = db.cursor()

    # SQL query to match argument taken in from user, with placeholder
    sql_query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    # Tuple containing string to search, to prevent SQL injection
    state_name_parameter = (f"%{sys.argv[4]}%",)

    # Execute the SQL query to list all states
    cursor.execute(sql_query, state_name_parameter)

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    for result in results:
        print(f"({result[0] }, '{result[1]}')")

    # Close the cursor and the database connection
    cursor.close()
    db.close()
