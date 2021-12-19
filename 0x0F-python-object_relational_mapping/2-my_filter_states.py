#!/usr/bin/python3
"""Filterates by user input"""

import MySQLdb
import sys

if __main__ == "__name__":
    arglist = sys.argv
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=arglist[1],
        passwd=arglist[2],
        db=arglist[3],
        charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                .format(arglist[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
