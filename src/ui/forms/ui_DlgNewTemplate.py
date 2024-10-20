# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgNewTemplate.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgNewTemplate(object):
    def setupUi(self, DlgNewTemplate):
        if not DlgNewTemplate.objectName():
            DlgNewTemplate.setObjectName(u"DlgNewTemplate")
        DlgNewTemplate.resize(741, 421)
        self.verticalLayout = QVBoxLayout(DlgNewTemplate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DlgNewTemplate)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.leName = QLineEdit(DlgNewTemplate)
        self.leName.setObjectName(u"leName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leName)

        self.label_2 = QLabel(DlgNewTemplate)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(DlgNewTemplate)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(DlgNewTemplate)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.leIdentifier = QLineEdit(DlgNewTemplate)
        self.leIdentifier.setObjectName(u"leIdentifier")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leIdentifier)

        self.leVersion = QLineEdit(DlgNewTemplate)
        self.leVersion.setObjectName(u"leVersion")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leVersion)

        self.leAuthor = QLineEdit(DlgNewTemplate)
        self.leAuthor.setObjectName(u"leAuthor")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.leAuthor)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(DlgNewTemplate)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnCreate = QPushButton(DlgNewTemplate)
        self.btnCreate.setObjectName(u"btnCreate")

        self.horizontalLayout.addWidget(self.btnCreate)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgNewTemplate)

        QMetaObject.connectSlotsByName(DlgNewTemplate)
    # setupUi

    def retranslateUi(self, DlgNewTemplate):
        DlgNewTemplate.setWindowTitle(QCoreApplication.translate("DlgNewTemplate", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DlgNewTemplate", u"Name :", None))
        self.label_2.setText(QCoreApplication.translate("DlgNewTemplate", u"Identifier :", None))
        self.label_3.setText(QCoreApplication.translate("DlgNewTemplate", u"Version :", None))
        self.label_4.setText(QCoreApplication.translate("DlgNewTemplate", u"Author :", None))
        self.btnCancel.setText(QCoreApplication.translate("DlgNewTemplate", u"Cancel", None))
        self.btnCreate.setText(QCoreApplication.translate("DlgNewTemplate", u"Create", None))
    # retranslateUi

