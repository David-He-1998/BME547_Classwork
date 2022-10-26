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
app = Flask(__name__)


db = []


def add_patient(name, patient_id, blood_type, check):
    if check is not True:
        message = check
        return message, 400
    new_patient = {'name': name, 'id': patient_id, 'blood type': blood_type,
                   'test_name': [], 'test_result': []}
    db.append(new_patient)
    message = "Patient added successfully"
    return message, 200


@app.route('/new_patient', methods=['GET'])
def new_patient_2_server():
    in_data = request.get_json()
    check = validate_info(in_data)
    message, status = add_patient(in_data['name'], in_data['id'],
                                  in_data['blood type'], check)


def validate_info(in_data):
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


if __name__ == "__main__":
    app.run()
