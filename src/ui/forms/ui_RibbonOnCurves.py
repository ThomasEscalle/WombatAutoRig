# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RibbonOnCurve(object):
    def setupUi(self, RibbonOnCurve):
        if not RibbonOnCurve.objectName():
            RibbonOnCurve.setObjectName(u"RibbonOnCurve")
        RibbonOnCurve.resize(447, 333)
        self.verticalLayout = QVBoxLayout(RibbonOnCurve)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titre = QLabel(RibbonOnCurve)
        self.label_titre.setObjectName(u"label_titre")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_titre.setFont(font)

        self.verticalLayout.addWidget(self.label_titre)

        self.label_2 = QLabel(RibbonOnCurve)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(RibbonOnCurve)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.leName = QLineEdit(RibbonOnCurve)
        self.leName.setObjectName(u"leName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leName)

        self.label_4 = QLabel(RibbonOnCurve)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.sp_nbrDrvJnt = QSpinBox(RibbonOnCurve)
        self.sp_nbrDrvJnt.setObjectName(u"sp_nbrDrvJnt")
        self.sp_nbrDrvJnt.setMinimum(2)
        self.sp_nbrDrvJnt.setMaximum(30)
        self.sp_nbrDrvJnt.setValue(3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sp_nbrDrvJnt)

        self.label = QLabel(RibbonOnCurve)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.comBOrientDrv = QComboBox(RibbonOnCurve)
        self.comBOrientDrv.addItem("")
        self.comBOrientDrv.addItem("")
        self.comBOrientDrv.setObjectName(u"comBOrientDrv")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comBOrientDrv)

        self.label_3 = QLabel(RibbonOnCurve)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.sb_nbrBindJoint = QSpinBox(RibbonOnCurve)
        self.sb_nbrBindJoint.setObjectName(u"sb_nbrBindJoint")
        self.sb_nbrBindJoint.setMinimum(2)
        self.sb_nbrBindJoint.setMaximum(30)
        self.sb_nbrBindJoint.setValue(3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sb_nbrBindJoint)

        self.label_7 = QLabel(RibbonOnCurve)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.comBOrientBind = QComboBox(RibbonOnCurve)
        self.comBOrientBind.addItem("")
        self.comBOrientBind.addItem("")
        self.comBOrientBind.setObjectName(u"comBOrientBind")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comBOrientBind)

        self.label_8 = QLabel(RibbonOnCurve)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.cbReverse = QCheckBox(RibbonOnCurve)
        self.cbReverse.setObjectName(u"cbReverse")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cbReverse)

        self.label_6 = QLabel(RibbonOnCurve)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.label_9 = QLabel(RibbonOnCurve)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_9)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_OK = QPushButton(RibbonOnCurve)
        self.btn_OK.setObjectName(u"btn_OK")

        self.horizontalLayout.addWidget(self.btn_OK)

        self.btn_Close = QPushButton(RibbonOnCurve)
        self.btn_Close.setObjectName(u"btn_Close")

        self.horizontalLayout.addWidget(self.btn_Close)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(RibbonOnCurve)

        QMetaObject.connectSlotsByName(RibbonOnCurve)
    # setupUi

    def retranslateUi(self, RibbonOnCurve):
        RibbonOnCurve.setWindowTitle(QCoreApplication.translate("RibbonOnCurve", u"Dialog", None))
        self.label_titre.setText(QCoreApplication.translate("RibbonOnCurve", u"Ribbon On Curves", None))
        self.label_2.setText(QCoreApplication.translate("RibbonOnCurve", u"(selectionner 2 curves avant de lancer le programme)", None))
        self.label_5.setText(QCoreApplication.translate("RibbonOnCurve", u"Nom", None))
        self.label_4.setText(QCoreApplication.translate("RibbonOnCurve", u"Nombre de DrvJnt", None))
        self.label.setText(QCoreApplication.translate("RibbonOnCurve", u"Orientation DrvJnt", None))
        self.comBOrientDrv.setItemText(0, QCoreApplication.translate("RibbonOnCurve", u"Local", None))
        self.comBOrientDrv.setItemText(1, QCoreApplication.translate("RibbonOnCurve", u"World", None))

        self.label_3.setText(QCoreApplication.translate("RibbonOnCurve", u"Nombre de BindJoint", None))
        self.label_7.setText(QCoreApplication.translate("RibbonOnCurve", u"Orientation BindJoint", None))
        self.comBOrientBind.setItemText(0, QCoreApplication.translate("RibbonOnCurve", u"Local", None))
        self.comBOrientBind.setItemText(1, QCoreApplication.translate("RibbonOnCurve", u"World", None))

        self.label_8.setText("")
        self.cbReverse.setText(QCoreApplication.translate("RibbonOnCurve", u"Reverse Ribbon", None))
        self.label_6.setText("")
        self.label_9.setText("")
        self.btn_OK.setText(QCoreApplication.translate("RibbonOnCurve", u"OK", None))
        self.btn_Close.setText(QCoreApplication.translate("RibbonOnCurve", u"Close", None))
    # retranslateUi

