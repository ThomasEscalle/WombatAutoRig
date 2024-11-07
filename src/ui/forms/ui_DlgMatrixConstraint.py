# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgMatrixConstraint.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgMatrixConstraint(object):
    def setupUi(self, DlgMatrixConstraint):
        if not DlgMatrixConstraint.objectName():
            DlgMatrixConstraint.setObjectName(u"DlgMatrixConstraint")
        DlgMatrixConstraint.resize(601, 331)
        self.verticalLayout = QVBoxLayout(DlgMatrixConstraint)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DlgMatrixConstraint)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cb_offset = QCheckBox(DlgMatrixConstraint)
        self.cb_offset.setObjectName(u"cb_offset")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_offset)

        self.label_2 = QLabel(DlgMatrixConstraint)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.line = QFrame(DlgMatrixConstraint)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line)

        self.label_3 = QLabel(DlgMatrixConstraint)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.cb_translate_all = QCheckBox(DlgMatrixConstraint)
        self.cb_translate_all.setObjectName(u"cb_translate_all")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_translate_all)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cb_translate_X = QCheckBox(DlgMatrixConstraint)
        self.cb_translate_X.setObjectName(u"cb_translate_X")

        self.horizontalLayout.addWidget(self.cb_translate_X)

        self.cb_translate_Y = QCheckBox(DlgMatrixConstraint)
        self.cb_translate_Y.setObjectName(u"cb_translate_Y")

        self.horizontalLayout.addWidget(self.cb_translate_Y)

        self.cb_translate_Z = QCheckBox(DlgMatrixConstraint)
        self.cb_translate_Z.setObjectName(u"cb_translate_Z")

        self.horizontalLayout.addWidget(self.cb_translate_Z)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_4 = QLabel(DlgMatrixConstraint)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(DlgMatrixConstraint)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.cb_rotate_all = QCheckBox(DlgMatrixConstraint)
        self.cb_rotate_all.setObjectName(u"cb_rotate_all")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cb_rotate_all)

        self.label_6 = QLabel(DlgMatrixConstraint)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cb_rotate_X = QCheckBox(DlgMatrixConstraint)
        self.cb_rotate_X.setObjectName(u"cb_rotate_X")

        self.horizontalLayout_2.addWidget(self.cb_rotate_X)

        self.cb_rotate_Y = QCheckBox(DlgMatrixConstraint)
        self.cb_rotate_Y.setObjectName(u"cb_rotate_Y")

        self.horizontalLayout_2.addWidget(self.cb_rotate_Y)

        self.checkBox_6 = QCheckBox(DlgMatrixConstraint)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout_2.addWidget(self.checkBox_6)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_apply = QPushButton(DlgMatrixConstraint)
        self.btn_apply.setObjectName(u"btn_apply")

        self.horizontalLayout_3.addWidget(self.btn_apply)

        self.btn_create = QPushButton(DlgMatrixConstraint)
        self.btn_create.setObjectName(u"btn_create")

        self.horizontalLayout_3.addWidget(self.btn_create)

        self.btn_cancel = QPushButton(DlgMatrixConstraint)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_3.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DlgMatrixConstraint)

        QMetaObject.connectSlotsByName(DlgMatrixConstraint)
    # setupUi

    def retranslateUi(self, DlgMatrixConstraint):
        DlgMatrixConstraint.setWindowTitle(QCoreApplication.translate("DlgMatrixConstraint", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Maintain Offset", None))
        self.cb_offset.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Translate :", None))
        self.cb_translate_all.setText(QCoreApplication.translate("DlgMatrixConstraint", u"All", None))
        self.cb_translate_X.setText(QCoreApplication.translate("DlgMatrixConstraint", u"X", None))
        self.cb_translate_Y.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Y", None))
        self.cb_translate_Z.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Z", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Rotate", None))
        self.cb_rotate_all.setText(QCoreApplication.translate("DlgMatrixConstraint", u"All", None))
        self.label_6.setText("")
        self.cb_rotate_X.setText(QCoreApplication.translate("DlgMatrixConstraint", u"X", None))
        self.cb_rotate_Y.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Y", None))
        self.checkBox_6.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Z", None))
        self.btn_apply.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Apply", None))
        self.btn_create.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Create", None))
        self.btn_cancel.setText(QCoreApplication.translate("DlgMatrixConstraint", u"Cancel", None))
    # retranslateUi

