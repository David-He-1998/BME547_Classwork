#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:29:27 2022

@author: david
"""
import requests


# r = requests.get("http://127.0.0.1:5000/info")
# if r.status_code == 200:
#     # send = {"name": "Ziwei", "hdl_value": "39"}
#     # r = requests.post("http://127.0.0.1:5000/hdl_check", json=send)
#     send = {'a': 50, 'b': 11}
#     r = requests.post("http://127.0.0.1:5000/add_num", json=send)
#     ans = r.json()
def upload_patient_info(name, ID, blood_type):
    data = {"name": name, "id": ID, "blood type": blood_type}
    r = requests.post("http://127.0.0.1:5000/new_patient", json=data)
    return r.text, r.status_code


if __name__ == "__main__":
    patient = {'test_result': 120}
    r = requests.post("http://127.0.0.1:5000/add_test", json=patient)
