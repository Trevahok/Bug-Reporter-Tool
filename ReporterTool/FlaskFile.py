# This script creates a web server using the Flask framework and gets the information
# from mapErrors.py and displays it to the user in a neat and clean UI utilising the W3.css framework
# Moreover, there is also utility for the end user to input and store details of the errors that have
# occurred in a .json file for future references
from flask import Flask, request, redirect, render_template
from mapErrors import *
import json, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "Uploads\\"

wordPath = './Uploads'
sourcePath = './Uploads'
errorCode = "red error id"

@app.route('/')
def index():
    return render_template('action.html')

@app.route('/upload', methods=['POST'])
def upload():
    global wordPath
    global sourcePath
    global errorCode
    wordFile = request.files["wordFile"]
    sourceFile = request.files["sourceFile"]
    wordFile.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], secure_filename(wordFile.filename)))
    sourceFile.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], secure_filename(sourceFile.filename)))
    wordPath = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], secure_filename(wordFile.filename))
    sourcePath = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], secure_filename(sourceFile.filename))
    return redirect("/report")

@app.route('/report')
def report():
    global errorCode
    file = open("saveFile.json","r")
    data = file.read()
    inputValues = json.loads(data)
    print(inputValues)
    dictionary = getDictionaryOfErrorToReport(wordPath, sourcePath)
    return render_template('report.html', dictionary=dictionary, inputValues=inputValues, errorCode=errorCode)

@app.route('/postcomments/', methods = ['POST'])
def postcomments():
    commentText = request.form['comments']
    errorID = request.form['button']
    diction = {}
    with open('saveFile.json' , 'r+') as file:
        data= file.read()
        diction = json.loads(data)
        diction[errorID] = commentText

    with open('saveFile.json', 'w') as file:
        file.write(json.dumps(diction))

    return redirect("/report")

if __name__ == "__main__":
    app.run()
