#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def hello_world():
    #return "<p>Hello, tess you can tell me the h!</p>"

#if __name__ =='__main__':   #__name__變數
    #app.run(host='0.0.0.0',port=3000, debug=True)

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Flask! </p>"

db = [] #資料容器 list

@app.route("/th")
def getTemperatureHumidity():
    global db
    args = request.args
    db += [[args.get("t"), args.get("h")]] #有2個list
    return db

if __name__ =='__main__':   #__name__變數
    app.run(host='0.0.0.0',port=3000, debug=True)

