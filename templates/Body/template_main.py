from wombatAutoRig.src.core import TemplateBase
from wombatAutoRig.src.core import AutorigHelper
from wombatAutoRig.src.core import Offset
from maya import cmds


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
        AutorigHelper.createDefaultAutorigFolder("autorig")
    
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
        AutorigHelper.makeTemplate(settings["geo"], 1)
        AutorigHelper.hideJointsPlacement(0)

        # Root
        cmds.select(clear=True)
        root = cmds.joint(name="Placement_root", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (0, 50, 0)))

        # Hip_Left
        cmds.select(clear=True)
        hip_left = cmds.joint(name="Placement_hip_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5, 46, 0)))
        # Knee_Left
        cmds.select(clear=True)
        knee_left = cmds.joint(name="Placement_knee_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5, 26, 0)))
        # Ankle_Left
        cmds.select(clear=True)
        ankle_left = cmds.joint(name="Placement_ankle_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5,  6, 0)))
        # Foot_Left
        cmds.select(clear=True)
        foot_left = cmds.joint(name="Placement_foot_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5,  2, 4)))
        # Foot_left_end
        cmds.select(clear=True)
        foot_left_end = cmds.joint(name="Placement_foot_left_end", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5,  2, 7)))

        # Hip_Right
        cmds.select(clear=True)
        hip_right = cmds.joint(name="Placement_hip_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -5, 46, 0)))
        # Knee_Right
        cmds.select(clear=True)
        knee_right = cmds.joint(name="Placement_knee_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -5, 26, 0)))
        # Ankle_Right
        cmds.select(clear=True)
        ankle_right = cmds.joint(name="Placement_ankle_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -5,  6, 0)))
        # Foot_Right
        cmds.select(clear=True)
        foot_right = cmds.joint(name="Placement_foot_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  -5,  2, 4)))
        # Foot_right_end
        cmds.select(clear=True)
        foot_right_end = cmds.joint(name="Placement_foot_right_end", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  -5,  2, 7)))


        # Spine end
        cmds.select(clear=True)
        spine_end = cmds.joint(name="Placement_spine_end", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (0, 70, 0)))

        # Neck
        cmds.select(clear=True)
        neck = cmds.joint(name="Placement_neck", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (0, 78, -2)))


        # Clavicle_Left
        cmds.select(clear=True)
        clavicle_left = cmds.joint(name="Placement_clavicle_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  1, 70, 2)))
        # Shoulder_Left
        cmds.select(clear=True)
        shoulder_left = cmds.joint(name="Placement_shoulder_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  7, 70, -2)))
        # Elbow_Left
        cmds.select(clear=True)
        elbow_left = cmds.joint(name="Placement_elbow_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  16, 60, -4)))
        # Wrist_Left
        cmds.select(clear=True)
        wrist_left = cmds.joint(name="Placement_wrist_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  25, 52, -2)))

        # Clavicle_Right
        cmds.select(clear=True)
        clavicle_right = cmds.joint(name="Placement_clavicle_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -1, 70, 2)))
        # Shoulder_Right
        cmds.select(clear=True)
        shoulder_right = cmds.joint(name="Placement_shoulder_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -7, 70, -2)))
        # Elbow_Right
        cmds.select(clear=True)
        elbow_right = cmds.joint(name="Placement_elbow_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -16, 60, -4)))
        # Wrist_Right
        cmds.select(clear=True)
        wrist_right = cmds.joint(name="Placement_wrist_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -25, 52, -2)))


        # Parent the joints together
        cmds.parent(hip_left, root)
        cmds.parent(hip_right, root)
        cmds.parent(knee_left, hip_left)
        cmds.parent(knee_right, hip_right)
        cmds.parent(ankle_left, knee_left)
        cmds.parent(ankle_right, knee_right)
        cmds.parent(foot_left, ankle_left)
        cmds.parent(foot_right, ankle_right)
        cmds.parent(foot_left_end, foot_left)
        cmds.parent(foot_right_end, foot_right)
        cmds.parent(spine_end, root)
        cmds.parent(neck, spine_end)
        cmds.parent(clavicle_left, spine_end)
        cmds.parent(shoulder_left, clavicle_left)
        cmds.parent(elbow_left, shoulder_left)
        cmds.parent(wrist_left, elbow_left)
        cmds.parent(clavicle_right, spine_end)
        cmds.parent(shoulder_right, clavicle_right)
        cmds.parent(elbow_right, shoulder_right)
        cmds.parent(wrist_right, elbow_right)

        # Place the root inside of the "AutoRig_Data|JointsPlacement"
        cmds.parent(root, "AutoRig_Data|JointsPlacement")
        Offset.offset(root)




        




    # This method is called when the joint placement is finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    def onJointPlacementFinished(self, settings):
        print("onJointPlacementFinished")
        return True
    
    # This method is called when the joint placement is accepted
    def onJointPlacementAccepted(self, settings):
        print("onJointPlacementAccepted")
        AutorigHelper.hideJointsPlacement(1)
        AutorigHelper.makeTemplate(settings["geo"], 0)


    ################################################################################################
    ################### C O N T R O L L E R   P L A C E M E N T   P A G E ##########################
    ################################################################################################
    # region 3 - Controller

    # This method is called when the controller placement is entered
    def onControllerPlacementEntered(self, settings):
        AutorigHelper.hideControllersPlacement(0)
        print("onControllerPlacementEntered")

    # This method is called when the controller placement is finished (when the user clicks the "Next" button)
    # It is used to verify that the settings are correct
    # If the settings are correct, the method should return True and the next page will be shown
    def onControllerPlacementFinished(self, settings):
        print("onControllerPlacementFinished")
        return True
    
    # This method is called when the controller placement is accepted
    def onControllerPlacementAccepted(self, settings):
        AutorigHelper.hideControllersPlacement(1)
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
        # Create the folder hierarchy
        AutorigHelper.createDefaultFolder(settings["name"])


        # Remove the autorig folder
        AutorigHelper.removeDefaultAutorigFolder("autorig")
        return True