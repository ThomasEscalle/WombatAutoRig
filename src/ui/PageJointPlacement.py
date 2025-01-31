from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wombatAutoRig.src.core import AutorigHelper

from wombatAutoRig.src.ui import IconLoader

from maya import cmds

from wombatAutoRig.src.ui.forms import ui_PageJointPlacement
from wombatAutoRig.src.ui.PageBase import PageBase

class PageJointPlacement(PageBase):
    def __init__(self):
        super(PageJointPlacement, self).__init__()

        self.ui = ui_PageJointPlacement.Ui_PageJointPlacement()
        self.ui.setupUi(self)

        self.ui.btnShowLRA.clicked.connect(self.showLraButtonClicked)
        self.ui.btnShowLRA.setIcon(IconLoader.loadIcon("LRA"))

        self.ui.btnTemplate.clicked.connect(self.templateButtonClicked)
        self.ui.btnTemplate.setIcon(IconLoader.loadIcon("eye"))

        self.ui.cb_MirrorDirection.clear()
        self.ui.cb_MirrorDirection.addItem("Leg L -> R")
        self.ui.cb_MirrorDirection.addItem("Leg R -> L")
        self.ui.cb_MirrorDirection.addItem("Arm L -> R")
        self.ui.cb_MirrorDirection.addItem("Arm R -> L")
        self.ui.btnMirro.clicked.connect(self.mirror)

    # Signal to create the rig
    canceled = Signal()
    accepted = Signal()
    entered = Signal()
    
    def mirror(self):
        print("Mirror")
        mirrorDirection = self.ui.cb_MirrorDirection.currentIndex()
        # Leg L -> R
        if(mirrorDirection == 0):
            pass

    # Triggers the signals
    def onCanceled(self):
        self.canceled.emit()

    # Triggers the signals
    def onAccepted(self):
        self.accepted.emit()

    # Triggers the signals
    def onEntered(self):
        self.entered.emit()

    # Say if the user can go sto the next page or not
    def canGoNext(self):
        return True

    def addDataToSettings(self,settings):
        print("Add the data to the settings")
        return settings
    
    def showLraButtonClicked(self):
        # Loop for all the joints in the scene
        # If their prefix is "PlacementJnt" then show or hide the LRA
        for jnt in cmds.ls(type="joint"):
            if jnt.startswith("PlacementJnt_"):
                # Check if the LRA is visible
                if cmds.getAttr(jnt + ".displayLocalAxis"):
                    cmds.setAttr(jnt + ".displayLocalAxis", 0)
                else:
                    cmds.setAttr(jnt + ".displayLocalAxis", 1)
        return
    
    def templateButtonClicked(self):
        print("Template button clicked")

    def autoFill(self):
        pass
    
