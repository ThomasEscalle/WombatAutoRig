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

from wombatAutoRig.src.ui.forms.ui_DlgQuickLoad import Ui_DlgQuickLoad
from wombatAutoRig.src.core import FileHelper


from wombatAutoRig.src.core import TemplateManager

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgQuickLoad(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgQuickLoad, self).__init__(parent)

        self.ui = Ui_DlgQuickLoad()
        self.ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)


        self.setWindowTitle("Quick Load")

        self.ui.btnShowJnts.clicked.connect(self.btnShowJoints)
        self.ui.btnShowIkCtrls.clicked.connect(self.btnShowIkCtrls)
        self.ui.btnShowFkCtrls.clicked.connect(self.btnShowFkCtrls)
        self.ui.btnShowOtherCtrls.clicked.connect(self.btnShowOtherCtrls)
        self.ui.btnCreate.clicked.connect(self.apply)
        self.ui.btnCancel.clicked.connect(self.cancel)


        # Initialise the template list
        self.refresh()  




    # Show window with docking ability
    def run(self):
        self.show(dockable = True)


    def apply(self):   
        # Check if the "AutoRig_Data" group exists
        if not cmds.objExists("AutoRig_Data"):
            print("AutoRig_Data group doesn't exist")
            self.close()

        
    # Search for the templates installed in the templates folder
    def refresh(self):
        manager = TemplateManager.TemplateManager()
        templates = manager.getTemplates()

        # Clear the combobox
        self.ui.cb_Template.clear()

        # Add the templates to the combobox
        for template in templates:
            self.ui.cb_Template.addItem(template[0])
            self.ui.cb_Template.setItemData(self.ui.cb_Template.count() - 1, template[1], QtCore.Qt.UserRole)

        # Check if the "AutoRig_Data" group exists
        if not cmds.objExists("AutoRig_Data"):
            print("AutoRig_Data group doesn't exist")
            self.close()
        

    def cancel(self):
        print("cancel")

        self.close()

    # Get the selected template
    def getSelectedTemplate(self):
        template = TemplateManager.TemplateManager().getTemplate(self.ui.cb_Template.currentText())
        return template

    def btnShowIkCtrls(self):
        print("btnShowIkCtrls")

    def btnShowFkCtrls(self):
        print("btnShowFkCtrls")

    def btnShowOtherCtrls(self):
        print("btnShowOtherCtrls")

    def btnShowJoints(self):
        print("btnShowJoints")