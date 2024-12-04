from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class PageBase(QWidget):
    def __init__(self):
        super().__init__()

    # Say if the user can go to the next page or not
    def canGoNext(self):
        return True
    
    # Say if the next and cancel button should be hidden or not
    def hideNextAndCancel(self):
        return False

    def addDataToSettings(self,settings):
        print("Add the data to the settings")
        return settings
    
    def autoFill(self):
        print("Auto fill the data")
