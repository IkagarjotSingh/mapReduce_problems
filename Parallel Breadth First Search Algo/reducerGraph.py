#!/usr/bin/env python
import string
import sys

p_node = ""
node_adj_list = ""
min_score = 99999999
darkest_color = ""
min_source = ""

for line in sys.stdin:
    line = line.rstrip()
    c_node,val = line.split('\t')
    c_adj_list,c_score,c_color,c_source = val.split("|")
    if c_score == "Integer.MAX_VALUE":
        c_score = 99999999
    
    if p_node == "":
        p_node = c_node
    if c_node != p_node:
        print (record)
        p_node = c_node
        node_adj_list = c_adj_list
        min_score = c_score
        darkest_color = c_color
        min_source = c_source
        record =  c_node+"\t"+node_adj_list+"|"+str(min_score)+"|"+darkest_color+"|"+str(min_source)
        
    else:
        if c_adj_list != "null":
            node_adj_list = c_adj_list
        if int(c_score) <= int(min_score):
            min_score = c_score
            min_source = c_source

        if c_color == "BLACK" or darkest_color == "BLACK":
            darkest_color = "BLACK"
        elif c_color == "GRAY" or darkest_color == "GRAY":
            sys.stderr.write("reporter:counter:reducerGraph,toBeProcessedCounter,1\n")
            darkest_color = "GRAY"
        else:
            sys.stderr.write("reporter:counter:reducerGraph,toBeProcessedCounter,1\n")
            darkest_color = "WHITE"
        
        record =  c_node+"\t"+node_adj_list+"|"+str(min_score)+"|"+darkest_color+"|"+str(min_source)
    
print (record)   