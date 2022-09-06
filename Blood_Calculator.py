#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:28:31 2022

@author: david
"""

def interface():
    print("My Program")
    print("Options:")
    print("1 - Check HDL value")
    print("2 - Check LDL value")
    print("9 - Quit")
    run_tag = True
    while run_tag:
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='1':
            HDL_driver()
        elif choice=='2':
            LDL_driver()

def user_input():
    value = input("Please input your HDL value, press enter to confirm:")
    return int(value)

def check_HDL(HDL_value):
    if HDL_value>=60:
        return "Normal"
    elif HDL_value>=40:
        return "Borderline Low"
    else:
        return "Low"
    
def check_LDL(LDL_value):
    if LDL_value>=190:
        return "Very high"
    elif LDL_value>=160:
        return "High"
    elif LDL_value>=130:
        return "Borderline high"
    else:
        return "Normal"
    
def HDL_driver():
    hdl_value=user_input()
    ans=check_HDL(hdl_value)
    print("The result of your HDL is {} and {}".format(hdl_value,ans))
    
def LDL_driver():
    ldl_value=user_input()
    ans=check_LDL(ldl_value)
    print("The result of your LDL is {} and {}".format(ldl_value,ans))
    

    
    
            
   
interface()