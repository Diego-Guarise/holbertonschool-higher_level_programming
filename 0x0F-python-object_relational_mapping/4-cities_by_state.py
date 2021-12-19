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
cur.execute("SELECT cities.id, cities.name,states.name\
            FROM states JOIN cities ON states.id =\
            cities.state_id ORDER BY cities.id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
