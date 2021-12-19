#!/usr/bin/python3
"""All cities byate"""


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
    cur.execute("SELECT C.name FROM cities C JOINates S ON C.state_id\
                = S.id WHERE S.name = (%s) ORDER BY C.id", (arglist[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
