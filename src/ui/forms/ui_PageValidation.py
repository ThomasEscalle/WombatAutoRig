# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageValidation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PageValidation(object):
    def setupUi(self, PageValidation):
        if not PageValidation.objectName():
            PageValidation.setObjectName(u"PageValidation")
        PageValidation.resize(591, 254)
        self.verticalLayout = QVBoxLayout(PageValidation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageValidation)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(PageValidation)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 392, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(PageValidation)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnYes = QPushButton(PageValidation)
        self.btnYes.setObjectName(u"btnYes")

        self.horizontalLayout.addWidget(self.btnYes)

        self.btnNo = QPushButton(PageValidation)
        self.btnNo.setObjectName(u"btnNo")

        self.horizontalLayout.addWidget(self.btnNo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btnSaveState = QPushButton(PageValidation)
        self.btnSaveState.setObjectName(u"btnSaveState")

        self.verticalLayout.addWidget(self.btnSaveState)

        self.verticalSpacer_2 = QSpacerItem(20, 392, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(PageValidation)

        QMetaObject.connectSlotsByName(PageValidation)
    # setupUi

    def retranslateUi(self, PageValidation):
        PageValidation.setWindowTitle(QCoreApplication.translate("PageValidation", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageValidation", u"Validation", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("PageValidation", u"Do you want to validate ?", None))
        self.btnYes.setText(QCoreApplication.translate("PageValidation", u"Yes", None))
        self.btnNo.setText(QCoreApplication.translate("PageValidation", u"No", None))
        self.btnSaveState.setText(QCoreApplication.translate("PageValidation", u"Save State As", None))
    # retranslateUi

