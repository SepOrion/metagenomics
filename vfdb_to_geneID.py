#!/usr/bin/env python3

# Usage:vfdb_to_geneId.py <input_file> <output_file>
# 转换格式：毒力因子对应多个基因ID

import sys
from pandas import Series

args = sys.argv
input_file = args[1]
output_file = args[2]
my_dict = {}

with open(input_file) as F:
	for line in F.readlines():
		value,key = line.strip("\n").split("\t")
		new_value = my_dict.get(key,'')
		if new_value:
			my_dict[key] = new_value + '\t' + value
		else:
			my_dict[key] = value
sdata = Series(my_dict)
sdata.to_csv(output_file,sep = "\t")
