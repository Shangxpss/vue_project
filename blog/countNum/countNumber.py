from collections import Counter
from docx import Document
from pathlib import Path
import os

def cuntWord(name:str):
    fileList = getpath(name)
    # assert os.path.isfile(fileList[0])
    document = Document("new.docx")

    paragraph = document.paragraphs
    text:list[str] = []
    for item in paragraph:
        text.extend(item.text.lower().split(" "))
    
    result = Counter(text)
    print(result)

def getpath(name:str):
    cwd = Path.cwd()
    dirPath = os.path.join(cwd.parent,name)
    allFile = os.listdir(dirPath)
    fileList:list[str] = []
    for name in allFile:
        fullName = os.path.join(dirPath,name)
        fileList.append(fullName)
    return fileList

if __name__ == "__main__":
    cuntWord("store")
