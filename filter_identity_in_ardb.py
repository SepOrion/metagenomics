#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="用途：根据ARDB数据库序列要求的最低identity，过滤diamond比对结果。")
parser.add_argument("-i",dest="input1",metavar="",help="输入文件1：ARDB索引文件:ardb_index_table.txt")
parser.add_argument("-ii",dest="input2",metavar="",help="输入文件2：diamond比对后的m8格式文件:ardb.m8")
parser.add_argument("-o",dest="outFile",metavar="",help="输出文件名")
args = parser.parse_args()

#读取index_table文件
with open(args.input1) as f1:
	myDict = {}
	for line in f1:
		k = line.strip("\n").split("\t")
		myDict[k[0]] = k[3]

#去除不满足数据库序列要求的最低identity
with open(args.input2) as f2:
	LL = []
	for line in f2:
		L = line.strip("\n").split("\t")[0:3]
		newline = ''
		if L[1] in myDict.keys():
			if float(L[2]) >= float(myDict[L[1]]):
				newline = "\t".join(L[0:2]) #输出gene ID和database ID
				LL.append(newline+"\n")

with open(args.outFile,"w") as f3:
	for value in LL:
		f3.write(value)
