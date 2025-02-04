# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgMatchIkFk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgMatchIkFk(object):
    def setupUi(self, DlgMatchIkFk):
        if not DlgMatchIkFk.objectName():
            DlgMatchIkFk.setObjectName(u"DlgMatchIkFk")
        DlgMatchIkFk.resize(422, 124)
        self.verticalLayout = QVBoxLayout(DlgMatchIkFk)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cb_Side = QComboBox(DlgMatchIkFk)
        self.cb_Side.addItem("")
        self.cb_Side.addItem("")
        self.cb_Side.addItem("")
        self.cb_Side.addItem("")
        self.cb_Side.setObjectName(u"cb_Side")

        self.verticalLayout.addWidget(self.cb_Side)

        self.cb_Match = QComboBox(DlgMatchIkFk)
        self.cb_Match.addItem("")
        self.cb_Match.addItem("")
        self.cb_Match.setObjectName(u"cb_Match")

        self.verticalLayout.addWidget(self.cb_Match)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnApply = QPushButton(DlgMatchIkFk)
        self.btnApply.setObjectName(u"btnApply")

        self.horizontalLayout_2.addWidget(self.btnApply)

        self.btnCancel = QPushButton(DlgMatchIkFk)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_2.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(DlgMatchIkFk)

        QMetaObject.connectSlotsByName(DlgMatchIkFk)
    # setupUi

    def retranslateUi(self, DlgMatchIkFk):
        DlgMatchIkFk.setWindowTitle(QCoreApplication.translate("DlgMatchIkFk", u"Dialog", None))
        self.cb_Side.setItemText(0, QCoreApplication.translate("DlgMatchIkFk", u"Arm L", None))
        self.cb_Side.setItemText(1, QCoreApplication.translate("DlgMatchIkFk", u"Arm R", None))
        self.cb_Side.setItemText(2, QCoreApplication.translate("DlgMatchIkFk", u"Leg L", None))
        self.cb_Side.setItemText(3, QCoreApplication.translate("DlgMatchIkFk", u"Leg R", None))

        self.cb_Match.setItemText(0, QCoreApplication.translate("DlgMatchIkFk", u"Ik -> Fk", None))
        self.cb_Match.setItemText(1, QCoreApplication.translate("DlgMatchIkFk", u"Fk -> Ik", None))

        self.btnApply.setText(QCoreApplication.translate("DlgMatchIkFk", u"Apply", None))
        self.btnCancel.setText(QCoreApplication.translate("DlgMatchIkFk", u"Cancel", None))
    # retranslateUi

