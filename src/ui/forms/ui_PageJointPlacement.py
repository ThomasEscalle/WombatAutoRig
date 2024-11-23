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
        PageJointPlacement.resize(723, 640)
        self.verticalLayout = QVBoxLayout(PageJointPlacement)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageJointPlacement)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
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
    # retranslateUi

