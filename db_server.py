#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:21:17 2022

@author: david

Database format1:
    {'id':{
        'name': str,
        'id': int,
        'test':{'test_name1': [<test_result>], ...}},
        ...}
Database format2:
    [{
      'name': str
      'id': int
      'blood type': str
      'test_name': [str]
      'test_result': [str]
      }]
"""
from flask import Flask, request, jsonify
from pymodm.connection import connect
from pymodm import errors as pymodm_er
from db_def import Patient
app = Flask(__name__)


db = []


def add_patient(in_data, check):
    if check is not True:
        message = check
        return message, 400
    # new_patient = {'name': in_data['name'], 'id': in_data['id'],
    #                'blood type': in_data['blood type'], 'test_name': [],
    #                'test_result': []}
    ex_bloodtype = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']
    if in_data['blood type'] not in ex_bloodtype:
        message = "Wrong blood type"
        return message, 400
    new_patient = Patient(name=in_data['name'], ID=in_data['id'],
                          blood_type=in_data['blood type'])
    db.append(new_patient)
    new_patient.save()
    message = "Patient added successfully"
    return message, 200


def validate_info_patient(in_data):
    if type(in_data) is not dict:
        return "Patient data should be in a dictionary"
    expect_keys = ["name", "id", "blood type"]
    expect_type = [str, int, str]
    for key, ex_type in zip(expect_keys, expect_type):
        if key not in in_data:
            return "Key {} is missing".format(key)
        if type(in_data[key]) != ex_type:
            return "Key {}'s value has wrong data type".format(key)
    return True


def validate_test(in_data):
    if type(in_data) is not dict:
        return "Patient data should be in a dictionary"
    expect_keys = ["test_name", "id", "test_result"]
    expect_type = [str, int, int]
    for key, ex_type in zip(expect_keys, expect_type):
        if key not in in_data:
            return "Key {} is missing".format(key)
        if type(in_data[key]) != ex_type:
            return "Key {}'s value has wrong data type".format(key)
    return True


def add_test(in_data, check):
    if check is not True:
        message = check
        return message, 400
    # flag = False
    # for item in db:
    #     if item['id'] == in_data['id']:
    #         item['test_name'].append(in_data['test_name'])
    #         item['test_result'].append(in_data['test_result'])
    #         flag = True
    # if flag is False:
    #     message = "Unable to find the patient"
    #     status = 400
    # else:
    #     message = "Test result added successfully"
    #     status = 200
    # return message, status
    try:
        patient = Patient.objects.raw({"_id": in_data['id']}).first()
        patient.test_name.append(in_data['test_name'])
        patient.test_result.append(in_data['test_result'])
        patient.save()
        message = "Test result added"
        status = 200
    except pymodm_er.DoesNotExist:
        message = "Patients not found"
        status = 400
    return message, status


@app.route('/new_patient', methods=['POST'])
def new_patient_2_server():
    in_data = request.get_json()
    check = validate_info_patient(in_data)
    message, status = add_patient(in_data, check)
    return message, status


@app.route('/add_test', methods=['POST'])
def add_test_handler():
    in_data = request.get_json()
    check = validate_test(in_data)
    message, status = add_test(in_data, check)
    return message, status


def init_database():
    connect("mongodb+srv://davidhe:password@cluster0.grsdcun.mongodb.net/test?"
            "retryWrites=true&w=majority")
    new_patient = {"name": "david", "id": 2, "blood type": "O+"}
    add_patient(new_patient, True)


if __name__ == "__main__":
    init_database()
    app.run()
