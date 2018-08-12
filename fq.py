
import sys
import gzip

args = sys.argv
filename = args[1]

NUM = 0
count = 0
q30 = 0
with open(filename,"r") as fq:
	while True:
		line_1 = fq.readline().strip('\n')
		if not (line_1 and fq):
			break
		line_2 = fq.readline().strip('\n')
		line_3 = fq.readline().strip('\n')
		line_4 = fq.readline().strip('\n')
		NUM +=len(line_2)

		for q in line_4:
			qual = ord(q)-33
			if qual >=30:
				q30 +=1
		
		
with open(filename,"r") as fq:
	while True:
		buffer = fq.read(8*1024*1024)
		if not buffer:
			break
		count +=buffer.count('\n')

print(filename,end='\t')
print(int(count/4),end='\t')
print(NUM/1000000,end='\t')
print('%.2f' % (q30/NUM*100))


