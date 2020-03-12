#!/usr/bin/env python
import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    for i in range(len(line)):
        for j in range(len(line)):
            if (line[i]!=line[j]):
                print (line[i]+"\t"+"*"+"\t"+str(1))
                print (line[i]+"\t"+line[j]+"\t"+str(1))