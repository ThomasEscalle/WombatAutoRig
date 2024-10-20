from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


from wombatAutoRig.src.ui.forms import ui_DlgNewTemplate
from wombatAutoRig.src.ui import IconLoader
from wombatAutoRig.src.core import FileHelper


# Classe de la fenêtre de création de template
class DlgNewTemplate(QtWidgets.QDialog):
    def __init__(self):
        super(DlgNewTemplate, self).__init__()

        self.ui = ui_DlgNewTemplate.Ui_DlgNewTemplate()
        self.ui.setupUi(self)

        self.setWindowTitle("New Template")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setModal(True)

        # Connect signals
        self.ui.btnCreate.clicked.connect(self.createTemplate)
        self.ui.btnCancel.clicked.connect(self.close)
        
        # Set icons
        self.ui.btnCreate.setIcon(IconLoader.loadIcon("add"))
        self.ui.btnCancel.setIcon(IconLoader.loadIcon("close"))

    def createTemplate(self):
        # Check if all the fields are filled
        if self.ui.leName.text() == "":
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill the name field.")
            return
        if self.ui.leIdentifier.text() == "":
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill the identifier field.")
            return
        if self.ui.leAuthor.text() == "":
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill the author field.")
            return
        if self.ui.leVersion.text() == "":
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill the version field.")
            return


        # Get the informations
        name = self.ui.leName.text()
        identifier = self.ui.leIdentifier.text()
        author = self.ui.leAuthor.text()
        version = self.ui.leVersion.text()

        # Template Path
        templatePath = FileHelper.getTemplatesPath()
        templatePath = templatePath + "/" + name

        # Create the folder
        FileHelper.createFolderIfNotExists(templatePath)

        # Get the path to the resources folder
        filePath = FileHelper.getRcPath()
        filePath = filePath + "/template.txt"

        # Open the file
        file = open(filePath, "r")
        fileContent = file.read()
        file.close()

        fileContent = fileContent.replace("@name", name)
        fileContent = fileContent.replace("@identifier", identifier)
        fileContent = fileContent.replace("@author", author)
        fileContent = fileContent.replace("@version", version)

        # Write the file
        filePath = templatePath + "/template_main.py"
        file = open(filePath, "w")
        file.write(fileContent)
        file.close()

        # Close the dialog
        self.accept()


