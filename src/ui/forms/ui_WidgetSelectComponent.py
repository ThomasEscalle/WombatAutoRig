# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetSelectComponent.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WidgetSelectComponent(object):
    def setupUi(self, WidgetSelectComponent):
        if not WidgetSelectComponent.objectName():
            WidgetSelectComponent.setObjectName(u"WidgetSelectComponent")
        WidgetSelectComponent.resize(482, 35)
        self.horizontalLayout = QHBoxLayout(WidgetSelectComponent)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(WidgetSelectComponent)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btnSelect = QPushButton(WidgetSelectComponent)
        self.btnSelect.setObjectName(u"btnSelect")

        self.horizontalLayout.addWidget(self.btnSelect)


        self.retranslateUi(WidgetSelectComponent)

        QMetaObject.connectSlotsByName(WidgetSelectComponent)
    # setupUi

    def retranslateUi(self, WidgetSelectComponent):
        WidgetSelectComponent.setWindowTitle(QCoreApplication.translate("WidgetSelectComponent", u"Form", None))
        self.btnSelect.setText(QCoreApplication.translate("WidgetSelectComponent", u"Select", None))
    # retranslateUi

