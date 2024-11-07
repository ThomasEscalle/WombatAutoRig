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


from wombatAutoRig.src.ui.forms import ui_DlgRibbonOnCurves
from wombatAutoRig.src.core import RibbonOnCurves



def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# Classe de la fenêtre de création de template
class DlgRibbonOnCurves(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(DlgRibbonOnCurves, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.ui = ui_DlgRibbonOnCurves.Ui_DlgRibbonOnCurves()
        self.ui.setupUi(self)

        self.setWindowTitle("Ribbons on curves")

        self.ui.btn_apply.clicked.connect(self.apply)
        self.ui.btn_accept.clicked.connect(self.accept)
        self.ui.btn_close.clicked.connect(self.close)

    # Show window with docking ability
    def run(self):
        self.show(dockable = True)

    def apply(self) :
        # Name
        name = self.ui.le_name.text()

        # Number of joints
        nbrJnts = self.ui.sb_jntNumber.value()
        nbtDrvJnts = self.ui.sb_drvJntNumber.value()

        # Joints orientation
        jntsOrientation = self.ui.cb_jntOrientation.currentText()
        jntsOrientationValue = True
        if(jntsOrientation == "Rivet") :
            jntsOrientationValue = False

        # DrvJnts orientation
        drvJntsOrientation = self.ui.cb_drvJntOrientation.currentText()
        drvJntsOrientationValue = True
        if(drvJntsOrientation == "Rivet") :
            drvJntsOrientationValue

        # Reverse
        cb_reverse = self.ui.cb_reverse.isChecked()

        # Run the function
        RibbonOnCurves.RibbonOnCurve(Joints=nbrJnts, DrvJnt=nbtDrvJnts, Rev=cb_reverse, Name=name, ws=jntsOrientationValue, wsDrvJnt=drvJntsOrientationValue)
    
    def accept(self):
        self.apply()
        super(DlgRibbonOnCurves, self).accept()
    
    def close(self):
        super(DlgRibbonOnCurves, self).close()