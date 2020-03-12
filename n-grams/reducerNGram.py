#!/usr/bin/env python

import string
import sys

#provide initial values to variables.
prev_key = None
tot_count = 0
for line in sys.stdin:
    line = line.rstrip()
    word,count = line.split('\t')
    if prev_key==None:
        prev_key=word
        tot_count=int(count)
        continue
    if prev_key==word:
        tot_count=tot_count+int(count)
        continue
    if prev_key!=word:
        print (str(prev_key)+"\t"+str(tot_count))
	prev_key=word
	tot_count=int(count)
print (str(prev_key)+"\t"+str(tot_count))