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

        self.setupColors()

    def setupColors(self):


        self.ui.btn_00.setStyleSheet("background-color: #FA8072") # Salmon
        self.ui.btn_01.setStyleSheet("background-color: #FF0000") # Red
        self.ui.btn_02.setStyleSheet("background-color: #FF4500") # Orange
        self.ui.btn_03.setStyleSheet("background-color: #FFD700") # Gold
        self.ui.btn_04.setStyleSheet("background-color: #FFFF00") # Yellow
        self.ui.btn_05.setStyleSheet("background-color: #9ACD32") # Yellow-Green
        self.ui.btn_06.setStyleSheet("background-color: #008000") # Green
        self.ui.btn_07.setStyleSheet("background-color: #008080") # Teal
        self.ui.btn_08.setStyleSheet("background-color: #00FF7F") # Spring Green
        self.ui.btn_09.setStyleSheet("background-color: #7FFFD4") # Aqua Marine
        self.ui.btn_10.setStyleSheet("background-color: #007FFF") # Azure
        self.ui.btn_11.setStyleSheet("background-color: #0000FF") # Blue
        self.ui.btn_12.setStyleSheet("background-color: #8A2BE2") # Blue Violet
        self.ui.btn_13.setStyleSheet("background-color: #4B0082") # Indigo
        self.ui.btn_14.setStyleSheet("background-color: #800080") # Purple
        self.ui.btn_15.setStyleSheet("background-color: #DDA0DD") # Plum
        self.ui.btn_16.setStyleSheet("background-color: #FFFFFF") # White
        self.ui.btn_17.setStyleSheet("background-color: #A9A9A9") # Grey
        self.ui.btn_18.setStyleSheet("background-color: #808080") # Dark Grey
        self.ui.btn_19.setStyleSheet("background-color: #000000") # Black

    # Show window with docking ability
    def run(self):
        self.show(dockable = True)