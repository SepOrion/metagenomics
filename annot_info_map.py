#!/usr/bin/env python3

# 输入文件分别为基因对应的注释编号、注释编号对应的注释信息，输出文件为annot_info_genes.txt
# Usage:annot_info_map.py <annot_to_genesID_file> <annot_info_table>
# 用于将注释信息映射到对应的编号：例如diamond比对后，只会输出序列的编号，不会输出空格后面的详细解释说明

import sys
import pandas as pd
from pandas import Series,DataFrame

args = sys.argv
input_file = args[1]
annot_file = args[2]

df = pd.read_table(input_file,header=None,names=['SeqID','GenesID'])

annot_dict = {}

with open(annot_file) as f:
	for a in f:
		k = a.strip("\n").split("\t")
		annot_dict[k[0]] = k[1]
df['annot_info'] = df['SeqID'].map(annot_dict)

dff = DataFrame(df,columns=['SeqID','annot_info','GenesID'])

dff.to_csv("annot_info_genes.txt",sep="\t",index=False,header=False)
