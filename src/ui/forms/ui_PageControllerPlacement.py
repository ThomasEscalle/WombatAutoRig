# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageControllerPlacement.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PageControllerPlacement(object):
    def setupUi(self, PageControllerPlacement):
        if not PageControllerPlacement.objectName():
            PageControllerPlacement.setObjectName(u"PageControllerPlacement")
        PageControllerPlacement.resize(699, 771)
        self.verticalLayout = QVBoxLayout(PageControllerPlacement)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageControllerPlacement)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(PageControllerPlacement)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cb_IkCTRLS = QCheckBox(PageControllerPlacement)
        self.cb_IkCTRLS.setObjectName(u"cb_IkCTRLS")

        self.horizontalLayout.addWidget(self.cb_IkCTRLS)

        self.cb_fkCTRLS = QCheckBox(PageControllerPlacement)
        self.cb_fkCTRLS.setObjectName(u"cb_fkCTRLS")

        self.horizontalLayout.addWidget(self.cb_fkCTRLS)

        self.cb_otherCTRLS = QCheckBox(PageControllerPlacement)
        self.cb_otherCTRLS.setObjectName(u"cb_otherCTRLS")

        self.horizontalLayout.addWidget(self.cb_otherCTRLS)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cb_ShowGeo = QCheckBox(PageControllerPlacement)
        self.cb_ShowGeo.setObjectName(u"cb_ShowGeo")

        self.horizontalLayout_3.addWidget(self.cb_ShowGeo)

        self.cb_ShowJoints = QCheckBox(PageControllerPlacement)
        self.cb_ShowJoints.setObjectName(u"cb_ShowJoints")

        self.horizontalLayout_3.addWidget(self.cb_ShowJoints)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_3 = QLabel(PageControllerPlacement)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.btnControllers = QPushButton(PageControllerPlacement)
        self.btnControllers.setObjectName(u"btnControllers")

        self.verticalLayout.addWidget(self.btnControllers)

        self.btnColors = QPushButton(PageControllerPlacement)
        self.btnColors.setObjectName(u"btnColors")

        self.verticalLayout.addWidget(self.btnColors)

        self.label_4 = QLabel(PageControllerPlacement)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cb_MirrorDirection = QComboBox(PageControllerPlacement)
        self.cb_MirrorDirection.addItem("")
        self.cb_MirrorDirection.addItem("")
        self.cb_MirrorDirection.addItem("")
        self.cb_MirrorDirection.addItem("")
        self.cb_MirrorDirection.setObjectName(u"cb_MirrorDirection")

        self.horizontalLayout_2.addWidget(self.cb_MirrorDirection)

        self.pushButton = QPushButton(PageControllerPlacement)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PageControllerPlacement)

        QMetaObject.connectSlotsByName(PageControllerPlacement)
    # setupUi

    def retranslateUi(self, PageControllerPlacement):
        PageControllerPlacement.setWindowTitle(QCoreApplication.translate("PageControllerPlacement", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageControllerPlacement", u"Controllers Placement", None))
        self.label_2.setText("")
        self.cb_IkCTRLS.setText(QCoreApplication.translate("PageControllerPlacement", u"IK CTRLs", None))
        self.cb_fkCTRLS.setText(QCoreApplication.translate("PageControllerPlacement", u"FK CTRLs", None))
        self.cb_otherCTRLS.setText(QCoreApplication.translate("PageControllerPlacement", u"OTHER CTRLs", None))
        self.cb_ShowGeo.setText(QCoreApplication.translate("PageControllerPlacement", u"Show Geo", None))
        self.cb_ShowJoints.setText(QCoreApplication.translate("PageControllerPlacement", u"Show Joints", None))
        self.label_3.setText("")
        self.btnControllers.setText(QCoreApplication.translate("PageControllerPlacement", u"Replace controllers", None))
        self.btnColors.setText(QCoreApplication.translate("PageControllerPlacement", u"Colors", None))
        self.label_4.setText("")
        self.cb_MirrorDirection.setItemText(0, QCoreApplication.translate("PageControllerPlacement", u"Leg : L -> R", None))
        self.cb_MirrorDirection.setItemText(1, QCoreApplication.translate("PageControllerPlacement", u"Leg : R -> L", None))
        self.cb_MirrorDirection.setItemText(2, QCoreApplication.translate("PageControllerPlacement", u"Arm : L -> R", None))
        self.cb_MirrorDirection.setItemText(3, QCoreApplication.translate("PageControllerPlacement", u"Arm : R -> L", None))

        self.pushButton.setText(QCoreApplication.translate("PageControllerPlacement", u"Mirror", None))
    # retranslateUi

