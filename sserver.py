#!/usr/bin/env python
#coding=utf8
"""
# Author: litc
# Created Time : 2015/10/30 14:28:53
  Last Modified: 2015/11/2 10:20:31
# File Name: sserver.py
# Description:

"""
import socket
import time
import threading

HOST = '0.0.0.0'
PORT = 19852
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( (HOST, PORT) )
s.listen(5)
#while True:
#    time.sleep(0.1)
#    conn, addr = s.accept()
#    print '####################################'
#    print 'Connected by ', addr
#    print '####################################'
#    while True:
#        data=conn.recv(1024)
#        print('[Client %s:%s said]:%s' % (addr[0],addr[1],data))
#        conn.sendall(data)
#conn.close()
def response(sock, addr):
    while 1:
        data = sock.recv(1024)
        if not data:
            break
        print('[Client %s:%s said]:%s' % (addr[0],addr[1],data))
        sock.sendall(data)
    sock.close()
while True:
    time.sleep(0.1)
    conn, addr = s.accept()
    print '####################################'
    print 'Connected by ', addr
    print '####################################'
    t = threading.Thread(target=response,args=(conn,addr))
    t.start()
