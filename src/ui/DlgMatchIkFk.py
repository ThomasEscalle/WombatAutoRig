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

from wombatAutoRig.src.ui.forms.ui_DlgMatchIkFk import Ui_DlgMatchIkFk

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


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

        print("###################")
        print("Side: ", side_Str)
        print("Match: ", match_Str)
        print("###################")
        pass

    
    def cancel(self):
        print("cancel")

        self.close()
