#!python
#coding:utf-8
import time
print("content-type:text/html")
print("")
now = time.localtime()
nowt = time.strftime("%Y-%m-%d-%H_%M_%S", now)  
print(nowt)
