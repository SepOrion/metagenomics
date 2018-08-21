#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="用途：将一个基因对应多条分类信息的格式文件，转换为一条分类信息对应多个基因格式")
parser.add_argument("-i",dest="inputFile",metavar="",help="输入文件：过滤最低identity后文件")
parser.add_argument("-o",dest="outFile",metavar="",help="输出文件名")
args = parser.parse_args()

my_dict = {}
with open(args.inputFile) as F:
	for line in F.readlines():
		value,key = line.strip("\n").split("\t")
		new_value = my_dict.get(key,'')
		if new_value:
			my_dict[key] = new_value + '\t' + value
		else:
			my_dict[key] = value

with open(args.outFile,"w") as f:
	for k in my_dict.keys():
		f.write(k+"\t")
		f.write(my_dict[k]+"\n")
