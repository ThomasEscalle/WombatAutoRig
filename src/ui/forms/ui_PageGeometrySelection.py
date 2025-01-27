# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageGeometrySelection.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PageGeometrySelection(object):
    def setupUi(self, PageGeometrySelection):
        if not PageGeometrySelection.objectName():
            PageGeometrySelection.setObjectName(u"PageGeometrySelection")
        PageGeometrySelection.resize(369, 250)
        self.verticalLayout = QVBoxLayout(PageGeometrySelection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageGeometrySelection)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(PageGeometrySelection)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.listWidget = QListWidget(PageGeometrySelection)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAdd = QPushButton(PageGeometrySelection)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnRemove = QPushButton(PageGeometrySelection)
        self.btnRemove.setObjectName(u"btnRemove")

        self.horizontalLayout.addWidget(self.btnRemove)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(PageGeometrySelection)

        QMetaObject.connectSlotsByName(PageGeometrySelection)
    # setupUi

    def retranslateUi(self, PageGeometrySelection):
        PageGeometrySelection.setWindowTitle(QCoreApplication.translate("PageGeometrySelection", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageGeometrySelection", u"Geometry selection", None))
        self.label_2.setText("")
        self.btnAdd.setText(QCoreApplication.translate("PageGeometrySelection", u"Add", None))
        self.btnRemove.setText(QCoreApplication.translate("PageGeometrySelection", u"Remove", None))
    # retranslateUi

