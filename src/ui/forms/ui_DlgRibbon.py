# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgRibbon.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgRibbon(object):
    def setupUi(self, DlgRibbon):
        if not DlgRibbon.objectName():
            DlgRibbon.setObjectName(u"DlgRibbon")
        DlgRibbon.resize(423, 159)
        self.verticalLayout = QVBoxLayout(DlgRibbon)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DlgRibbon)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_name = QLineEdit(DlgRibbon)
        self.le_name.setObjectName(u"le_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_name)

        self.label_2 = QLabel(DlgRibbon)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.sb_nurbs = QSpinBox(DlgRibbon)
        self.sb_nurbs.setObjectName(u"sb_nurbs")
        self.sb_nurbs.setMinimum(2)
        self.sb_nurbs.setValue(5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sb_nurbs)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_apply = QPushButton(DlgRibbon)
        self.btn_apply.setObjectName(u"btn_apply")

        self.horizontalLayout.addWidget(self.btn_apply)

        self.btn_create = QPushButton(DlgRibbon)
        self.btn_create.setObjectName(u"btn_create")

        self.horizontalLayout.addWidget(self.btn_create)

        self.btn_cancel = QPushButton(DlgRibbon)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgRibbon)

        QMetaObject.connectSlotsByName(DlgRibbon)
    # setupUi

    def retranslateUi(self, DlgRibbon):
        DlgRibbon.setWindowTitle(QCoreApplication.translate("DlgRibbon", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DlgRibbon", u"Name", None))
        self.le_name.setText(QCoreApplication.translate("DlgRibbon", u"Ribbon", None))
        self.label_2.setText(QCoreApplication.translate("DlgRibbon", u"Nurbs", None))
        self.btn_apply.setText(QCoreApplication.translate("DlgRibbon", u"Apply", None))
        self.btn_create.setText(QCoreApplication.translate("DlgRibbon", u"Create", None))
        self.btn_cancel.setText(QCoreApplication.translate("DlgRibbon", u"Cancel", None))
    # retranslateUi

