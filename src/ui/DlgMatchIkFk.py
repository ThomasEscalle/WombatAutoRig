from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import sys
from PySide6 import QtWidgets, QtCore, QtGui
import maya.OpenMayaUI as omui
import shiboken6
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.cmds as cmds
from maya.OpenMayaUI import MQtUtil

from wombatAutoRig.src.ui.forms.ui_DlgMatchIkFk import Ui_DlgMatchIkFk

from wombatAutoRig.src.core import MatchingIkFk

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken6.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgMatchIkFk(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgMatchIkFk, self).__init__(parent)

        self.ui = Ui_DlgMatchIkFk()
        self.ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.setWindowTitle("Match Ik Fk")

        self.ui.btnApply.clicked.connect(self.apply)



    # Show window with docking ability
    def run(self):
        self.show(dockable = True)


    def apply(self):   
        side_Str = self.ui.cb_Side.currentText()
        match_Str = self.ui.cb_Match.currentText()

        #get the CTRL selected
        slection = cmds.ls(selection=True)
        if slection == None:
            return "Please select a CTRL to have the relative path"
        CTRL = slection[0]

        if match_Str == "Ik -> Fk":
            MatchingIkFk.matchFkIk(CTRL=CTRL, Member = side_Str)

        if match_Str == "Fk -> Ik":
            MatchingIkFk.matchIkFk(CTRL=CTRL, Member = side_Str)

        pass

    
    def cancel(self):
        print("cancel")

        self.close()
