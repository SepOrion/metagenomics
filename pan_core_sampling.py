#!/usr/bin/env python3
# Usage:pan_core_sampling.py <geneAbundance.txt> <outputName>
# geneAbundance.txt :基因丰度表
# outputName:输出文件名

import argparse
import pandas as pd
from pandas import DataFrame
 
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input",dest="inputFile",metavar="",help="输入文件:基因丰度表")
parser.add_argument("-o","--output",dest="outputFile",metavar="",help="输出文件名")
parser.add_argument("-m",dest="m",metavar="",help="要抽取的样本数",type=int)
parser.add_argument("-n",dest="n",metavar="",help="重复抽样次数",type=int)
args = parser.parse_args()

# 读取基因丰度表，并统计每个样品丰度不为0的基因个数
df1 = pd.read_table(args.inputFile,index_col=[0])
geneCounts =(df1>0).sum()

pan_1= []
core_1 = []
i = 1
while i <=args.m: # 抽取样品数
	pan_2 = []
	core_2 = []
	for x in range(args.n): # 重复次数
		# pan genes
		pan_2.append(geneCounts.sample(n=i).mean())
		
		# core genes
		coreSample = df1.sample(n=i,axis=1)
		commonRow =coreSample[(coreSample>0).all(1)]
		core_counts = commonRow.count()[0]
		core_2.append(core_counts)
	pan_1.append(pan_2)
	core_1.append(core_2)
	i +=1

Index = list(range(1,args.m+1))
col = list(range(1,args.n+1))

panDf = pd.DataFrame(pan_1,index = Index,columns = col)
coreDf = pd.DataFrame(core_1,index = Index,columns = col)

panDf_T = panDf.T
coreDf_T = coreDf.T

panDf_T.to_csv("pan_"+args.outputFile,sep="\t")
coreDf_T.to_csv("core_"+args.outputFile,sep="\t")

