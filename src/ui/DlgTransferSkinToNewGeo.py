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


def getInfluencingJoints(sel=None):

    if not sel:
        print("No object selected.")
        return

    # Get the skin cluster
    skinCluster = cmds.ls(cmds.listHistory(sel), type="skinCluster")
    if not skinCluster:
        print("No skin cluster found in " + sel)
        return None

    # Get the influencing joints
    joints = cmds.skinCluster(skinCluster[0], query=True, inf=True)
    print(joints)
    return joints


def process( skinedGrp, targetGrp):
    print ("###### INFO : Processing " + skinedGrp + " to " + targetGrp)    
    # Iterate over all the objects in the skinedGrp, get their path
    for obj in cmds.listRelatives(skinedGrp, children=True, fullPath=True, allDescendents=True):
        # Check if there is an object with the same name and the same relative path in the targetGrp
        relativePath = obj.replace(skinedGrp, "")

        # If the object is a shape, get the parent
        if cmds.objectType(obj) == "mesh":
            obj = cmds.listRelatives(obj, parent=True, fullPath=True)[0]

        if "Orig" in relativePath:
            continue

        # Get the target object
        targetObj = targetGrp + relativePath



        # Check if the target object exists and is a mesh, and is visible
        if cmds.objExists(targetObj)  and cmds.getAttr(obj + ".visibility") == 1 and cmds.objectType(targetObj) == "mesh":

            print("############# INFO : Processing " + relativePath +  " to " + targetObj)
        
            # Get the skin cluster of the object
            skinCluster = cmds.ls(cmds.listHistory(obj), type="skinCluster")

            # Check if the object has a skin cluster
            if skinCluster == []:
                print("# ERROR # No skin cluster found in " + obj)
                continue
            if not skinCluster:
                print("# ERROR # No skin cluster found in " + obj)
                return None
            
            # Get the influencing joints
            joints = cmds.skinCluster(skinCluster[0], query=True, inf=True)

            # If there are no influencing joints, skip the object
            if not joints:
                print("# ERROR # No influencing joints found in " + obj)
                continue

            print("############# INFO : Influencing joints : " + str(joints))
            

            # Skin the target object with the joints
            cmds.select(joints, r=True)
            cmds.select(targetObj, add=True)
            cmds.skinCluster(tsb=True)

            # Copy the skin weights
            cmds.select(obj, r=True)
            cmds.select(targetObj, add=True)
            cmds.CopySkinWeights()

            print("")








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

        process(skinedGrp, targetGrp)


        super(DlgTransferSkinToNewGeo, self).accept()

    
    def close(self):
        super(DlgTransferSkinToNewGeo, self).close()