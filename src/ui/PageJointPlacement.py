from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

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

    # Say if the user can go to the next page or not
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