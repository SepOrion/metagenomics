#!/usr/bin/env python

# Useage:merge_abundance_table.py <output_file>
# 用于合并每个样品的丰度表，从而获得矩阵

import pandas as pd
import glob
import sys

args = sys.argv
output_file = args[1]

file_list = glob.glob('*abundance.txt')

dfs = [pd.read_table(filename,index_col=[0]) for filename in file_list]

output_table = dfs[0].join(dfs[1:])
output_table.to_csv(output_file,sep = "\t")



