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
    print("3 - Check the total cholesterol")
    print("9 - Quit")
    run_tag = True
    while run_tag:
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()
        elif choice == '3':
            Chol_driver()

def user_input():
    while True:
        value = input("Please input your corresponding value, press enter to confirm:")
        if str.isdigit(value) == False:
            print("Please input a positive integer to continue")
        else:
            break
    return int(value)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif HDL_value >= 40:
        return "Borderline Low"
    else:
        return "Low"
    
    
def check_LDL(LDL_value):
    if LDL_value >= 190:
        return "Very High"
    elif LDL_value >= 160:
        return "High"
    elif LDL_value >= 130:
        return "Borderline High"
    else:
        return "Normal"
    
#Cholesterol  
def check_chol(chol_value): 
    if chol_value >= 240:
        return "High"
    elif chol_value >= 200:
        return "Borderline High"
    else:
        return "Normal"
    
def HDL_driver():
    hdl_value = user_input()
    ans = check_HDL(hdl_value)
    print("The result of your HDL is {} and {}".format(hdl_value, ans))
    
    
def LDL_driver():
    ldl_value = user_input()
    ans = check_LDL(ldl_value)
    print("The result of your LDL is {} and {}".format(ldl_value, ans))
    
    
def Chol_driver():
    chol_value = user_input()
    ans = check_chol(chol_value)
    print("The result of your total cholesterol is {} and {}".format(chol_value, ans))
     
       
if __name__ == "__main__":   
    interface()             
# If the script is on main module, excute the interface command.  
# If the script is imported as module, this command will not be executed
    