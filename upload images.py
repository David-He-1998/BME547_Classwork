#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:26:57 2022

@author: david
"""
from tkinter import filedialog
import base64
import requests


count = 1


def upload_img():
    global count
    img = filedialog.askopenfilename()
    b64_img_str = convert_2_64(img)
    result = upload_2_server(b64_img_str, count)
    count += 1
    return result


def convert_2_64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def upload_2_server(img_str, count):
    img_dict = {"image": img_str, "net_id": "zh128", "id_no": count}
    r = requests.post("http://vcm-21170.vm.duke.edu/add_image", json=img_dict)
    return r.text


if __name__ == "__main__":
    respond = upload_img()
