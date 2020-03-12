#!/usr/bin/env python
from __future__ import division
import string
import sys


prod1_total_occurence = 0
prod1_prod2_cooccurence = 0
prev_primary_prod = ""
prev_secondary_prod = ""

for line in sys.stdin:
    line = line.rstrip()
    prod_1,prod_2,count = line.split()
    if (prev_primary_prod == prev_secondary_prod == ""):
        prev_primary_prod = prod_1
        prev_secondary_prod = prod_2
    if prod_1 == prev_primary_prod:
        if prod_2 == prev_secondary_prod:
            if prod_2 == "*":
                prod1_total_occurence = prod1_total_occurence +int(count)
            else:        
                prod1_prod2_cooccurence = prod1_prod2_cooccurence + int(count)
        elif prod_2 != prev_secondary_prod:
            if prod_2 == "*":
                prod1_total_occurence = prod1_total_occurence +int(count)
            else:
                if prev_secondary_prod != "*":
                    #Swap the primary and secondary product values inorder to make sure the results are in sync with the formula.
                    print (prev_secondary_prod+"\t"+prev_primary_prod+"\t"+str(prod1_prod2_cooccurence/prod1_total_occurence))        
            prev_primary_prod = prod_1
            prev_secondary_prod = prod_2
            prod1_prod2_cooccurence = int(count)
    else:
        print (prev_secondary_prod+"\t"+prev_primary_prod+"\t"+str(prod1_prod2_cooccurence/prod1_total_occurence))
        prev_primary_prod = prod_1
        prev_secondary_prod = prod_2
        if prev_secondary_prod == "*":
            prod1_total_occurence = int(count)
        else:
            prod1_prod2_cooccurence = int(count)   
print (prev_secondary_prod+"\t"+prev_primary_prod+"\t"+str(prod1_prod2_cooccurence/prod1_total_occurence))