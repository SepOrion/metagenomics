#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description="用途：计算contigs序列N50、N90、GC含量等，输出结果从左到右为：样品名、碱基总数、contigs总数、平均长度、N50、N90、最长contigs、最短contigs、GC含量")
parser.add_argument("-i",dest="contigs",metavar="",help="输入文件：组装生成的contigs文件")
args = parser.parse_args()

L = []
gc = 0
N50_num = 0
N90_num = 0

with open(args.contigs) as fa:
	for line in fa:
		if line.startswith(">"):
			seqLine = next(fa).strip("\n")
			seq_len = len(seqLine) #每条序列长度
			L.append(seq_len)
			gc += seqLine.count("G")+seqLine.count("C") # GC总数

len_sorted = sorted(L,reverse=True) # 从长到短排序
Total_len = sum(len_sorted)
Max_len = max(len_sorted)
Min_len = min(len_sorted)
contigNum = len(len_sorted)
Avg_len  = '%.2f' % (Total_len/contigNum)
GC = '%.2f' % (gc/Total_len*100)

for value in len_sorted:
	N50_num += value
	if N50_num/Total_len>0.5:
		N50 = value
		break

for value in len_sorted:
	N90_num += value
	if N90_num/Total_len>0.9:
		N90 = value
		break
print(args.contigs,end="\t")
print(Total_len,end="\t") # 碱基总数
print(contigNum,end="\t")   # contigs总数
print(Avg_len,end="\t") #平均长度
print(N50,end="\t") # N50
print(N90,end="\t") # N90
print(Max_len,end="\t") #最长contigs
print(Min_len,end="\t") #最短contigs
print(GC,end="\t")  #GC含量
