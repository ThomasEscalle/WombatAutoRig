# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgRibbonOnCurves.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgRibbonOnCurves(object):
    def setupUi(self, DlgRibbonOnCurves):
        if not DlgRibbonOnCurves.objectName():
            DlgRibbonOnCurves.setObjectName(u"DlgRibbonOnCurves")
        DlgRibbonOnCurves.resize(286, 357)
        self.verticalLayout = QVBoxLayout(DlgRibbonOnCurves)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(DlgRibbonOnCurves)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(DlgRibbonOnCurves)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.le_name = QLineEdit(DlgRibbonOnCurves)
        self.le_name.setObjectName(u"le_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_name)

        self.label = QLabel(DlgRibbonOnCurves)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.sb_jntNumber = QSpinBox(DlgRibbonOnCurves)
        self.sb_jntNumber.setObjectName(u"sb_jntNumber")
        self.sb_jntNumber.setMinimum(1)
        self.sb_jntNumber.setValue(5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sb_jntNumber)

        self.label_4 = QLabel(DlgRibbonOnCurves)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.cb_jntOrientation = QComboBox(DlgRibbonOnCurves)
        self.cb_jntOrientation.addItem("")
        self.cb_jntOrientation.addItem("")
        self.cb_jntOrientation.setObjectName(u"cb_jntOrientation")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_jntOrientation)

        self.label_2 = QLabel(DlgRibbonOnCurves)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.sb_drvJntNumber = QSpinBox(DlgRibbonOnCurves)
        self.sb_drvJntNumber.setObjectName(u"sb_drvJntNumber")
        self.sb_drvJntNumber.setMinimum(2)
        self.sb_drvJntNumber.setValue(3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sb_drvJntNumber)

        self.label_5 = QLabel(DlgRibbonOnCurves)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.cb_drvJntOrientation = QComboBox(DlgRibbonOnCurves)
        self.cb_drvJntOrientation.addItem("")
        self.cb_drvJntOrientation.addItem("")
        self.cb_drvJntOrientation.setObjectName(u"cb_drvJntOrientation")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cb_drvJntOrientation)

        self.cb_reverse = QCheckBox(DlgRibbonOnCurves)
        self.cb_reverse.setObjectName(u"cb_reverse")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cb_reverse)

        self.label_6 = QLabel(DlgRibbonOnCurves)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_apply = QPushButton(DlgRibbonOnCurves)
        self.btn_apply.setObjectName(u"btn_apply")

        self.horizontalLayout.addWidget(self.btn_apply)

        self.btn_accept = QPushButton(DlgRibbonOnCurves)
        self.btn_accept.setObjectName(u"btn_accept")

        self.horizontalLayout.addWidget(self.btn_accept)

        self.btn_close = QPushButton(DlgRibbonOnCurves)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgRibbonOnCurves)

        self.cb_jntOrientation.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DlgRibbonOnCurves)
    # setupUi

    def retranslateUi(self, DlgRibbonOnCurves):
        DlgRibbonOnCurves.setWindowTitle(QCoreApplication.translate("DlgRibbonOnCurves", u"Dialog", None))
        self.label_7.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Select two curves.", None))
        self.label_3.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Name", None))
        self.le_name.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Ribbon", None))
        self.label.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Joints Number", None))
        self.label_4.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Joints Orientation", None))
        self.cb_jntOrientation.setItemText(0, QCoreApplication.translate("DlgRibbonOnCurves", u"World", None))
        self.cb_jntOrientation.setItemText(1, QCoreApplication.translate("DlgRibbonOnCurves", u"Rivet", None))

        self.label_2.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Drv Jnt Number", None))
        self.label_5.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Drv Jnt Orientation", None))
        self.cb_drvJntOrientation.setItemText(0, QCoreApplication.translate("DlgRibbonOnCurves", u"World", None))
        self.cb_drvJntOrientation.setItemText(1, QCoreApplication.translate("DlgRibbonOnCurves", u"Rivet", None))

        self.cb_reverse.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Reverse", None))
        self.label_6.setText("")
        self.btn_apply.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Apply", None))
        self.btn_accept.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Accept", None))
        self.btn_close.setText(QCoreApplication.translate("DlgRibbonOnCurves", u"Close", None))
    # retranslateUi

