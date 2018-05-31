#!/usr/bin/env python
import psycopg2
try:
    conn = psycopg2.connect("dbname='news' user='vagrant' password='vagrant'")
    print("connection established")
except:
    print("connection failed")
cur = conn.cursor()
try:
    cur.execute("select title,views from noofviews limit 3")
except:
    print("i can't select from noofviews")
c = cur.fetchall()
i = 0
while i < len(c):
    print (' \t ' + str(c[i]) + 'views')
    i = i+1
try:
    cur.execute("select name,views from viewauthor")
except:
    print("cannot select")
d = cur.fetchall()
i = 0
while i < len(d):
    print('\t' + str(d[i]) + 'views')
    i = i+1
try:
    cur.execute("select * from finalview where perc>1;")
except:
    print("cannot connect")
e = cur.fetchall()
i = 0
while i < len(e):
    print('\t'+str(e[i]) + 'errors')
    i = i+1
cur.close()
