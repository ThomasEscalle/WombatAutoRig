# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgTransferSkinToNewGeo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TransferSkinToNewGeo(object):
    def setupUi(self, TransferSkinToNewGeo):
        if not TransferSkinToNewGeo.objectName():
            TransferSkinToNewGeo.setObjectName(u"TransferSkinToNewGeo")
        TransferSkinToNewGeo.resize(437, 151)
        self.verticalLayout = QVBoxLayout(TransferSkinToNewGeo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(TransferSkinToNewGeo)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leSkinedGrp = QLineEdit(TransferSkinToNewGeo)
        self.leSkinedGrp.setObjectName(u"leSkinedGrp")
        self.leSkinedGrp.setReadOnly(True)

        self.horizontalLayout.addWidget(self.leSkinedGrp)

        self.btnSelectSkinedGrp = QPushButton(TransferSkinToNewGeo)
        self.btnSelectSkinedGrp.setObjectName(u"btnSelectSkinedGrp")

        self.horizontalLayout.addWidget(self.btnSelectSkinedGrp)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leTargetGrp = QLineEdit(TransferSkinToNewGeo)
        self.leTargetGrp.setObjectName(u"leTargetGrp")
        self.leTargetGrp.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.leTargetGrp)

        self.btnSelectGrp = QPushButton(TransferSkinToNewGeo)
        self.btnSelectGrp.setObjectName(u"btnSelectGrp")

        self.horizontalLayout_2.addWidget(self.btnSelectGrp)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnApply = QPushButton(TransferSkinToNewGeo)
        self.btnApply.setObjectName(u"btnApply")

        self.horizontalLayout_3.addWidget(self.btnApply)

        self.btnCancel = QPushButton(TransferSkinToNewGeo)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_3.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(TransferSkinToNewGeo)

        QMetaObject.connectSlotsByName(TransferSkinToNewGeo)
    # setupUi

    def retranslateUi(self, TransferSkinToNewGeo):
        TransferSkinToNewGeo.setWindowTitle(QCoreApplication.translate("TransferSkinToNewGeo", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("TransferSkinToNewGeo", u"Select two groups with same object name and hierarchy.", None))
        self.leSkinedGrp.setPlaceholderText(QCoreApplication.translate("TransferSkinToNewGeo", u"Skined Geo Group", None))
        self.btnSelectSkinedGrp.setText(QCoreApplication.translate("TransferSkinToNewGeo", u"Select", None))
        self.leTargetGrp.setPlaceholderText(QCoreApplication.translate("TransferSkinToNewGeo", u"Target Group", None))
        self.btnSelectGrp.setText(QCoreApplication.translate("TransferSkinToNewGeo", u"Select", None))
        self.btnApply.setText(QCoreApplication.translate("TransferSkinToNewGeo", u"Apply", None))
        self.btnCancel.setText(QCoreApplication.translate("TransferSkinToNewGeo", u"Cancel", None))
    # retranslateUi

