from flask import Flask
from flask import request

app = Flask(__name__)

tasks = []

@app.route('/')
def hello_world():
    msg = "<h1> Hello World </h1>"
    msg = msg + "<ul>"
    for task in tasks:
        msg = msg + f"<li> {task} </li>"
    msg = msg + "</ul>"
    return msg

@app.route('/tasks', methods=['POST'])
def new_task():
    content = request.json
    print(content)
    return content
    