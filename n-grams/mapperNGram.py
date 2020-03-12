#!/usr/bin/env python

import string
import sys
import nltk

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    
    for char in string.punctuation:
        line = line.replace(char,"") #Remove the punctuations
        #Create bigrams
        biGrams = nltk.ngrams(line.split(),n=2)
    for val in biGrams:
        #Print bigrams with count 1 as intermediate Key Value Pair.
        print (str(val) +"\t"+str(1))
