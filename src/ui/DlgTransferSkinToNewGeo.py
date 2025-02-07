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

        self.ui.btnSelectSkinedGrp.clicked.connect(self.selectSkinedGrp)
        self.ui.btnSelectGrp.clicked.connect(self.selectGrp)

    # Show window with docking ability
    def run(self):
        self.show(dockable = True)

    # Select the skined group
    def selectSkinedGrp(self):
        self.ui.leSkinedGrp.setText(cmds.ls(sl=True, long=True)[0])
    
    # Select the target group
    def selectGrp(self):
        self.ui.leTargetGrp.setText(cmds.ls(sl=True, long=True)[0])

    # Apply the transfer of the skin
    def apply(self) :
        
        # Get the groups as string
        skinedGrp = self.ui.leSkinedGrp.text()
        targetGrp = self.ui.leTargetGrp.text()

        # Check if the skinedGrp and targetGrp are not empty
        if skinedGrp == "" or targetGrp == "":
            print("Please fill all fields")
            return

        # Iterate over all the objects in the skinedGrp, get their path
        for obj in cmds.listRelatives(skinedGrp, children=True, fullPath=True):

            # Check if there is an object with the same name and the same relative path in the targetGrp
            relativePath = obj.replace(skinedGrp, "")
            if cmds.objExists(targetGrp + relativePath):


                print("Transfer the skin from " + obj + " to " + targetGrp + relativePath)  

            else:
                print("obj doesn't exist : " + targetGrp + relativePath)
                continue


        super(DlgTransferSkinToNewGeo, self).accept()

    
    def close(self):
        super(DlgTransferSkinToNewGeo, self).close()