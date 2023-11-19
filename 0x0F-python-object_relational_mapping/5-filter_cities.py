#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
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

    # SQL query to list all cities
    sql_query = """
            SELECT c.id, c.name, s.name AS state_name
            FROM cities AS c
            JOIN states AS s ON c.state_id = s.id
            WHERE s.name LIKE %s
            ORDER BY c.id ASC
    """
    # Tuple containing the state name(to prevent SQL injection)
    state_name = (f"%{sys.argv[4]}%",)

    # Execute the query
    cursor.execute(sql_query, state_name)

    # Fetch all results
    results = cursor.fetchall()

    # Print the cities
    cities = ""
    for result in results:
        if cities:
            cities += ", "
        cities += result[1]
    print(cities)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
