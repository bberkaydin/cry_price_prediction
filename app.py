import flask
from flask import Flask
from api.info import info_blueprint

app = Flask(__name__)
app.register_blueprint(info_blueprint, url_prefix="/api/info")


@app.route('/health')
def test():
    return flask.Response(status=200).status


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
