#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:57:52 2019

@author: emreyuksel
"""
from itertools import permutations
n = int(input("n sayısını giriniz: "))
yasaklı = []
permsayı = []
for i in range(n):
    print("X%d sayısını giriniz: " % (i+1))
    X=list(map(int,input().split(',')))
    yasaklı.append(X)
for a in range(1,n+1):
    permsayı.append(a)
permütasyonlar = list(permutations(permsayı))
permütasyonlaryedek = list(permutations(permsayı))
for number in range(10):
    for sayi in range(n):
        for pozisyon in yasaklı[sayi]:
            if pozisyon == 0:
                pass
            else:
                for iterasyon in permütasyonlar:
                    if iterasyon[pozisyon-1] == sayi+1:
                        permütasyonlaryedek.remove(iterasyon)
            permütasyonlar = permütasyonlaryedek
        
print(permütasyonlaryedek)
print("Permütasyonların sayısı: {}".format(len(permütasyonlaryedek)))