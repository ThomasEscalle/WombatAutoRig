from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
from PySide2 import QtWidgets, QtCore, QtGui
import maya.OpenMayaUI as omui
import shiboken2
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.cmds as cmds
from maya.OpenMayaUI import MQtUtil

from wombatAutoRig.src.ui.forms import ui_DlgControllers
from wombatAutoRig.src.ui import IconLoader
from wombatAutoRig.src.core import FileHelper

from wombatAutoRig.src.core import Controllers

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgControllers(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgControllers, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.ui = ui_DlgControllers.Ui_DlgControllers()
        self.ui.setupUi(self)

        self.setWindowTitle("Create Controllers")
        self.mode = "create"

        self.setup()

        self.ui.btnOptions.clicked.connect(self.showOptions)

        # Connect the combo box to the stacked widget
        self.ui.comboBox.currentIndexChanged.connect(self.ui.stackedWidget.setCurrentIndex)


    def setCreateMode(self):
        self.mode = "create"
        self.setWindowTitle("Create Controllers")

    def setReplaceMode(self):
        self.mode = "replace"
        self.setWindowTitle("Replace Controllers")

    def showOptions(self):
        # Show a menu with the options
        menu = QtWidgets.QMenu(self)
        createAction = menu.addAction("Create controller")
        createAction.triggered.connect(self.createAction)

        # Show the menu at the cursor position
        action = menu.exec_(QtGui.QCursor.pos())


    def createAction(self):
        # Ask the user for the controller name
        controllerName, ok = QtWidgets.QInputDialog.getText(self, 'Create controller', 'Enter the controller name:')
        if ok:
            Controllers.saveController(controllerName)

    # Load the controllers from the controllers directory
    # And add the buttons to the UI
    def setup(self):
        # Controllers directory
        controllersPath = FileHelper.getControllersPath()

        # Get all the controllers files in the directory
        folders = FileHelper.getAllFoldersInFolder(controllersPath)

        for folder in folders:
            files = FileHelper.getAllFilesInFolder(folder)

            # Create a page in the stacked widget for each folder
            # Add a scroll area to the page
            # Add a grid layout to the scroll area

            page = QtWidgets.QWidget()
            scrollArea = QtWidgets.QScrollArea()
            scrollArea.setWidget(page)
            scrollArea.setWidgetResizable(True)

            gridLayout = QtWidgets.QGridLayout()
            page.setLayout(gridLayout)
            
            self.ui.stackedWidget.addWidget(scrollArea)

            # Add the page to the combo box
            self.ui.comboBox.addItem(folder.split("/")[-1])


            btnNumber = 0

            # Loop through the files
            for file in files:
                # Check if the file contains the .ctrl.txt extension
                if file.endswith(".ctrl.txt"):

                    # Create a button for each controller
                    button = QtWidgets.QPushButton()

                    # Get the position of the button in the grid layout
                    row = btnNumber // 4
                    col = btnNumber % 4

                    # Set the button text
                    # button.setText("Ctrl")

                    gridLayout.addWidget(button, row, col)

                    # Increment the button number
                    btnNumber += 1

                    # Connect the button to the execFile function
                    button.clicked.connect(lambda self=self, file=file: self.execFile(file))
                    # Check if there is a file named "file".png
                    # If so, set the button icon
                    iconPath = file + ".png"
                    if FileHelper.fileExists(iconPath):
                        button.setIcon(QIcon(iconPath))
                        button.setIconSize(QSize(32, 32))


    def execFile(self, file):

        if self.mode == "create":
            Controllers.createController(file)
        elif self.mode == "replace":
            Controllers.replaceController(file)
        

    # Show window with docking ability
    def run(self):
        self.show(dockable = True)