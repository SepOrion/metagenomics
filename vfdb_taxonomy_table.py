#!/usr/bin/env python3

import re
import argparse
import pandas as pd
import numpy as np
from pandas import DataFrame

def get_args():
	parser = argparse.ArgumentParser(description="用于计算VFDB数据库比对结果")
	parser.add_argument("-i",dest="m8File",metavar="",help="VFDB比对结果，M8格式")
	parser.add_argument("-k",dest="keyWord",metavar="",help="VFDB的注释信息keyword表：VFID_keyword.txt")
	parser.add_argument("-o",dest="outPutFile",metavar="",help="输出文件名")
	parser.add_argument("--min-score",dest="minScore",metavar="",default=60,help="比对结果的最小得分,默认60")
	return parser.parse_args()
args = get_args()

#过滤比对结果
df = pd.read_table(args.m8File,header=None)
drop_df = df.drop_duplicates([0])
score_df = drop_df[drop_df[11]>=args.minScore]
score_dff  = DataFrame(score_df,columns=[0,1])

#数据映射
with open(args.keyWord) as f:
	vfdb = {}
	for line in f:
		k = line.strip("\n").split("\t")
		vfdb[k[0]] = k[2]
score_dff[2] = score_dff[1].map(vfdb)
dff = score_dff.dropna()
dfs = DataFrame(dff,columns=[0,2])

#格式转换
train_dfs = np.array(dfs)
train_list = train_dfs.tolist()
dfDict = {}
for value in train_list:
	v,k = value
	new_v = dfDict.get(k,'')
	if new_v:
		dfDict[k] = new_v + '\t' + v
	else:
		dfDict[k] = v

#输出结果
with open(args.outPutFile,"w") as f:
	for k in dfDict.keys():
		f.write(k+"\t")
		f.write(dfDict[k]+"\n")











