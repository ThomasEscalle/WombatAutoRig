# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageTemplateSelection.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PageTemplateSelection(object):
    def setupUi(self, PageTemplateSelection):
        if not PageTemplateSelection.objectName():
            PageTemplateSelection.setObjectName(u"PageTemplateSelection")
        PageTemplateSelection.resize(1067, 1036)
        self.verticalLayout = QVBoxLayout(PageTemplateSelection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(PageTemplateSelection)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(PageTemplateSelection)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(PageTemplateSelection)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.cbSelectTemplate = QComboBox(PageTemplateSelection)
        self.cbSelectTemplate.setObjectName(u"cbSelectTemplate")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbSelectTemplate.sizePolicy().hasHeightForWidth())
        self.cbSelectTemplate.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cbSelectTemplate)

        self.btnRefresh = QPushButton(PageTemplateSelection)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout.addWidget(self.btnRefresh)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 301, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(PageTemplateSelection)

        QMetaObject.connectSlotsByName(PageTemplateSelection)
    # setupUi

    def retranslateUi(self, PageTemplateSelection):
        PageTemplateSelection.setWindowTitle(QCoreApplication.translate("PageTemplateSelection", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("PageTemplateSelection", u"Template Selection", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("PageTemplateSelection", u"Select a template :", None))
        self.btnRefresh.setText(QCoreApplication.translate("PageTemplateSelection", u"Refresh", None))
    # retranslateUi

