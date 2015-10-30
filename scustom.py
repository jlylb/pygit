#!/usr/bin/env python
#coding=utf8
"""
# Author: litc
# Created Time : 2015/10/30 14:28:53
  Last Modified: 2015/10/30 15:10:30
# File Name: sserver.py
# Description:

"""
import socket
HOST = '127.0.0.1'
PORT = 19852
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.connect( (HOST, PORT) )
while True:
    cmd=raw_input("please input cmd:")
    s.sendall(cmd)
    data = s.recv(1024)
    print '####################################'
    print '',data,'\n'
    print '####################################'
s.close()

