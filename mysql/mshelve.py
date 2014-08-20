#coding:utf-8
#shelve模块 Python文件存储 可以存小型的数据
#可参考  http://www.cnblogs.com/hongten/p/hongten_python_shelve.html

import sys,shelve

def store(db):
    pid = raw_input('Enter unique ID number:')
    person = {}
    person['name'] = raw_input('Enter name:')
    person['age'] = raw_input('Enter age:')
    person['phone'] = raw_input('Enter phone:')
    db[pid] = person
	
def lookup(db):
    pid = raw_input('Enter ID number:')
    print db[pid]['name'],db[pid]['age'],db[pid]['phone']

def show(db):
    for item in db.items():
	    print "id=%s name=%s age=%s phone=%s" % (item[0],db[item[0]]['name'],db[item[0]]['age'],db[item[0]]['phone'])
	
def phelp():
    print 'The available commands are:'
    print 'store : Stores information about a person'
    print 'shows : Show all person information'
    print 'query : Looks up a person from ID number'
    print 'quit : Save changes and exit'
    print '? : Prints this message'
	
def command():
    cmd = raw_input('Enter command “?” get help : ')
    cmd = cmd.strip().lower()
    return cmd
	
def main():
    database = shelve.open("C:\\database.dat")
    try:
        while True:
            cmd = command()
            if cmd == 'store' :
                store(database)
            elif cmd == 'show' :
                 show(database)
            elif cmd == 'query' :
                lookup(database)
            elif cmd == '?' :
                phelp()
            elif cmd == 'quit':
                return
    finally:
        database.close()
		
if __name__ == '__main__' : main()