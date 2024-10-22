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

from wombatAutoRig.src.ui.forms import ui_DlgColor
from wombatAutoRig.src.ui import IconLoader
from wombatAutoRig.src.core import FileHelper

from wombatAutoRig.src.core import Color

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgColor(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgColor, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.ui = ui_DlgColor.Ui_DlgColor()
        self.ui.setupUi(self)

        self.setWindowTitle("Color Picker")

        # Setup the buttons
        self.setupButtons()

    def setupButtons(self):
        # Set the background color of the buttons
        self.ui.btn_00.setStyleSheet("background-color: #A62A2A")
        self.ui.btn_01.setStyleSheet("background-color: #ED1E24")
        self.ui.btn_02.setStyleSheet("background-color: #D36A28")
        self.ui.btn_03.setStyleSheet("background-color: #FAA419")
        self.ui.btn_04.setStyleSheet("background-color: #E4BD20")
        self.ui.btn_05.setStyleSheet("background-color: #F7EC14")
        self.ui.btn_06.setStyleSheet("background-color: #9AC93B")
        self.ui.btn_07.setStyleSheet("background-color: #10813F")
        self.ui.btn_08.setStyleSheet("background-color: #FFFFFF")
        self.ui.btn_09.setStyleSheet("background-color: #D3D3D3")
        self.ui.btn_10.setStyleSheet("background-color: #99D4C0")
        self.ui.btn_11.setStyleSheet("background-color: #63C6C1")
        self.ui.btn_12.setStyleSheet("background-color: #008181")
        self.ui.btn_13.setStyleSheet("background-color: #3853A4")
        self.ui.btn_14.setStyleSheet("background-color: #272974")
        self.ui.btn_15.setStyleSheet("background-color: #7651A1")
        self.ui.btn_16.setStyleSheet("background-color: #B9539F")
        self.ui.btn_17.setStyleSheet("background-color: #7d277E")
        self.ui.btn_18.setStyleSheet("background-color: #696969")
        self.ui.btn_19.setStyleSheet("background-color: #020202")

        # Connect the buttons to the setColor function
        self.ui.btn_00.clicked.connect(lambda: self.setColor("#A62A2A"))
        self.ui.btn_01.clicked.connect(lambda: self.setColor("#ED1E24"))
        self.ui.btn_02.clicked.connect(lambda: self.setColor("#D36A28"))
        self.ui.btn_03.clicked.connect(lambda: self.setColor("#FAA419"))
        self.ui.btn_04.clicked.connect(lambda: self.setColor("#E4BD20"))
        self.ui.btn_05.clicked.connect(lambda: self.setColor("#F7EC14"))
        self.ui.btn_06.clicked.connect(lambda: self.setColor("#9AC93B"))
        self.ui.btn_07.clicked.connect(lambda: self.setColor("#10813F"))
        self.ui.btn_08.clicked.connect(lambda: self.setColor("#FFFFFF"))
        self.ui.btn_09.clicked.connect(lambda: self.setColor("#D3D3D3"))
        self.ui.btn_10.clicked.connect(lambda: self.setColor("#99D4C0"))
        self.ui.btn_11.clicked.connect(lambda: self.setColor("#63C6C1"))
        self.ui.btn_12.clicked.connect(lambda: self.setColor("#008181"))
        self.ui.btn_13.clicked.connect(lambda: self.setColor("#3853A4"))
        self.ui.btn_14.clicked.connect(lambda: self.setColor("#272974"))
        self.ui.btn_15.clicked.connect(lambda: self.setColor("#7651A1"))
        self.ui.btn_16.clicked.connect(lambda: self.setColor("#B9539F"))
        self.ui.btn_17.clicked.connect(lambda: self.setColor("#7d277E"))
        self.ui.btn_18.clicked.connect(lambda: self.setColor("#696969"))
        self.ui.btn_19.clicked.connect(lambda: self.setColor("#020202"))

        # Connect the pick color button to the pickColor function
        self.ui.btn_pickColor.clicked.connect(self.pickColor)


    # Show window with docking ability
    def run(self):
        self.show(dockable = True)

    # Set the color to the selected object
    def setColor(self, color):
        selected = cmds.ls(selection=True)
        Color.setColor(selected, color)

    # Open the color dialog and set the color to the selected object
    def pickColor(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            selected = cmds.ls(selection=True)
            Color.setColor(selected, color.name())
        