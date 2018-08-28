#!/usr/bin/env python

# Useage:merge_abundance_table.py <output_file>
# 用于合并每个样品的丰度表，从而获得矩阵

import glob
import argparse
import pandas as pd
parser = argparse.ArgumentParser(description="用途：合并样品注释丰度表，包括物种分类、kegg注释、抗性基因注释等。格式要求：第一列为注释分类名，第二列为丰度值，tab键分割")
parser.add_argument("-i",dest="inputFile",metavar="",help="需要合并文件名的关键词")
parser.add_argument("-o",dest="outFile",metavar="",help="输出文件")
args = parser.parse_args()

fileList = glob.glob('*'+args.inputFile+'*')

dfs = [pd.read_table(filename,index_col=[0]) for filename in fileList]

outputTable = dfs[0].join(dfs[1:])
outputTable.to_csv(args.outFile,sep = "\t")
