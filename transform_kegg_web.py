#!/usr/bin/env python3

# Usage: transform_kegg_web.py <input> <output>
# 用于将来自kegg官网的网页文件转为level3水平pathway对应多个基因ID文件

import sys
import re

args = sys.argv

input_file = args[1]
output_file = args[2]

kg = {}
L = []

with open(input_file) as f1:
	for line in f1:
		line = line.lstrip() # 删除开头空格
		if re.search('^[0-9]{5}',line): # 获取level3水平pathway名称
			name = ' '.join(line.split()[1:][:-1])
			kg[name] = ''
		elif re.search('^K[0-9]{5}',line): # 获取geneId
			nextLine = next(f1).lstrip().strip("\n")
			L.append(nextLine)
			newLine = ','.join(L)
			newLine = newLine.replace(',','\t')
			kg[name] = newLine

# 输出结果：一条通路对应多个genes
with open(output_file,'w')  as f2:
	for key in kg.keys():
		f2.write(key)
		f2.write('\t')
		f2.write(kg[key])
		f2.write('\n')

# 输出通路名称
with open("kegg_pathway_name.txt","w") as f3:
	for key in kg.keys():
		f3.write(key+"\n")
