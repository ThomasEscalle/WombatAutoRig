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


def transformRelative(controller, position = [0,0,0], rotation = [0,0,0], scale = [1, 1, 1] , settings = None):
    goodPos = AutorigHelper.resizeCtrl(bbox = settings["bbox"] , size = position)
    goodScale = AutorigHelper.resizeCtrl(bbox = settings["bbox"] , size = scale)


    cmds.setAttr(controller + ".translate", goodPos[0], goodPos[1], goodPos[2] , settings)
    cmds.setAttr(controller + ".rotate", rotation[0], rotation[1], rotation[2] , settings)
    cmds.setAttr(controller + ".scale", goodScale[0], goodScale[1], goodScale[2] , settings)

def setShapeSize(controller, size):
    shapes = cmds.listRelatives(controller, shapes=True)
    for shape in shapes:
        cmds.setAttr(shape + ".lineWidth", size)




def placeControllers(settings):
    print("Place the controllers")
    

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
    # PlacementJnt_Pimky_Metacarpus_R
    ctrl_05 = createFingerController("PlacementCtrl_Finger_Pinky_Metacarpus_R", "PlacementJnt_Pimky_Metacarpus_R", settings)


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
    ctrl_05_01 = createFingerController("PlacementCtrl_Finger_Pinky_01_R", "PlacementJnt_Pimky_01_R", settings)
    # PlacementJnt_Pinky_02_R
    ctrl_05_02 = createFingerController("PlacementCtrl_Finger_Pinky_02_R", "PlacementJnt_Pimky_02_R", settings)
    # PlacementJnt_Pinky_03_R
    ctrl_05_03 = createFingerController("PlacementCtrl_Finger_Pinky_03_R", "PlacementJnt_Pimky_03_R", settings)


    # region LEFT FINGERS

    # PlacementJnt_Thumb_Metacarpus_L
    ctrl_06 = createFingerController("PlacementCtrl_Finger_Thumb_Metacarpus_L", "PlacementJnt_Thumb_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Index_Metacarpus_L
    ctrl_07 = createFingerController("PlacementCtrl_Finger_Index_Metacarpus_L", "PlacementJnt_Index_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Middle_Metacarpus_L
    ctrl_08 = createFingerController("PlacementCtrl_Finger_Middle_Metacarpus_L", "PlacementJnt_Middle_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Ring_Metacarpus_L
    ctrl_09 = createFingerController("PlacementCtrl_Finger_Ring_Metacarpus_L", "PlacementJnt_Ring_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Pimky_Metacarpus_L
    ctrl_10 = createFingerController("PlacementCtrl_Finger_Pinky_Metacarpus_L", "PlacementJnt_Pimky_Metacarpus_L", settings, rotation=[90, 90, 0], color="turquoise")


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
    ctrl_10_01 = createFingerController("PlacementCtrl_Finger_Pinky_01_L", "PlacementJnt_Pimky_01_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Pinky_02_L
    ctrl_10_02 = createFingerController("PlacementCtrl_Finger_Pinky_02_L", "PlacementJnt_Pimky_02_L", settings, rotation=[90, 90, 0], color="turquoise")
    # PlacementJnt_Pinky_03_L
    ctrl_10_03 = createFingerController("PlacementCtrl_Finger_Pinky_03_L", "PlacementJnt_Pimky_03_L", settings, rotation=[90, 90, 0], color="turquoise")







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
def placeGlobalControllers(settings) :
    # PlacementCtrl_Global
    PlacementCtrl_Global = Controllers.createController("2D_Shapes/star", "PlacementCtrl_Global")
    transformRelative("PlacementCtrl_Global", [0, 1, 0], [0, 0, 0], [65, 65, 65] , settings)
    setShapeSize("PlacementCtrl_Global", 2)
    Color.setColor("PlacementCtrl_Global", "yellow")
    cmds.parent("PlacementCtrl_Global", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Root
    PlacementCtrl_Root = cmds.circle(name="PlacementCtrl_Root", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Root", [0, 87, -1.7], [0, 0, 0], [20, 20, 16] , settings)
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
# - PlacementCtrl_Neck_01
# - PlacementCtrl_Spine_01
def placeSpineControllers(settings) :

    # PlacementCtrl_Hip
    PlacementCtrl_Hip = Controllers.createController("3D_Shapes/boat", "PlacementCtrl_Hip")
    transformRelative("PlacementCtrl_Hip", [0, 101, -2.0], [180, 90, 0], [14.6, 8, 8.2] , settings)
    Color.setColor("PlacementCtrl_Hip", "chocolate")
    cmds.parent("PlacementCtrl_Hip", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Shoulder
    PlacementCtrl_Shoulder = Controllers.createController("3D_Shapes/tube", "PlacementCtrl_Shoulder")
    transformRelative("PlacementCtrl_Shoulder", [0, 118, 0.5], [-4, 0, 0], [2.5, 1.2, 2.5] , settings)
    setShapeSize("PlacementCtrl_Shoulder", 2)
    Color.setColor("PlacementCtrl_Shoulder", "yellow")
    cmds.parent("PlacementCtrl_Shoulder", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Neck_01
    PlacementCtrl_Neck_01 = cmds.circle(name="PlacementCtrl_Neck_01", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Neck_01", [0, 140, -3.4], [0, 0, 0], [7.7, 7.7, 7.7] , settings)
    setShapeSize("PlacementCtrl_Neck_01", 2)
    Color.setColor("PlacementCtrl_Neck_01", "yellow")
    cmds.parent("PlacementCtrl_Neck_01", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Spine_01
    PlacementCtrl_Spine_01 = cmds.circle(name="PlacementCtrl_Spine_01", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Spine_01", [0, 107, 2], [0, 0, 0], [14.7, 14.7, 12.7] , settings)
    Color.setColor("PlacementCtrl_Spine_01", "chocolate")
    cmds.parent("PlacementCtrl_Spine_01", "AutoRig_Data|ControllersPlacement|Global_Controllers")



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
def placeLegsControllers(settings) :
    ###############################
    ###  CONTROLLERS RIGHT LEG  ###
    ###############################

    # PlacementCtrl_Fk_Leg_R
    PlacementCtrl_Fk_Leg_R = cmds.circle(name="PlacementCtrl_Fk_Leg_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Leg_R", [-9.621,82.611, -1.5], [0, 0, 0], [10, 10, 10] , settings)
    Color.setColor("PlacementCtrl_Fk_Leg_R", "red")
    setShapeSize("PlacementCtrl_Fk_Leg_R", 2)
    cmds.parent("PlacementCtrl_Fk_Leg_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Knee_R
    PlacementCtrl_Fk_Knee_R = cmds.circle(name="PlacementCtrl_Fk_Knee_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Knee_R", [-8.677, 49, -1.5], [0, 0, 0], [7.2, 7.2, 7.2] , settings)
    Color.setColor("PlacementCtrl_Fk_Knee_R", "red")
    setShapeSize("PlacementCtrl_Fk_Knee_R", 2)
    cmds.parent("PlacementCtrl_Fk_Knee_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Ankle_R
    PlacementCtrl_Fk_Ankle_R = cmds.circle(name="PlacementCtrl_Fk_Ankle_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Ankle_R", [-7.324, 12.9, 0], [0, 0, 0], [7, 7, 7] , settings)
    Color.setColor("PlacementCtrl_Fk_Ankle_R", "red")
    setShapeSize("PlacementCtrl_Fk_Ankle_R", 2)
    cmds.parent("PlacementCtrl_Fk_Ankle_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Ball_R
    PlacementCtrl_Fk_Ball_R = cmds.circle(name="PlacementCtrl_Fk_Ball_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Ball_R", [-7.7, 3, 7.7], [-65.46, 0, 0], [7, 7, 7] , settings)
    Color.setColor("PlacementCtrl_Fk_Ball_R", "red")
    setShapeSize("PlacementCtrl_Fk_Ball_R", 2)
    cmds.parent("PlacementCtrl_Fk_Ball_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Foot_R
    PlacementCtrl_Foot_R = Controllers.createController("Foot/foot", "PlacementCtrl_Foot_R")
    transformRelative("PlacementCtrl_Foot_R", [-7.9, 0, 6.497], [0, 0, 0], [8.6, 7, 6.8] , settings)
    Color.setColor("PlacementCtrl_Foot_R", "red")
    setShapeSize("PlacementCtrl_Foot_R", 2)
    cmds.parent("PlacementCtrl_Foot_R", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Pv_Leg_R
    PlacementCtrl_Pv_Leg_R = Controllers.createController("3D_Shapes/corner" , "PlacementCtrl_Pv_Leg_R")
    transformRelative("PlacementCtrl_Pv_Leg_R", [-9, 50, 38], [-90, 0, 0], [1, 1, 1] , settings)
    Color.setColor("PlacementCtrl_Pv_Leg_R", "red")
    cmds.parent("PlacementCtrl_Pv_Leg_R", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Ribbon_Leg_R
    PlacementCtrl_Ribbon_Leg_R = cmds.circle(name="PlacementCtrl_Ribbon_Leg_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Leg_R", [-9.621, 67, -0.8], [0, 0, 0], [8.4, 8.4, 8.4] , settings)
    Color.setColor("PlacementCtrl_Ribbon_Leg_R", "red")
    cmds.parent("PlacementCtrl_Ribbon_Leg_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Ribbon_Knee_R
    PlacementCtrl_Ribbon_Knee_R = cmds.circle(name="PlacementCtrl_Ribbon_Knee_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Knee_R", [-8.677, 30, -4], [0, 0, 0], [6.4, 6.4, 6.4] , settings)
    Color.setColor("PlacementCtrl_Ribbon_Knee_R", "red")
    cmds.parent("PlacementCtrl_Ribbon_Knee_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Pin_Knee_R
    PlacementCtrl_Pin_Knee_R = cmds.circle(name="PlacementCtrl_Pin_Knee_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Pin_Knee_R", [-8.677, 49, -1.5], [0, 0, 0], [5.4, 5.4, 5.4] , settings)
    Color.setColor("PlacementCtrl_Pin_Knee_R", "red")
    cmds.parent("PlacementCtrl_Pin_Knee_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")


    ##############################
    ###  CONTROLLERS LEFT LEG  ###
    ##############################

    # PlacementCtrl_Fk_Leg_L
    PlacementCtrl_Fk_Leg_L = cmds.circle(name="PlacementCtrl_Fk_Leg_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Leg_L", [9.621, 82.611, -1.5], [0, 0, 0], [10, 10, 10] , settings)
    Color.setColor("PlacementCtrl_Fk_Leg_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Leg_L", 2)
    cmds.parent("PlacementCtrl_Fk_Leg_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Knee_L
    PlacementCtrl_Fk_Knee_L = cmds.circle(name="PlacementCtrl_Fk_Knee_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Knee_L", [8.677, 49, -1.5], [0, 0, 0], [7.2, 7.2, 7.2] , settings)
    Color.setColor("PlacementCtrl_Fk_Knee_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Knee_L", 2)
    cmds.parent("PlacementCtrl_Fk_Knee_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Ankle_L
    PlacementCtrl_Fk_Ankle_L = cmds.circle(name="PlacementCtrl_Fk_Ankle_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Ankle_L", [7.324, 12.9, 0], [0, 0, 0], [7, 7, 7] , settings)
    Color.setColor("PlacementCtrl_Fk_Ankle_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Ankle_L", 2)
    cmds.parent("PlacementCtrl_Fk_Ankle_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Ball_L
    PlacementCtrl_Fk_Ball_L = cmds.circle(name="PlacementCtrl_Fk_Ball_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Ball_L", [7.7, 3, 7.7], [-65.46, 0, 0], [7, 7, 7] , settings)
    Color.setColor("PlacementCtrl_Fk_Ball_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Ball_L", 2)
    cmds.parent("PlacementCtrl_Fk_Ball_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Foot_L
    PlacementCtrl_Foot_L = Controllers.createController("Foot/foot", "PlacementCtrl_Foot_L")
    transformRelative("PlacementCtrl_Foot_L", [7.9, 0, 6.497], [0, 0, 0], [8.6, 7, 6.8] , settings)
    Color.setColor("PlacementCtrl_Foot_L", "turquoise")
    setShapeSize("PlacementCtrl_Foot_L", 2)
    cmds.parent("PlacementCtrl_Foot_L", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Pv_Leg_L
    PlacementCtrl_Pv_Leg_L = Controllers.createController("3D_Shapes/corner", "PlacementCtrl_Pv_Leg_L")
    transformRelative("PlacementCtrl_Pv_Leg_L", [9, 50, 38], [-90, 0, 0], [1, 1, 1] , settings)
    Color.setColor("PlacementCtrl_Pv_Leg_L", "turquoise")
    cmds.parent("PlacementCtrl_Pv_Leg_L", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Ribbon_Leg_L
    PlacementCtrl_Ribbon_Leg_L = cmds.circle(name="PlacementCtrl_Ribbon_Leg_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Leg_L", [9.621, 67, -0.8], [0, 0, 0], [8.4, 8.4, 8.4] , settings)
    Color.setColor("PlacementCtrl_Ribbon_Leg_L", "turquoise")
    cmds.parent("PlacementCtrl_Ribbon_Leg_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Ribbon_Knee_L
    PlacementCtrl_Ribbon_Knee_L = cmds.circle(name="PlacementCtrl_Ribbon_Knee_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Knee_L", [8.677, 30, -4], [0, 0, 0], [6.4, 6.4, 6.4] , settings)
    Color.setColor("PlacementCtrl_Ribbon_Knee_L", "turquoise")
    cmds.parent("PlacementCtrl_Ribbon_Knee_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Pin_Knee_L
    PlacementCtrl_Pin_Knee_L = cmds.circle(name="PlacementCtrl_Pin_Knee_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Pin_Knee_L", [8.677, 49, -1.5], [0, 0, 0], [5.4, 5.4, 5.4] , settings)
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
def placeArmsControllers(settings):
    ###############################
    ###  CONTROLLERS RIGHT ARM  ###
    ###############################

    # PlacementCtrl_Clavicle_R
    PlacementCtrl_Clavicle_R = Controllers.createController("3D_Shapes/boat", "PlacementCtrl_Clavicle_R")
    transformRelative("PlacementCtrl_Clavicle_R", [-12, 132, -5.4], [0, 0, 15], [5, 5, 4.5] , settings)
    Color.setColor("PlacementCtrl_Clavicle_R", "red")
    cmds.parent("PlacementCtrl_Clavicle_R", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Fk_Shoulder_R
    PlacementCtrl_Fk_Shoulder_R = cmds.circle(name="PlacementCtrl_Fk_Shoulder_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Shoulder_R", [-16.5, 130, -5.2], [0, 0, -58.2], [6.5, 6.5, 6.5] , settings)
    Color.setColor("PlacementCtrl_Fk_Shoulder_R", "red")
    setShapeSize("PlacementCtrl_Fk_Shoulder_R", 2)
    cmds.parent("PlacementCtrl_Fk_Shoulder_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Elbow_R
    PlacementCtrl_Fk_Elbow_R = cmds.circle(name="PlacementCtrl_Fk_Elbow_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Elbow_R", [-30,116,-8.4], [0, 0, -51], [6, 6, 6] , settings)
    Color.setColor("PlacementCtrl_Fk_Elbow_R", "red")
    setShapeSize("PlacementCtrl_Fk_Elbow_R", 2)
    cmds.parent("PlacementCtrl_Fk_Elbow_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Wrist_R
    PlacementCtrl_Fk_Wrist_R = cmds.circle(name="PlacementCtrl_Fk_Wrist_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Wrist_R", [-49,98,-4], [-12.4, 0.7,-47], [-3.7, 3.7, 3.7] , settings)
    Color.setColor("PlacementCtrl_Fk_Wrist_R", "red")
    setShapeSize("PlacementCtrl_Fk_Wrist_R", 2)
    cmds.parent("PlacementCtrl_Fk_Wrist_R", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Ik_Arm_R
    PlacementCtrl_Ik_Arm_R = cmds.circle(name="PlacementCtrl_Ik_Arm_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ik_Arm_R", [-49,98,-4], [-12.4, 0.7,-47], [-3.7, 3.7, 3.7] , settings)
    Color.setColor("PlacementCtrl_Ik_Arm_R", "red")
    setShapeSize("PlacementCtrl_Ik_Arm_R", 2)
    cmds.parent("PlacementCtrl_Ik_Arm_R", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Pv_Arm_R
    PlacementCtrl_Pv_Arm_R = Controllers.createController("3D_Shapes/corner", "PlacementCtrl_Pv_Arm_R")
    transformRelative("PlacementCtrl_Pv_Arm_R", [-29, 116, -34], [-90, 180, 0], [1, 1, 1] , settings)
    Color.setColor("PlacementCtrl_Pv_Arm_R", "red")
    cmds.parent("PlacementCtrl_Pv_Arm_R", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Ribbon_Arm_R
    PlacementCtrl_Ribbon_Arm_R = cmds.circle(name="PlacementCtrl_Ribbon_Arm_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Arm_R", [-22, 123,-6.5], [7.1,0,-51], [6, 6, 6] , settings)
    Color.setColor("PlacementCtrl_Ribbon_Arm_R", "red")
    cmds.parent("PlacementCtrl_Ribbon_Arm_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Ribbon_Elbow_R
    PlacementCtrl_Ribbon_Elbow_R = cmds.circle(name="PlacementCtrl_Ribbon_Elbow_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Elbow_R", [-40, 106 , -6.5], [-6, 0 , -51], [5, 5, 5] , settings)
    Color.setColor("PlacementCtrl_Ribbon_Elbow_R", "red")
    cmds.parent("PlacementCtrl_Ribbon_Elbow_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Pin_Elbow_R
    PlacementCtrl_Pin_Elbow_R = cmds.circle(name="PlacementCtrl_Pin_Elbow_R", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Pin_Elbow_R", [-30,116,-8.4], [0, 0, -51], [5.2, 5.2, 5.2] , settings)
    Color.setColor("PlacementCtrl_Pin_Elbow_R", "red")
    cmds.parent("PlacementCtrl_Pin_Elbow_R", "AutoRig_Data|ControllersPlacement|Other_Controllers")


    ##############################
    ###  CONTROLLERS LEFT ARM  ###
    ##############################
    
    # PlacementCtrl_Clavicle_L
    PlacementCtrl_Clavicle_L = Controllers.createController("3D_Shapes/boat", "PlacementCtrl_Clavicle_L")
    transformRelative("PlacementCtrl_Clavicle_L", [12, 132, -5.4], [0, 0, -15], [5, 5, 4.5] , settings)
    Color.setColor("PlacementCtrl_Clavicle_L", "turquoise")
    cmds.parent("PlacementCtrl_Clavicle_L", "AutoRig_Data|ControllersPlacement|Global_Controllers")

    # PlacementCtrl_Fk_Shoulder_L
    PlacementCtrl_Fk_Shoulder_L = cmds.circle(name="PlacementCtrl_Fk_Shoulder_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Shoulder_L", [16.5, 130, -5.2], [0, 0, 58.2], [6.5, 6.5, 6.5] , settings)
    Color.setColor("PlacementCtrl_Fk_Shoulder_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Shoulder_L", 2)
    cmds.parent("PlacementCtrl_Fk_Shoulder_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Elbow_L
    PlacementCtrl_Fk_Elbow_L = cmds.circle(name="PlacementCtrl_Fk_Elbow_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Elbow_L", [30, 116, -8.4], [0, 0, 51], [6, 6, 6] , settings)
    Color.setColor("PlacementCtrl_Fk_Elbow_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Elbow_L", 2)
    cmds.parent("PlacementCtrl_Fk_Elbow_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Fk_Wrist_L
    PlacementCtrl_Fk_Wrist_L = cmds.circle(name="PlacementCtrl_Fk_Wrist_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Fk_Wrist_L", [49, 98, -4], [12.4, -0.7, 47], [3.7, 3.7, 3.7] , settings)
    Color.setColor("PlacementCtrl_Fk_Wrist_L", "turquoise")
    setShapeSize("PlacementCtrl_Fk_Wrist_L", 2)
    cmds.parent("PlacementCtrl_Fk_Wrist_L", "AutoRig_Data|ControllersPlacement|FK_Controllers")

    # PlacementCtrl_Ik_Arm_L
    PlacementCtrl_Ik_Arm_L = cmds.circle(name="PlacementCtrl_Ik_Arm_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ik_Arm_L", [49, 98, -4], [12.4, -0.7, 47], [3.7, 3.7, 3.7] , settings)
    Color.setColor("PlacementCtrl_Ik_Arm_L", "turquoise")
    setShapeSize("PlacementCtrl_Ik_Arm_L", 2)
    cmds.parent("PlacementCtrl_Ik_Arm_L", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Pv_Arm_L
    PlacementCtrl_Pv_Arm_L = Controllers.createController("3D_Shapes/corner", "PlacementCtrl_Pv_Arm_L")
    transformRelative("PlacementCtrl_Pv_Arm_L", [29, 116, -34], [-90, 0, 0], [1, 1, 1] , settings)
    Color.setColor("PlacementCtrl_Pv_Arm_L", "turquoise")
    cmds.parent("PlacementCtrl_Pv_Arm_L", "AutoRig_Data|ControllersPlacement|IK_Controllers")

    # PlacementCtrl_Ribbon_Arm_L
    PlacementCtrl_Ribbon_Arm_L = cmds.circle(name="PlacementCtrl_Ribbon_Arm_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Arm_L", [22, 123, -6.5], [-7.1, 0, 51], [6, 6, 6] , settings)
    Color.setColor("PlacementCtrl_Ribbon_Arm_L", "turquoise")
    cmds.parent("PlacementCtrl_Ribbon_Arm_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Ribbon_Elbow_L
    PlacementCtrl_Ribbon_Elbow_L = cmds.circle(name="PlacementCtrl_Ribbon_Elbow_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Ribbon_Elbow_L", [40, 106, -6.5], [6, 0, 51], [5, 5, 5] , settings)
    Color.setColor("PlacementCtrl_Ribbon_Elbow_L", "turquoise")
    cmds.parent("PlacementCtrl_Ribbon_Elbow_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")

    # PlacementCtrl_Pin_Elbow_L
    PlacementCtrl_Pin_Elbow_L = cmds.circle(name="PlacementCtrl_Pin_Elbow_L", normal=[0, 1, 0], radius=1)
    transformRelative("PlacementCtrl_Pin_Elbow_L", [30, 116, -8.4], [0, 0, 51], [5.2, 5.2, 5.2] , settings)
    Color.setColor("PlacementCtrl_Pin_Elbow_L", "turquoise")
    cmds.parent("PlacementCtrl_Pin_Elbow_L", "AutoRig_Data|ControllersPlacement|Other_Controllers")