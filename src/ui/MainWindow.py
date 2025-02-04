### Command : ./pyside2-uic.exe -o S:/3D/ScriptsMaya/SaveAs/generatedUi.py S:/3D/ScriptsMaya/SaveAs/save_as.ui


import sys
from PySide2 import QtWidgets, QtCore, QtGui
import maya.OpenMayaUI as omui
import shiboken2
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.cmds as cmds
from maya.OpenMayaUI import MQtUtil

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wombatAutoRig.src.ui import IconLoader
from wombatAutoRig.src.core import FileHelper

from wombatAutoRig.src.ui.forms import ui_MainWindow

from wombatAutoRig.src.ui import PageTemplateSelection
from wombatAutoRig.src.ui import PageGlobalSettings
from wombatAutoRig.src.ui import PageGeometrySelection
from wombatAutoRig.src.ui import PageJointPlacement
from wombatAutoRig.src.ui import PageControllerPlacement
from wombatAutoRig.src.ui import PageValidation



from wombatAutoRig.src.ui import DlgAddToShelf
from wombatAutoRig.src.ui import DlgNewTemplate
from wombatAutoRig.src.ui import DlgQuickLoad


from wombatAutoRig.src.core import TemplateBase

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


class MainWindow(MayaQWidgetDockableMixin, QtWidgets.QMainWindow):
    
    def __init__(self, parent=maya_main_window()):
        super(MainWindow, self).__init__(parent)

        self.ui = ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Wombat Auto Rigger")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        # The current template
        self.template = None
        self.settings = {}

        # Add pages to the stacked widget
        self.pageTemplateSelection = PageTemplateSelection.PageTemplateSelection()
        self.ui.stackedWidget.addWidget(self.pageTemplateSelection)

        """
        self.pageGlobalSettings = PageGlobalSettings.PageGlobalSettings()
        self.ui.stackedWidget.addWidget(self.pageGlobalSettings)

        self.pageGeometrySelection = PageGeometrySelection.PageGeometrySelection()
        self.ui.stackedWidget.addWidget(self.pageGeometrySelection)

        self.pageJointPlacement = PageJointPlacement.PageJointPlacement()
        self.ui.stackedWidget.addWidget(self.pageJointPlacement)

        self.pageControllerPlacement = PageControllerPlacement.PageControllerPlacement()
        self.ui.stackedWidget.addWidget(self.pageControllerPlacement)
        """

        
        self.pageValidation = PageValidation.PageValidation()
        self.ui.stackedWidget.addWidget(self.pageValidation)



        # Connect signals
        self.ui.btnNext.clicked.connect(self.nextPage)
        self.ui.btnCancel.clicked.connect(self.cancel)
        self.ui.actionNew_template.triggered.connect(self.newTemplate)
        self.ui.actionNext.triggered.connect(self.nextPage)
        self.ui.actionClose.triggered.connect(self.cancel)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionTemplate_Folder.triggered.connect(self.openTemplateFolder)
        self.ui.actionPreferences.triggered.connect(self.preferences)
        self.ui.actionAdd_to_shelf.triggered.connect(self.addToShelf)
        self.ui.actionAuto_Fill.triggered.connect(self.autoFill)
        self.ui.actionQuick_Load.triggered.connect(self.quickLoad)
        self.pageValidation.yesClicked.connect(self.nextPage)
        self.pageValidation.noClicked.connect(self.cancel)
        


        # Set icons
        self.ui.btnNext.setIcon(IconLoader.loadIcon("arrow_forward.png"))
        self.ui.btnCancel.setIcon(IconLoader.loadIcon("close.png"))
        self.ui.actionNew_template.setIcon(IconLoader.loadIcon("add.png"))
        self.ui.actionNext.setIcon(IconLoader.loadIcon("arrow_forward.png"))
        self.ui.actionClose.setIcon(IconLoader.loadIcon("close.png"))
        self.ui.actionAbout.setIcon(IconLoader.loadIcon("about.png"))
        self.ui.actionHelp.setIcon(IconLoader.loadIcon("help.png"))
        self.ui.actionTemplate_Folder.setIcon(IconLoader.loadIcon("folder.png"))
        self.ui.actionPreferences.setIcon(IconLoader.loadIcon("settings.png"))
        self.ui.actionAdd_to_shelf.setIcon(IconLoader.loadIcon("shelf.png"))
        self.ui.actionAuto_Fill.setIcon(IconLoader.loadIcon("skip.png"))

    validationAccepted = Signal()
    validationEntered = Signal()

    # Show window with docking ability
    def run(self):
        self.show(dockable = True)
        

    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def nextPage(self):
        
        # Check if the current page is the last one
        if self.ui.stackedWidget.currentIndex() == self.ui.stackedWidget.count() - 1:
            # Close the window
            self.close()
        
        currentIndex = self.ui.stackedWidget.currentIndex()


        # Check if the current page can go to the next page
        if not self.ui.stackedWidget.currentWidget().canGoNext():
            return
        
        # Get the current template if it is the first page
        if currentIndex == 0:
            self.template = self.pageTemplateSelection.getSelectedTemplate()
            if self.template == None:
                return

            # Set the main window of the template
            self.template.setMainwindow(self)

            # Get the array of pages from the template
            pages = self.template.getPages()

            # Add the pages to the stacked widget (between the template selection page and the validation page)
            for page in pages:
                print("Adding page")
                self.ui.stackedWidget.insertWidget(self.ui.stackedWidget.count() - 1, page)




        ################################################################
        ##################### Finished events ##########################
        ################################################################
        """
        if self.template != None and currentIndex == 1:
            # Global settings
            if not self.template.onGlobalSettingsFinished(self.settings):
                return
        if self.template != None and currentIndex == 2:
            # Geometry selection
            if not self.template.onGeometrySelectionFinished(self.settings):
                return
        if self.template != None and currentIndex == 3:
            # Joint placement
            if not self.template.onJointPlacementFinished(self.settings):
                return
        if self.template != None and currentIndex == 4:
            # Controller placement
            if not self.template.onControllerPlacementFinished(self.settings):
                return
        """
        ################################################################
        ################################################################
        ################################################################


        ## Add the data to the settings object
        self.settings = self.ui.stackedWidget.currentWidget().addDataToSettings(self.settings)

        
        ################################################################
        ##################### Accepted events ##########################
        ################################################################
        self.ui.stackedWidget.currentWidget().onAccepted()

        # if the page is the last one, emit the validation accepted signal
        if currentIndex == self.ui.stackedWidget.count() - 1:
            self.validationAccepted.emit()
        ################################################################
        ################################################################
        ################################################################




        # Go to the next page
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex() + 1)

        # Check if we should hide the next and cancel buttons
        if self.ui.stackedWidget.currentWidget().hideNextAndCancel():
            self.ui.btnNext.hide()
            self.ui.btnCancel.hide()
        else:
            self.ui.btnNext.show()
            self.ui.btnCancel.show()
        
        # Update the current index
        currentIndex = self.ui.stackedWidget.currentIndex()


        ################################################################
        ##################### Entered events ###########################
        ################################################################
        self.ui.stackedWidget.currentWidget().onEntered()

        # if the page is the last one, emit the validation entered signal
        if currentIndex == self.ui.stackedWidget.count() - 1:
            self.validationEntered.emit()

        ################################################################
        ################################################################
        ################################################################


    # When the user triggers the "New template" action
    def newTemplate(self):
        # Show the dialog
        dlg = DlgNewTemplate.DlgNewTemplate()
        dlg.exec()

    
    def quickLoad(self):
        dlg = DlgQuickLoad.DlgQuickLoad()
        dlg.setMainwindow(self)
        dlg.run()

    def autoFill(self):
        # Call the autoFill method of the current page
        self.ui.stackedWidget.currentWidget().autoFill()

        self.nextPage()
        pass

    # When the cancel button is pressed
    def cancel(self):
        self.close()
    
    def addToShelf(self):
        dialog = DlgAddToShelf.DlgAddToShelf()
        dialog.run()

    def about(self):
        QtWidgets.QMessageBox.about(self, "About Wombat Auto Rigger", "Wombat Auto Rigger is a tool to create rigs automatically.")

    def help(self):
        QtWidgets.QMessageBox.about(self, "Help", "This is the help message.")

    def openTemplateFolder(self):
        FileHelper.openFolderInExplorer(FileHelper.getTemplatesPath())

    def preferences(self):
        FileHelper.openFolderInExplorer(FileHelper.getPreferencesPath())



