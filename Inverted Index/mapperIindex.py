#!/usr/bin/env python
import sys
import os
import string

for line in sys.stdin:
    #Since we need to know which word is coming from which txt file.
    #os.environ["map_input_file"] provides the complete path of the file.
    file_name = os.environ["map_input_file"] 

    #Sample file name : hdfs://10.1.3.45:9000/user/15.txt
    
    #Now, we need to split the file name based on / to get the file name.
    #Assuming we are not bothered about the complete path where the file is stored.
    file_name = file_name.split("/")[-1]
    #file name after splitting : 15.txt

    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word = word.replace(c,"")
        #Intermediate Key Value pair will be of the form (<word,file_name:1>)
        print (word+"\t"+file_name+":1")