#!/usr/bin/env python3
from flask import Flask,redirect,request,send_from_directory
import os.path
from os import path
import subprocess
import time

app = Flask(__name__)
app.config["DEBUG"] = True
data_dir = '../data/'
# data_dir = './'

header = "<html><head></head><body>\n"
footer = "</body></head>\n"
filelist = [
        "cachedInlineTables.js",
        "final_book.xls",
        "final_book_es.csv",
        "final_book.csv",
        "final_book_es.xls"
    ]

def make_page(body):
    return header+body+footer

@app.route('/index.htm', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    requested_file = request.args.get('file')
    if requested_file:
        if requested_file in filelist:
            return send_from_directory(data_dir,
                               requested_file, as_attachment=True)
        else:
            body = "<h1>You are not allowed to download "+requested_file+"<h1>"
            return make_page(body)

    with open('button_htm.txt', 'r') as file:
        body = file.read()
    body += "<ul>"
    for name in filelist:
        full_name = data_dir + name
        if os.path.isfile(full_name):
            ctime = time.ctime(os.path.getctime(full_name))
            body += '<li><a href=/?file='+name+'>'+name+'</a> created '+ctime+'</li>'
        else:
            body += "<li>"+name+" doesn't exist</li>"
    body += "</ul>"
    return make_page(body)

@app.route('/index.htm', methods=['POST'])
@app.route('/', methods=['POST'])
def submit():
    print('before')
    subprocess.run(['./get_table.py', data_dir])
    # subprocess.run('./get_table.py')
    print('after')
    return redirect("/")

app.run(host='0.0.0.0')