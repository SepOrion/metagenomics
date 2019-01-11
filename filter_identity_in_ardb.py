#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description=
				 "用途：根据ARDB数据库序列要求的最低identity，过滤diamond比对结果，并输出注释丰度表。\n"
				"Usage:filter_identity_in_ardb.py -i ardb_index_table.txt -ii ardb.m8 -o ardb_annoPath.txt",formatter_class = ap.RawTextHelpFormatter")
parser.add_argument("-i",dest="input1",metavar="",help="输入文件1：ARDB索引文件:ardb_index_table.txt")
parser.add_argument("-ii",dest="input2",metavar="",help="输入文件2：diamond比对后的m8格式文件:ardb.m8")
parser.add_argument("-o",dest="outFile",metavar="",help="输出文件名")
args = parser.parse_args()

#读取index_table文件
with open(args.input1) as f1:
	myDict_1 = {} # 过滤最低identity
	myDict_2 = {} # 转换格式
	for line in f1:
		k = line.strip("\n").split("\t")
		myDict_1[k[0]] = k[3]
		myDict_2[k[0]] = k[1]+"+"+k[2]+"+"+k[4]

#去除不满足数据库序列要求的最低identity
with open(args.input2) as f2:
	LL = []
	for line in f2:
		L = line.strip("\n").split("\t")[0:3]
		newline = ''
		if L[1] in myDict_1.keys():
			if float(L[2]) >= float(myDict_1[L[1]]):
				newline = "\t".join(L[0:2]) #输出gene ID和database ID
				LL.append(newline)
#转换格式
new_L = []
for v in LL:
	line = v.split("\t")
	new_v = line[0]
	if line[1] in myDict_2.keys():
		new_v += "\t"+myDict_2[line[1]]
	new_L.append(new_v)

myDict_3 = {}
for k in new_L:
	value,key = k.split("\t")
	new_value = myDict_3.get(key,'')
	if new_value:
		myDict_3[key] = new_value + "\t" + value
	else:
		myDict_3[key] = value
# 输出结果
with open(args.outFile,"w") as f3:
	for k in myDict_3.keys():
		f3.write(k+"\t")
		f3.write(myDict_3[k]+"\n")
