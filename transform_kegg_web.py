#!/usr/bin/env python3

# Usage: transform_kegg_web.py <input web.txt> <output>
# 用于将来自kegg官网的注释结果网页文件转为level3水平pathway对应多个基因ID文件

import sys
import re

args = sys.argv

input_file = args[1]
output_file = args[2]

kg = {}
L = []

# 匹配level3和对应的基因ID并存入列表中
with open(input_file) as f1:
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
with open(output_file,'w')  as f2:
	for k in kg.keys():
		f2.write(k)
		f2.write('\t')
		f2.write(kg[k].rstrip("\t")) # 去掉最后一个\t
		f2.write('\n')

# 输出通路名称
with open("Pathway_name.L3","w") as f3:
	for k in kg.keys():
		f3.write(k+"\n")
