#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


"""
REFERENCE: The self taught programmer

>MEMO
AF_INET: comminicating over the internet
socket.SOCK_STREAM: use TCP to ensure delivery

> HOW TO USE
1. run the code
$python2.7 simpleserver.py
2. access localhost:8885

"""
import socket
import datetime
today = str(datetime.datetime.today())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",8885))
s.listen(10)

while True:
    connect, address = s.accept()
    resp = (connect.recv(1024)).strip() # limit request to 1024 bytes
    connect.send(today)
    # close the connection when finished
    connect.close()

