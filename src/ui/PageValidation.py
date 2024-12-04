from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtCore import Signal

from wombatAutoRig.src.ui.forms import ui_PageValidation

from wombatAutoRig.src.ui import IconLoader
from wombatAutoRig.src.ui.PageBase import PageBase

# Page to validate and create the rig or not
class PageValidation(PageBase):
    def __init__(self):
        super(PageValidation, self).__init__()

        self.ui = ui_PageValidation.Ui_PageValidation()
        self.ui.setupUi(self)

        self.ui.btnYes.clicked.connect(self.onYesClicked)
        self.ui.btnNo.clicked.connect(self.onNoClicked)

        

        self.ui.btnYes.setIcon(IconLoader.loadIcon("yes"))
        self.ui.btnNo.setIcon(IconLoader.loadIcon("close"))


    # Signal to create the rig
    yesClicked = Signal()
    noClicked = Signal()


    def hideNextAndCancel(self):
        """
        Hides the "Next" and "Cancel" buttons in the UI.

        Returns:
            bool: Always returns True.
        """
        return True



    # When the user clicks the Yes button
    def onYesClicked(self):
        # Emit the signal to create the rig
        self.yesClicked.emit()

    def addDataToSettings(self,settings):
        print("Add the data to the settings")
        return settings
        
    def autoFill(self):
        pass

    # When the user clicks the No button
    def onNoClicked(self):
        self.noClicked.emit()
