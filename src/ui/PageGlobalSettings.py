from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wombatAutoRig.src.ui.PageBase import PageBase

from wombatAutoRig.src.ui.forms import ui_PageGlobalSettings

from wombatAutoRig.src.ui import WidgetSelectComponent

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

            # if the input is a QSpinBox
            if isinstance(input, QSpinBox):
                settings[input.whatsThis()] = input.value()
            
            # if the input is a QDoubleSpinBox
            if isinstance(input, QDoubleSpinBox):
                settings[input.whatsThis()] = input.value()

        print(settings)
        return settings



    # Set the title of the page
    def setPageTitle(self, name):
        self.ui.label.setText(name)

    # Add a label to the page
    def addLabel(self, name ):
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

    # Add an integer input to the page (QSpinBox)
    def addIntegerInput(self, name , identifier, min = 0, max = 100):
        spinBox = QSpinBox()
        spinBox.setWhatsThis(identifier)
        spinBox.setMinimum(min)
        spinBox.setMaximum(max)
        self.ui.formLayout.addRow(name, spinBox)
        self.inputs.append(spinBox)

    # Add a float input to the page (QDoubleSpinBox)
    def addFloatInput(self, name , identifier, min = 0, max = 100):
        spinBox = QDoubleSpinBox()
        spinBox.setWhatsThis(identifier)
        spinBox.setMinimum(min)
        spinBox.setMaximum(max)
        self.ui.formLayout.addRow(name, spinBox)
        self.inputs.append(spinBox)

    # Add a combobox to the page
    # Items is a list of strings
    def addComboBox(self, name, identifier, items, defaultIndex = 0):
        comboBox = QComboBox()
        comboBox.setWhatsThis(identifier)
        for item in items:
            comboBox.addItem(item)
        if defaultIndex < len(items):
            comboBox.setCurrentIndex(defaultIndex)
        self.ui.formLayout.addRow(name, comboBox)
        self.inputs.append(comboBox)

    # Add a spacer to the page
    def addSpacer(self):
        self.ui.formLayout.addRow("", QLabel())


    def addVertexSelection(self, name, identifier):
        widget = WidgetSelectComponent.WidgetSelectComponent()
        widget.setMode("vertex")
        widget.setWhatsThis(identifier)
        self.ui.formLayout.addRow(name, widget)

    def addEdgeSelection(self, name, identifier):
        widget = WidgetSelectComponent.WidgetSelectComponent()
        widget.setMode("edge")
        widget.setWhatsThis(identifier)
        self.ui.formLayout.addRow(name, widget)

    def addFaceSelection(self, name, identifier):
        widget = WidgetSelectComponent.WidgetSelectComponent()
        widget.setMode("face")
        widget.setWhatsThis(identifier)
        self.ui.formLayout.addRow(name, widget)

    def addObjectSelection(self, name, identifier):
        widget = WidgetSelectComponent.WidgetSelectComponent()
        widget.setMode("object")
        widget.setWhatsThis(identifier)
        self.ui.formLayout.addRow(name, widget)






    def autoFill(self):
        # Loop through the inputs, if it is a QLineEdit, fill it with "AutoRig"
        for input in self.inputs:
            if isinstance(input, QLineEdit):
                input.setText("AutoRig")
            if isinstance(input, QCheckBox):
                input.setChecked(True)




    # Say if the user can go to the next page or not
    def canGoNext(self):

        ########################################################
        #### Check if all the required fields are filled in ####
        ########################################################


        return True