#!/usr/bin/env python

import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
        word = word.strip()
        if len(word)>=1:
            if word[0] in ['a','b','c','d','e','f','g','h']:
                print (str("a")+"\t"+word)
            elif word[0] in ['i','j','k','l','m','n','o','p']:
                print (str('b')+"\t"+word)
            elif word[0] in ['q','r','s','t','u','v','w','x','y','z']:
                print (str('c')+"\t"+word)
            else:
                print (str('d')+"\t"+word)