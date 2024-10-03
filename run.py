from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def getCurTime():
    curTime = datetime.now()
    formatedCurTime = curTime.strftime('%Y-%m-%d %H:%M:%S')
    return 'Current time: {}'.format(formatedCurTime)

if __name__ == "__main__":
    app.run(host='0.0.0.0', 
            port=8080, 
            debug=True)
