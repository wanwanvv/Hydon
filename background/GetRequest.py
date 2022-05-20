'''
Descripttion: 
version: 
Author: Wan Jingyi
Date: 2021-08-26 16:26:12
LastEditors: Wan Jingyi
LastEditTime: 2021-08-26 20:24:03
'''
import os
from flask import Flask, render_template,jsonify,request,make_response,send_from_directory

from ReturnData import return_monitor_data_dynamic_one,return_monitor_data_dynamic

root_folder=os.path.dirname(__file__)
get_status_full_file=os.path.join(root_folder,"GetStatus_test.py")

app=Flask(__name__)
app.config['get_status_file']=get_status_full_file

#connection test
@app.route("/monitor/test")
def connect_test():
    return "Welcome to monitor api!"

#return status data
@app.route("/monitor/status",methods=['GET','POST'])
def get_status_data():
    results=return_monitor_data_dynamic_one()
    return jsonify(results)

#return dynamic data
@app.route("/monitor/data/<int:num>",methods=['GET','POST'])
def get_dynamic_data(num):
    results=return_monitor_data_dynamic(num)
    return jsonify(results)

#if __name__ == '__main__':
    #app.run(host="127.0.0.1",port="8000",debug = True)
    #from werkzeug.contrib.fixers import ProxyFix
    #app.wsgi_app = ProxyFix(app.wsgi_app)
    #app.run()
