# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgAddToShelf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DlgAddToShelf(object):
    def setupUi(self, DlgAddToShelf):
        if not DlgAddToShelf.objectName():
            DlgAddToShelf.setObjectName(u"DlgAddToShelf")
        DlgAddToShelf.resize(266, 113)
        self.verticalLayout = QVBoxLayout(DlgAddToShelf)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(DlgAddToShelf)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(DlgAddToShelf)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_close = QPushButton(DlgAddToShelf)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgAddToShelf)

        QMetaObject.connectSlotsByName(DlgAddToShelf)
    # setupUi

    def retranslateUi(self, DlgAddToShelf):
        DlgAddToShelf.setWindowTitle(QCoreApplication.translate("DlgAddToShelf", u"Dialog", None))
        self.btn_add.setText(QCoreApplication.translate("DlgAddToShelf", u"Add", None))
        self.btn_close.setText(QCoreApplication.translate("DlgAddToShelf", u"Close", None))
    # retranslateUi

