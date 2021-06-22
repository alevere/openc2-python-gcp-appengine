import flask
import request
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)


@app.route("/openc2", methods=["GET","POST"])
def hello():
    """ Return a friendly HTTP greeting. """
    header_1 = request.headers.get('X-Request-ID')
    header_2 = request.headers.get('Content-Type')
    print(header_1)
    print(header_2)
    return "OpenC2!\n"


if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
