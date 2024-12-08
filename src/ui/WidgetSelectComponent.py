from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import maya.cmds as cmds

from wombatAutoRig.src.ui.forms import ui_WidgetSelectComponent


from wombatAutoRig.src.ui import IconLoader


# Widget to select a component
class WidgetSelectComponent(QWidget):
    def __init__(self):
        super(WidgetSelectComponent, self).__init__()

        self.ui = ui_WidgetSelectComponent.Ui_WidgetSelectComponent()
        self.ui.setupUi(self)

        # Possible modes : vertex, edge, face, object
        self.mode = "vertex"

        self.ui.btnSelect.clicked.connect(self.onSelectClicked)


    def setMode(self, mode):
        self.mode = mode
    

    
    # When the select button is clicked
    def onSelectClicked(self):
        # Get the selection
        selection = cmds.ls(selection=True, flatten=True)

        # If the selection is empty
        if not selection:
            return
        
        txt = ""
        # Loop through the selection
        for obj in selection:
            # If the mode is vertex and the object is a vertex
            if self.mode == "vertex" and ".vtx[" in obj:
                txt += obj + " "
            # If the mode is edge and the object is an edge
            elif self.mode == "edge" and ".e[" in obj:
                txt += obj + " "
            # If the mode is face and the object is a face
            elif self.mode == "face" and ".f[" in obj:
                txt += obj + " "
            # If the mode is object
            elif self.mode == "object":
                txt += obj + " "

           
        # Set the text in the line edit
        self.ui.lineEdit.setText(txt)