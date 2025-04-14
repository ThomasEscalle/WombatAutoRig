# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgAttachBlendShape.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgAttachBlendShape(object):
    def setupUi(self, DlgAttachBlendShape):
        if not DlgAttachBlendShape.objectName():
            DlgAttachBlendShape.setObjectName(u"DlgAttachBlendShape")
        DlgAttachBlendShape.resize(804, 278)
        self.verticalLayout = QVBoxLayout(DlgAttachBlendShape)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CB_Chanel = QComboBox(DlgAttachBlendShape)
        self.CB_Chanel.addItem("")
        self.CB_Chanel.addItem("")
        self.CB_Chanel.addItem("")
        self.CB_Chanel.addItem("")
        self.CB_Chanel.addItem("")
        self.CB_Chanel.addItem("")
        self.CB_Chanel.addItem("")
        self.CB_Chanel.addItem("")
        self.CB_Chanel.addItem("")
        self.CB_Chanel.setObjectName(u"CB_Chanel")

        self.verticalLayout.addWidget(self.CB_Chanel)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DlgAttachBlendShape)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.LE_BshpName = QLineEdit(DlgAttachBlendShape)
        self.LE_BshpName.setObjectName(u"LE_BshpName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LE_BshpName)

        self.label_2 = QLabel(DlgAttachBlendShape)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.Le_TargetName = QLineEdit(DlgAttachBlendShape)
        self.Le_TargetName.setObjectName(u"Le_TargetName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Le_TargetName)

        self.LE_MaxValue = QLineEdit(DlgAttachBlendShape)
        self.LE_MaxValue.setObjectName(u"LE_MaxValue")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.LE_MaxValue)

        self.label_3 = QLabel(DlgAttachBlendShape)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BtnApply = QPushButton(DlgAttachBlendShape)
        self.BtnApply.setObjectName(u"BtnApply")

        self.horizontalLayout.addWidget(self.BtnApply)

        self.BtnCancel = QPushButton(DlgAttachBlendShape)
        self.BtnCancel.setObjectName(u"BtnCancel")

        self.horizontalLayout.addWidget(self.BtnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgAttachBlendShape)

        QMetaObject.connectSlotsByName(DlgAttachBlendShape)
    # setupUi

    def retranslateUi(self, DlgAttachBlendShape):
        DlgAttachBlendShape.setWindowTitle(QCoreApplication.translate("DlgAttachBlendShape", u"Dialog", None))
        self.CB_Chanel.setItemText(0, QCoreApplication.translate("DlgAttachBlendShape", u"Translate X", None))
        self.CB_Chanel.setItemText(1, QCoreApplication.translate("DlgAttachBlendShape", u"Translate Y", None))
        self.CB_Chanel.setItemText(2, QCoreApplication.translate("DlgAttachBlendShape", u"Translate Z", None))
        self.CB_Chanel.setItemText(3, QCoreApplication.translate("DlgAttachBlendShape", u"Rotate X", None))
        self.CB_Chanel.setItemText(4, QCoreApplication.translate("DlgAttachBlendShape", u"RotateY", None))
        self.CB_Chanel.setItemText(5, QCoreApplication.translate("DlgAttachBlendShape", u"Rotate Z", None))
        self.CB_Chanel.setItemText(6, QCoreApplication.translate("DlgAttachBlendShape", u"Scale X", None))
        self.CB_Chanel.setItemText(7, QCoreApplication.translate("DlgAttachBlendShape", u"Scale Y", None))
        self.CB_Chanel.setItemText(8, QCoreApplication.translate("DlgAttachBlendShape", u"Scale Z", None))

        self.label.setText(QCoreApplication.translate("DlgAttachBlendShape", u"Blenshape Name", None))
        self.label_2.setText(QCoreApplication.translate("DlgAttachBlendShape", u"Target Name", None))
        self.label_3.setText(QCoreApplication.translate("DlgAttachBlendShape", u"Max Value", None))
        self.BtnApply.setText(QCoreApplication.translate("DlgAttachBlendShape", u"Apply", None))
        self.BtnCancel.setText(QCoreApplication.translate("DlgAttachBlendShape", u"Cancel", None))
    # retranslateUi

