# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 1020)
        self.actionNew_template = QAction(MainWindow)
        self.actionNew_template.setObjectName(u"actionNew_template")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionNext = QAction(MainWindow)
        self.actionNext.setObjectName(u"actionNext")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionTemplate_Folder = QAction(MainWindow)
        self.actionTemplate_Folder.setObjectName(u"actionTemplate_Folder")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionAdd_to_shelf = QAction(MainWindow)
        self.actionAdd_to_shelf.setObjectName(u"actionAdd_to_shelf")
        self.actionAuto_Fill = QAction(MainWindow)
        self.actionAuto_Fill.setObjectName(u"actionAuto_Fill")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.centralwidget)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnNext = QPushButton(self.centralwidget)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setIconSize(QSize(26, 26))
        self.btnNext.setFlat(False)

        self.horizontalLayout.addWidget(self.btnNext)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1056, 29))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew_template)
        self.menuFile.addAction(self.actionNext)
        self.menuFile.addAction(self.actionAuto_Fill)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionTemplate_Folder)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuTools.addAction(self.actionAdd_to_shelf)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_template.setText(QCoreApplication.translate("MainWindow", u"New template", None))
#if QT_CONFIG(shortcut)
        self.actionNew_template.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl++", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(shortcut)
        self.actionNext.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionTemplate_Folder.setText(QCoreApplication.translate("MainWindow", u"Template Folder", None))
#if QT_CONFIG(shortcut)
        self.actionTemplate_Folder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionAdd_to_shelf.setText(QCoreApplication.translate("MainWindow", u"Add to shelf", None))
        self.actionAuto_Fill.setText(QCoreApplication.translate("MainWindow", u"Auto Fill", None))
#if QT_CONFIG(shortcut)
        self.actionAuto_Fill.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.btnCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btnNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

