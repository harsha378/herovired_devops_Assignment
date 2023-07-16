from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloWorld():
    return 'Hello World'

@app.route('/aboutus')
def aboutUs():
    return 'this is about us page'