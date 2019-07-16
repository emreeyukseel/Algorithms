#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:54:59 2019

@author: emreyuksel
"""

def permutations(list):
    if len(list) == 0:
        return []
    elif len(list) == 1:
        return [list]
    else:
        perms = permutations(list[1:]);
        firstelem = list[0]
        allperms=[];
        for perm in perms:
            for i in range(len(perm)+1):
                allperms.append(perm[:i] + [firstelem] + perm[i:])
        return allperms
