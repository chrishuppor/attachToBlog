#!/usr/bin/env python
#-*- coding:utf-8 -*-

import popen2,string

INFILE = "fx"
CMD = "./pin -t source/tools/ManualExamples/obj-ia32/inscount1.so -- ./SimpleVM <" + INFILE

def execlCommand(command):
	fin,fout = popen2.popen2(command)
	result1 = fin.readline()#获取程序自带打印信息，wrong或者correct
	result2 = fin.readline()#获取pintools打印的信息
	result3 = fin.readline()#获取pintools打印的信息
	fin.close()
	return result1,result2,result3

choices = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def writefile(data):
	f = open(INFILE,'w')
	f.write(data)
	f.close()

def findRealCount(res1, res2, res3):
	mincount = 0;
	if "count" in res1:
		count = int(res1[len("count"):len(res1)-1])
		if mincount == 0:
			mincount = count

	if "count" in res2:
		count = int(res2[len("count"):len(res2)-1])
		if mincount == 0:
			mincount = count
		elif count < mincount:
			mincount = count

	if "count" in res3:
		count = int(res3[len("count"):len(res3)-1])
		if mincount == 0:
			mincount = count
		elif count < mincount:
			mincount = count

	return mincount


#-------------------------------------------------------
curkey = ''
while(1):
	print "[+]cur key-\"" + curkey + "\""

	maxCount = 0;
	tmpkey = curkey
	lastkey = curkey

	for char in choices:
		tmpkey = lastkey + char
		writefile(tmpkey)
		res1, res2, res3 = execlCommand(CMD)
		print ">", tmpkey, '\n', res1, res2, res3, "maxcount:", maxCount, "\n"
		if "Wrong" not in (res1 + res2 + res3):
			print "[+]the key is : ", tmpkey
			exit()

		curcount = findRealCount(res1, res2, res3)
		if curcount > maxCount:
			maxCount = curcount
			curkey = tmpkey