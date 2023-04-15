#!/usr/bin/python3
"""module for 0-select_states.sql"""

import sys
import MySQLdb
"""import MySQLdb"""


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=dbname, charset='utf8')

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
