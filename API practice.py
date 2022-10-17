#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:11:48 2022

@author: david
"""
import requests

# r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
# if r.status_code == 200:  # Bad status code will raise an error
#     ans = r.json()
# else:
#     print("Bad request")
# info = {"name": "Ziwei He", "net_id": "zh128", "e-mail":"ziweihe.974@duke.edu
#        "}
# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json = info)

info1 = {"user": "Ziwei_He", "message": "Hello"}
R = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=info1)
Get = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/jl922")
