#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:45:45 2022

@author: david
"""
from pymodm import MongoModel, fields


class Patient(MongoModel):
    name = fields.CharField()
    ID = fields.IntegerField(primary_key=True)
    blood_type = fields.CharField()
    test_name = fields.ListField()
    test_result = fields.ListField()
