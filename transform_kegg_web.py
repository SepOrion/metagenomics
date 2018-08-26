#!/usr/bin/env python3

import re
import argparse
parser = argparse.ArgumentParser(description="用途：将来自kegg官网注释的网页格式文件，转换为pathway(level3)通路表")
parser.add_argument("-i",dest="inputFile",metavar="",help="输入文件：来自kegg网页文件:kegg.web")
parser.add_argument("-o",dest="outFile",metavar="",help="输出文件名")
args = parser.parse_args()

kg = {}
L = []

# 匹配level3和对应的基因ID并存入列表中
with open(args.inputFile) as f1:
	for line in f1:
		line = line.lstrip() # 删除开头空格
		if re.search('^[0-9]{5}',line): # 获取level3水平pathway名称
			L.append(line)
		elif re.search('^K[0-9]{5}',line): # 获取geneId
			L.append(next(f1).lstrip())
			
# 将通路名称存为key，对应基因ID存为value
for value in L:
	if re.search('^[0-9]{5}',value):
		name = ' '.join(value.split()[1:][:-1])
		kg[name] = ''
	else:
		new_v = value.replace('\n','\t').replace(', ','\t') #去掉换行符\n,用\t替换“, ”
		kg[name] +=new_v

# 输出结果：一条通路对应多个genes
with open(args.outFile,'w')  as f2:
	for k in kg.keys():
		f2.write(k)
		f2.write('\t')
		f2.write(kg[k].rstrip("\t")) # 去掉最后一个\t
		f2.write('\n')
"""
# 输出通路名称
with open("Pathway_name.L3","w") as f3:
	for k in kg.keys():
		f3.write(k+"\n")
"""
