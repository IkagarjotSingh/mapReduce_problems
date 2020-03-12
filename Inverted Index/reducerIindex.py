#!/usr/bin/env python

import sys
import string

prev_key = None
fName = None
total_count = 0

for line in sys.stdin:
    line = line.rstrip()
    
    key,value = line.split("\t")
    file_name,count = value.split(":")
    if prev_key == None:
        prev_key = key
        total_count = int(count)
        fName = file_name
        continue
    if prev_key == key: 
        if fName == file_name:
            total_count = total_count + int (count)
            continue
        else:
            print (prev_key+"\t"+fName+":"+str(total_count))
            fName = file_name
            total_count = int (count)
    if prev_key!=key:
        #Output Key Value pair will be of the form (<word,file_name:total_count>)
        print (prev_key+"\t"+fName+":"+str(total_count))
    prev_key = key
    fName = file_name
    total_count = int(count)
#Output Key Value pair will be of the form (<word,file_name:total_count>)
print (str(prev_key)+"\t"+fName+":"+str(total_count))