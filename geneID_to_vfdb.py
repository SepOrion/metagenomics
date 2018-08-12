#!/usr/bin/env python3

# Usage:gene_to_vfdb.py <input_file> <output_file>
# 转换格式：一个基因ID对应多个毒力因子

import sys
from pandas import Series

args = sys.argv
input_file = args[1]
output_file = args[2]
my_dict = {}

with open(input_file) as F:
	for line in F.readlines():
		k,v = line.strip("\n").split("\t")
		new_v = my_dict.get(k,'')
		if new_v:
			my_dict[k] = new_v + '\t'+v
		else:
			my_dict[k] = v
sdata = Series(my_dict)
sdata.to_csv(output_file,sep = "\t")
