# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageJointPlacement.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PageJointPlacement(object):
    def setupUi(self, PageJointPlacement):
        if not PageJointPlacement.objectName():
            PageJointPlacement.setObjectName(u"PageJointPlacement")
        PageJointPlacement.resize(740, 438)
        self.verticalLayout = QVBoxLayout(PageJointPlacement)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageJointPlacement)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(PageJointPlacement)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.btnShowLRA = QPushButton(PageJointPlacement)
        self.btnShowLRA.setObjectName(u"btnShowLRA")

        self.verticalLayout.addWidget(self.btnShowLRA)

        self.btnTemplate = QPushButton(PageJointPlacement)
        self.btnTemplate.setObjectName(u"btnTemplate")

        self.verticalLayout.addWidget(self.btnTemplate)

        self.label_3 = QLabel(PageJointPlacement)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cb_MirrorDirection = QComboBox(PageJointPlacement)
        self.cb_MirrorDirection.addItem("")
        self.cb_MirrorDirection.addItem("")
        self.cb_MirrorDirection.addItem("")
        self.cb_MirrorDirection.addItem("")
        self.cb_MirrorDirection.setObjectName(u"cb_MirrorDirection")

        self.horizontalLayout.addWidget(self.cb_MirrorDirection)

        self.btnMirro = QPushButton(PageJointPlacement)
        self.btnMirro.setObjectName(u"btnMirro")

        self.horizontalLayout.addWidget(self.btnMirro)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PageJointPlacement)

        QMetaObject.connectSlotsByName(PageJointPlacement)
    # setupUi

    def retranslateUi(self, PageJointPlacement):
        PageJointPlacement.setWindowTitle(QCoreApplication.translate("PageJointPlacement", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageJointPlacement", u"Joints placement", None))
        self.label_2.setText("")
        self.btnShowLRA.setText(QCoreApplication.translate("PageJointPlacement", u"Show LRA", None))
        self.btnTemplate.setText(QCoreApplication.translate("PageJointPlacement", u"Toggle template geo", None))
        self.label_3.setText("")
        self.cb_MirrorDirection.setItemText(0, QCoreApplication.translate("PageJointPlacement", u"Leg : L -> R", None))
        self.cb_MirrorDirection.setItemText(1, QCoreApplication.translate("PageJointPlacement", u"Leg : R -> L", None))
        self.cb_MirrorDirection.setItemText(2, QCoreApplication.translate("PageJointPlacement", u"Arm : L -> R", None))
        self.cb_MirrorDirection.setItemText(3, QCoreApplication.translate("PageJointPlacement", u"Arm : R -> L", None))

        self.btnMirro.setText(QCoreApplication.translate("PageJointPlacement", u"Mirror", None))
    # retranslateUi

