#function to mirror the place the opposite CTRL a the mirror position of the source during the placement
import maya.cmds as cmds

def mirrorCtrl(Ctrl, side):
    Ctrl = Ctrl[:-1]
    Left = "L"
    Right = "R"
    if side == "R":
        Left = "R"
        Right = "L"
    translate = cmds.getAttr(f"{Ctrl}{Left}.t")
    cmds.setAttr(f"{Ctrl}{Right}.t", -1*translate[0][0], translate[0][1], translate[0][2])
    rotate = cmds.getAttr(f"{Ctrl}{Left}.r")
    cmds.setAttr(f"{Ctrl}{Right}.r", rotate[0][0], -1*rotate[0][1], -1*rotate[0][2])
    scale = cmds.getAttr(f"{Ctrl}{Left}.s")
    cmds.setAttr(f"{Ctrl}{Right}.s", scale[0][0], scale[0][1], scale[0][2])
    pass

def mirrorCtrlsLegLtoR():
    #CTRL IK
    mirrorCtrl("PlacementCtrl_Foot_L", "L")

    #CTRL FK
    mirrorCtrl("PlacementCtrl_Fk_Leg_L", "L")
    mirrorCtrl("PlacementCtrl_Fk_Knee_L", "L")
    mirrorCtrl("PlacementCtrl_Fk_Ankle_L", "L")
    mirrorCtrl("PlacementCtrl_Fk_Ball_L", "L")

    #Other
    mirrorCtrl("PlacementCtrl_Ribbon_Leg_L", "L")
    mirrorCtrl("PlacementCtrl_Pin_Knee_L", "L")
    mirrorCtrl("PlacementCtrl_Ribbon_Knee_L", "L")


def mirrorCtrlsLegRtoL():
    #CTRL IK
    mirrorCtrl("PlacementCtrl_Foot_L", "R")

    #CTRL FK
    mirrorCtrl("PlacementCtrl_Fk_Leg_L", "R")
    mirrorCtrl("PlacementCtrl_Fk_Knee_L", "R")
    mirrorCtrl("PlacementCtrl_Fk_Ankle_L", "R")
    mirrorCtrl("PlacementCtrl_Fk_Ball_L", "R")

    #Other
    mirrorCtrl("PlacementCtrl_Ribbon_Leg_L", "R")
    mirrorCtrl("PlacementCtrl_Pin_Knee_L", "R")
    mirrorCtrl("PlacementCtrl_Ribbon_Knee_L", "R")
    
def mirrorCtrlsArmLtoR():
    #CTRL IK
    mirrorCtrl("PlacementCtrl_Ik_Arm_L", "L")

    #CTRL FK
    mirrorCtrl("PlacementCtrl_Fk_Shoulder_L", "L")
    mirrorCtrl("PlacementCtrl_Fk_Elbow_L", "L")
    mirrorCtrl("PlacementCtrl_Fk_Wrist_L", "L")
    mirrorCtrl("PlacementCtrl_Clavicle_L", "L")

    #finger daaaaa...
    mirrorCtrl("PlacementCtrl_Finger_Index_Metacarpus_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Index_01_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Index_02_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Index_03_L", "L")

    mirrorCtrl("PlacementCtrl_Finger_Middle_Metacarpus_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Middle_01_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Middle_02_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Middle_03_L", "L")

    mirrorCtrl("PlacementCtrl_Finger_Pinky_Metacarpus_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Pinky_01_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Pinky_02_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Pinky_03_L", "L")

    mirrorCtrl("PlacementCtrl_Finger_Ring_Metacarpus_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Ring_01_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Ring_02_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Ring_03_L", "L")

    mirrorCtrl("PlacementCtrl_Finger_Thumb_Metacarpus_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Thumb_01_L", "L")
    mirrorCtrl("PlacementCtrl_Finger_Thumb_02_L", "L")

    #Other
    mirrorCtrl("PlacementCtrl_Ribbon_Arm_L", "L")
    mirrorCtrl("PlacementCtrl_Pin_Elbow_L", "L")
    mirrorCtrl("PlacementCtrl_Ribbon_Elbow_L", "L")

    
def mirrorCtrlsArmRtoL():
    #CTRL IK
    mirrorCtrl("PlacementCtrl_Ik_Arm_L", "R")

    #CTRL FK
    mirrorCtrl("PlacementCtrl_Fk_Shoulder_L", "R")
    mirrorCtrl("PlacementCtrl_Fk_Elbow_L", "R")
    mirrorCtrl("PlacementCtrl_Fk_Wrist_L", "R")
    mirrorCtrl("PlacementCtrl_Clavicle_L", "R")

    #finger daaaaa...
    mirrorCtrl("PlacementCtrl_Finger_Index_Metacarpus_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Index_01_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Index_02_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Index_03_L", "R")

    mirrorCtrl("PlacementCtrl_Finger_Middle_Metacarpus_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Middle_01_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Middle_02_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Middle_03_L", "R")

    mirrorCtrl("PlacementCtrl_Finger_Pinky_Metacarpus_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Pinky_01_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Pinky_02_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Pinky_03_L", "R")

    mirrorCtrl("PlacementCtrl_Finger_Ring_Metacarpus_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Ring_01_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Ring_02_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Ring_03_L", "R")

    mirrorCtrl("PlacementCtrl_Finger_Thumb_Metacarpus_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Thumb_01_L", "R")
    mirrorCtrl("PlacementCtrl_Finger_Thumb_02_L", "R")

    #Other
    mirrorCtrl("PlacementCtrl_Ribbon_Arm_L", "R")
    mirrorCtrl("PlacementCtrl_Pin_Elbow_L", "R")
    mirrorCtrl("PlacementCtrl_Ribbon_Elbow_L", "R")
