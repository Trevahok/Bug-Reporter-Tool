import FileManager
import re 

word_file =FileManager.WordFileManager('./Developer Report/Test_DeveloperReview_with Bug.docx')

source = FileManager.FileManager('./Source Code/Original_sample_code.c')
text = re.findall(r'\/\*.*\*\/', source )
print(text)
