from docx import Document
from docx.text.run import Font, Run
from docx.dml.color import ColorFormat

class WordFileManager:

    def __init__(self, path):
        self.document = path

    def setFilePath(self, path):
        self.document = path

    def readCells(self):
        wordDoc = Document(self.document)

        rows = []
        cells = []

        for table in wordDoc.tables:
            for row in table.rows:
                rows.append([cell.text for cell in row.cells])

        return rows

class FileManager:

    def __init__(self, path):
        self.document = path

    def readFile(self):
        file = open(self.document, "r")
        return file.read()