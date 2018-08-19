#!/usr/bin/env python3
# 用于计算相关注释分类丰度：kegg，物种分类等

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g",dest="geneAbundance",metavar="",help="样品基因丰度表：第一列为基因ID，第二列为丰度值")
parser.add_argument("-a",dest="annot",metavar="",help="注释文件：第一列为注释ID，其余各列为对应的基因ID")
#parser.add_argument("-o",dest="output",metavar="",help="输出文件名")
args = parser.parse_args()

ab = {}
with open(args.geneAbundance) as F:
	for a in F:
		k = a.strip("\n").split("\t")
		ab[k[0]] = k[1]

with open(args.annot) as an:
	myDict = {}
	for line in an.readlines():
		num = 0
		array = line.strip("\n").split("\t")
		myDict[array[0]] = ''
		for value in array[1:]:
			if value in ab.keys():
				num +=float(ab[value])
			else:
				continue
		myDict[array[0]] = num

outputName = ab['Gene_ID']+"_abundance.txt"
with open(outputName,"wt") as outFile:
	for k in myDict.keys():
		outFile.write(k+"\t")
		outFile.write(str(myDict[k]))
		outFile.write("\n")
