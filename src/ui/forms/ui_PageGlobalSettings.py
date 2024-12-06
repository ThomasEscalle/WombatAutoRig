# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageGlobalSettings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PageGlobalSettings(object):
    def setupUi(self, PageGlobalSettings):
        if not PageGlobalSettings.objectName():
            PageGlobalSettings.setObjectName(u"PageGlobalSettings")
        PageGlobalSettings.resize(581, 454)
        self.verticalLayout = QVBoxLayout(PageGlobalSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageGlobalSettings)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(PageGlobalSettings)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.scrollArea = QScrollArea(PageGlobalSettings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 563, 68))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 363, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PageGlobalSettings)

        QMetaObject.connectSlotsByName(PageGlobalSettings)
    # setupUi

    def retranslateUi(self, PageGlobalSettings):
        PageGlobalSettings.setWindowTitle(QCoreApplication.translate("PageGlobalSettings", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageGlobalSettings", u"Global Settings", None))
        self.label_2.setText("")
    # retranslateUi

