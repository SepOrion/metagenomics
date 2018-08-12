#!/usr/bin/env python
#Usage:calculate_kegg_abundance.py <input_file>

import sys
import pandas as pd
from pandas import Series,DataFrame

args = sys.argv
input_file = args[1]
Name = input_file.split("_")[0]

#sum abundance
df = pd.read_table(input_file,header=None,index_col=[0],low_memory=False)
data = df.sum(axis=1)

data.index.name = 'Pathway'
data1 = DataFrame(data,columns=[Name])

#output abundance
output_file1 =Name+"_kegg.txt"
data1.to_csv(output_file1,sep="\t")

'''
#output relative abundance %
f = lambda x : x/data1[Name].sum()*100
percentage = data1.apply(f).round(2)
output_file2 =Name+"_relative_abundance.txt"
percentage.to_csv(output_file2,sep="\t")
'''

