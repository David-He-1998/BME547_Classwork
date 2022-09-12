#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:28:17 2022

@author: david
"""
weight = 20 / 2.205
dosage = weight * 30

print("CORRECT DOSAGE")
print("For a patient weighing {} kg,".format(round(weight,1)))
print("  the correct dosage is {} mg the first day".format(dosage))