from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wombatAutoRig.src.ui.forms import ui_PageTemplateSelection
from wombatAutoRig.src.ui.PageBase import PageBase

from wombatAutoRig.src.ui import IconLoader

from wombatAutoRig.src.core import TemplateManager

class PageTemplateSelection(PageBase):

    def __init__(self):
        super(PageTemplateSelection, self).__init__()

        self.ui = ui_PageTemplateSelection.Ui_PageTemplateSelection()
        self.ui.setupUi(self)


        # Connect the signals
        self.ui.btnRefresh.clicked.connect(self.refresh)

        # Set the icons
        self.ui.btnRefresh.setIcon(IconLoader.loadIcon("refresh.png"))
        self.ui.btnRefresh.setText("")
        self.ui.btnRefresh.setFlat(True)

        # Refresh the page
        self.refresh()

    # Get the selected template
    def getSelectedTemplate(self):
        template = TemplateManager.TemplateManager().getTemplate(self.ui.cbSelectTemplate.currentText())
        return template

    def addDataToSettings(self,settings):
        print("Add the data to the settings")
        return settings

    def autoFill(self):
        pass


    # Say if the user can go to the next page or not
    def canGoNext(self):
        # Check if the selected template's name is not empty
        if self.ui.cbSelectTemplate.currentText() == "":
            # Warn the user
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a template to continue.")
            return False
        
        """
        templateManager = TemplateManager.TemplateManager()
        templateData = self.ui.cbSelectTemplate.currentText()
        templateManager.runTemplate(templateData)
        """

        return True
    
    # Search for the templates installed in the templates folder
    def refresh(self):
        manager = TemplateManager.TemplateManager()
        templates = manager.getTemplates()

        # Clear the combobox
        self.ui.cbSelectTemplate.clear()

        # Add the templates to the combobox
        for template in templates:
            self.ui.cbSelectTemplate.addItem(template[0])
            self.ui.cbSelectTemplate.setItemData(self.ui.cbSelectTemplate.count() - 1, template[1], QtCore.Qt.UserRole)
        

        