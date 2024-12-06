# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgControllers.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgControllers(object):
    def setupUi(self, DlgControllers):
        if not DlgControllers.objectName():
            DlgControllers.setObjectName(u"DlgControllers")
        DlgControllers.resize(484, 412)
        self.verticalLayout = QVBoxLayout(DlgControllers)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(DlgControllers)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.btnOptions = QPushButton(DlgControllers)
        self.btnOptions.setObjectName(u"btnOptions")

        self.horizontalLayout_2.addWidget(self.btnOptions)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.stackedWidget = QStackedWidget(DlgControllers)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_apply = QPushButton(DlgControllers)
        self.btn_apply.setObjectName(u"btn_apply")

        self.horizontalLayout.addWidget(self.btn_apply)

        self.btn_create = QPushButton(DlgControllers)
        self.btn_create.setObjectName(u"btn_create")

        self.horizontalLayout.addWidget(self.btn_create)

        self.btn_cancel = QPushButton(DlgControllers)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgControllers)

        QMetaObject.connectSlotsByName(DlgControllers)
    # setupUi

    def retranslateUi(self, DlgControllers):
        DlgControllers.setWindowTitle(QCoreApplication.translate("DlgControllers", u"Dialog", None))
        self.btnOptions.setText(QCoreApplication.translate("DlgControllers", u"...", None))
        self.btn_apply.setText(QCoreApplication.translate("DlgControllers", u"Apply", None))
        self.btn_create.setText(QCoreApplication.translate("DlgControllers", u"Create", None))
        self.btn_cancel.setText(QCoreApplication.translate("DlgControllers", u"Cancel", None))
    # retranslateUi

