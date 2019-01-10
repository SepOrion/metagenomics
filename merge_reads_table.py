#!/usr/bin/env python3
# Usage :
# merge_reads_table.py --input txt --output reads_table.txt

import glob
import argparse
import pandas as pd
from pandas import DataFrame

parser = argparse.ArgumentParser(description=
								 "用于合并来自samtools统计reads的文件\n"
								"Usage :merge_reads_table.py --input txt --output reads_table.txt",formatter_class = argparse.RawTextHelpFormatter)
parser.add_argument("--filename",dest="inputFile",metavar="",help="需要合并文件的关键词")
parser.add_argument("--output",dest="outFile",metavar="",help="输出文件名")
args = parser.parse_args()

file_list = glob.glob('*'+args.inputFile+'*')

dfs = []
for filename in file_list:
	newName = filename.split('.')[0]
	df = pd.read_table(filename,index_col=[0,1],header=None)
	df1 = DataFrame(df,columns=[2])
	df1.columns=[newName]
	dfs.append(df1)

merge_dfs = dfs[0].join(dfs[1:])
merge_dfs.index.names=['Gene_ID','Length']
merge_dfs.to_csv(args.outFile,sep="\t")
