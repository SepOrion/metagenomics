#!/usr/bin/env python3

# Usage:calculate_megan_abundance.py <input_file> 
# 用于计算注释分类丰度
# input_file:form megan's replace output file
# eg:sampleName_replace.txt

import sys
import pandas as pd
from pandas import Series,DataFrame

input_file = sys.argv[1]
colName = input_file.split("_")[0]

# Determine maximum column count
with open(input_file) as f:
    lines = f.readlines()
    colcount = max([len(l.strip().split("\t")) for l in lines])

# Add column headers and sum
df = pd.read_table(input_file,index_col=[0],names=range(colcount))
data = df.sum(axis=1)

# Add index name and columns name
data.index.name="taxonID"
df_data = DataFrame(data,columns=[colName])

# Output: abundance file
output_file1 = colName+"_abundance.txt"
df_data.to_csv(output_file1,sep="\t")

'''
# Output: relative abundance %
f = lambda x : x/df_data[colName].sum()*100
percentage = df_data.apply(f).round(2)
output_file2 =colName+"_relative_abundance.txt"
percentage.to_csv(output_file2,sep="\t")
'''
