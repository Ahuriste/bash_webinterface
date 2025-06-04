from flask import Flask, render_template, request, jsonify
from flask_shell2http import Shell2HTTP
from flask_executor import Executor
from commands import list_commands
from config import port
import json
import sys
import requests


app = Flask(__name__)
executor = Executor(app)
shell = Shell2HTTP(app, executor=executor)



for label, command in list_commands().items():
    endpoint = label.lower().replace(" ", "_")
    shell.register_command(command_name=command, endpoint=endpoint)

@app.route('/<path>/<endpoint>', methods=['POST','GET'])
def forward_post(path, endpoint):
    if request.method == 'POST':
        data=json.loads(bytearray(request.get_data()))
        print(data["args"])
        response = requests.post(
                "http://localhost:"+str(port)+'/'+endpoint,
                json=data
        )


        print(request.get_data())
        r = response.json ()
        return r
    else:
        response = requests.get(
                "http://localhost:"+str(port)+'/'+endpoint,
            data=request.get_data(),      
            params=request.args
        )
        r = response.json ()
        return r
@app.route("/<path>/", methods=["GET"])
def index(path):
    return render_template("index.html", commands=list(list_commands().keys()))

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=port)
