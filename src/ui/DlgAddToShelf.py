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
import maya.mel as mel
from maya.OpenMayaUI import MQtUtil

from wombatAutoRig.src.ui.forms import ui_DlgAddToShelf
from wombatAutoRig.src.ui import IconLoader
from wombatAutoRig.src.core import FileHelper

from wombatAutoRig.src.core import Color

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgAddToShelf(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgAddToShelf, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.ui = ui_DlgAddToShelf.Ui_DlgAddToShelf()
        self.ui.setupUi(self)

        self.setWindowTitle("Add tools to shelf")

        self.ui.btn_add.clicked.connect(self.add_to_shelf)
        self.ui.btn_close.clicked.connect(self.close)

        self.ui.comboBox.addItem("Color")
        self.ui.comboBox.addItem("Ribbon")
        self.ui.comboBox.addItem("Ribbon on Curve")
        self.ui.comboBox.addItem("Hook")




    # Show window with docking ability
    def run(self):
        self.show(dockable = True)





    def add_to_shelf(self):
        selectedItem = self.ui.comboBox.currentText()
        name = ""
        command = ""

        if(selectedItem == "Color"):
            name = "Color"
            command = "import wombatAutoRig.src.ui.DlgColor as DlgColor\\nDialog = DlgColor.DlgColor()\\nDialog.run()"
        elif(selectedItem == "Ribbon"):
            name = "Ribbon"
            command = "import wombatAutoRig.src.ui.DlgRibbon as DlgRibbon\\nDialog = DlgRibbon.DlgRibbon()\\nDialog.run()"
        elif(selectedItem == "Ribbon on Curve"):
            name = "Ribbon on Curve"
            command = "import wombatAutoRig.src.ui.DlgRibbonOnCurves as DlgRibbonOnCurves\\nDialog = DlgRibbonOnCurves.DlgRibbonOnCurves()\\nDialog.run()"
        elif(selectedItem == "Hook"):
            name = "Hook"
            command = "from wombatAutoRig.src.core import Offset\\nOffset.offset(cmds.ls(selection=True), 3)"


        melCmd = "scriptToShelf \"" + name + "\" \""+ command + "\" \"0\";"
        mel.eval(melCmd)

        print(melCmd)
    