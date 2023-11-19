#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb
if __name__ == "__main__":
    # Connect to the MySQL server
    db =  MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
            )

    # Get a cursor object
    cursor = db.cursor()

    # SQL query to list all cities
    sql_query = """
            SELECT c.id, c.name, s.name AS state_name
            FROM cities AS c
            JOIN states AS s ON c.state_id = s.id
            ORDER BY c.id ASC
    """
    # Execute the query
    cursor.execute(sql_query)

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    for result in results:
        print(f"({result[0]}, '{result[1]}', '{result[2]}')")

    # Close the cursor and the database connection
    cursor.close()
    db.close()
