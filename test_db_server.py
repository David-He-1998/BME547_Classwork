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
    connect("mongodb+srv://davidhe:wzhOWNEK@cluster0.grsdcun.mongodb.net/test?"
            "retryWrites=true&w=majority")
    add_patient(test, True)
    new = Patient.objects.raw({"name": "David"})
    new.delete()
    #  assert new == Patient(name="David", ID=3, blood_type="B+")
