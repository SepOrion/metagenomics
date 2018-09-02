#!/usr/bin/env python3

import gzip
import argparse

def get_args():
	parser = argparse.ArgumentParser(description="用途：根据ncbi对比结果计算物种分类丰度")
	parser.add_argument("-i",dest="m8File",metavar="",help="diamond比对结果m8格式")
	parser.add_argument("-ii",dest="ncbiTax",metavar="",help="ncbi 分类信息：meta_acc_taxid_taxPath.txt.gz")
	parser.add_argument("-o",dest="outFile",metavar="",help="输出文件名")
	parser.add_argument("--min-score",dest="minScore",metavar="",default=60,help="比对结果的最小得分,默认60")
	return parser.parse_args()

args = get_args()

# 读取m8文件，过滤最低score
with open(args.m8File) as f1:
	cleanDict = {}
	for line in f1:
		k = line.strip('\n').split('\t')
		if float(k[-1]) >=args.minScore:
			cleanDict[k[1]] = k[0]

# 读取ncbi分类文件
with gzip.open(args.ncbiTax,"rt") as f2:
	taxList = []
	for line in f2:
		v = line.strip('\n').split('\t')
		if v[0] in cleanDict.keys():
			newline = cleanDict[v[0]] + "\t" +v[2]
			taxList.append(newline)

# 转换格式
outDict = {}
for k in taxList:
	value,key = k.split("\t")
	new_v = outDict.get(key,'')
	if new_v:
		outDict[key] = new_v +'\t'+value
	else:
		outDict[key] = value
with open(args.outFile,"w") as f3:
	for k in outDict.keys():
		f3.write(k+"\t"+outDict[k]+"\n")
