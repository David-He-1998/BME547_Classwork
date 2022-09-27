#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:30:51 2022

@author: david
"""


class Patient:
    '''
    def __init__(self):
        self.First_name = ""
        self.Last_name = ""
        self.Id = ""
        self.age = ""
        self.test = ""
    '''
    def __init__(self, first_name, last_name, Id, age, test):
        self.First_name = first_name
        self.Last_name = last_name
        self.Id = Id
        self.age = age
        self.test = test

    def get_full_name(self):
        full_name = "{} {}".format(self.First_name, self.Last_name)
        return full_name


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

    db = {}
    db[11] = (patient_entry("Ann", "Ables", 11, 30, ''))
    db[22] = (patient_entry("Bob", "Boyles", 22, 34, ''))
    db[3] = (patient_entry("Charis", "Chou", 3, 23, ''))
    return db
    '''
    db = {}
    db[11] = Patient("Ann", "Ables", 11, 30, [])
    db[22] = Patient("Bob", "Boyles", 2, 34, [])
    db[3] = Patient("Charis", "Chou", 3, 23, [])
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
        if db[patient].Id == index:
            return patient
    return False


def add(entry, Test, test_result):
    entry.test = (Test, test_result)
    return entry


def patient_entry(First_name, Last_name, ID, Age, Tests):
    new_patient = Patient()
    new_patient.First_name = First_name
    new_patient.Last_name = Last_name
    new_patient.Id = ID
    new_patient.age = Age
    new_patient.test = Tests
    return new_patient
    # dictionary = {"First Name": First_name, "Last Name": Last_name,
    #              "Id": ID, "Age": Age, "Tests": Tests}
    # return dictionary


def print_db(db):
    for patient_key in db:
        # print("Name: {}, Id: {}, age: {}".format(get_full_name(db[patient]),
        #                                         db[patient]["Id"],
        #                                         db[patient]["Age"]))
        print("Name: {}, Id: {}, age: {}".format(
                db[patient_key].get_full_name(), db[patient_key].Id,
                db[patient_key].age, db[patient_key].test))
    print("Method 2")
    for patient in db.values():
        print("Name: {}, Id: {}, age: {}".format(patient.get_full_name(),
              patient.Id, patient.age, patient.test))


def adult_or_minor(patient):
    if patient.age >= 18:
        return "Adult"
    else:
        return "Minor"


if __name__ == "__main__":
    # db = main()
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
    '''
    patient = search(db, 3)
    if patient is not False:
        print("The patient is {}".format(adult_or_minor(db[patient])))
        add(db[patient], 'HDL', 40)
        print_db(db)
    '''
    patient = Patient("Ziwei", "He", 44, 30, ['HDL', 40])
    print("Full name:{}, ID:{}, Age:{}, test:{}".format(
          patient.get_full_name(), patient.Id, patient.age, patient.test))
    print(type(patient))
    # patient1 = patient_entry("Ann", "Ables", 1, 30, ["HDL", 40])
    # print("{}, age {}".format(patient1.get_full_name(), patient1.age))
    db = main()
    print_db(db)
    index = search(db, 3)
    add(db[index], "HDL", 100)
    print("Patient {} is {}".format(db[index].get_full_name(),
          adult_or_minor(db[index])))
