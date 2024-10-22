
import os
import importlib.util

# QDesktopServices
from PySide2.QtGui import QDesktopServices


# Return the path of the templates folder
def getTemplatesPath():
    filePath = os.path.abspath(__file__)
    filePath = filePath.replace("\\", "/")
    filePath = filePath.replace("/src/core/FileHelper.py", "")
    filePath += "/templates"

    createFolderIfNotExists(filePath)

    print("Templates folder path: " + filePath)

    return filePath

# Return the path of the preferences file (preferences.json)    
def getPreferencesPath():
    filePath = os.path.abspath(__file__)
    filePath = filePath.replace("\\", "/")
    filePath = filePath.replace("/src/core/FileHelper.py", "")
    filePath += "/preferences.json"

    print("Preferences folder path: " + filePath)

    return filePath

# Return the path of the rc folder
def getRcPath():
    filePath = os.path.abspath(__file__)
    filePath = filePath.replace("\\", "/")
    filePath = filePath.replace("/src/core/FileHelper.py", "")
    filePath += "/rc"

    createFolderIfNotExists(filePath)

    print("Rc folder path: " + filePath)

    return filePath


# Create a folder if it doesn't exist
def createFolderIfNotExists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("Folder created: " + path)

    return path

# Get an array of all the files in a folder
def getAllFilesInFolder(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files

# Get an array of all the folders in a folder
def getAllFoldersInFolder(path):
    folders = []
    for r, d, f in os.walk(path):
        for folder in d:
            folders.append(os.path.join(r, folder))
    return folders


# Import a file
def importFile(filePath):

    spec = importlib.util.spec_from_file_location("module.name", filePath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


    return module

# Open a folder in the explorer
def openFolderInExplorer(path):
    QDesktopServices.openUrl("file:///" + path)