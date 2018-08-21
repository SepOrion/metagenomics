#!/usr/bin/env python3

# Usage:taxonomy_to_geneId.py <input_file> <output_file>
# 转换格式：一个注释分类对应多个基因ID

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i",dest="inputFile",metavar="",help="输入文件：过滤最低identity后文件")
parser.add_argument("-0",dest="outFile",metavar="",help="输出文件名")
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
