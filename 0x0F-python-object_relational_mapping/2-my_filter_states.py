#!/usr/bin/python3
"""module for 0-select_states.py"""

import MySQLdb
import sys
"""import module"""


if __name__ == '__main__':
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    search_name = sys.argv[4]

    # Connect to MySQL server
    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=dbname, charset='utf8')

    # Create a cursor object
    cur = conn.cursor()

    # Execute SQL query to select all states that match the search name, sorted by id in ascending order
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY %s "
                "ORDER BY id ASC", (search_name,))

    # Fetch all rows and display them
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
