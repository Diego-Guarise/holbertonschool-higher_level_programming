#!/usr/bin/python3
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
cur.execute("SELECT cities.name FROM states JOIN cities ON\
cities.states.id = state_id WHERE states.name =\
            %s ORDER BY cities.id ASC", [arglist[4]])
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
