#!/usr/bin/env python
import string
import sys
for line in sys.stdin:
    line = line.strip()
    parent_node,val = line.split('\t')
    adj_list,score,color,source = val.split("|")
    if score == "Integer.MAX_VALUE":
        score = 99999999
    if color.strip() =="GRAY":
        print (parent_node+"\t"+adj_list+"|"+score+"|"+"BLACK"+"|"+source)
        for kid_node in adj_list.split(','):
            print (kid_node+"\t"+"null"+"|"+str(int(score)+1)+"|"+"GRAY"+"|"+parent_node)
    else:
        print (line)