#!/usr/bin/python3
"""
Lists all states from the  database hbtn_0e_0_usa
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
            database=sys.argv[3]
            )

    # Get a cursor object
    cursor = db.cursor()

    # Execute the SQL query to list all states
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    for result in results:
        print(f"({result[0] }, '{result[1]}')")

    # Close the cursor and the database connection
    cursor.close()
    db.close()
