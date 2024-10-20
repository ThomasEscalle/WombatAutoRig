from wombatAutoRig.src.core import TemplateBase
from wombatAutoRig.src.core import JointPlacement
from maya import cmds
import maya.mel



# Autorig template : Body
# Version : v01
# Author : ThomasEsc
# Identifier : body
# Description : This is a template for an autorig
class Template(TemplateBase.TemplateBase):

    def __init__(self):
        super(Template, self).__init__()

        self.name = "Body"
        self.identifier = "body"
        self.version = "v01"
        self.author = "ThomasEsc"

        self.jnts = {}
        self.ctrls = {}

        

    # This method is called when the template is initialized
    # It should be used to set up any necessary variables
    def onInit(self):
        print("onInit")

    # This method is called when the autorig is canceled
    # It shoud be used to clean up any temporary files or variables
    def onCanceled(self):
        print("onCanceled")


    ################################################################################################
    ################### G L O B A L   S E T T I N G S   P A G E ####################################
    ################################################################################################
    # region 0 - Global Settings

    # This method is called when the global settings are entered
    def onGlobalSettingsEntered(self, settings):
        print("onGlobalSettingsEntered")
    
    # This method is called when the global settings are finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    # If the settings are incorrect, the method should return False, and the next page will not be shown
    def onGlobalSettingsFinished(self, settings):
        print("onGlobalSettingsFinished")
        return True
    
    # This method is called when the global settings are accepted
    def onGlobalSettingsAccepted(self, settings):
        print("onGlobalSettingsAccepted")




    ################################################################################################
    ################### G E O M E T R Y   S E L E C T I O N   P A G E ##############################
    ################################################################################################
    # region 1 - Geometry

    # This method is called when the geometry selection is entered
    def onGeometrySelectionEntered(self, settings):
        print("onGeometrySelectionEntered")

    # This method is called when the geometry selection is finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    def onGeometrySelectionFinished(self, settings):
        print("onGeometrySelectionFinished")
        return True
    
    # This method is called when the geometry selection is accepted
    def onGeometrySelectionAccepted(self, settings):
        print("onGeometrySelectionAccepted")



    ################################################################################################
    ################### J O I N T   P L A C E M E N T   P A G E ####################################
    ################################################################################################
    # region 2 - Joint

    # This method is called when the joint placement is entered
    def onJointPlacementEntered(self, settings):
        print("onJointPlacementEntered")

        self.jnts["ctrl_00"] = JointPlacement.createController([0,0,0], 0.3, "CTRL_00")
        self.jnts["ctrl_01"] = JointPlacement.createController([0,8,0], 0.3, "CTRL_01")
        self.jnts["line_00"] = JointPlacement.connectLine(self.jnts["ctrl_00"], self.jnts["ctrl_01"], "LINE_00")




    # This method is called when the joint placement is finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    def onJointPlacementFinished(self, settings):
        print("onJointPlacementFinished")
        return True
    
    # This method is called when the joint placement is accepted
    def onJointPlacementAccepted(self, settings):
        print("onJointPlacementAccepted")

        # Hide the two controllers by switching the LOD_visibility attribute of the shapes to 0
        cmds.setAttr(self.jnts["ctrl_00"] + "Shape" + ".lodVisibility", 0)
        cmds.setAttr(self.jnts["ctrl_01"] + "Shape" + ".lodVisibility", 0)
        cmds.hide(self.jnts["line_00"])


    ################################################################################################
    ################### C O N T R O L L E R   P L A C E M E N T   P A G E ##########################
    ################################################################################################
    # region 3 - Controller

    # This method is called when the controller placement is entered
    def onControllerPlacementEntered(self, settings):
        print("onControllerPlacementEntered")
        
        # Create a controller circle  with a scale of 0.3
        self.ctrls["ctrl_00"] = cmds.circle(name="CTRL_00", radius=0.3, normal=[0,1,0], degree=1)[0]
        # Move the controller to the transformations of the jnts["ctrl_00"]
        cmds.xform(self.ctrls["ctrl_00"], translation=cmds.xform(self.jnts["ctrl_00"], query=True, translation=True), worldSpace=True)
        # Parent the controller to the jnt["ctrl_00"]
        cmds.parent(self.ctrls["ctrl_00"], self.jnts["ctrl_00"])

        # Create a controller circle  with a scale of 0.3
        self.ctrls["ctrl_01"] = cmds.circle(name="CTRL_01", radius=0.3, normal=[0,1,0], degree=1)[0]
        # Move the controller to the transformations of the jnts["ctrl_01"]
        cmds.xform(self.ctrls["ctrl_01"], translation=cmds.xform(self.jnts["ctrl_01"], query=True, translation=True), worldSpace=True)
        # Parent the controller to the jnt["ctrl_01"]
        cmds.parent(self.ctrls["ctrl_01"], self.jnts["ctrl_01"])


        


    # This method is called when the controller placement is finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    def onControllerPlacementFinished(self, settings):
        print("onControllerPlacementFinished")
        return True
    
    # This method is called when the controller placement is accepted
    def onControllerPlacementAccepted(self, settings):
        print("onControllerPlacementAccepted")



    ################################################################################################
    ################### V A L I D A T I O N   P A G E ##############################################
    ################################################################################################
    # region 4 - Validation

    # This method is called when the joint limits are entered
    def onValidationEntered(self, settings):
        print("onValidationEntered")

    # This method is called when the joint limits are finished (when the user clicks the "Next" button)
    def onValidationAccepted(self, settings):
        print("onValidationAccepted")

        # Select the first controller
        cmds.select(self.jnts["ctrl_00"])
        # Freeze the transformations
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        # Create a joint inside of the controller
        jnt_00 = cmds.joint(name="JNT_00")
        # Unparent the joint
        cmds.parent(jnt_00, world=True)
        
        # Select the second controller
        cmds.select(self.jnts["ctrl_01"])
        # Create a joint inside of the controller
        jnt_01 = cmds.joint(name="JNT_01")
        # Unparent the joint
        cmds.parent(jnt_01, world=True)
        # Parent the jnt_01 inside the jnt_00
        cmds.parent(jnt_01, jnt_00)



        return True