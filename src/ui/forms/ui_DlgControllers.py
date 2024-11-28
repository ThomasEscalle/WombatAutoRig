# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgControllers.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgControllers(object):
    def setupUi(self, DlgControllers):
        if not DlgControllers.objectName():
            DlgControllers.setObjectName(u"DlgControllers")
        DlgControllers.resize(484, 412)
        self.verticalLayout = QVBoxLayout(DlgControllers)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnOptions = QPushButton(DlgControllers)
        self.btnOptions.setObjectName(u"btnOptions")

        self.horizontalLayout_2.addWidget(self.btnOptions)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(DlgControllers)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scroll_area_widget = QWidget()
        self.scroll_area_widget.setObjectName(u"scroll_area_widget")
        self.scroll_area_widget.setGeometry(QRect(0, 0, 458, 294))
        self.gridLayout = QGridLayout(self.scroll_area_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.scroll_area_widget)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_apply = QPushButton(DlgControllers)
        self.btn_apply.setObjectName(u"btn_apply")

        self.horizontalLayout.addWidget(self.btn_apply)

        self.btn_create = QPushButton(DlgControllers)
        self.btn_create.setObjectName(u"btn_create")

        self.horizontalLayout.addWidget(self.btn_create)

        self.btn_cancel = QPushButton(DlgControllers)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgControllers)

        QMetaObject.connectSlotsByName(DlgControllers)
    # setupUi

    def retranslateUi(self, DlgControllers):
        DlgControllers.setWindowTitle(QCoreApplication.translate("DlgControllers", u"Dialog", None))
        self.btnOptions.setText(QCoreApplication.translate("DlgControllers", u"...", None))
        self.btn_apply.setText(QCoreApplication.translate("DlgControllers", u"Apply", None))
        self.btn_create.setText(QCoreApplication.translate("DlgControllers", u"Create", None))
        self.btn_cancel.setText(QCoreApplication.translate("DlgControllers", u"Cancel", None))
    # retranslateUi

