#!/usr/bin/python3
"""Filterates"""


if __name__ == "__main__":
    import MySQLdb
    import sys

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
        "SELECT * FROM states WHERE name LIKE BINARY 'N%'\
        ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
