#coding:utf-8
#资料http://drizzlewalk.blog.51cto.com/2203401/448874

import MySQLdb

conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "123456", db = "test")
cursor = conn.cursor ()

cursor.execute ("select * from person")
rows = cursor.fetchall()
for row in rows:
    print "id = %d, name = %s, age = %d" % (row[0], row[1], row[2])

cursor.execute("select count(*) from person")
rst = cursor.fetchone()
print "Current Query result count : %d" % rst[0]

cursor.close()
conn.close()
