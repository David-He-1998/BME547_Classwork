#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:12:57 2022

@author: david
"""
from db_def import Patient
from pymodm.connection import connect


def test_add_patient():
    from db_server import add_patient
    test = {"name": "David", "id": 3, "blood type": "B+"}
    connect("mongodb+srv://davidhe:password@cluster0.grsdcun.mongodb.net/test?"
            "retryWrites=true&w=majority")
    # Remove password for safety reasons
    # add_patient(test, True)
    # new = Patient.objects.raw({"name": "David"}).first()
    # new.delete()
    # assert new == Patient(name="David", ID=3, blood_type='B+')


def test_add_test():
    from db_server import add_patient, add_test
    test = {'name': "Ceasar", 'id': 3, 'blood type': 'B-'}
    connect("mongodb+srv://davidhe:password@cluster0.grsdcun.mongodb.net/test?"
            "retryWrites=true&w=majority")
    add_patient(test, True)
    test = {'test_name': "HDL", 'id': 3, 'test_result': 'Normal'}
    msg, status = add_test(test, True)
    new = Patient.objects.raw({"_id": 3}).first()
    new.delete()
    assert new == Patient(name="Ceasar", ID=3, blood_type="B-",
                          test_name=["HDL"], test_result=["Normal"])
