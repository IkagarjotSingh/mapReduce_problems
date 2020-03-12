#!/usr/bin/env python

import string
import sys

prev_key = None
for word in sys.stdin:
    word = word.rstrip()
    word = word.split("\t")[1]
    if prev_key==None:
        prev_key=word
        continue
    if prev_key==word:
        continue
    if prev_key!=word:
        print (prev_key)
    prev_key=word
print (prev_key)