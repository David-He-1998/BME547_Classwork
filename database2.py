#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:30:51 2022

@author: david
"""

def patient_entry(patient_name,patient_id,patient_age): # For the ease of future modification.
    new_patient=[patient_name, patient_id, patient_age, []] # For example, you need to add a new entry.
    return new_patient                                     # In this case, you only need to change here

def main():
    db=[]
    db.append(patient_entry("Ann Ables", 1, 30))
    db.append(patient_entry("Bob Boyles", 2, 34))
    db.append(patient_entry("Charis Chou", 3, 23))
    return db

def list_all(db):
    for i in db:
        print("Name: {},ID: {}, Age: {}".format(i[0],i[1],i[2]))

def search(db,index):
    for i,content in enumerate(db):
        if content[1]==index:
            return i,content
    return False,False
    
def add(entry,test,test_result):
    entry[-1]=(test,test_result)
    return entry
    

if __name__ == "__main__":
    entry=main()
    #list_all(entry)
    #output=search(entry,4)
    #print(output)
    index,patient=search(entry,3)
    if index!=False:
        add(patient,'HDL',40)
        entry[index]=patient
        print(entry[index])
    