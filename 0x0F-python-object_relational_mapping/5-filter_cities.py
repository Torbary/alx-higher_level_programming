#!/usr/bin/python3
"""Script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv
"""import modules"""


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cur = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s ORDER BY cities.id ASC"

    cur.execute(query, (argv[4],))
    rows = cur.fetchall()

    cities = ", ".join([row[1] for row in rows])
    print(cities)

    cur.close()
    conn.close()
