#!/usr/bin/python
# -*- coding:utf-8 -*-


 

f = open("in.rtf","r+")             # 返回一个文件对象

line = f.read()             # 调用文件的 readline()方法
 
texta = line.split('{')[-1].split('}')[0]
# print(texta)
textb = texta.replace('\n','')
# print(textb)
textc = textb.replace(' ','')
# print(textc)
textd = textc.replace('\\','')
# print(textd)
listData = textd.split(',')
# print(listData)




strLast = ''
for stra in listData:
	keyval = stra.split(':')
	key = keyval[0].replace('"','') 
	# print('key: ' + key)
	strStand = "/**"
	strStand = strStand + "\n"
	strStand = strStand + "* " + key
	strStand = strStand + "\n"
	strStand = strStand + "*/"
	strStand = strStand + "\n"

	if "\""  in keyval[-1]:
		strStand = strStand + "@property(nonatomic,copy) NSString * "
	else:
		strStand = strStand + "@property(nonatomic,assign) NSInteger  "
	# strStand = strStand + "@property(nonatomic,copy) NSString * "
	strStand = strStand+key+";"
	strLast = strLast + strStand
	strLast = strLast + '\n'

print(strLast)
 
 
f.close()
 

