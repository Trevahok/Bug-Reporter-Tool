
document = r'C:\Users\Sainath\Documents\Codeathon\CODE-A-THON-readme-master\CODE-A-THON-readme-master\Question-5\Source and report\Developer Report\Test_DeveloperReview_with Bug.docx'

from docx import Document
from docx.text.run import Font, Run
from docx.dml.color import ColorFormat

wordDoc = Document(document)

for table in wordDoc.tables:
    for row in table.rows:
        for cell in row.cells:
            print (cell.text)

print()

from docx import *
document = opendocx(document)
words = document.xpath('//w:r', namespaces=document.nsmap)
WPML_URI = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
tag_rPr = WPML_URI + 'rPr'
tag_highlight = WPML_URI + 'highlight'
tag_val = WPML_URI + 'val'
tag_t = WPML_URI + 't'
for word in words:
    for rPr in word.findall(tag_rPr):
        high=rPr.findall(tag_highlight)
        for hi in high:
            if hi.attrib[tag_val] == 'yellow':
                print word.find(tag_t).text.encode('utf-8').lower()
