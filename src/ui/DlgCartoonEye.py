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

from wombatAutoRig.src.ui.forms.ui_DlgCartoonEye import Ui_DlgCartoonEye
from wombatAutoRig.src.core import CartoonEye


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgCartoonEye(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgCartoonEye, self).__init__(parent)

        self.ui = Ui_DlgCartoonEye()
        self.ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)


        self.setWindowTitle("Cartoon Eye")


        # Connect signals
        self.ui.btnApply.clicked.connect(self.apply)
        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnCreate.clicked.connect(self.create)
        self.ui.btnTopVtxAdd.clicked.connect(self.addTopVtx)
        self.ui.btnTopVtxRemove.clicked.connect(self.removeTopVtx)
        self.ui.btnBottomVtxAdd.clicked.connect(self.addBottomVtx)
        self.ui.btnBottomVtxRemove.clicked.connect(self.removeBottomVtx)
        self.ui.btnEyeGeoAdd.clicked.connect(self.addEyeGeo)
        self.ui.btnFaceGeoAdd.clicked.connect(self.addFaceGeo)



    # Show window with docking ability
    def run(self):
        self.show(dockable = True)

    # Apply the changes
    def apply(self):
        # Get the values from the UI
        eyeGeo = self.ui.leEyeGeo.text()
        faceGeo = self.ui.leFaceGeo.text()
        
        
        topVtx = self.ui.leTopVtx.text()
        topVtx = topVtx.split(" ")

        bottomVtx = self.ui.leBottomVtx.text()
        bottomVtx = bottomVtx.split(" ")

        # Get the side of the eye (cbSide)
        side = self.ui.cbSide.currentText()

        CartoonEye.cartoonEye(eyeGeo, faceGeo, topVtx, bottomVtx, side)




    # Create and close
    def create(self):
        self.apply()
        self.close()

    # Add top vtx
    def addTopVtx(self):
        # Get the selected vertices and store them into the line edit 'leTopVtx'
        sel = cmds.ls(sl=True, fl=True)
        if sel:
            self.ui.leTopVtx.setText(" ".join(sel))
    
    # Remove top vtx
    def removeTopVtx(self):
        self.ui.leTopVtx.setText("")

    # Add bottom vtx
    def addBottomVtx(self):
        # Get the selected vertices and store them into the line edit 'leTopVtx'
        sel = cmds.ls(sl=True, fl=True)
        if sel:
            self.ui.leBottomVtx.setText(" ".join(sel))

    # Remove bottom vtx
    def removeBottomVtx(self):
        self.ui.leBottomVtx.setText("")

    # Add eye geometry
    def addEyeGeo(self):
        # Get the selected geometry and set it to the line edit 'leEyeGeo'
        # Only the first selected object is taken into account
        sel = cmds.ls(sl=True)
        if sel:
            self.ui.leEyeGeo.setText(sel[0])
    
    # Add face geometry
    def addFaceGeo(self):
        # Get the selected geometry and set it to the line edit 'leFaceGeo'
        # Only the first selected object is taken into account
        sel = cmds.ls(sl=True)
        if sel:
            self.ui.leFaceGeo.setText(sel[0])