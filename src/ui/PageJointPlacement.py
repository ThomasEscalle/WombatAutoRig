from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wombatAutoRig.src.ui.forms import ui_PageJointPlacement
from wombatAutoRig.src.ui.PageBase import PageBase

class PageJointPlacement(PageBase):
    def __init__(self):
        super(PageJointPlacement, self).__init__()

        self.ui = ui_PageJointPlacement.Ui_PageJointPlacement()
        self.ui.setupUi(self)

    # Say if the user can go to the next page or not
    def canGoNext(self):
        return True