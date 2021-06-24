import flask
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

@app.route('/openc2', methods=['GET','POST'])
def index():
    consumer_response=server_200('complete',json.loads('{"status":200}'))
    data = json.dumps(consumer_response, sort_keys=True, indent=4)
    response = app.response_class(response=data,status=200,mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
   
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
