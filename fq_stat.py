#!/usr/bin/env python3

import gzip
import argparse

parser = argparse.ArgumentParser(description="用途：统计双端fastq序列文件数据量、reads数、q30比例、GC含量")
parser.add_argument("-i",dest="read1",metavar="",help="read1文件")
parser.add_argument("-ii",dest="read2",metavar="",help="read2文件")
args = parser.parse_args()

# read fq file
def fun_stat(Fq):
    with gzip.open(Fq,"rt") as fq:
        baseNums = 0; counts = 0
        q30 = 0; gc = 0
        while True:
            line_1 = fq.readline().strip('\n')
            if not (line_1 and fq):  #检查是否已经读完，不然会报错
                break
            line_2 = fq.readline().strip('\n')
            line_3 = fq.readline().strip('\n')
            line_4 = fq.readline().strip('\n')          
            for q in line_4:
                qual = ord(q)-33
                if qual >=30:
                    q30 +=1
            baseNums += len(line_2)
            counts += 1
            gc += line_2.count("G")+line_2.count("C")
        return baseNums,counts,gc,q30

fq1 = fun_stat(args.read1)
fq2 = fun_stat(args.read2)

totalBase = fq1[0] + fq2[0] #总碱基数
readNums = fq1[1] #reads数
GC =fq1[2] + fq2[2]
Q30 = fq1[3] + fq2[3]

name = args.read1.split("_")[0]
        
print(name,end='\t') # 样品名
print(totalBase/1000000,end='\t') # 碱基数目（单位：百万）
print(readNums,end='\t') # 总reads数目
print('%.2f' % (Q30/totalBase*100),end='\t') # q30比例%
print('%.2f' % (GC/totalBase*100)) # GC含量

