#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:30:51 2022

@author: david
"""


# For the ease of future modification
# For example, you need to add a new entry.
# In this case, you only need to change here
'''
def patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient
'''


def main():
    '''
    db = []
    db.append(patient_entry("Ann Ables", 1, 30))
    db.append(patient_entry("Bob Boyles", 2, 34))
    db.append(patient_entry("Charis Chou", 3, 23))
    return db
    '''
    db = {}
    db[11] = (patient_entry("Ann", "Ables", 1, 30, ''))
    db[22] = (patient_entry("Bob", "Boyles", 2, 34, ''))
    db[33] = (patient_entry("Charis", "Chou", 3, 23, ''))
    return db


def list_all(db):
    for i in db:
        print("Name: {},ID: {}, Age: {}".format(i[0], i[1], i[2]))


def search(db, index):
    '''
    for i, content in enumerate(db):
        if content[1] == index:
            return i, content
    return False, False
    '''
    for patient in db:
        if db[patient]['Id'] == index:
            return patient
    return False


def add(entry, test, test_result):
    entry[test] = test_result
    return entry


def patient_entry(First_name, Last_name, ID, Age, Tests):
    dictionary = {"First Name": First_name, "Last Name": Last_name,
                  "Id": ID, "Age": Age, "Tests": Tests}
    return dictionary


def get_full_name(patient):
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name


def print_db(db):
    for patient in db:
        print("Name: {}, Id: {}, age: {}".format(get_full_name(db[patient]),
                                                 db[patient]["Id"],
                                                 db[patient]["Age"]))


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "Adult"
    else:
        return "Minor"


if __name__ == "__main__":
    db = main()
    # list_all(entry)
    # output=search(entry,4)
    # print(output)
    '''
    index, patient = search(entry, 3)
    if index is not False:
        add(patient, 'HDL', 40)
        entry[index] = patient
        print(entry[index])
    '''

    patient = search(db, 3)
    if patient is not False:
        print("The patient {} is {}".format(get_full_name(db[patient]),
              adult_or_minor(db[patient])))
        add(db[patient], 'HDL', 40)
        print_db(db)
