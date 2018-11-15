from flask import Flask


app = Flask(__name__)
app.config.from_object('config')
def hello_world():
    return "hello, world!"