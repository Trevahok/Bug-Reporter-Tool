from flask import Flask
from FileManager import *

app = Flask(__name__)

f = FileManager('./index.html')
@app.route('/')
def index():
    return f.readFile()

if __name__ == "__main__":
    app.run(debug = True)