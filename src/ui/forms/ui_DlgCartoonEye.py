# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgCartoonEye.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgCartoonEye(object):
    def setupUi(self, DlgCartoonEye):
        if not DlgCartoonEye.objectName():
            DlgCartoonEye.setObjectName(u"DlgCartoonEye")
        DlgCartoonEye.resize(476, 332)
        self.verticalLayout = QVBoxLayout(DlgCartoonEye)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DlgCartoonEye)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leTopVtx = QLineEdit(DlgCartoonEye)
        self.leTopVtx.setObjectName(u"leTopVtx")
        self.leTopVtx.setReadOnly(True)

        self.horizontalLayout.addWidget(self.leTopVtx)

        self.btnTopVtxAdd = QPushButton(DlgCartoonEye)
        self.btnTopVtxAdd.setObjectName(u"btnTopVtxAdd")

        self.horizontalLayout.addWidget(self.btnTopVtxAdd)

        self.btnTopVtxRemove = QPushButton(DlgCartoonEye)
        self.btnTopVtxRemove.setObjectName(u"btnTopVtxRemove")

        self.horizontalLayout.addWidget(self.btnTopVtxRemove)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_2 = QLabel(DlgCartoonEye)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leBottomVtx = QLineEdit(DlgCartoonEye)
        self.leBottomVtx.setObjectName(u"leBottomVtx")
        self.leBottomVtx.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.leBottomVtx)

        self.btnBottomVtxAdd = QPushButton(DlgCartoonEye)
        self.btnBottomVtxAdd.setObjectName(u"btnBottomVtxAdd")

        self.horizontalLayout_2.addWidget(self.btnBottomVtxAdd)

        self.btnBottomVtxRemove = QPushButton(DlgCartoonEye)
        self.btnBottomVtxRemove.setObjectName(u"btnBottomVtxRemove")

        self.horizontalLayout_2.addWidget(self.btnBottomVtxRemove)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_3 = QLabel(DlgCartoonEye)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.leEyeGeo = QLineEdit(DlgCartoonEye)
        self.leEyeGeo.setObjectName(u"leEyeGeo")
        self.leEyeGeo.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.leEyeGeo)

        self.btnEyeGeoAdd = QPushButton(DlgCartoonEye)
        self.btnEyeGeoAdd.setObjectName(u"btnEyeGeoAdd")

        self.horizontalLayout_3.addWidget(self.btnEyeGeoAdd)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leFaceGeo = QLineEdit(DlgCartoonEye)
        self.leFaceGeo.setObjectName(u"leFaceGeo")
        self.leFaceGeo.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.leFaceGeo)

        self.btnFaceGeoAdd = QPushButton(DlgCartoonEye)
        self.btnFaceGeoAdd.setObjectName(u"btnFaceGeoAdd")

        self.horizontalLayout_4.addWidget(self.btnFaceGeoAdd)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_4 = QLabel(DlgCartoonEye)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(DlgCartoonEye)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.cbSide = QComboBox(DlgCartoonEye)
        self.cbSide.addItem("")
        self.cbSide.addItem("")
        self.cbSide.setObjectName(u"cbSide")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cbSide)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnApply = QPushButton(DlgCartoonEye)
        self.btnApply.setObjectName(u"btnApply")

        self.horizontalLayout_5.addWidget(self.btnApply)

        self.btnCreate = QPushButton(DlgCartoonEye)
        self.btnCreate.setObjectName(u"btnCreate")

        self.horizontalLayout_5.addWidget(self.btnCreate)

        self.btnCancel = QPushButton(DlgCartoonEye)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_5.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(DlgCartoonEye)

        QMetaObject.connectSlotsByName(DlgCartoonEye)
    # setupUi

    def retranslateUi(self, DlgCartoonEye):
        DlgCartoonEye.setWindowTitle(QCoreApplication.translate("DlgCartoonEye", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DlgCartoonEye", u"Top Eyelid Vertices :", None))
        self.btnTopVtxAdd.setText(QCoreApplication.translate("DlgCartoonEye", u"+", None))
        self.btnTopVtxRemove.setText(QCoreApplication.translate("DlgCartoonEye", u"X", None))
        self.label_2.setText(QCoreApplication.translate("DlgCartoonEye", u"Bottom Eyelid Vertices :", None))
        self.btnBottomVtxAdd.setText(QCoreApplication.translate("DlgCartoonEye", u"+", None))
        self.btnBottomVtxRemove.setText(QCoreApplication.translate("DlgCartoonEye", u"X", None))
        self.label_3.setText(QCoreApplication.translate("DlgCartoonEye", u"Eye Geo :", None))
        self.btnEyeGeoAdd.setText(QCoreApplication.translate("DlgCartoonEye", u"+", None))
        self.btnFaceGeoAdd.setText(QCoreApplication.translate("DlgCartoonEye", u"+", None))
        self.label_4.setText(QCoreApplication.translate("DlgCartoonEye", u"Face Geo :", None))
        self.label_5.setText(QCoreApplication.translate("DlgCartoonEye", u"Side", None))
        self.cbSide.setItemText(0, QCoreApplication.translate("DlgCartoonEye", u"L", None))
        self.cbSide.setItemText(1, QCoreApplication.translate("DlgCartoonEye", u"R", None))

        self.btnApply.setText(QCoreApplication.translate("DlgCartoonEye", u"Apply", None))
        self.btnCreate.setText(QCoreApplication.translate("DlgCartoonEye", u"Create", None))
        self.btnCancel.setText(QCoreApplication.translate("DlgCartoonEye", u"Cancel", None))
    # retranslateUi

