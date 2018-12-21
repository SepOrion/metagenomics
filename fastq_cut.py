#!/usr/bin/env python3

# Usage :fastq_cut.py -i sample.fq.gz -o sample_cut.fq.gz --cut_f 5 --cut_r 5

import gzip
import argparse as ap

parser = ap.ArgumentParser(description=
"用途：用于截取fastq文件序列\n"
"Example:前后各截取5个碱基：fastq_cut.py -i sample.fq.gz -o sample_cut.fq.gz --cut_f 5 --cut_r 5",formatter_class = ap.RawTextHelpFormatter)
parser.add_argument("-i",dest="inputFile",metavar="",help="输出fastq文件，gzip压缩")
parser.add_argument("-o",dest="outputFile",metavar="",help="输出文件名，gzip压缩")
parser.add_argument("--cut_f",dest="cut_f",metavar="",default=0,help="前面截取的碱基数，默认0",type=int)
parser.add_argument("--cut_r",dest="cut_r",metavar="",default=1,help="后面截取的碱基数，默认0",type=int)
args = parser.parse_args()

with gzip.open(args.outputFile,"wt") as output:
    with gzip.open(args.inputFile,"rt") as fq:
        while True:
            line_1 = fq.readline().strip("\n")
            if not (line_1 and fq):
                break
            line_2 = fq.readline().strip("\n")[args.cut_f:][:-args.cut_r]
            line_3 = fq.readline().strip("\n")
            line_4 = fq.readline().strip("\n")[args.cut_f:][:-args.cut_r]
            output.write(line_1+"\n")
            output.write(line_2+"\n")
            output.write(line_3+"\n")
            output.write(line_4+"\n")            

