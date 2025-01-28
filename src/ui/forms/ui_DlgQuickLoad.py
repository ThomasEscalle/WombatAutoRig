# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgQuickLoad.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgQuickLoad(object):
    def setupUi(self, DlgQuickLoad):
        if not DlgQuickLoad.objectName():
            DlgQuickLoad.setObjectName(u"DlgQuickLoad")
        DlgQuickLoad.resize(597, 165)
        self.verticalLayout = QVBoxLayout(DlgQuickLoad)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnShowJnts = QPushButton(DlgQuickLoad)
        self.btnShowJnts.setObjectName(u"btnShowJnts")

        self.verticalLayout.addWidget(self.btnShowJnts)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnShowIkCtrls = QPushButton(DlgQuickLoad)
        self.btnShowIkCtrls.setObjectName(u"btnShowIkCtrls")

        self.horizontalLayout.addWidget(self.btnShowIkCtrls)

        self.btnShowFkCtrls = QPushButton(DlgQuickLoad)
        self.btnShowFkCtrls.setObjectName(u"btnShowFkCtrls")

        self.horizontalLayout.addWidget(self.btnShowFkCtrls)

        self.btnShowOtherCtrls = QPushButton(DlgQuickLoad)
        self.btnShowOtherCtrls.setObjectName(u"btnShowOtherCtrls")

        self.horizontalLayout.addWidget(self.btnShowOtherCtrls)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 53, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnCreate = QPushButton(DlgQuickLoad)
        self.btnCreate.setObjectName(u"btnCreate")

        self.horizontalLayout_2.addWidget(self.btnCreate)

        self.btnCancel = QPushButton(DlgQuickLoad)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_2.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(DlgQuickLoad)

        QMetaObject.connectSlotsByName(DlgQuickLoad)
    # setupUi

    def retranslateUi(self, DlgQuickLoad):
        DlgQuickLoad.setWindowTitle(QCoreApplication.translate("DlgQuickLoad", u"Dialog", None))
        self.btnShowJnts.setText(QCoreApplication.translate("DlgQuickLoad", u"Show Joints", None))
        self.btnShowIkCtrls.setText(QCoreApplication.translate("DlgQuickLoad", u"Show Ik Ctrls", None))
        self.btnShowFkCtrls.setText(QCoreApplication.translate("DlgQuickLoad", u"Show Fk Ctrls", None))
        self.btnShowOtherCtrls.setText(QCoreApplication.translate("DlgQuickLoad", u"Show Other Ctrls", None))
        self.btnCreate.setText(QCoreApplication.translate("DlgQuickLoad", u"Create", None))
        self.btnCancel.setText(QCoreApplication.translate("DlgQuickLoad", u"Cancel", None))
    # retranslateUi

