from FileManager import *

f = WordFileManager(r'C:\Users\Sainath\Documents\Codeathon\CODE-A-THON-readme-master\CODE-A-THON-readme-master\Question-5\Source and report\Developer Report\Test_DeveloperReview_with Bug.docx')
f2 = FileManager(r'C:\Users\Sainath\Desktop\bleh.txt')
print(f.readCells())
wordstring = f2.readFile()
print(wordstring)