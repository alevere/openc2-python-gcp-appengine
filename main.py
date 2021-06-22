import flask
import urllib.request
import json
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def server_error():
   """ Return a friendly HTTP error. """
   print('Status: 500 Internal Server Error')
   print('Content-Type: application/openc2-rsp+json;version=1.0')
   print('')
   print(json.dumps({'status': (500), 'status_text': 'Server error'}, sort_keys=True, indent=4))
   print('')
   return 0

@app.route('/openc2', methods=['GET','POST'])
def index():
    @after_this_request
    def add_header(response):
        response.headers['X-Foo'] = 'Parachute'
        return response
    return 'Hello World!'


if __name__ == '__main__':
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
