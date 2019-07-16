#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:18:29 2019

@author: emreyuksel
"""

print('Please enter first x values, then y values so that x=mod(y).')
x = list(map(int,input().split(',')));
y = list(map(int,input().split(',')));
i=0;
X=0;
j=1;
plus=1;
firstelem=x[0];
mylist=[0] * max(y);
modlist=[0] * max(y);

for i in range(len(y)-1):
    plus=plus*y[i];
    mylist=[0]*max(y);
    for j in range(y[i+1]):
        mylist[0] = firstelem;
        mylist[j] = mylist[j] + mylist[j-1] + plus;
        modlist[0] = firstelem % y[i+1];
        modlist[j] = listem[j] % y[i+1];
    firstelem = mylist[modlist.index(x[i+1])];
    
X = firstelem;
print('X number:',X)
