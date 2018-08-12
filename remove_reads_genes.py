#!/usr/bin/env python3

# Usage:filter_reads_in_genes.py <genes_reads_file> <output_name>
# 去除在各样品中支持reads数小于等于2的基因，并统计每个样品中丰度大于0的基因数

import sys
import pandas as pd
import numpy as np

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_table(input_file,index_col=[0])

# remove reads<=2 genes
dff = df[(np.abs(df.iloc[:,1:])>2).any(1)] 

f = lambda x: x/dff['Length']
data = dff.iloc[:,1:].apply(f)

# Calculate relative abundance
num = data.sum()
data1=data/num 
data1.to_csv(output_file,sep="\t")

# Count the number of genes in each sample
counts = (dff>0).sum()
counts.to_csv("genes_counts.txt",sep="\t")
