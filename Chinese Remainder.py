#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:18:29 2019

@author: emreyuksel
"""

print('x=mod(y) olacak şekilde sistemin ilk x değerlerini daha sonra y değerlerini giriniz.')
x = list(map(int,input().split(',')));
y = list(map(int,input().split(',')));
i=0;
X=0;
j=1;
eklencekterim=1;
ilkeleman=x[0];
listem=[0] * max(y);
modlist=[0] * max(y);
for i in range(len(y)-1):
    eklencekterim=eklencekterim*y[i];
    listem=[0]*max(y);
    for j in range(y[i+1]):
        listem[0] = ilkeleman;
        listem[j] = listem[j] + listem[j-1] + eklencekterim;
        modlist[0] = ilkeleman % y[i+1];
        modlist[j] = listem[j] % y[i+1];
    ilkeleman = listem[modlist.index(x[i+1])];
X = ilkeleman;
print('İstenilen X sayısı:',X)