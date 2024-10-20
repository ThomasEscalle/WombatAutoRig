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
        PageGlobalSettings.resize(643, 632)
        self.verticalLayout = QVBoxLayout(PageGlobalSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageGlobalSettings)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(PageGlobalSettings)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelName = QLabel(PageGlobalSettings)
        self.labelName.setObjectName(u"labelName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelName)

        self.labelIdentifier = QLabel(PageGlobalSettings)
        self.labelIdentifier.setObjectName(u"labelIdentifier")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelIdentifier)

        self.labelVersion = QLabel(PageGlobalSettings)
        self.labelVersion.setObjectName(u"labelVersion")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelVersion)

        self.labelAuthor = QLabel(PageGlobalSettings)
        self.labelAuthor.setObjectName(u"labelAuthor")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelAuthor)

        self.leName = QLineEdit(PageGlobalSettings)
        self.leName.setObjectName(u"leName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leName)

        self.leIdentifier = QLineEdit(PageGlobalSettings)
        self.leIdentifier.setObjectName(u"leIdentifier")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leIdentifier)

        self.leVersion = QLineEdit(PageGlobalSettings)
        self.leVersion.setObjectName(u"leVersion")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leVersion)

        self.leAuthor = QLineEdit(PageGlobalSettings)
        self.leAuthor.setObjectName(u"leAuthor")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.leAuthor)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 363, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PageGlobalSettings)

        QMetaObject.connectSlotsByName(PageGlobalSettings)
    # setupUi

    def retranslateUi(self, PageGlobalSettings):
        PageGlobalSettings.setWindowTitle(QCoreApplication.translate("PageGlobalSettings", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageGlobalSettings", u"Global Settings", None))
        self.label_2.setText("")
        self.labelName.setText(QCoreApplication.translate("PageGlobalSettings", u"Name :", None))
        self.labelIdentifier.setText(QCoreApplication.translate("PageGlobalSettings", u"Identifier :", None))
        self.labelVersion.setText(QCoreApplication.translate("PageGlobalSettings", u"Version :", None))
        self.labelAuthor.setText(QCoreApplication.translate("PageGlobalSettings", u"Author", None))
    # retranslateUi

