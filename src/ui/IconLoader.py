
import os
try:
    from PySide6.QtGui import QIcon
except:
    from PySide2.QtGui import QIcon


def loadIcon(name):
    # Get the path of the script
    scriptPath = os.path.realpath(__file__)
    scriptPath = scriptPath.replace("\\", "/")
    scriptPath = scriptPath.replace("/src/ui/IconLoader.py" , "")
    scriptPath += "/rc/icons/" + name 
    return QIcon(scriptPath)