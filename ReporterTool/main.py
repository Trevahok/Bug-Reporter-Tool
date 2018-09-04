import FileManager

def getDictionaryOfErrorToReport(wordPath, sourcePath):
    word_file = FileManager.WordFileManager(wordPath)
    source = FileManager.FileManager(sourcePath)

    sourceErrorIDs = source.getErrorID("red error id")

    print()

    sourceToWordDictionary = {}
    for i in word_file.getErrorRows():
        for k, v in sourceErrorIDs.items():
            if (v in i[0]):
                sourceToWordDictionary.update({k: i})

    for k, v in sourceToWordDictionary.items():
        print(v)

    #print(sourceErrorIDs)
    return sourceToWordDictionary


wordPath = './Developer Report/Test_DeveloperReview_with Bug.docx'
sourcePath = './Source Code/modified_sample_code.c'
getDictionaryOfErrorToReport(wordPath,sourcePath)
