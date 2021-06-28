import flask
from flask import request
import urllib.request
import json
import subprocess
import os
import sys
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def server_error():
   return json.dumps({'status': (501), 'status_text': 'Server error, not implemented'}, sort_keys=True, indent=4),500

@app.route('/openc2', methods=['GET'])
def server_error_two():
   return json.dumps({'status': (501), 'status_text': 'Server error, not implemented'}, sort_keys=True, indent=4),500

@app.route('/openc2', methods=['POST'])
def index():
    client_data = request.get_json(force = True) 
    consumer_response=server_200('complete',json.loads('{"status":200}'))
    data = json.dumps(consumer_response, sort_keys=True, indent=4)
    response = app.response_class(response=data,status=200,mimetype='application/json')
    response.headers['X-Request-ID'] = '0bc6dc48-0eaa-42a8-802f-0acbb3e3fa00'
    response.headers['Cache-control'] = 'no-cache'
    response.headers['action'] = client_data
    return response

#function to handle GET, POST, cli request and make calls to other functions to execute commands
#figure out exactly what we want this function to do as far as parsing
def request_handler():
conformance=0
   openc2_actions=['query', 'deny', 'allow', 'update', 'delete']
   openc2_targets=['file', 'ipv4_net', 'ipv6_net', 'ipv4_connection', 'ipv6_connection', 'features', 'slpf:rulenumber']
   openc2_query=['versions','profiles','pairs','rate_limit']
   openc2_response_requested=['none','ack','status','complete']
   complete_response="complete"
   openc2_query_versions=['1.0']
   the_action=""
   the_target=""
   
# tell producer things were ok
def server_200(complete,resultant):
   if complete=="complete":
      return json.dumps(resultant, sort_keys=True, indent=4)
   elif complete=="none":
      return
   else:
      return json.loads('{"status":200}')
   
if __name__ == '__main__':
   # Used when running locally only. When deploying to Google App
   # Engine, a webserver process such as Gunicorn will serve the app. This
   # can be configured by adding an `entrypoint` to app.yaml.
   app.run(host="localhost", port=8080, debug=True)
