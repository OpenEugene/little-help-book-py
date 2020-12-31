#!/usr/bin/env python
from flask import Flask,redirect,request,send_from_directory
import os.path
from os import path
import subprocess
import time

app = Flask(__name__)
app.config["DEBUG"] = True

header = "<html><head></head><body>\n"
footer = "</body></head>\n"

def make_page(body):
    return header+body+footer

@app.route('/index.htm', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    requested_file = request.args.get('file')
    if requested_file:
        print("downloading", requested_file)
        return send_from_directory('.',
                               requested_file, as_attachment=True)

    with open('index.htm', 'r') as file:
        body = file.read()
    body += "<ul>"
    for name in [
        "cachedInlineTables.js",
        "final_book.xls",
        "final_book_es.csv",
        "final_book.csv",
        "final_book_es.xls"
    ]:
        if os.path.isfile(name):
            ctime = time.ctime(os.path.getctime(name))
            # body += '<li><a href="'+name+'">'+name+'</a> created '+ctime+'</li>'
            body += '<li><a href=/?file='+name+'>'+name+'</a> created '+ctime+'</li>'
        else:
            body += "<li>"+name+" doesn't exist</li>"
    body += "</ul>"
    return make_page(body)

@app.route('/index.htm', methods=['POST'])
@app.route('/', methods=['POST'])
def submit():
    subprocess.run('./get_table.py')
    return redirect("/")

app.run()