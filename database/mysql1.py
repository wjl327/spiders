#coding:utf-8
#资料http://drizzlewalk.blog.51cto.com/2203401/448874

import MySQLdb

conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "123456", db = "test")
cursor = conn.cursor ()

cursor.execute ("""
	create table person
	(
	        id int primary key,
		name VARCHAR(40),
		age int
	)
	""")

cursor.execute ("""
	insert into person
	VALUES
		(1, 'xiaoMi', 18),
		(2, 'Mike', 20),
		(3, 'xiaoLei', 19)
	""")

conn.commit()
cursor.close ()
