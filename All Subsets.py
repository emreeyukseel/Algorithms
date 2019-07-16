#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:22:28 2019

@author: emreyuksel
"""

    
def allsubset():
    array = list(map(str,input().split(',')));
    lastsubset = [];
    counter=0;
    
    for i in range(0, 2**len(array)):
        tempset = [];
        num_bin = "{0:b}".format(i)
        
        while len(num_bin) < len(array):
            num_bin = '0' + num_bin
        
        for k in range(0,len(num_bin)):
            if num_bin[k] == '1':
                tempset.append(array[k])          
        lastsubset.append(tempset)
        counter+=1;
        lastsubset.sort()
    return lastsubset, "The number of subsets of set you entered: {}".format(counter)

