#!/usr/bin/python3
"""module for 0-select_states.py"""

import MySQLdb
import sys
"""import module"""


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    search_name = sys.argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=dbname, charset='utf8')

    cur = conn.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY %s "
                "ORDER BY id ASC", (search_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
