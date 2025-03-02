from wombatAutoRig.src.core import TemplateBase
from wombatAutoRig.src.core import AutorigHelper
from wombatAutoRig.src.core import Offset
from maya import cmds
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Controllers

from wombatAutoRig.src.ui import PageGlobalSettings
from wombatAutoRig.src.ui import PageGeometrySelection
from wombatAutoRig.src.ui import PageJointPlacement
from wombatAutoRig.src.ui import PageControllerPlacement


from wombatAutoRig.templates.Body import placement_joints
from wombatAutoRig.templates.Body import placement_controllers
from wombatAutoRig.templates.Body import compute


def setShapeSize(controller, size):
    shapes = cmds.listRelatives(controller, shapes=True)
    for shape in shapes:
        cmds.setAttr(shape + ".lineWidth", size)


def resizeCtrl(bbox, size):
    referenceSizeY = 10
    sizeY = bbox[4] - bbox[1]

    sizeList = list(size)

    sizeList[0] = sizeList[0] * (sizeY / referenceSizeY)
    sizeList[1] = sizeList[1] * (sizeY / referenceSizeY)
    sizeList[2] = sizeList[2] * (sizeY / referenceSizeY)

    return tuple(sizeList)



# Autorig template : Prop
# Version : 0.0.1
# Author : ThomasEsc
# Identifier : Prop
# Description : This is a template for an autorig
class Template(TemplateBase.TemplateBase):

    def __init__(self):
        super(Template, self).__init__()

        # Check if the "matrixNodes" plugin is loaded
        if not cmds.pluginInfo("matrixNodes", query=True, loaded=True):
            cmds.loadPlugin("matrixNodes")

        self.name = "Prop"
        self.identifier = "Prop"
        self.version = "0.0.1"
        self.author = "ThomasEsc"
        

        # The pages of the template
        self.pages = [
            PageGlobalSettings.PageGlobalSettings(),
            PageGeometrySelection.PageGeometrySelection(),
            PageGlobalSettings.PageGlobalSettings(),
        ]

        self.pages[0].entered.connect(self.onGlobalSettingsEntered)
        self.pages[0].accepted.connect(self.onGlobalSettingsAccepted)

        self.pages[1].entered.connect(self.onGeometrySelectionEntered)
        self.pages[1].accepted.connect(self.onGeometrySelectionAccepted)

        self.pages[2].entered.connect(self.onControllerPlacementEntered)
        self.pages[2].accepted.connect(self.onControllerPlacementAccepted)

        self.pages[0].setPageTitle("Global Settings")
        self.pages[0].addTextInput("Identifier", "identifier")

        self.pages[2].setPageTitle("Controller Placement")

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
    ################### C O N T R O L L E R   P L A C E M E N T   P A G E ##########################
    ################################################################################################
    # region 3 - Controller

    # This method is called when the controller placement is entered
    def onControllerPlacementEntered(self):

        settings = self.mw.getSettings()
        print(settings) 

        print("onControllerPlacementEntered")
        AutorigHelper.hideControllersPlacement(0)

        # Create a controller (circle) at the origin
        controller = cmds.circle(name="PlacementCtrl_Global", radius=1, normal=[0, 1, 0])[0]


        ### Reference size for the controller
        position = [0,0,0]
        scale = [8,8,8]

        goodPos = resizeCtrl(bbox = settings["bbox"] , size = position)
        goodScale = resizeCtrl(bbox = settings["bbox"] , size = scale)

        cmds.setAttr(controller + ".translate", goodPos[0], goodPos[1], goodPos[2])
        cmds.setAttr(controller + ".scale", goodScale[0], goodScale[1], goodScale[2])


        setShapeSize("PlacementCtrl_Global", 2)
        Color.setColor("PlacementCtrl_Global", "yellow")
        cmds.parent("PlacementCtrl_Global", "AutoRig_Data|ControllersPlacement|Global_Controllers")


    # This method is called when the controller placement is finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    def onControllerPlacementFinished(self):
        print("onControllerPlacementFinished")
        AutorigHelper.hideControllersPlacement(1)
        
        return True
    
    # This method is called when the controller placement is accepted
    def onControllerPlacementAccepted(self):
        print("onControllerPlacementAccepted")



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
        AutorigHelper.createDefaultFolder(settings["identifier"])



        # Create a joint at the origin of the world, rename it Bind_Jnt_Root
        cmds.select(clear=True)
        rootJoint = cmds.joint(name="Bind_Jnt_Root")
        cmds.setAttr(rootJoint + ".radius", 0.5)
        # Parent it to the "AutoRig_Data|GlobalMove_01|Joints_01" group
        cmds.parent(rootJoint, settings["identifier"] + "|GlobalMove_01|Joints_01")
        # Add an offset to the joint
        Offset.offset("Bind_Jnt_Root", nbr=2)

        # Bind the geo to the joint
        cmds.select(clear=True)
        for geo in settings["geo"]:
            cmds.select(geo, add=True)
            cmds.select("Bind_Jnt_Root", add=True)
            cmds.skinCluster(tsb=True)
            cmds.select(clear=True)

        # Move the controller to settings["identifier"] + "|GlobalMove_01|CTRLs_01"
        cmds.parent("PlacementCtrl_Global", settings["identifier"])
        # Freeze the transformations
        cmds.makeIdentity("PlacementCtrl_Global", apply=True)
        # Rename the controller to "Ctrl_Global"
        cmds.rename("PlacementCtrl_Global", "Ctrl_Global")


        # Add a scale constraint  between the controller and the GlobalMove_01 group
        cmds.scaleConstraint("Ctrl_Global", settings["identifier"] + "|GlobalMove_01")
        # Add a parent constraint between the controller and the GlobalMove_01 group
        cmds.parentConstraint("Ctrl_Global", settings["identifier"] + "|GlobalMove_01") 

        # Move every geo that is located in settings["geo"] array to the settings["identifier"]|settings["identifier"]_Geo folder
        geoPath = settings["identifier"] + "|" + settings["identifier"] + "_Geo"
        for geo in settings["geo"]:
            cmds.parent(geo, geoPath)

        # Remove the autorig folder
        AutorigHelper.removeDefaultAutorigFolder("autorig")

        return True