#!/usr/bin/python3
"""SQL Injection..."""

import MySQLdb
import sys

if __name__ == "__main__":
    arglist = sys.argv
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=arglist[1],
        passwd=arglist[2],
        db=arglist[3],
        charset="utf8")

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE states.name= (%s) ORDER BY states.id",
        (arglist[4],
         ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
