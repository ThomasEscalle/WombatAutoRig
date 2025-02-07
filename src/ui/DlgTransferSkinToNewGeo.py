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


from wombatAutoRig.src.ui.forms import ui_DlgTransferSkinToNewGeo



def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgTransferSkinToNewGeo(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgTransferSkinToNewGeo, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.ui = ui_DlgTransferSkinToNewGeo.Ui_TransferSkinToNewGeo()
        self.ui.setupUi(self)

        self.setWindowTitle("Transfer Skin to New Geo")

        self.ui.btnApply.clicked.connect(self.apply)
        self.ui.btnCancel.clicked.connect(self.close)

    # Show window with docking ability
    def run(self):
        self.show(dockable = True)

    def apply(self) :
        pass
        super(DlgTransferSkinToNewGeo, self).accept()

    
    def close(self):
        super(DlgTransferSkinToNewGeo, self).close()