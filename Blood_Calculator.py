#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:28:31 2022

@author: david
"""

def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    run_tag = True
    while run_tag:
        choice = input("Enter your choice: ")
        if choice=='9':
            return
   
interface()