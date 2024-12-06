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

        self.inputs = []
        

    # Signal to create the rig
    canceled = Signal()
    accepted = Signal()
    entered = Signal()
    
    # Triggers the signals
    def onCanceled(self):
        self.canceled.emit()

    # Triggers the signals
    def onAccepted(self):
        self.accepted.emit()

    # Triggers the signals
    def onEntered(self):
        self.entered.emit()

    def addDataToSettings(self,settings):
        print("Add the data to the settings")
        """
        settings["name"] = self.ui.leName.text()
        settings["identifier"] = self.ui.leIdentifier.text()
        settings["version"] = self.ui.leVersion.text()
        settings["author"] = self.ui.leAuthor.text()
        """

        for input in self.inputs:
            # if the input is a QLineEdit
            if isinstance(input, QLineEdit):
                settings[input.whatsThis()] = input.text()            
            # if the input is a QCheckBox
            if isinstance(input, QCheckBox):
                settings[input.whatsThis()] = input.isChecked()
        print(settings)
        return settings



    # Set the title of the page
    def setPageTitle(self, name):
        self.ui.label.setText(name)

    # Add a label to the page
    def addLabel(self, name , identifier):
        # Add a label to the formLayout
        label = QLabel(name)
        self.ui.formLayout.addRow("", label)
        pass
    
    # Add a text input to the page
    def addTextInput(self, name , identifier, canBeEmpty = False):
        # Add a label to the formLayout
        lineEdit = QLineEdit()
        lineEdit.setWhatsThis(identifier)
        self.ui.formLayout.addRow(name, lineEdit)
        self.inputs.append(lineEdit)

    # Add a checkbox to the page
    def addCheckbox(self, name , identifier):
        # Add a label to the formLayout
        checkBox = QCheckBox()
        checkBox.setText(name)
        checkBox.setWhatsThis(identifier)
        self.ui.formLayout.addRow("", checkBox)
        self.inputs.append(checkBox)
    
    # Add a separator to the page
    def addSeparator(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.HLine)
        frame.setFrameShadow(QFrame.Sunken)
        self.ui.formLayout.addRow("", frame)
        pass

    # Add a spacer to the page
    def addSpacer(self):
        self.ui.formLayout.addRow("", QLabel())









    def autoFill(self):
        pass




    # Say if the user can go to the next page or not
    def canGoNext(self):

        ########################################################
        #### Check if all the required fields are filled in ####
        ########################################################


        return True