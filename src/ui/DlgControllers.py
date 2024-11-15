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

        self.setWindowTitle("Controllers")

        self.setup()

    # Load the controllers from the controllers directory
    # And add the buttons to the UI
    def setup(self):
        # Controllers directory
        controllersPath = FileHelper.getControllersPath()

        # Get all the controllers files in the directory
        files = FileHelper.getAllFilesInFolder(controllersPath)

        btnNumber = 0

        # Loop through the files
        for file in files:
            # Check if the file contains the .ctrl.txt extension
            if file.endswith(".ctrl.txt"):
                print("Controller found: " + file)

                # Create a button for each controller
                button = QtWidgets.QPushButton()

                # Get the position of the button in the grid layout
                row = btnNumber // 4
                col = btnNumber % 4

                # Set the button text
                # button.setText("Ctrl")

                self.ui.gridLayout.addWidget(button, row, col)

                # Increment the button number
                btnNumber += 1


                


        pass


    # Show window with docking ability
    def run(self):
        self.show(dockable = True)