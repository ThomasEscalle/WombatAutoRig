from maya import cmds

from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Controllers
from wombatAutoRig.src.core import AutorigHelper

# - PlacementCtrl_Global
# - PlacementCtrl_Root
# - PlacementCtrl_Settings
# - PlacementCtrl_Settings_Head
# - PlacementCtrl_Settings_Leg_L
# - PlacementCtrl_Settings_Leg_R
# - PlacementCtrl_Settings_Arm_L
# - PlacementCtrl_Settings_Arm_R
# - PlacementCtrl_Settings_Spine
# - PlacementCtrl_Fk_Leg_L
# - PlacementCtrl_Fk_Leg_R
# - PlacementCtrl_Fk_Knee_R
# - PlacementCtrl_Fk_Knee_L
# - PlacementCtrl_Fk_Ankle_R
# - PlacementCtrl_Fk_Ankle_L
# - PlacementCtrl_Fk_Ball_R
# - PlacementCtrl_Fk_Ball_L
# - PlacementCtrl_Foot_R
# - PlacementCtrl_Foot_L
# - PlacementCtrl_Pv_Leg_R
# - PlacementCtrl_Pv_Leg_L
# - PlacementCtrl_Ribbon_Leg_L
# - PlacementCtrl_Ribbon_Leg_R
# - PlacementCtrl_Ribbon_Knee_L
# - PlacementCtrl_Ribbon_Knee_R
# - PlacementCtrl_Pin_Knee_R
# - PlacementCtrl_Pin_Knee_L
# - PlacementCtrl_Hip
# - PlacementCtrl_Shoulder
# - PlacementCtrl_Neck_01
# - PlacementCtrl_Spine_01
# - PlacementCtrl_Fk_Leg_L
# - PlacementCtrl_Fk_Leg_R
# - PlacementCtrl_Fk_Knee_R
# - PlacementCtrl_Fk_Knee_L
# - PlacementCtrl_Fk_Ankle_R
# - PlacementCtrl_Fk_Ankle_L
# - PlacementCtrl_Fk_Ball_R
# - PlacementCtrl_Fk_Ball_L
# - PlacementCtrl_Foot_R
# - PlacementCtrl_Foot_L
# - PlacementCtrl_Pv_Leg_R
# - PlacementCtrl_Pv_Leg_L
# - PlacementCtrl_Ribbon_Leg_L
# - PlacementCtrl_Ribbon_Leg_R
# - PlacementCtrl_Ribbon_Knee_L
# - PlacementCtrl_Ribbon_Knee_R
# - PlacementCtrl_Pin_Knee_R
# - PlacementCtrl_Pin_Knee_L

# @param snapTo : The joint to snap the controller to, we have it's position
def transformRelative(controller, position = [0,0,0], rotation = [0,0,0], scale = [1, 1, 1] , settings = None, snapTo = ""):
    goodPos = AutorigHelper.resizeCtrl(bbox = settings["bbox"] , size = position)
    goodScale = AutorigHelper.resizeCtrl(bbox = settings["bbox"] , size = scale)

    if snapTo != "":
        # Check if the snapTo is a joint and if it is located in the settings
        for joint in settings["joints"]:
            if joint["name"] == snapTo:
                positionSrc = joint["position"]
                goodPosSrc = joint["goodPos"]

                rotationSrc = joint["orientation"]

                # Check if the "snapTo" joint exists in the scene
                if cmds.objExists(snapTo):
                    # Get the world position of the joint named snapTo
                    positionScene = cmds.xform(snapTo, q=True, ws=True, t=True)

                    # Get the offset between the positionScene and the goodPosSrc
                    offset = [positionScene[0] - goodPosSrc[0], positionScene[1] - goodPosSrc[1], positionScene[2] - goodPosSrc[2]]

                    # Add the offset to the goodPos
                    goodPos = [goodPos[0] + offset[0], goodPos[1] + offset[1], goodPos[2] + offset[2]]


                    # Get the world rotation of the joint named snapTo
                    rotationScene = cmds.xform(snapTo, q=True, ws=True, ro=True)

                    # Get the offset between the rotationScene and the rotation
                    offsetRotation = [rotationScene[0] - rotationSrc[0], rotationScene[1] - rotationSrc[1], rotationScene[2] - rotationSrc[2]]

                    # Add the offset to the rotation
                    # rotation = [rotation[0] + offsetRotation[0], rotation[1] + offsetRotation[1], rotation[2] + offsetRotation[2]]


                break
    
    cmds.setAttr(controller + ".translate", goodPos[0], goodPos[1], goodPos[2])
    cmds.setAttr(controller + ".rotate", rotation[0], rotation[1], rotation[2])
    cmds.setAttr(controller + ".scale", goodScale[0], goodScale[1], goodScale[2])

def setShapeSize(controller, size):
    shapes = cmds.listRelatives(controller, shapes=True)
    for shape in shapes:
        cmds.setAttr(shape + ".lineWidth", size)




def placeControllers(settings):
    print("Place the controllers")
    
    # Hide the LRAs of the joints
    AutorigHelper.disableLocalRotationAxis()


    placeGlobalControllers(settings)
    placeSpineControllers(settings)
    placeLegsControllers(settings)
    placeArmsControllers(settings)
    placeFingersControllers(settings)




# Create a finger controller
def createFingerController(name, parentJoint, settings , rotation = [-90, -90 , 0], color = "red"):
    ctrl = Controllers.createController("2D_Shapes/Finger", name)
    # Match the transformations to 'PlacementJnt_Thumb_Metacarpus_R'
    cmds.matchTransform(name, parentJoint)
    cmds.rotate(rotation[0], 0, 0, name, r=True, os=True, fo=True)
    cmds.rotate(0, rotation[1], 0, name, r=True, os=True, fo=True)
    cmds.scale(0.5, 0.5, 0.5, name, r=True, ws=True)

    goodScale = AutorigHelper.resizeCtrl(bbox = settings["bbox"] , size = [0.5,0.5,0.5])
    cmds.setAttr(name + ".scale", goodScale[0], goodScale[1], goodScale[2])
    

    Color.setColor(name, color)
    cmds.parent(name, "AutoRig_Data|ControllersPlacement|Global_Controllers")

    return "AutoRig_Data|ControllersPlacement|Global_Controllers|" + name


# PlacementCtrl_Finger_Thumb_Metacarpus_R
# PlacementCtrl_Finger_Index_Metacarpus_R
# PlacementCtrl_Finger_Middle_Metacarpus_R
# PlacementCtrl_Finger_Ring_Metacarpus_R
# PlacementCtrl_Finger_Pinky_Metacarpus_R
# PlacementCtrl_Finger_Thumb_01_R
# PlacementCtrl_Finger_Thumb_02_R
# PlacementCtrl_Finger_Index_01_R
# PlacementCtrl_Finger_Index_02_R
# PlacementCtrl_Finger_Index_03_R
# PlacementCtrl_Finger_Middle_01_R
# PlacementCtrl_Finger_Middle_02_R
# PlacementCtrl_Finger_Middle_03_R
# PlacementCtrl_Finger_Ring_01_R
# PlacementCtrl_Finger_Ring_02_R
# PlacementCtrl_Finger_Ring_03_R
# PlacementCtrl_Finger_Pinky_01_R
# PlacementCtrl_Finger_Pinky_02_R
# PlacementCtrl_Finger_Pinky_03_R
# PlacementCtrl_Finger_Thumb_Metacarpus_L
# PlacementCtrl_Finger_Index_Metacarpus_L
# PlacementCtrl_Finger_Middle_Metacarpus_L
# PlacementCtrl_Finger_Ring_Metacarpus_L
# PlacementCtrl_Finger_Pinky_Metacarpus_L
# PlacementCtrl_Finger_Thumb_01_L
# PlacementCtrl_Finger_Thumb_02_L
# PlacementCtrl_Finger_Index_01_L
# PlacementCtrl_Finger_Index_02_L
# PlacementCtrl_Finger_Index_03_L
# PlacementCtrl_Finger_Middle_01_L
# PlacementCtrl_Finger_Middle_02_L
# PlacementCtrl_Finger_Middle_03_L
# PlacementCtrl_Finger_Ring_01_L
# PlacementCtrl_Finger_Ring_02_L
# PlacementCtrl_Finger_Ring_03_L
# PlacementCtrl_Finger_Pinky_01_L
# PlacementCtrl_Finger_Pinky_02_L
# PlacementCtrl_Finger_Pinky_03_L
def placeFingersControllers(settings):
    print("Fingers controllers")

    # region RIGHT FINGERS
    
    # PlacementJnt_Thumb_Metacarpus_R
    ctrl_01 = createFingerController("PlacementCtrl_Finger_Thumb_Metacarpus_R", "PlacementJnt_Thumb_Metacarpus_R", settings)
    # Bind_Index_Metacarpus_R
    ctrl_02 = createFingerController("PlacementCtrl_Finger_Index_Metacarpus_R", "PlacementJnt_Index_Metacarpus_R", settings)
    # PlacementJnt_Middle_Metacarpus_R
    ctrl_03 = createFingerController("PlacementCtrl_Finger_Middle_Metacarpus_R", "PlacementJnt_Middle_Metacarpus_R", settings)
    # PlacementJnt_Ring_Metacarpus_R
    ctrl_04 = createFingerController("PlacementCtrl_Finger_Ring_Metacarpus_R", "PlacementJnt_Ring_Metacarpus_R", settings)
    # PlacementJnt_Pinky_Metacarpus_R
    ctrl_05 = createFingerController("PlacementCtrl_Finger_Pinky_Metacarpus_R", "PlacementJnt_Pinky_Metacarpus_R", settings)


    # PlacementJnt_Thumb_01_R
    ctrl_01_01 = createFingerController("PlacementCtrl_Finger_Thumb_01_R", "PlacementJnt_Thumb_01_R", settings)
    # PlacementJnt_Thumb_02_R
    ctrl_01_02 = createFingerController("PlacementCtrl_Finger_Thumb_02_R", "PlacementJnt_Thumb_02_R", settings)

    # PlacementJnt_Index_01_R
    ctrl_02_01 = createFingerController("PlacementCtrl_Finger_Index_01_R", "PlacementJnt_Index_01_R", settings)
    # PlacementJnt_Index_02_R
    ctrl_02_02 = createFingerController("PlacementCtrl_Finger_Index_02_R", "PlacementJnt_Index_02_R", settings)
    # PlacementJnt_Index_03_R
    ctrl_02_03 = createFingerController("PlacementCtrl_Finger_Index_03_R", "PlacementJnt_Index_03_R", settings)

    # PlacementJnt_Middle_01_R
    ctrl_03_01 = createFingerController("PlacementCtrl_Finger_Middle_01_R", "PlacementJnt_Middle_01_R", settings)
    # PlacementJnt_Middle_02_R
    ctrl_03_02 = createFingerController("PlacementCtrl_Finger_Middle_02_R", "PlacementJnt_Middle_02_R", settings)
    # PlacementJnt_Middle_03_R
    ctrl_03_03 = createFingerController("PlacementCtrl_Finger_Middle_03_R", "PlacementJnt_Middle_03_R", settings)

    # PlacementJnt_Ring_01_R
    ctrl_04_01 = createFingerController("PlacementCtrl_Finger_Ring_01_R", "PlacementJnt_Ring_01_R", settings)
    # PlacementJnt_Ring_02_R
    ctrl_04_02 = createFingerController("PlacementCtrl_Finger_Ring_02_R", "PlacementJnt_Ring_02_R", settings)
    # PlacementJnt_Ring_03_R
    ctrl_04_03 = createFingerController("PlacementCtrl_Finger_Ring_03_R", "PlacementJnt_Ring_03_R", settings)
    

    # PlacementJnt_Pinky_01_R
    ctrl_05_01 = createFingerController("PlacementCtrl_Finger_Pinky_01_R", "PlacementJnt_Pinky_01_R", settings)
    # PlacementJnt_Pinky_02_R
    ctrl_05_02 = createFingerController("PlacementCtrl_Finger_Pinky_02_R", "PlacementJnt_Pinky_02_R", settings)
    # PlacementJnt_Pinky_03_R
    ctrl_05_03 = createFingerController("PlacementCtrl_Finger_Pinky_03_R", "PlacementJnt_Pinky_03_R", settings)


    # region LEFT FINGERS

    # PlacementJnt_Thumb_Metacarpus_L
    ctrl_06 = createFingerController("PlacementCtrl_Finger_Thumb_Metacarpus_L", "PlacementJnt_Thumb_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Index_Metacarpus_L
    ctrl_07 = createFingerController("PlacementCtrl_Finger_Index_Metacarpus_L", "PlacementJnt_Index_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Middle_Metacarpus_L
    ctrl_08 = createFingerController("PlacementCtrl_Finger_Middle_Metacarpus_L", "PlacementJnt_Middle_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Ring_Metacarpus_L
    ctrl_09 = createFingerController("PlacementCtrl_Finger_Ring_Metacarpus_L", "PlacementJnt_Ring_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Pinky_Metacarpus_L
    ctrl_10 = createFingerController("PlacementCtrl_Finger_Pinky_Metacarpus_L", "PlacementJnt_Pinky_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")


    # PlacementJnt_Thumb_01_L
    ctrl_06_01 = createFingerController("PlacementCtrl_Finger_Thumb_01_L", "PlacementJnt_Thumb_01_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Thumb_02_L
    ctrl_06_02 = createFingerController("PlacementCtrl_Finger_Thumb_02_L", "PlacementJnt_Thumb_02_L", settings, rotation=[90, 90, 0], color="turquoise")

    # PlacementJnt_Index_01_L
    ctrl_07_01 = createFingerController("PlacementCtrl_Finger_Index_01_L", "PlacementJnt_Index_01_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Index_02_L
    ctrl_07_02 = createFingerController("PlacementCtrl_Finger_Index_02_L", "PlacementJnt_Index_02_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Index_03_L
    ctrl_07_03 = createFingerController("PlacementCtrl_Finger_Index_03_L", "PlacementJnt_Index_03_L", settings, rotation=[90, 90, 0], color="turquoise")

    # PlacementJnt_Middle_01_L
    ctrl_08_01 = createFingerController("PlacementCtrl_Finger_Middle_01_L", "PlacementJnt_Middle_01_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Middle_02_L
    ctrl_08_02 = createFingerController("PlacementCtrl_Finger_Middle_02_L", "PlacementJnt_Middle_02_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Middle_03_L
    ctrl_08_03 = createFingerController("PlacementCtrl_Finger_Middle_03_L", "PlacementJnt_Middle_03_L", settings, rotation=[90, 90, 0], color="turquoise")

    # PlacementJnt_Ring_01_L
    ctrl_09_01 = createFingerController("PlacementCtrl_Finger_Ring_01_L", "PlacementJnt_Ring_01_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Ring_02_L
    ctrl_09_02 = createFingerController("PlacementCtrl_Finger_Ring_02_L", "PlacementJnt_Ring_02_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Ring_03_L
    ctrl_09_03 = createFingerController("PlacementCtrl_Finger_Ring_03_L", "PlacementJnt_Ring_03_L", settings, rotation=[90, 90, 0], color="turquoise")

    # PlacementJnt_Pinky_01_L
    ctrl_10_01 = createFingerController("PlacementCtrl_Finger_Pinky_01_L", "PlacementJnt_Pinky_01_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Pinky_02_L
    ctrl_10_02 = createFingerController("PlacementCtrl_Finger_Pinky_02_L", "PlacementJnt_Pinky_02_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Pinky_03_L
    ctrl_10_03 = createFingerController("PlacementCtrl_Finger_Pinky_03_L", "PlacementJnt_Pinky_03_L", settings, rotation=[90, 90, 0], color="turquoise")







# Place the global controllers
# - PlacementCtrl_Global
# - PlacementCtrl_Root
# - PlacementCtrl_Settings
# - PlacementCtrl_Settings_Head
# - PlacementCtrl_Settings_Leg_L
# - PlacementCtrl_Settings_Leg_R
# - PlacementCtrl_Settings_Arm_L
# - PlacementCtrl_Settings_Arm_R
# - PlacementCtrl_Settings_Spine
#region Global Controllers
def placeGlobalControllers(settings) :
    # PlacementCtrl_Global
    PlacementCtrl_Global = Controllers.createController("2D_Shapes/star", "PlacementCtrl_Global")
    transformRelative("PlacementCtrl_Global", [0, 1, 0], [0, 0, 0], [65, 65, 65] , settings)
    setShapeSize("PlacementCtrl_Global", 2)
    Color.setColor("PlacementCtrl_Global", "yellow")
    cmds.parent("PlacementCtrl_Global", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Root
    PlacementCtrl_Root = cmds.circle(name="PlacementCtrl_Root", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Root", [0, 93, -1.7], [0, 0, 0], [20, 20, 16] , settings , snapTo="PlacementJnt_Root")
    setShapeSize("PlacementCtrl_Root", 2)
    Color.setColor("PlacementCtrl_Root", "yellow")
    cmds.parent("PlacementCtrl_Root", "AutoRig_Data|ControllersPlacement|Global_Controllers")



    # PlacementCtrl_Settings
    PlacementCtrl_Settings = cmds.circle(name="PlacementCtrl_Settings", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Settings", [0, 1, -68], [0, 0, 0], [17, 17, 17] , settings)
    Color.setColor("PlacementCtrl_Settings", "yellow")
    cmds.parent("PlacementCtrl_Settings", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Settings_Head
    PlacementCtrl_Settings_Head = cmds.circle(name="PlacementCtrl_Settings_Head", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Settings_Head", [0, 1, -57], [0, 0, 0], [2.6, 2.6, 2.6] , settings)
    Color.setColor("PlacementCtrl_Settings_Head", "chocolate")
    cmds.parent("PlacementCtrl_Settings_Head", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Settings_Leg_L
    PlacementCtrl_Settings_Leg_L = cmds.circle(name="PlacementCtrl_Settings_Leg_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Settings_Leg_L", [4.19, 1, -77], [0, -15, 0], [1.5, 3.9, 5.0] , settings)
    Color.setColor("PlacementCtrl_Settings_Leg_L", "turquoise")
    cmds.parent("PlacementCtrl_Settings_Leg_L", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Settings_Leg_R
    PlacementCtrl_Settings_Leg_R = cmds.circle(name="PlacementCtrl_Settings_Leg_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Settings_Leg_R", [-4.19, 1, -77], [0, 15, 0], [1.5, 3.9, 5.0] , settings)
    Color.setColor("PlacementCtrl_Settings_Leg_R", "red")
    cmds.parent("PlacementCtrl_Settings_Leg_R", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Settings_Arm_L
    PlacementCtrl_Settings_Arm_L = cmds.circle(name="PlacementCtrl_Settings_Arm_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Settings_Arm_L", [6.5, 1, -65], [0, -50, 0], [1.6, 5, 5] , settings)
    Color.setColor("PlacementCtrl_Settings_Arm_L", "turquoise")
    cmds.parent("PlacementCtrl_Settings_Arm_L", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Settings_Arm_R
    PlacementCtrl_Settings_Arm_R = cmds.circle(name="PlacementCtrl_Settings_Arm_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Settings_Arm_R", [-6.5, 1, -65], [0, 50, 0], [1.6, 5, 5] , settings)
    Color.setColor("PlacementCtrl_Settings_Arm_R", "red")
    cmds.parent("PlacementCtrl_Settings_Arm_R", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Settings_Spine
    PlacementCtrl_Settings_Spine = cmds.circle(name="PlacementCtrl_Settings_Spine", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Settings_Spine", [0, 1, -67], [0, 0, 0], [2.7, 6.4, 5.3] , settings)
    Color.setColor("PlacementCtrl_Settings_Spine", "chocolate")
    cmds.parent("PlacementCtrl_Settings_Spine", "AutoRig_Data|ControllersPlacement|Global_Controllers")



# Place the spine controllers
# - PlacementCtrl_Hip
# - PlacementCtrl_Shoulder

# region Spine Controllers
def placeSpineControllers(settings) :

    # PlacementCtrl_Hip
    PlacementCtrl_Hip = Controllers.createController("3D_Shapes/boat", "PlacementCtrl_Hip")
    transformRelative("PlacementCtrl_Hip", [0, 101, -2.0], [180, 90, 0], [14.6, 8, 8.2] , settings, snapTo="PlacementJnt_Root")
    Color.setColor("PlacementCtrl_Hip", "chocolate")
    cmds.parent("PlacementCtrl_Hip", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Shoulder
    PlacementCtrl_Shoulder = cmds.circle(name="PlacementCtrl_Shoulder", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Shoulder", [0, 139, -1.8], [0, 0, 0], [13.6, 13.6, 9.6] , settings, snapTo="PlacementJnt_Chest")
    cmds.move(0, -3.633511, 0, "PlacementCtrl_Shoulder.cv[5]", "PlacementCtrl_Shoulder.cv[1]", r=True, os=True, wd=True)
    setShapeSize("PlacementCtrl_Shoulder", 2)
    Color.setColor("PlacementCtrl_Shoulder", "yellow")
    cmds.parent("PlacementCtrl_Shoulder", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_ShoulderIk
    PlacementCtrl_ShoulderIk = cmds.circle(name="PlacementCtrl_ShoulderIk", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_ShoulderIk", [0, 139, -4.1], [0, 0, 0], [10.5, 10.5, 7] , settings, snapTo="PlacementJnt_Chest")
    cmds.move(0, -3.633511, 0, "PlacementCtrl_ShoulderIk.cv[5]", "PlacementCtrl_ShoulderIk.cv[1]", r=True, os=True, wd=True)
    Color.setColor("PlacementCtrl_ShoulderIk", "blue")
    cmds.parent("PlacementCtrl_ShoulderIk", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_IkRoot
    PlacementCtrl_IkRoot = cmds.circle(name="PlacementCtrl_IkRoot", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_IkRoot", [0, 93, -1.7], [0, 0, 0], [18.156, 18.156, 14.525] , settings, snapTo="PlacementJnt_Root")
    Color.setColor("PlacementCtrl_IkRoot", "blue")
    cmds.parent("PlacementCtrl_IkRoot", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # Placement Ctrl_Tangent_Root
    PlacementCtrl_Tangent_Root = cmds.circle(name="PlacementCtrl_Tangent_Root", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Tangent_Root", [22.5, 93, -3.2], [90, 0, 0], [1.97, 1.97, 1.97] , settings, snapTo="PlacementJnt_Root")
    Color.setColor("PlacementCtrl_Tangent_Root", "blue")
    cmds.parent("PlacementCtrl_Tangent_Root", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Tangent_Chest
    PlacementCtrl_Tangent_Chest = cmds.circle(name="PlacementCtrl_Tangent_Chest", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Tangent_Chest", [21, 139, -3.2], [90, 0, 0], [1.97, 1.97, 1.97] , settings, snapTo="PlacementJnt_Chest")
    Color.setColor("PlacementCtrl_Tangent_Chest", "blue")
    cmds.parent("PlacementCtrl_Tangent_Chest", "AutoRig_Data|ControllersPlacement|IK_Controllers")


    # Ik, Fk controllers
    nbrSpineControllersStr = settings["nbrCtrlFkSpine"]
    nbrSpineControllers = int(nbrSpineControllersStr)
    worldPosRoot = cmds.xform("PlacementJnt_Root", q=True, ws=True, t=True)
    worldPosChest = cmds.xform("PlacementJnt_Chest", q=True, ws=True, t=True)


    # Create the controllers
    # - PlacementCtrl_Spine_Fk_#
    # - PlacementCtrl_Spine_Ik_#
    #  Where # is the index of the controller
    for i in range(nbrSpineControllers):

        interpol = (i + 1) / (nbrSpineControllers + 1)

        # Place the controller in the middle of the spine
        pos = [worldPosRoot[0] + (worldPosChest[0] - worldPosRoot[0]) * interpol,
                worldPosRoot[1] + (worldPosChest[1] - worldPosRoot[1]) * interpol, 
                worldPosRoot[2] + (worldPosChest[2] - worldPosRoot[2]) * interpol]
        print("pos", pos)

        cmds.circle(name="PlacementCtrl_Spine_Fk_" + str(i + 1), normal=[0, 1, 0], radius=1)
        transformRelative("PlacementCtrl_Spine_Fk_" + str(i + 1), pos, [0, 0, 0], [14.8, 14.8, 14.8] , settings,snapTo="PlacementJnt_Root")
        cmds.setAttr("PlacementCtrl_Spine_Fk_" + str(i + 1) + ".translate", pos[0], pos[1], pos[2])
        Color.setColor("PlacementCtrl_Spine_Fk_" + str(i + 1), "yellow")
        cmds.parent("PlacementCtrl_Spine_Fk_" + str(i + 1), "AutoRig_Data|ControllersPlacement|FK_Controllers")

        cmds.circle(name="PlacementCtrl_Spine_Ik_" + str(i + 1), normal=[0, 1, 0], radius=1)
        transformRelative("PlacementCtrl_Spine_Ik_" + str(i + 1), pos, [0, 0, 0], [16, 16, 16] , settings,snapTo="PlacementJnt_Root")
        cmds.setAttr("PlacementCtrl_Spine_Ik_" + str(i + 1) + ".translate", pos[0], pos[1], pos[2])
        Color.setColor("PlacementCtrl_Spine_Ik_" + str(i + 1), "blue")
        cmds.parent("PlacementCtrl_Spine_Ik_" + str(i + 1), "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Spine_Ribbon_#
    #  Where # is the index of the controller
    nbrSpineJntsStr = settings["nbrJointsSpine"]
    nbrSpineJnts = int(nbrSpineJntsStr) - 2
    for i in range(nbrSpineJnts):
        pos = [worldPosRoot[0] + (worldPosChest[0] - worldPosRoot[0]) * (i + 1) / (nbrSpineJnts + 1), worldPosRoot[1] + (worldPosChest[1] - worldPosRoot[1]) * (i + 1) / (nbrSpineJnts + 1), worldPosRoot[2] + (worldPosChest[2] - worldPosRoot[2]) * (i + 1) / (nbrSpineJnts + 1)]

        cmds.circle(name="PlacementCtrl_Spine_Ribbon_" + str(i + 1), normal=[0, 1, 0], radius=1)
        transformRelative("PlacementCtrl_Spine_Ribbon_" + str(i + 1), pos, [0, 0, 0], [13, 13, 13] , settings,snapTo="PlacementJnt_Root")
        cmds.setAttr("PlacementCtrl_Spine_Ribbon_" + str(i + 1) + ".translate", pos[0], pos[1], pos[2])
        Color.setColor("PlacementCtrl_Spine_Ribbon_" + str(i + 1), "purple")
        cmds.parent("PlacementCtrl_Spine_Ribbon_" + str(i + 1), "AutoRig_Data|ControllersPlacement|Other_Controllers")







# Place the controllers in the legs
# - PlacementCtrl_Fk_Leg_L
# - PlacementCtrl_Fk_Leg_R
# - PlacementCtrl_Fk_Knee_R
# - PlacementCtrl_Fk_Knee_L
# - PlacementCtrl_Fk_Ankle_R
# - PlacementCtrl_Fk_Ankle_L
# - PlacementCtrl_Fk_Ball_R
# - PlacementCtrl_Fk_Ball_L
# - PlacementCtrl_Foot_R
# - PlacementCtrl_Foot_L
# - PlacementCtrl_Pv_Leg_R
# - PlacementCtrl_Pv_Leg_L
# - PlacementCtrl_Ribbon_Leg_L
# - PlacementCtrl_Ribbon_Leg_R
# - PlacementCtrl_Ribbon_Knee_L
# - PlacementCtrl_Ribbon_Knee_R
# - PlacementCtrl_Pin_Knee_R
# - PlacementCtrl_Pin_Knee_L
# region Legs Controllers
def placeLegsControllers(settings) :
    ###############################
    ###  CONTROLLERS RIGHT LEG  ###
    ###############################

    # PlacementCtrl_Fk_Leg_R
    PlacementCtrl_Fk_Leg_R = cmds.circle(name="PlacementCtrl_Fk_Leg_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Leg_R", [-9.621,82.611, -1.5], [0, 0, 0], [10, 10, 10] , settings , snapTo="PlacementJnt_Hip_R")
    Color.setColor("PlacementCtrl_Fk_Leg_R", "red")
    setShapeSize("PlacementCtrl_Fk_Leg_R", 2)
    cmds.parent("PlacementCtrl_Fk_Leg_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Knee_R
    PlacementCtrl_Fk_Knee_R = cmds.circle(name="PlacementCtrl_Fk_Knee_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Knee_R", [-8.677, 49, -1.5], [0, 0, 0], [7.2, 7.2, 7.2] , settings, snapTo="PlacementJnt_Knee_R")
    Color.setColor("PlacementCtrl_Fk_Knee_R", "red")
    setShapeSize("PlacementCtrl_Fk_Knee_R", 2)
    cmds.parent("PlacementCtrl_Fk_Knee_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Ankle_R
    PlacementCtrl_Fk_Ankle_R = cmds.circle(name="PlacementCtrl_Fk_Ankle_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Ankle_R", [-7.324, 12.9, 0], [0, 0, 0], [7, 7, 7] , settings, snapTo="PlacementJnt_Ankle_R")
    Color.setColor("PlacementCtrl_Fk_Ankle_R", "red")
    setShapeSize("PlacementCtrl_Fk_Ankle_R", 2)
    cmds.parent("PlacementCtrl_Fk_Ankle_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Ball_R
    PlacementCtrl_Fk_Ball_R = cmds.circle(name="PlacementCtrl_Fk_Ball_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Ball_R", [-7.7, 3, 7.7], [-65.46, 0, 0], [7, 7, 7] , settings, snapTo="PlacementJnt_Ball_R")
    Color.setColor("PlacementCtrl_Fk_Ball_R", "red")
    setShapeSize("PlacementCtrl_Fk_Ball_R", 2)
    cmds.parent("PlacementCtrl_Fk_Ball_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Foot_R
    PlacementCtrl_Foot_R = Controllers.createController("Foot/foot", "PlacementCtrl_Foot_R")
    transformRelative("PlacementCtrl_Foot_R", [-7.9, 0, 6.497], [0, 0, 0], [8.6, 7, 6.8] , settings , snapTo="PlacementJnt_Ankle_R")
    Color.setColor("PlacementCtrl_Foot_R", "red")
    setShapeSize("PlacementCtrl_Foot_R", 2)
    cmds.parent("PlacementCtrl_Foot_R", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Pv_Leg_R
    PlacementCtrl_Pv_Leg_R = Controllers.createController("3D_Shapes/corner" , "PlacementCtrl_Pv_Leg_R")
    transformRelative("PlacementCtrl_Pv_Leg_R", [-9, 50, 38], [-90, 0, 0], [1, 1, 1] , settings , snapTo="PlacementJnt_Knee_L")
    Color.setColor("PlacementCtrl_Pv_Leg_R", "red")
    cmds.parent("PlacementCtrl_Pv_Leg_R", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Ribbon_Leg_R
    PlacementCtrl_Ribbon_Leg_R = cmds.circle(name="PlacementCtrl_Ribbon_Leg_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Leg_R", [-9.621, 67, -0.8], [0, 0, 0], [8.4, 8.4, 8.4] , settings, snapTo="PlacementJnt_Hip_L")
    Color.setColor("PlacementCtrl_Ribbon_Leg_R", "red")
    cmds.parent("PlacementCtrl_Ribbon_Leg_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Ribbon_Knee_R
    PlacementCtrl_Ribbon_Knee_R = cmds.circle(name="PlacementCtrl_Ribbon_Knee_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Knee_R", [-8.677, 30, -4], [0, 0, 0], [6.4, 6.4, 6.4] , settings, snapTo="PlacementJnt_Knee_R")
    Color.setColor("PlacementCtrl_Ribbon_Knee_R", "red")
    cmds.parent("PlacementCtrl_Ribbon_Knee_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Pin_Knee_R
    PlacementCtrl_Pin_Knee_R = cmds.circle(name="PlacementCtrl_Pin_Knee_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Pin_Knee_R", [-8.677, 49, -1.5], [0, 0, 0], [5.4, 5.4, 5.4] , settings, snapTo="PlacementJnt_Knee_R")
    Color.setColor("PlacementCtrl_Pin_Knee_R", "red")
    cmds.parent("PlacementCtrl_Pin_Knee_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")


    ##############################
    ###  CONTROLLERS LEFT LEG  ###
    ##############################

    # PlacementCtrl_Fk_Leg_L
    PlacementCtrl_Fk_Leg_L = cmds.circle(name="PlacementCtrl_Fk_Leg_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Leg_L", [9.621, 82.611, -1.5], [0, 0, 0], [10, 10, 10] , settings, snapTo="PlacementJnt_Hip_L")
    Color.setColor("PlacementCtrl_Fk_Leg_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Leg_L", 2)
    cmds.parent("PlacementCtrl_Fk_Leg_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Knee_L
    PlacementCtrl_Fk_Knee_L = cmds.circle(name="PlacementCtrl_Fk_Knee_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Knee_L", [8.677, 49, -1.5], [0, 0, 0], [7.2, 7.2, 7.2] , settings, snapTo="PlacementJnt_Knee_L")
    Color.setColor("PlacementCtrl_Fk_Knee_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Knee_L", 2)
    cmds.parent("PlacementCtrl_Fk_Knee_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Ankle_L
    PlacementCtrl_Fk_Ankle_L = cmds.circle(name="PlacementCtrl_Fk_Ankle_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Ankle_L", [7.324, 12.9, 0], [0, 0, 0], [7, 7, 7] , settings, snapTo="PlacementJnt_Ankle_L")
    Color.setColor("PlacementCtrl_Fk_Ankle_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Ankle_L", 2)
    cmds.parent("PlacementCtrl_Fk_Ankle_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Ball_L
    PlacementCtrl_Fk_Ball_L = cmds.circle(name="PlacementCtrl_Fk_Ball_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Ball_L", [7.7, 3, 7.7], [-65.46, 0, 0], [7, 7, 7] , settings, snapTo="PlacementJnt_Ball_L")
    Color.setColor("PlacementCtrl_Fk_Ball_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Ball_L", 2)
    cmds.parent("PlacementCtrl_Fk_Ball_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Foot_L
    PlacementCtrl_Foot_L = Controllers.createController("Foot/foot", "PlacementCtrl_Foot_L")
    transformRelative("PlacementCtrl_Foot_L", [7.9, 0, 6.497], [0, 0, 0], [8.6, 7, 6.8] , settings, snapTo="PlacementJnt_Ankle_L")
    Color.setColor("PlacementCtrl_Foot_L", "turquoise")
    setShapeSize("PlacementCtrl_Foot_L", 2)
    cmds.parent("PlacementCtrl_Foot_L", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Pv_Leg_L
    PlacementCtrl_Pv_Leg_L = Controllers.createController("3D_Shapes/corner", "PlacementCtrl_Pv_Leg_L")
    transformRelative("PlacementCtrl_Pv_Leg_L", [9, 50, 38], [-90, 0, 0], [1, 1, 1] , settings, snapTo="PlacementJnt_Knee_L")
    Color.setColor("PlacementCtrl_Pv_Leg_L", "turquoise")
    cmds.parent("PlacementCtrl_Pv_Leg_L", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Ribbon_Leg_L
    PlacementCtrl_Ribbon_Leg_L = cmds.circle(name="PlacementCtrl_Ribbon_Leg_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Leg_L", [9.621, 67, -0.8], [0, 0, 0], [8.4, 8.4, 8.4] , settings, snapTo="PlacementJnt_Hip_L")
    Color.setColor("PlacementCtrl_Ribbon_Leg_L", "turquoise")
    cmds.parent("PlacementCtrl_Ribbon_Leg_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Ribbon_Knee_L
    PlacementCtrl_Ribbon_Knee_L = cmds.circle(name="PlacementCtrl_Ribbon_Knee_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Knee_L", [8.677, 30, -4], [0, 0, 0], [6.4, 6.4, 6.4] , settings, snapTo="PlacementJnt_Knee_L")
    Color.setColor("PlacementCtrl_Ribbon_Knee_L", "turquoise")
    cmds.parent("PlacementCtrl_Ribbon_Knee_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Pin_Knee_L
    PlacementCtrl_Pin_Knee_L = cmds.circle(name="PlacementCtrl_Pin_Knee_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Pin_Knee_L", [8.677, 49, -1.5], [0, 0, 0], [5.4, 5.4, 5.4] , settings, snapTo="PlacementJnt_Knee_L")
    Color.setColor("PlacementCtrl_Pin_Knee_L", "turquoise")
    cmds.parent("PlacementCtrl_Pin_Knee_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")




# Place the controllers for the arms
# - PlacementCtrl_Clavicle_L
# - PlacementCtrl_Clavicle_R
# - PlacementCtrl_Fk_Shouder_R
# - PlacementCtrl_Fk_Elbow_R
# - PlacementCtrl_Fk_Wrist_R
# - PlacementCtrl_Fk_Shoulder_L
# - PlacementCtrl_Fk_Elbow_L
# - PlacementCtrl_Fk_Wrist_L
# - PlacementCtrl_Ik_Arm_R
# - PlacementCtrl_Ik_Arm_L
# - PlacementCtrl_Pv_Arm_R
# - PlacementCtrl_Pv_Arm_L
# - PlacementCtrl_Ribbon_Arm_R
# - PlacementCtrl_Ribbon_Arm_L
# - PlacementCtrl_Ribbon_Elbow_R
# - PlacementCtrl_Ribbon_Elbow_L
# - PlacementCtrl_Pin_Elbow_R
# - PlacementCtrl_Pin_Elbow_L
# region Arms Controllers
def placeArmsControllers(settings):
    ###############################
    ###  CONTROLLERS RIGHT ARM  ###
    ###############################

    # PlacementCtrl_Clavicle_R
    PlacementCtrl_Clavicle_R = Controllers.createController("3D_Shapes/boat", "PlacementCtrl_Clavicle_R")
    transformRelative("PlacementCtrl_Clavicle_R", [-12, 132, -5.4], [0, 0, 15], [5, 5, 4.5] , settings, snapTo="PlacementJnt_Clavicle_R")
    Color.setColor("PlacementCtrl_Clavicle_R", "red")
    cmds.parent("PlacementCtrl_Clavicle_R", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Fk_Shoulder_R
    PlacementCtrl_Fk_Shoulder_R = cmds.circle(name="PlacementCtrl_Fk_Shoulder_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Shoulder_R", [-16.5, 130, -5.2], [0, 0, -58.2], [6.5, 6.5, 6.5] , settings, snapTo="PlacementJnt_Arm_R")
    Color.setColor("PlacementCtrl_Fk_Shoulder_R", "red")
    setShapeSize("PlacementCtrl_Fk_Shoulder_R", 2)
    cmds.parent("PlacementCtrl_Fk_Shoulder_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Elbow_R
    PlacementCtrl_Fk_Elbow_R = cmds.circle(name="PlacementCtrl_Fk_Elbow_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Elbow_R", [-30,116,-8.4], [0, 0, -51], [6, 6, 6] , settings, snapTo="PlacementJnt_Elbow_R")
    Color.setColor("PlacementCtrl_Fk_Elbow_R", "red")
    setShapeSize("PlacementCtrl_Fk_Elbow_R", 2)
    cmds.parent("PlacementCtrl_Fk_Elbow_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Wrist_R
    PlacementCtrl_Fk_Wrist_R = cmds.circle(name="PlacementCtrl_Fk_Wrist_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Wrist_R", [-49,98,-4], [-12.4, 0.7,-47], [-3.7, 3.7, 3.7] , settings , snapTo="PlacementJnt_Wrist_R")
    Color.setColor("PlacementCtrl_Fk_Wrist_R", "red")
    setShapeSize("PlacementCtrl_Fk_Wrist_R", 2)
    cmds.parent("PlacementCtrl_Fk_Wrist_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Ik_Arm_R
    PlacementCtrl_Ik_Arm_R = cmds.circle(name="PlacementCtrl_Ik_Arm_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ik_Arm_R", [-49,98,-4], [-12.4, 0.7,-47], [-3.7, 3.7, 3.7] , settings , snapTo="PlacementJnt_Wrist_R")
    Color.setColor("PlacementCtrl_Ik_Arm_R", "red")
    setShapeSize("PlacementCtrl_Ik_Arm_R", 2)
    cmds.parent("PlacementCtrl_Ik_Arm_R", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Pv_Arm_R
    PlacementCtrl_Pv_Arm_R = Controllers.createController("3D_Shapes/corner", "PlacementCtrl_Pv_Arm_R")
    transformRelative("PlacementCtrl_Pv_Arm_R", [-29, 116, -34], [-90, 180, 0], [1, 1, 1] , settings, snapTo="PlacementJnt_Elbow_R")
    Color.setColor("PlacementCtrl_Pv_Arm_R", "red")
    cmds.parent("PlacementCtrl_Pv_Arm_R", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Ribbon_Arm_R
    PlacementCtrl_Ribbon_Arm_R = cmds.circle(name="PlacementCtrl_Ribbon_Arm_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Arm_R", [-22, 123,-6.5], [7.1,0,-51], [6, 6, 6] , settings, snapTo="PlacementJnt_Arm_R")
    Color.setColor("PlacementCtrl_Ribbon_Arm_R", "red")
    cmds.parent("PlacementCtrl_Ribbon_Arm_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Ribbon_Elbow_R
    PlacementCtrl_Ribbon_Elbow_R = cmds.circle(name="PlacementCtrl_Ribbon_Elbow_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Elbow_R", [-40, 106 , -6.5], [-6, 0 , -51], [5, 5, 5] , settings, snapTo="PlacementJnt_Elbow_R")
    Color.setColor("PlacementCtrl_Ribbon_Elbow_R", "red")
    cmds.parent("PlacementCtrl_Ribbon_Elbow_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Pin_Elbow_R
    PlacementCtrl_Pin_Elbow_R = cmds.circle(name="PlacementCtrl_Pin_Elbow_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Pin_Elbow_R", [-30,116,-8.4], [0, 0, -51], [5.2, 5.2, 5.2] , settings, snapTo="PlacementJnt_Elbow_R")
    Color.setColor("PlacementCtrl_Pin_Elbow_R", "red")
    cmds.parent("PlacementCtrl_Pin_Elbow_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")


    ##############################
    ###  CONTROLLERS LEFT ARM  ###
    ##############################
    
    # PlacementCtrl_Clavicle_L
    PlacementCtrl_Clavicle_L = Controllers.createController("3D_Shapes/boat", "PlacementCtrl_Clavicle_L")
    transformRelative("PlacementCtrl_Clavicle_L", [12, 132, -5.4], [0, 0, -15], [5, 5, 4.5] , settings, snapTo="PlacementJnt_Clavicle_L")
    Color.setColor("PlacementCtrl_Clavicle_L", "turquoise")
    cmds.parent("PlacementCtrl_Clavicle_L", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Fk_Shoulder_L
    PlacementCtrl_Fk_Shoulder_L = cmds.circle(name="PlacementCtrl_Fk_Shoulder_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Shoulder_L", [16.5, 130, -5.2], [0, 0, 58.2], [6.5, 6.5, 6.5] , settings, snapTo="PlacementJnt_Arm_L")
    Color.setColor("PlacementCtrl_Fk_Shoulder_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Shoulder_L", 2)
    cmds.parent("PlacementCtrl_Fk_Shoulder_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Elbow_L
    PlacementCtrl_Fk_Elbow_L = cmds.circle(name="PlacementCtrl_Fk_Elbow_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Elbow_L", [30, 116, -8.4], [0, 0, 51], [6, 6, 6] , settings, snapTo="PlacementJnt_Elbow_L")
    Color.setColor("PlacementCtrl_Fk_Elbow_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Elbow_L", 2)
    cmds.parent("PlacementCtrl_Fk_Elbow_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Wrist_L
    PlacementCtrl_Fk_Wrist_L = cmds.circle(name="PlacementCtrl_Fk_Wrist_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Wrist_L", [49, 98, -4], [12.4, -0.7, 47], [3.7, 3.7, 3.7] , settings, snapTo="PlacementJnt_Wrist_L")
    Color.setColor("PlacementCtrl_Fk_Wrist_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Wrist_L", 2)
    cmds.parent("PlacementCtrl_Fk_Wrist_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Ik_Arm_L
    PlacementCtrl_Ik_Arm_L = cmds.circle(name="PlacementCtrl_Ik_Arm_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ik_Arm_L", [49, 98, -4], [12.4, -0.7, 47], [3.7, 3.7, 3.7] , settings, snapTo="PlacementJnt_Wrist_L")
    Color.setColor("PlacementCtrl_Ik_Arm_L", "turquoise")
    setShapeSize("PlacementCtrl_Ik_Arm_L", 2)
    cmds.parent("PlacementCtrl_Ik_Arm_L", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Pv_Arm_L
    PlacementCtrl_Pv_Arm_L = Controllers.createController("3D_Shapes/corner", "PlacementCtrl_Pv_Arm_L")
    transformRelative("PlacementCtrl_Pv_Arm_L", [29, 116, -34], [-90, 180, 0], [1, 1, 1] , settings, snapTo="PlacementJnt_Elbow_L")
    Color.setColor("PlacementCtrl_Pv_Arm_L", "turquoise")
    cmds.parent("PlacementCtrl_Pv_Arm_L", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Ribbon_Arm_L
    PlacementCtrl_Ribbon_Arm_L = cmds.circle(name="PlacementCtrl_Ribbon_Arm_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Arm_L", [22, 123, -6.5], [-7.1, 0, 51], [6, 6, 6] , settings, snapTo="PlacementJnt_Arm_L")
    Color.setColor("PlacementCtrl_Ribbon_Arm_L", "turquoise")
    cmds.parent("PlacementCtrl_Ribbon_Arm_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Ribbon_Elbow_L
    PlacementCtrl_Ribbon_Elbow_L = cmds.circle(name="PlacementCtrl_Ribbon_Elbow_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Elbow_L", [40, 106, -6.5], [6, 0, 51], [5, 5, 5] , settings, snapTo="PlacementJnt_Elbow_L")
    Color.setColor("PlacementCtrl_Ribbon_Elbow_L", "turquoise")
    cmds.parent("PlacementCtrl_Ribbon_Elbow_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Pin_Elbow_L
    PlacementCtrl_Pin_Elbow_L = cmds.circle(name="PlacementCtrl_Pin_Elbow_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Pin_Elbow_L", [30, 116, -8.4], [0, 0, 51], [5.2, 5.2, 5.2] , settings, snapTo="PlacementJnt_Elbow_L")
    Color.setColor("PlacementCtrl_Pin_Elbow_L", "turquoise")
    cmds.parent("PlacementCtrl_Pin_Elbow_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")