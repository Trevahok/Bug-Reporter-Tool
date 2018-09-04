from flask import Flask, request
from FileManager import *
from main import *

app = Flask(__name__)
wordPath = './Developer Report/Test_DeveloperReview_with Bug.docx'
sourcePath = './Source Code/modified_sample_code.c'
f = open('./ErrorDisplay.html', "r")

@app.route('/')
def index():
    dictionary = getDictionaryOfErrorToReport(wordPath, sourcePath)
    html = f.read()

    for k, v in dictionary.items():
        err = k[k.lower().find("red error id") + len("red error id"):-3]

        html += "<br><div class='w3-container w3-content w3-card-4 w3-white w3-padding-small'>"
        html += "<div class = 'w3-row w3-blue w3-border w3-card'>" + "Defect ID: " + err + "</div>"
        html += "<div class = 'w3-row'>Error Description: </div>"
        html += "<div class = 'w3-row w3-grey'>"
        c = 0
        for i in v:
            if c == 1:
                html += "<div class='w3-col w3-text-red w3-border' style='width:14.28%'>" + i + "</div>"
            else:
                html += "<div class='w3-col' style='width:14.28%'>" + i + "</div>"
            c += 1
        html += "</div>"
        html += "<div class = 'w3-row'>Error Fix: </div>"
        html += "<div class = 'w3-row w3-grey'>" + k + "</div>"
        html += "<div class ='w3-row'>Root Cause: </div>"
        html += "<div class = 'w3-row w3-grey'><input type='text' class='w3-input w3-border'></div>"
        html += "</div>"

    return html

if __name__ == "__main__":
    app.run()