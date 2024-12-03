from os import name
from flask import Flask 

# create app
app = Flask(__name__) 


@app.route('/')
def index():
    return 'app running nicecely'


if name == '__main__':
    app.run(debug=True)