import os


def readTxt(path: str):
    assert os.path.isfile(path)
    with open(path) as f:
        result = f.read()
    return result


def createFile(dir: str, num: int):
    assert os.path.isdir(dir)
    for index in range(num):
        filteName = dir + r"/" + str(index) + ".docx"
        with open(filteName, "w"):
            pass
        

