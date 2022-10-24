#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:07:34 2022

@author: david
"""
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on"


@app.route("/info", methods=["GET"])
def info():
    x = "This website calculates blood cholesterol level.\n by Ziwei He"
    return x


@app.route("/hdl_check", methods=["POST"])
def hdl_check_server():
    '''
    Args:
        incoming_json = {"name": <name_str>, "hdl_value": <hdl_value_int>}
    Returns

    '''
    from Blood_Calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    result = check_HDL(hdl_value)
    return result


@app.route("/add_num", methods=["POST"])
def add_num():
    in_data = request.get_json()
    ans = in_data['a'] + in_data['b']
    return jsonify(ans)


@app.route('/add_num1/<a>/<b>', methods=['GET'])
def add_num1(a, b):
    ans = float(a) + float(b)
    return ans


if __name__ == "__main__":
    app.run()
