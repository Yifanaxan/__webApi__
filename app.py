#https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application

#flask --app app run --debug
#flask --app app run --debug --port 5024

#(cmd) .\venv\Scripts\activate.bat
#(bash) source ./venv/Scripts/activate


from flask import Flask
from api import api01   #第一個api是檔案夾名稱，第二個api01是__init__裡面的實體api

app = Flask(__name__)
app.register_blueprint(api01)

@app.route("/")
def index():
    return "<h1>Hello, Index!</h1>"