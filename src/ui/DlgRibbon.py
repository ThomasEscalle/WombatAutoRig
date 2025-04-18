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

from wombatAutoRig.src.ui.forms import ui_DlgRibbon
from wombatAutoRig.src.ui import IconLoader
from wombatAutoRig.src.core import FileHelper

from wombatAutoRig.src.core import Ribbon
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgRibbon(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgRibbon, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.ui = ui_DlgRibbon.Ui_DlgRibbon()
        self.ui.setupUi(self)

        self.setWindowTitle("Ribbon")

        self.ui.btn_apply.clicked.connect(self.apply)
        self.ui.btn_create.clicked.connect(self.create)
        self.ui.btn_cancel.clicked.connect(self.cancel)



    def apply(self):
        name = self.ui.le_name.text()
        nurbs = self.ui.sb_nurbs.value()
        Ribbon.Ribbon(Span=nurbs , Name = name)


    def create(self):
        self.apply()
        self.close()

    def cancel(self):
        self.close()

    # Show window with docking ability
    def run(self):
        self.show(dockable = True)