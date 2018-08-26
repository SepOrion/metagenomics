#!/usr/bin/env python3

import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description="用途：去除在各样品中支持reads数小于等于2的基因，并统计每个样品中丰度大于0的基因数")
parser.add_argument("-i",dest="inputFile",metavar="",help="所有样品reads数矩阵表，第一列基因编号，第二列为长度，其余各列为样品名")
parser.add_argument("-o",dest="outFile",metavar="",help="输出文件名")
args = parser.parse_args()

df = pd.read_table(args.inputFile,index_col=[0])

# 过滤掉在各个样品中支持 reads 数目<=2的基因
dff = df[(np.abs(df.iloc[:,1:])>2).any(1)] 

f = lambda x: x/dff['Length']
data = dff.iloc[:,1:].apply(f)

# 计算基因相对丰度
num = data.sum()
data1=data/num 
data1.to_csv(args.outFile,sep="\t")

# 统计样品丰度不为0的基因数
counts = (dff>0).sum()
counts.to_csv("genes_counts.txt",sep="\t")
