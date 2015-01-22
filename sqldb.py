#!/usr/bin/python
# _*_ coding=utf-8 _*_
import MySQLdb
try:
   conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='www_2114_com',port=3306)
   cur=conn.cursor()
   #cur.execute('set names utf8')
   cur.execute('select * from lx_users')
   result=cur.fetchone()
   print(result)
   print(len(result))
   print(result[2])
   info=cur.fetchmany(20)
   for ii in info:
       print ii
   #sqli="insert into lx_users(user_id, email, nick_name, user_passwd) values(%s,%s,%s,%s)"
   #cur.execute(sqli,('','在在','2 year 1 class','7'))
   cur.close()
   conn.close()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
