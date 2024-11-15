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

from wombatAutoRig.src.core import MatrixConstrain

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

        # Set the checkbox to checked by default
        self.ui.cb_offset.setChecked(True)
        self.ui.cb_translate_all.setChecked(True)
        self.ui.cb_rotate_all.setChecked(True)
        self.ui.cb_translate_X.setChecked(True)
        self.ui.cb_translate_Y.setChecked(True)
        self.ui.cb_translate_Z.setChecked(True)
        self.ui.cb_rotate_X.setChecked(True)
        self.ui.cb_rotate_Y.setChecked(True)
        self.ui.cb_rotate_Z.setChecked(True)

        # Connect the signals to the slots
        self.ui.cb_translate_all.clicked.connect(self.on_translate_all)
        self.ui.cb_rotate_all.clicked.connect(self.on_rotate_all)
        self.ui.cb_translate_X.clicked.connect(lambda: self.on_translate("X"))
        self.ui.cb_translate_Y.clicked.connect(lambda: self.on_translate("Y"))
        self.ui.cb_translate_Z.clicked.connect(lambda: self.on_translate("Z"))
        self.ui.cb_rotate_X.clicked.connect(lambda: self.on_rotate("X"))
        self.ui.cb_rotate_Y.clicked.connect(lambda: self.on_rotate("Y"))
        self.ui.cb_rotate_Z.clicked.connect(lambda: self.on_rotate("Z"))

        self.ui.btn_apply.clicked.connect(self.apply)
        self.ui.btn_create.clicked.connect(self.create)
        self.ui.btn_cancel.clicked.connect(self.cancel)

    # Show window with docking ability
    def run(self):
        self.show(dockable = True)

    # Apply the matrix constraint
    def apply(self):
        # Get the two selected items
        selection = cmds.ls(selection=True)
        if len(selection) < 2:
            cmds.warning("Select 2 objects")
            return

        # Get the selected items
        Master  = []
        n = len(selection)
        for i in range(n):
            if i != n-1:
                Master.append(selection[i])
            else :
                Slave = selection[i]
        
        offset = self.ui.cb_offset.isChecked()

        tX = self.ui.cb_translate_X.isChecked()
        tY = self.ui.cb_translate_Y.isChecked()
        tZ = self.ui.cb_translate_Z.isChecked()

        rX = self.ui.cb_rotate_X.isChecked()
        rY = self.ui.cb_rotate_Y.isChecked()
        rZ = self.ui.cb_rotate_Z.isChecked()

        
        MatrixConstrain.MatrixConstrain(Master, Slave, Offset=offset, tX=tX, tY=tY, tZ=tZ, rX=rX, rY=rY, rZ=rZ)
        pass

    # Apply and close
    def create(self):
        self.apply()
        self.close()
        pass

    # Close the window
    def cancel(self):
        self.close()
        pass


    # When the user triggers the translate_all checkbox
    def on_translate_all(self):
        if self.ui.cb_translate_all.isChecked():
            self.ui.cb_translate_X.setChecked(True)
            self.ui.cb_translate_Y.setChecked(True)
            self.ui.cb_translate_Z.setChecked(True)
        else:
            self.ui.cb_translate_X.setChecked(False)
            self.ui.cb_translate_Y.setChecked(False)
            self.ui.cb_translate_Z.setChecked(False)

    # When the user triggers the rotate_all checkbox
    def on_rotate_all(self):
        if self.ui.cb_rotate_all.isChecked():
            self.ui.cb_rotate_X.setChecked(True)
            self.ui.cb_rotate_Y.setChecked(True)
            self.ui.cb_rotate_Z.setChecked(True)
        else:
            self.ui.cb_rotate_X.setChecked(False)
            self.ui.cb_rotate_Y.setChecked(False)
            self.ui.cb_rotate_Z.setChecked(False)

    # When the user triggers the translate checkbox (X, Y, Z)
    def on_translate(self, axis):
        # Uncheck the translate_all checkbox
        self.ui.cb_translate_all.setChecked(False)

        pass

    # When the user triggers the rotate checkbox (X, Y, Z)
    def on_rotate(self, axis):
        # Uncheck the rotate_all checkbox
        self.ui.cb_rotate_all.setChecked(False)
        pass


    
