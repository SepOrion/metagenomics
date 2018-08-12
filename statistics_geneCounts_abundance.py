#!/usr/bin/env python3

# 输入文件分别为样品基因丰度表、抗性基因或毒力因子基因的ID列表
# Useage:statistics_geneCounts_abundance.py <gene_abundance> <gens_id> > output_file_name
# 计算注释到抗性或毒力因子的基因个数比例和丰度总和

import sys
import pandas as pd
from pandas import Series,DataFrame

input_1 = sys.argv[1]
input_2 = sys.argv[2]

mydict = {}

# 读取样品的基因丰度表，并存为字典
with open(input_1) as f:
	for a in f:
		k = a.strip("\n").split("\t")
		mydict[k[0]] = k[1]
Name = mydict['Gene_ID']
mydict.pop('Gene_ID')

# 字典转为数据框，并统计丰度不为0的基因数
my_df = pd.DataFrame.from_dict(mydict,orient='index').astype({0:float})
my_counts = (my_df[0]>0).sum()

# 将基因丰度数值映射到注释基因id上
df = pd.read_table(input_2,header=None)
df[1]=df[0].map(mydict)
dff = df.astype({1:float})

dff_sum = dff[1].sum() #注释到的基因丰度总和
dff_counts = (dff[1]>0).sum() #已注释基因个数
dffout = dff_counts/my_counts #已注释基因个数占总数目比例

print(Name,end="\t")
print(my_counts,end="\t")
print(dff_counts,end="\t")
print(dffout,end="\t")
print(dff_sum)
