#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:57:52 2019

@author: emreyuksel
"""
from itertools import permutations
n = int(input("Please enter n: "))
forbidden = []
permnumber = []

for i in range(n):
    print("Enter X%d: " % (i+1))
    X=list(map(int,input().split(',')))
    forbidden.append(X)
for a in range(1,n+1):
    permnumber.append(a)
    
permütasyonlar = list(permutations(permnumber))
permütasyonlarcopy = list(permutations(permnumber))

for number in range(10):
    for numb in range(n):
        for pozisyon in forbidden[numb]:
            if pozisyon == 0:
                pass
            else:
                for iterasyon in permütasyonlar:
                    if iterasyon[pozisyon-1] == numb+1:
                        permütasyonlarcopy.remove(iterasyon)
            permütasyonlar = permütasyonlarcopy
        
print(permütasyonlarcopy)
print("Permütasyonların sayısı: {}".format(len(permütasyonlarcopy)))
