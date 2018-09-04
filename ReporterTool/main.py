import FileManager
import re

word_file =FileManager.WordFileManager('./Developer Report/Test_DeveloperReview_with Bug.docx')

source = FileManager.FileManager('./Source Code/modified_sample_code.c').readFile()
for line in source:
    if "red error id" in line.lower():
        print(line)
# text = re.findall(r'\/\*.*\*\/', source )
