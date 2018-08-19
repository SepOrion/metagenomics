#/usr/bin/env python3

import sys
import gzip

args = sys.argv
filename = args[1]
name = filename.split("_")[0]

NUM = 0
count = 0
q30 = 0
gc = 0

with gzip.open(filename,"rt") as fq:
	while True:
		line_1 = fq.readline().strip('\n')
		if not (line_1 and fq):
			break
		line_2 = fq.readline().strip('\n')
		line_3 = fq.readline().strip('\n')
		line_4 = fq.readline().strip('\n')
		for q in line_4:
			qual = ord(q)-33
			if qual >=30:
				q30 +=1
		NUM +=len(line_2)
		count += 1
		gc += line_2.count("G")+line_2.count("C"

print(name,end='\t')
print(count,end='\t')
print(NUM/1000000,end='\t')
print('%.2f' % (q30/NUM*100))


