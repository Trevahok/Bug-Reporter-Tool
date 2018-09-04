from flask import Flask, request, redirect
from FileManager import *
from main import *

app = Flask(__name__)
wordPath = './Developer Report/Test_DeveloperReview_with Bug.docx'
sourcePath = './Source Code/modified_sample_code.c'
f = open('./ErrorDisplay.html', "r")

file = open("saveFile.txt", "r")
inputValues = {}
for i in file.readlines():
    i = i.split(" ", 1)
    inputValues[i[0]] = i[1]

print(inputValues)
@app.route('/')
def index():
    dictionary = getDictionaryOfErrorToReport(wordPath, sourcePath)
    html = f.read()

    for k, v in dictionary.items():
        err = k[k.lower().find("red error id") + len("red error id"):-3]
        err = err.strip()

        html += "<br><div class='w3-container w3-content w3-card-4 w3-white' style='padding:0'>"
        html += "<div class = 'w3-row w3-blue w3-border w3-padding'>" + "Defect ID: " + err + "</div>"
        html += "<div class = 'w3-row w3-padding'>Error Description: </div>"
        html += "<div class = 'w3-row w3-grey w3-padding'>"
        c = 0
        for i in v:
            if c == 1:
                html += "<div class='w3-col w3-text-red' style='width:14.28%'>" + i + "</div>"
            else:
                html += "<div class='w3-col' style='width:14.28%'>" + i + "</div>"
            c += 1
        html += "</div>"
        html += "<div class = 'w3-row w3-padding'>Error Fix: </div>"
        html += "<div class = 'w3-row w3-grey w3-padding'>" + k + "</div>"
        html += "<div class ='w3-row w3-padding'>Root Cause: </div>"
        html += "<div class = 'w3-row w3-grey w3-padding'>" \
                "<form method = 'POST' action = '/postcomments/'>"

        if err in inputValues.keys():
            print(inputValues[err])
            html += "<input type='text' class='w3-input w3-border w3-col m910 w3-animate-input' style='width:30%;max-width:80%;' name='comments' placeholder = 'Error information' value='" + inputValues[err] + "'>"
        else:
            print(inputValues)
            html += "<input type='text' class='w3-input w3-border w3-col m910 w3-animate-input' style='width:30%;max-width:80%;' name='comments' placeholder = 'Error information'>"
        html += "<button class='w3-btn w3-black w3-right w3-col m2' name='button' value='"+ err +"'>Submit</button>" \
                "</form></div>"
        html += "</div><br>"

    html += "</body></html>"
    return html

@app.route('/postcomments/', methods = ['POST'])
def postcomments():
    commentText = request.form['comments']
    errorID = request.form['button']
    file = open("saveFile.txt", "a")
    writeString = errorID + " " + commentText
    file.write(writeString)
    file.write("\n")
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run()