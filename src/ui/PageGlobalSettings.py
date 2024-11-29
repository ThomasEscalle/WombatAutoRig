from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wombatAutoRig.src.ui.PageBase import PageBase

from wombatAutoRig.src.ui.forms import ui_PageGlobalSettings

# Page to set the global settings for the rig
class PageGlobalSettings(PageBase):

    def __init__(self):
        super(PageGlobalSettings, self).__init__()

        self.ui = ui_PageGlobalSettings.Ui_PageGlobalSettings()
        self.ui.setupUi(self)
        
    def addDataToSettings(self,settings):
        print("Add the data to the settings")
        settings["name"] = self.ui.leName.text()
        settings["identifier"] = self.ui.leIdentifier.text()
        settings["version"] = self.ui.leVersion.text()
        settings["author"] = self.ui.leAuthor.text()
        return settings


    def setPageTitle(name):
        pass

    def addLabel(name , identifier):
        pass
    
    def addTextInput(name , identifier, canBeEmpty = False)
        pass

    def addSeparator():
        pass

    def addSpacer():
        pass





    # Say if the user can go to the next page or not
    def canGoNext(self):

        ########################################################
        #### Check if all the required fields are filled in ####
        ########################################################.

        """
        # Check if the user has entered a name for the rig
        if self.ui.leName.text() == "":
            # Warn the user
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a name for the rig.")
            return False
        
        # Check if the user entered an identifier for the rig
        if self.ui.leIdentifier.text() == "":
            # Warn the user
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter an identifier for the rig.")
            return False
        
        # Check if the user entered a version for the rig
        if self.ui.leVersion.text() == "":
            # Warn the user
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a version for the rig.")
            return False
        
        # Check if the user entered a author for the rig
        if self.ui.leAuthor.text() == "":
            # Warn the user
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter an author for the rig.")
            return False

        """


        return True