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

from wombatAutoRig.src.ui.forms.ui_DlgAttachBlendShape import Ui_DlgAttachBlendShape



def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgAttachBlendShape(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgAttachBlendShape, self).__init__(parent)

        self.ui = Ui_DlgAttachBlendShape()
        self.ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)


        self.setWindowTitle("Attach Blend Shape")

        self.ui.BtnApply.clicked.connect(self.apply)
        self.ui.BtnCancel.clicked.connect(self.close)


    # Show window with docking ability
    def run(self):
        self.show(dockable = True)

    # Apply the changes
    def apply(self):

        channel = self.ui.CB_Chanel.currentText()
        blendShapeName = self.ui.LE_BshpName.text()
        BshpTarget = self.ui.Le_TargetName.text()
        maxValue = self.ui.LE_MaxValue.text()


        if(channel == "Translate X"):
            channel = "translateX"
        elif(channel == "Translate Y"):
            channel = "translateY"
        elif(channel == "Translate Z"):
            channel = "translateZ"
        elif(channel == "Rotate X"):
            channel = "rotateX"
        elif(channel == "Rotate Y"):
            channel = "rotateY"
        elif(channel == "Rotate Z"):
            channel = "rotateZ"
        elif(channel == "Scale X"):
            channel = "scaleX"
        elif(channel == "Scale Y"):
            channel = "scaleY"
        elif(channel == "Scale Z"):
            channel = "scaleZ"
        else:
            print("Invalid Channel")
            return

        # Get the selected object
        selection = cmds.ls(selection=True)
        if not selection:
            print("Please select an object")
            return
        obj = selection[0]


        print("Channel: ", channel)
        print("Blend Shape Name: ", blendShapeName)
        print("Target: ", BshpTarget)
        print("Max Value: ", maxValue)

        # Check if the max value is a number
        try:
            float(maxValue)
        except ValueError:
            print("The max value must be a number")
            return
        
        # Check if the blend shape exists
        if not cmds.objExists(blendShapeName):
            print("Blend Shape not found")
            return
        
        
        # Create a RemapValue node
        remapValue = cmds.createNode("remapValue", name="rmvBshp_" + blendShapeName + "_" + BshpTarget)
        cmds.setAttr(remapValue + ".inputMax", float(maxValue))

        # Connect the channel to the remapValue node
        print("Connecting: ", obj + "." + channel, " to ", remapValue + ".inputValue")
        cmds.connectAttr(obj + "." + channel, remapValue + ".inputValue")

        # Connect the remapValue node to the blend shape
        print("Connecting: ", remapValue + ".outValue", " to ", blendShapeName + "." + BshpTarget)
        cmds.connectAttr(remapValue + ".outValue", blendShapeName + "." + BshpTarget)

        print("Done")

        pass