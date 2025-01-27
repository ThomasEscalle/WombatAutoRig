# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageControllerPlacement.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PageControllerPlacement(object):
    def setupUi(self, PageControllerPlacement):
        if not PageControllerPlacement.objectName():
            PageControllerPlacement.setObjectName(u"PageControllerPlacement")
        PageControllerPlacement.resize(667, 267)
        self.verticalLayout = QVBoxLayout(PageControllerPlacement)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageControllerPlacement)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(PageControllerPlacement)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnFkMode = QPushButton(PageControllerPlacement)
        self.btnFkMode.setObjectName(u"btnFkMode")

        self.horizontalLayout.addWidget(self.btnFkMode)

        self.btnIkMode = QPushButton(PageControllerPlacement)
        self.btnIkMode.setObjectName(u"btnIkMode")

        self.horizontalLayout.addWidget(self.btnIkMode)

        self.btnOther = QPushButton(PageControllerPlacement)
        self.btnOther.setObjectName(u"btnOther")

        self.horizontalLayout.addWidget(self.btnOther)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(PageControllerPlacement)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.btnControllers = QPushButton(PageControllerPlacement)
        self.btnControllers.setObjectName(u"btnControllers")

        self.verticalLayout.addWidget(self.btnControllers)

        self.btnColors = QPushButton(PageControllerPlacement)
        self.btnColors.setObjectName(u"btnColors")

        self.verticalLayout.addWidget(self.btnColors)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PageControllerPlacement)

        QMetaObject.connectSlotsByName(PageControllerPlacement)
    # setupUi

    def retranslateUi(self, PageControllerPlacement):
        PageControllerPlacement.setWindowTitle(QCoreApplication.translate("PageControllerPlacement", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageControllerPlacement", u"Controllers Placement", None))
        self.label_2.setText("")
        self.btnFkMode.setText(QCoreApplication.translate("PageControllerPlacement", u"Fk Mode", None))
        self.btnIkMode.setText(QCoreApplication.translate("PageControllerPlacement", u"Ik Mode", None))
        self.btnOther.setText(QCoreApplication.translate("PageControllerPlacement", u"Other", None))
        self.label_3.setText("")
        self.btnControllers.setText(QCoreApplication.translate("PageControllerPlacement", u"Replace controllers", None))
        self.btnColors.setText(QCoreApplication.translate("PageControllerPlacement", u"Colors", None))
    # retranslateUi

