# This script creates a web server using the Flask framework and gets the information
# from mapErrors.py and displays it to the user in a neat and clean UI utilising the W3.css framework
# Moreover, there is also utility for the end user to input and store details of the errors that have
# occurred in a .json file for future references
from flask import Flask, request, redirect
from mapErrors import *
import json

app = Flask(__name__)
wordPath = './Developer Report/Test_DeveloperReview_with Bug.docx'
sourcePath = './Source Code/modified_sample_code.c'

@app.route('/')
def index():
    inputValues = {}
    file = open("saveFile.json","r")
    data = file.read()
    inputValues = json.loads(data)
    print(inputValues)
    dictionary = getDictionaryOfErrorToReport(wordPath, sourcePath)
    html = "<html><body style = 'background-color: #151616; color: #ddd;'>"
    html += "<title>Reporter Tool</title><link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>" \
            "<link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Lato'>" \
            "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'>"\
            "<style> body,h1,h2,h3,h4,h5,h6 {font-family: 'Lato', sans-serif;} </style>"

    html += "<div class = 'w3-top w3-padding-large w3-black w3-xlarge w3-wide w3-animate-opacity'>Reporter Tool</div><br><br>"
    html += "<div class='w3-animate-zoom'>"
    for k, v in dictionary.items():
        err = k[k.lower().find("red error id") + len("red error id"):-3]
        err = err.strip()

        html += "<br><div class='w3-container w3-content w3-card-4 w3-white w3-animate-opacity' style='padding:0'>"
        html += "<div class = 'w3-row w3-blue w3-padding'>" + "Defect ID: " + err + "</div>"
        html += "<div class = 'w3-row w3-padding'>Error Description: </div>"
        html += "<div class = 'w3-row w3-grey w3-padding'>"
        c = 0
        for i in v:
            if c == 1:
                html += "<div class='w3-col w3-text-red w3-padding' style='width:14.28%'>" + i + "</div>"
            else:
                html += "<div class='w3-col w3-padding' style='width:14.28%'>" + i + "</div>"
            c += 1
        html += "</div>"
        html += "<div class = 'w3-row w3-padding'>Error Fix: </div>"
        html += "<div class = 'w3-row w3-grey w3-padding'>" + k + "</div>"
        html += "<div class ='w3-row w3-padding'>Root Cause: </div>"
        html += "<div class = 'w3-row w3-grey w3-padding'>" \
                "<form method = 'POST' action = '/postcomments/'>"

        if err in inputValues.keys():
            print(inputValues[err])
            html += "<input type='text' class='w3-input w3-border w3-col m9 w3-animate-input' style='width:30%;max-width:80%;' name='comments' placeholder = 'Error information' value='" + inputValues[err] + "'>"
        else:
            html += "<input type='text' class='w3-input w3-border w3-col m9 w3-animate-input' style='width:30%;max-width:80%;' name='comments' placeholder = 'Error information'>"
        html += "<button class='w3-btn w3-black w3-right w3-col m2' name='button' value='"+ err +"'>Submit</button>" \
                "</form></div>"
        html += "</div><br>"

    html += "</div></body></html>"
    return html

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

    return redirect("/")

if __name__ == "__main__":
    app.run()