#!/usr/bin/env python3

import gzip
import argparse

parser = argparse.ArgumentParser(description="用途：统计双端fastq序列文件数据量、reads数、q30比例、GC含量")
parser.add_argument("-i",dest="read1",metavar="",help="read1文件")
parser.add_argument("-ii",dest="read2",metavar="",help="read2文件")
args = parser.parse_args()

# read R1
with gzip.open(filename,"rt") as fq1:
	num1 = 0
	count1 = 0
	q30_1 = 0
	gc_1 = 0	
	while True:
		line_1 = fq1.readline().strip('\n')
		if not (line_1 and fq):
			break
		line_2 = fq1.readline().strip('\n')
		line_3 = fq1.readline().strip('\n')
		line_4 = fq1.readline().strip('\n')
		for q in line_4:
			qual = ord(q)-33
			if qual >=30:
				q30 +=1
		NUM +=len(line_2)
		count += 1
		gc += line_2.count("G")+line_2.count("C"
											 
# read R2
with gzip.open(args.read2,"rt") as fq2:
	num2 = 0
	count2 = 0
	q30_2 = 0
	gc_2 = 0
	while True:
		line_1 = fq2.readline().strip('\n')
		if not (line_1 and fq2):
			break
		line_2 = fq2.readline().strip('\n')
		line_3 = fq2.readline().strip('\n')
		line_4 = fq2.readline().strip('\n')
		for q in line_4:
			qual = ord(q)-33
			if qual >=30:
				q30_2 +=1
		num2 +=len(line_2)
		count2 +=1
		gc_2 +=line_2.count("G")+line_2.count("C")

totalBase = num1 + num2
totalReads = count1 + count2
GC =gc_1 + gc_2
Q30 = q30_1 + q30_2

name = args.read1.split("_")[0]											 
											
print(name,end='\t')
print(totalBase/1000000,end='\t') # 碱基数目（单位：百万）											 
print(totalReads,end='\t') # 总reads数目
print('%.2f' % (Q30/totalBase*100),end='\t') # q30比例%
print('%.2f' % (GC/totalBase*100)) # GC含量


