from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from maya import cmds

from wombatAutoRig.src.ui.forms import ui_PageControllerPlacement

from wombatAutoRig.src.ui import DlgControllers

from wombatAutoRig.src.ui.PageBase import PageBase
from wombatAutoRig.src.ui import IconLoader

# Page to place the controllers
class PageControllerPlacement(PageBase):

    def __init__(self):
        super(PageControllerPlacement, self).__init__()

        self.ui = ui_PageControllerPlacement.Ui_PageControllerPlacement()
        self.ui.setupUi(self)

        # Connect signals
        self.ui.btnFkMode.clicked.connect(self.onFkModeClicked)
        self.ui.btnIkMode.clicked.connect(self.onIkModeClicked)
        self.ui.btnControllers.clicked.connect(self.onControllersClicked)

        # Set icons
        self.ui.btnFkMode.setIcon(IconLoader.loadIcon("skull"))
        self.ui.btnIkMode.setIcon(IconLoader.loadIcon("skeleton"))

        # Set the default mode to Fk
        self.ui.btnFkMode.hide()


    
    def autoFill(self):
        pass
    
    # Say if the user can go to the next page or not
    def canGoNext(self):
        return True

    # When the user clicks the Fk mode button
    # Hide the Fk mode button and show the Ik mode button to make it look like a toggle
    def onFkModeClicked(self):
        self.ui.btnIkMode.show()
        self.ui.btnFkMode.hide()

        cmds.showHidden("AutoRig_Data|ControllersPlacement|IK_Controllers")
        cmds.hide("AutoRig_Data|ControllersPlacement|FK_Controllers")

    def addDataToSettings(self,settings):
        print("Add the data to the settings")
        return settings

    # When the user clicks the Ik mode button
    # Hide the Ik mode button and show the Fk mode button to make it look like a toggle
    def onIkModeClicked(self):
        self.ui.btnFkMode.show()
        self.ui.btnIkMode.hide()

        cmds.showHidden("AutoRig_Data|ControllersPlacement|FK_Controllers")
        cmds.hide("AutoRig_Data|ControllersPlacement|IK_Controllers")

    def onControllersClicked(self):
        dlg = DlgControllers.DlgControllers()
        dlg.setReplaceMode()
        dlg.run()


