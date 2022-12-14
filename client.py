#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:29:27 2022

@author: david
"""
import requests
from pymodm.connection import connect
from db_server import Patient
from db_server import add_patient, add_test
import base64


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


def download_image(netid, no, filename):
    img_str = requests.get("http://vcm-21170.vm.duke.edu/get_image/" +
                           netid+"/"+no)
    b64_2_img(filename, img_str.text)


def b64_2_img(filename, img_str):
    image_bytes = base64.b64decode(img_str)
    with open(filename, "wb") as out_file:
        out_file.write(image_bytes)


if __name__ == "__main__":
    # patient = {'test_result': 120}
    # r = requests.post("http://127.0.0.1:5000/add_test", json=patient)
    # test = {'name': "Ceasar", 'id': 3, 'blood type': 'B-'}
    # connect("mongodb+srv://davidhe:password@cluster0.grsdcun.mongodb.net/test?"
    #         "retryWrites=true&w=majority")
    # add_patient(test, True)
    # test = {'test_name': "HDL", 'id': 3, 'test_result': 'Normal'}
    # msg, status = add_test(test, True)
    # new = Patient.objects.raw({"_id": 3}).first()
    download_image("zh128", "1", "img/new")
