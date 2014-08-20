import sqlite3
conn = sqlite3.connect('stu.db')
curs = conn.cursor()

curs.execute('''
create table student(
    id text primary key,
    name text,
    age text,
    sex text
)
''')

sql1 = "insert into student values('1','xiaoMei','20','man')"
sql2 = "insert into student values('2','LongXiong','21','woman')"
sql3 = "insert into student values('3','Aliexxx','18','man')"
sql4 = "insert into student values('4','YoursOkk','18','woman')"
curs.execute(sql1)
curs.execute(sql2)
curs.execute(sql3)
curs.execute(sql4)
conn.commit()

query = "select * from student"
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print '%s:%s' % pair
    print

conn.close()