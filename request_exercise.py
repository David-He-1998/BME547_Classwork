#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:37:50 2022

@author: david
"""
import requests
r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/zh128")
if r.status_code == 200:
    patient = r.json()
Recip_ID = patient["Recipient"]
Donor_ID = patient["Donor"]
R_Recip = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/" +
                       Recip_ID)
R_Donor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/" +
                       Donor_ID)
if R_Recip.status_code == 200 and R_Donor.status_code == 200:
    blood_R = R_Recip.text[0]
    blood_D = R_Donor.text[0]
blood_type = ["A", "B", "AB", "O"]
RBC_compatibility = {"A": ["A", "O"], "B": ["B", "O"], "O": ["O"]}  # key: Rcip
if blood_D not in blood_type or blood_R not in blood_type:
    print("Wrong blood type information")
else:
    ans = "No"
    if blood_R == "AB":
        ans = "Yes"
    if blood_R == "A":
        if blood_D in RBC_compatibility["A"]:
            ans = "Yes"
    if blood_R == "B":
        if blood_D in RBC_compatibility["B"]:
            ans = "Yes"
    if blood_D in RBC_compatibility["O"]:
        ans = "Yes"
    diagnosis = {"Name": "zh128", "Match": ans}
    check = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                          json=diagnosis)
