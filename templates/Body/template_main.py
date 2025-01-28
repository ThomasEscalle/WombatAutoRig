from wombatAutoRig.src.core import TemplateBase
from wombatAutoRig.src.core import AutorigHelper
from wombatAutoRig.src.core import Offset
from maya import cmds


from wombatAutoRig.src.ui import PageGlobalSettings
from wombatAutoRig.src.ui import PageGeometrySelection
from wombatAutoRig.src.ui import PageJointPlacement
from wombatAutoRig.src.ui import PageControllerPlacement


from wombatAutoRig.templates.Body import placement_joints
from wombatAutoRig.templates.Body import placement_controllers
from wombatAutoRig.templates.Body import compute



# Autorig template : Body
# Version : 0.0.1
# Author : ThomasEsc
# Identifier : Body
# Description : This is a template for an autorig
class Template(TemplateBase.TemplateBase):

    def __init__(self):
        super(Template, self).__init__()

        self.name = "Body"
        self.identifier = "Body"
        self.version = "0.0.1"
        self.author = "ThomasEsc"

        # The pages of the template
        self.pages = [
            PageGlobalSettings.PageGlobalSettings(),
            PageGeometrySelection.PageGeometrySelection(),
            PageJointPlacement.PageJointPlacement(),
            PageControllerPlacement.PageControllerPlacement(),
            PageGlobalSettings.PageGlobalSettings()
        ]

        self.pages[0].entered.connect(self.onGlobalSettingsEntered)
        self.pages[0].accepted.connect(self.onGlobalSettingsAccepted)

        self.pages[1].entered.connect(self.onGeometrySelectionEntered)
        self.pages[1].accepted.connect(self.onGeometrySelectionAccepted)

        self.pages[2].entered.connect(self.onJointPlacementEntered)
        self.pages[2].accepted.connect(self.onJointPlacementAccepted)

        self.pages[3].entered.connect(self.onControllerPlacementEntered)
        self.pages[3].accepted.connect(self.onControllerPlacementAccepted)

        self.pages[4].entered.connect(self.onBindEntered)
        self.pages[4].accepted.connect(self.onBindAccepted)

        self.pages[0].setPageTitle("Global Settings")
        self.pages[0].addTextInput("Name", "name")
        self.pages[0].addTextInput("Identifier", "identifier")
        self.pages[0].addSpacer()
        # Ask for the number of Fk controllers in the spine (combobox that can be 1, 3 or 5)
        self.pages[0].addLabel("Spine Settings")
        self.pages[0].addComboBox("Number of spine CTRLS", "nbrCtrlFkSpine", ["1", "3", "5"], 1)
        self.pages[0].addIntegerInput("Number of spine Joints", "nbrJointsSpine", defaultValue=7, min = 3, max = 50)

        self.pages[4].setPageTitle("Bind Skin")
        self.pages[4].addCheckbox("Bind Skin", "bindSkin")

        

    # This method is called when the template is initialized
    # It should be used to set up any necessary variables
    def onInit(self):
        print("onInit")

    # This method is called when the autorig is canceled
    # It shoud be used to clean up any temporary files or variables
    def onCanceled(self):
        print("onCanceled")

    # This method set the mainwindow
    def setMainwindow(self, mainwindow):
        self.mw = mainwindow

        self.mw.validationAccepted.connect(self.onValidationAccepted)
        self.mw.validationEntered.connect(self.onValidationEntered)










    ################################################################################################
    ################### G L O B A L   S E T T I N G S   P A G E ####################################
    ################################################################################################
    # region 0 - Global Settings

    # This method is called when the global settings are entered
    def onGlobalSettingsEntered(self):
        print("onGlobalSettingsEntered")
        AutorigHelper.createDefaultAutorigFolder("autorig")
    
    # This method is called when the global settings are finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    # If the settings are incorrect, the method should return False, and the next page will not be shown
    def onGlobalSettingsFinished(self):
        print("onGlobalSettingsFinished")
        return True
    
    # This method is called when the global settings are accepted
    def onGlobalSettingsAccepted(self):
        print("onGlobalSettingsAccepted")




    ################################################################################################
    ################### G E O M E T R Y   S E L E C T I O N   P A G E ##############################
    ################################################################################################
    # region 1 - Geometry

    # This method is called when the geometry selection is entered
    def onGeometrySelectionEntered(self):
        print("onGeometrySelectionEntered")

    # This method is called when the geometry selection is finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    def onGeometrySelectionFinished(self):
        print("onGeometrySelectionFinished")
        return True
    
    # This method is called when the geometry selection is accepted
    def onGeometrySelectionAccepted(self):
        print("onGeometrySelectionAccepted")



    ################################################################################################
    ################### J O I N T   P L A C E M E N T   P A G E ####################################
    ################################################################################################
    # region 2 - Joint

    # This method is called when the joint placement is entered
    def onJointPlacementEntered(self):
        print("onJointPlacementEntered")

        settings = self.mw.getSettings()
        
        AutorigHelper.makeTemplate(settings["geo"], 1)

        AutorigHelper.hideJointsPlacement(0)

        placement_joints.placeJoints(settings)


    # This method is called when the joint placement is finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    def onJointPlacementFinished(self):
        print("onJointPlacementFinished")
        return True
    
    # This method is called when the joint placement is accepted
    def onJointPlacementAccepted(self):
        print("onJointPlacementAccepted")
        settings = self.mw.getSettings()
        AutorigHelper.hideJointsPlacement(1)
        AutorigHelper.makeTemplate(settings["geo"], 0)


    ################################################################################################
    ################### C O N T R O L L E R   P L A C E M E N T   P A G E ##########################
    ################################################################################################
    # region 3 - Controller

    # This method is called when the controller placement is entered
    def onControllerPlacementEntered(self):
        settings = self.mw.getSettings()
        AutorigHelper.hideControllersPlacement(0)

        placement_controllers.placeControllers(settings)
        
        print("onControllerPlacementEntered")

    # This method is called when the controller placement is finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    def onControllerPlacementFinished(self):
        print("onControllerPlacementFinished")
        return True
    
    # This method is called when the controller placement is accepted
    def onControllerPlacementAccepted(self):
        AutorigHelper.hideControllersPlacement(1)
        print("onControllerPlacementAccepted")



    def onBindEntered(self):
        print("onBindEntered")

    def onBindAccepted(self):
        print("onBindAccepted")


    ################################################################################################
    ################### V A L I D A T I O N   P A G E ##############################################
    ################################################################################################
    # region 4 - Validation

    # This method is called when the joint limits are entered
    def onValidationEntered(self):
        print("onValidationEntered")

    # This method is called when the joint limits are finished (when the user clicks the "Next" button)
    def onValidationAccepted(self):
        print("onValidationAccepted")

        settings = self.mw.getSettings()

        # Create the folder hierarchy
        AutorigHelper.createDefaultFolder(settings["name"])

        ################################################################################################
        ################### C O M P U T E   ############################################################s
        ################################################################################################

        # Compute the autorig
        compute.compute(settings)


        # Remove the autorig folder
        if(settings["keepHistory"] == False):
            AutorigHelper.removeDefaultAutorigFolder("autorig")
        else :
            # Save the settings object into an attribute as json on the "AutoRig_Data" node (group)
            AutorigHelper.saveSettings(settings)
            pass

        AutorigHelper.disableLocalRotationAxis()
        return True