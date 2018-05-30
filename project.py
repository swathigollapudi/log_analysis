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
print(c)
try:
    cur.execute("select name,views from viewauthor")
except:
    print("cannot select")
d = cur.fetchall()
print(d)
try:
    cur.execute("select * from finalview where perc>1;")
except:
    print("cannot connect")
e = cur.fetchall()
print(e)
cur.close()
