#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser(description="It was used to calculate contigs  N50, N90, GC content and so on：sampleid、total_bases(Mbp)、total_contigs(#)、avLength(bp)、N50(bp)、N90(bp)、longest_contigs(bp)、shortest_contigs(bp)、GC含量(%)")
parser.add_argument("-i","--intput",dest="contigs",metavar="",help="Input file：contigs.fa")
parser.add_argument("-l","--contigs_length",dest="contigs_length",metavar="",default=500,type = int,help="All statistics are based on contigs of size,(default 500)")
parser.add_argument("-f","--file_name",dest="sample_name",metavar="",default="sample",help="Output file name")
args = parser.parse_args()

seq={}
with open(args.contigs) as fa:
	for line in fa:
		if line.startswith(">"):
			seq_name = line.split()[0]
			seq[seq_name] = ''
		else:
			seq[seq_name]+=line.replace('\n', '')

L = []
GC = 0
for value in seq.values():
    if len(value) >=args.contigs_length:        #设定统计contigs长度阈值
        L.append(len(value))
        GC += value.count("G")+value.count("C")
    
L_sorted = sorted(L,reverse=True) # 从长到短排序
Total_len = sum(L_sorted)

Max_len = max(L_sorted)
Min_len = min(L_sorted)

contigNum = len(L_sorted)
Avg_len  = '%.2f' % (Total_len/contigNum)
GC_percentage = '%.2f' % (GC/Total_len*100)

N50_num = 0
N90_num = 0
for value in L_sorted:
    N50_num += value
    if N50_num/Total_len>0.5:
        N50 = value
        break

for value in L_sorted:
    N90_num += value
    if N90_num/Total_len>0.9:
        N90 = value
        break
        
print(args.sample_name,end="\t")
print(Total_len/1000000,end="\t") # 碱基总数
print(contigNum,end="\t")   # contigs总数
print(Avg_len,end="\t") #平均长度
print(N50,end="\t") # N50
print(N90,end="\t") # N90
print(Max_len,end="\t") #最长contigs
print(Min_len,end="\t") #最短contigs
print(GC_percentage)  #GC含量
