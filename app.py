from flask import Flask
app = Flask(__name__)

@app.route('/test')
def test():
    return '<h1>TEST</h1>'
