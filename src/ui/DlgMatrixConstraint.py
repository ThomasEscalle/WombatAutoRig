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

from wombatAutoRig.src.ui.forms import ui_DlgMatrixConstraint
from wombatAutoRig.src.ui import IconLoader
from wombatAutoRig.src.core import FileHelper

from wombatAutoRig.src.core import Color

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgMatrixConstraint(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgMatrixConstraint, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.ui = ui_DlgMatrixConstraint.Ui_DlgMatrixConstraint()
        self.ui.setupUi(self)

        self.setWindowTitle("Matrix Constraint")

    # Show window with docking ability
    def run(self):
        self.show(dockable = True)
