#!/usr/bin/env python
import string
import sys
import random

#read stdin and split the lines.
doc = sys.stdin.read().splitlines()  

#compute total number of lines comprising of stdin.
total_lines = len(doc) 

#Sample 10% of the lines randomly.
sample_lines = random.sample(doc,total_lines/10)

for line in sample_lines:
    line = line.strip()
    line = line.lower()
    print (line)