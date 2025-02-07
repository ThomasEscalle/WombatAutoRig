from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from maya import cmds

from wombatAutoRig.src.ui.forms import ui_PageControllerPlacement

from wombatAutoRig.src.ui import DlgControllers
from wombatAutoRig.src.ui import DlgColor
from wombatAutoRig.src.core import MirrorControllerPlacement

from wombatAutoRig.src.ui.PageBase import PageBase
from wombatAutoRig.src.ui import IconLoader

# Page to place the controllers
class PageControllerPlacement(PageBase):

    def __init__(self):
        super(PageControllerPlacement, self).__init__()

        self.ui = ui_PageControllerPlacement.Ui_PageControllerPlacement()
        self.ui.setupUi(self)

        # Connect signals
        self.ui.cb_IkCTRLS.stateChanged.connect(self.onIkClicked)
        self.ui.cb_fkCTRLS.stateChanged.connect(self.onFkClicked)
        self.ui.cb_otherCTRLS.stateChanged.connect(self.onOtherClicked)
        self.ui.cb_ShowGeo.stateChanged.connect(self.onShowGeo)
        self.ui.cb_ShowJoints.stateChanged.connect(self.onShowJoints)

        self.ui.btnControllers.clicked.connect(self.onControllersClicked)
        self.ui.btnColors.clicked.connect(self.onColorsClicked)
        self.ui.pushButton.clicked.connect(self.mirror)

        self.ui.cb_IkCTRLS.setChecked(True)
        self.ui.cb_ShowGeo.setChecked(True)

        # Set icons
        self.ui.btnColors.setIcon(IconLoader.loadIcon("colors"))
        self.ui.btnControllers.setIcon(IconLoader.loadIcon("controller"))

        self.settings = None


    # Signal to create the rig
    canceled = Signal()
    accepted = Signal()
    entered = Signal()
    

    # When you want to mirror
    def mirror(self):
        print("Mirror")
        mirrorDirection = self.ui.cb_MirrorDirection.currentIndex()
        # Leg L -> R
        if(mirrorDirection == 0):
            MirrorControllerPlacement.mirrorCtrlsLegLtoR()
        # Leg R -> L
        if(mirrorDirection == 1):
            MirrorControllerPlacement.mirrorCtrlsLegRtoL()
        # Arm L -> R
        if(mirrorDirection == 2):
            MirrorControllerPlacement.mirrorCtrlsArmLtoR()
        # Arm R -> L
        if(mirrorDirection == 3):
            MirrorControllerPlacement.mirrorCtrlsArmRtoL()

    # Triggers the signals
    def onCanceled(self):
        self.canceled.emit()

    # Triggers the signals
    def onAccepted(self):
        self.accepted.emit()

    # Triggers the signals
    def onEntered(self):
        self.entered.emit()

    def setSettings(self,settings): 
        self.settings = settings
    
    
    def autoFill(self):
        pass
    
    # Say if the user can go to the next page or not
    def canGoNext(self):
        return True

    def addDataToSettings(self,settings):
        return settings


    def onFkClicked(self):
        if self.ui.cb_fkCTRLS.isChecked():
            cmds.showHidden("AutoRig_Data|ControllersPlacement|FK_Controllers")
        else:
            cmds.hide("AutoRig_Data|ControllersPlacement|FK_Controllers")

    def onIkClicked(self):
        if self.ui.cb_IkCTRLS.isChecked():
            cmds.showHidden("AutoRig_Data|ControllersPlacement|IK_Controllers")
        else:
            cmds.hide("AutoRig_Data|ControllersPlacement|IK_Controllers")

    def onOtherClicked(self):
        if self.ui.cb_otherCTRLS.isChecked():
            cmds.showHidden("AutoRig_Data|ControllersPlacement|Other_Controllers")
        else:
            cmds.hide("AutoRig_Data|ControllersPlacement|Other_Controllers")

    def onShowGeo(self):
        if self.settings is not None:
            geo_elements = self.settings["geo"]

            if self.ui.cb_ShowGeo.isChecked():
                for geo in geo_elements:
                    cmds.showHidden(geo)
            else:
                for geo in geo_elements:
                    cmds.hide(geo)

    def onShowJoints(self):
        if self.ui.cb_ShowJoints.isChecked():
            cmds.showHidden("AutoRig_Data|JointsPlacement")
        else:
            cmds.hide("AutoRig_Data|JointsPlacement")

    def onControllersClicked(self):
        dlg = DlgControllers.DlgControllers()
        dlg.setReplaceMode()
        dlg.run()

    def onColorsClicked(self):
        dlg = DlgColor.DlgColor()
        dlg.run()


