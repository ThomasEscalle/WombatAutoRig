from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import maya.cmds as cmds

from wombatAutoRig.src.ui.forms import ui_PageGeometrySelection

from wombatAutoRig.src.ui.PageBase import PageBase
from wombatAutoRig.src.ui import IconLoader


# Page to select the geometry for the rig
class PageGeometrySelection(PageBase):
    def __init__(self):
        super(PageGeometrySelection, self).__init__()

        self.ui = ui_PageGeometrySelection.Ui_PageGeometrySelection()
        self.ui.setupUi(self)

        # Connect signals
        self.ui.btnAdd.clicked.connect(self.add)
        self.ui.btnRemove.clicked.connect(self.remove)

        # Set icons
        self.ui.btnAdd.setIcon(IconLoader.loadIcon("add.png"))
        self.ui.btnRemove.setIcon(IconLoader.loadIcon("remove.png"))
    

    def autoFill(self):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItem("group_Harley_0000_Harley_Queen_Geo_Harley_0000_Harley_Queen_Geo")

    # Say if the user can go to the next page or not
    def canGoNext(self):
        # Check if there is at least one item in the list widget
        if self.ui.listWidget.count() == 0:
            # Show a message box
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select at least one geometry to continue.")
            return False

        return True

    # Action to add the selected geometry in maya to the list
    def add(self):
        # Get the selected items
        items = cmds.ls(selection=True)

        # Loop through the selected items
        for item in items:
            # Check if the item is in the list widget
            if self.ui.listWidget.findItems(item, Qt.MatchExactly):
                continue

            # Check if the item is a transform
            if not cmds.nodeType(item) == "transform":
                continue

            # Add the item to the list widget
            self.ui.listWidget.addItem(item)
        
    # Action to remove the selected item from the list
    def remove(self):
        # Delete the selected item from the list
        item = self.ui.listWidget.currentItem()
        self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
    
    def addDataToSettings(self,settings):
        selectedItems = []
        for i in range(self.ui.listWidget.count()):
            selectedItems.append(self.ui.listWidget.item(i).text())
        settings["geo"] = selectedItems

        # Get the bounding box of all the geo
        bbox = cmds.exactWorldBoundingBox(selectedItems)
        settings["bbox"] = bbox

        return settings