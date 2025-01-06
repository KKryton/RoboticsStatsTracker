import os

def fetchDataFiles():
    dataFolderPath = 'src\data'
    filesInFolder = os.listdir(dataFolderPath)
    dataFiles = [file for file in filesInFolder if file.endswith('.txt')]
    return dataFiles