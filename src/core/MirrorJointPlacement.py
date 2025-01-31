import maya.cmds as cmds


def mirrorJointLegLtoR():
    #Hip
    HipTrans = cmds.getAttr("PlacementJnt_Hip_L.translate")
    cmds.setAttr("PlacementJnt_Hip_R.translate", -HipTrans[0], HipTrans[1], HipTrans[2])

    HipRot = cmds.getAttr("PlacementJnt_Hip_L.rotate")
    cmds.setAttr("PlacementJnt_Hip_R.rotate", -HipRot[0], HipRot[1], -HipRot[2])

    #Leg
    KneeTrans = cmds.getAttr("PlacementJnt_Knee_L.translate")
    cmds.setAttr("PlacementJnt_Knee_R.translate", -KneeTrans[0], KneeTrans[1], KneeTrans[2])

    KneeRot = cmds.getAttr("PlacementJnt_Knee_L.rotate")
    cmds.setAttr("PlacementJnt_Knee_R.rotate", -KneeRot[0], KneeRot[1], -KneeRot[2])

    #Knee
    KneeTrans = cmds.getAttr("PlacementJnt_Knee_L.translate")
    cmds.setAttr("PlacementJnt_Knee_R.translate", -KneeTrans[0], KneeTrans[1], KneeTrans[2])

    KneeRot = cmds.getAttr("PlacementJnt_Knee_L.rotate")
    cmds.setAttr("PlacementJnt_Knee_R.rotate", -KneeRot[0], KneeRot[1], -KneeRot[2])

    #Ankle
    AnkleTrans = cmds.getAttr("PlacementJnt_Ankle_L.translate")
    cmds.setAttr("PlacementJnt_Ankle_R.translate", -AnkleTrans[0], AnkleTrans[1], AnkleTrans[2])

    AnkleRot = cmds.getAttr("PlacementJnt_Ankle_L.rotate")
    cmds.setAttr("PlacementJnt_Ankle_R.rotate", -AnkleRot[0], AnkleRot[1], -AnkleRot[2])

    #Ball
    BallTrans = cmds.getAttr("PlacementJnt_Ball_L.translate")
    cmds.setAttr("PlacementJnt_Ball_R.translate", -BallTrans[0], BallTrans[1], BallTrans[2])

    BallRot = cmds.getAttr("PlacementJnt_Ball_L.rotate")
    cmds.setAttr("PlacementJnt_Ball_R.rotate", -BallRot[0], BallRot[1], -BallRot[2])

    #Toe
    ToeTrans = cmds.getAttr("PlacementJnt_Toe_L.translate")
    cmds.setAttr("PlacementJnt_Toe_R.translate", -ToeTrans[0], ToeTrans[1], ToeTrans[2])

    ToeRot = cmds.getAttr("PlacementJnt_Toe_L.rotate")
    cmds.setAttr("PlacementJnt_Toe_R.rotate", -ToeRot[0], ToeRot[1], -ToeRot[2])

#Create the same function for the right leg

def mirrorJointLegRtoL():
    #Hip
    HipTrans = cmds.getAttr("PlacementJnt_Hip_R.translate")
    cmds.setAttr("PlacementJnt_Hip_L.translate", -HipTrans[0], HipTrans[1], HipTrans[2])

    HipRot = cmds.getAttr("PlacementJnt_Hip_R.rotate")
    cmds.setAttr("PlacementJnt_Hip_L.rotate", -HipRot[0], HipRot[1], -HipRot[2])

    #Leg
    KneeTrans = cmds.getAttr("PlacementJnt_Knee_R.translate")
    cmds.setAttr("PlacementJnt_Knee_L.translate", -KneeTrans[0], KneeTrans[1], KneeTrans[2])

    KneeRot = cmds.getAttr("PlacementJnt_Knee_R.rotate")
    cmds.setAttr("PlacementJnt_Knee_L.rotate", -KneeRot[0], KneeRot[1], -KneeRot[2])

    #Knee
    KneeTrans = cmds.getAttr("PlacementJnt_Knee_R.translate")
    cmds.setAttr("PlacementJnt_Knee_L.translate", -KneeTrans[0], KneeTrans[1], KneeTrans[2])

    KneeRot = cmds.getAttr("PlacementJnt_Knee_R.rotate")
    cmds.setAttr("PlacementJnt_Knee_L.rotate", -KneeRot[0], KneeRot[1], -KneeRot[2])

    #Ankle
    AnkleTrans = cmds.getAttr("PlacementJnt_Ankle_R.translate")
    cmds.setAttr("PlacementJnt_Ankle_L.translate", -AnkleTrans[0], AnkleTrans[1], AnkleTrans[2])

    AnkleRot = cmds.getAttr("PlacementJnt_Ankle_R.rotate")
    cmds.setAttr("PlacementJnt_Ankle_L.rotate", -AnkleRot[0], AnkleRot[1], -AnkleRot[2])

    #Ball
    BallTrans = cmds.getAttr("PlacementJnt_Ball_R.translate")
    cmds.setAttr("PlacementJnt_Ball_L.translate", -BallTrans[0], BallTrans[1], BallTrans[2])

    BallRot = cmds.getAttr("PlacementJnt_Ball_R.rotate")
    cmds.setAttr("PlacementJnt_Ball_L.rotate", -BallRot[0], BallRot[1], -BallRot[2])

    #Toe
    ToeTrans = cmds.getAttr("PlacementJnt_Toe_R.translate")
    cmds.setAttr("PlacementJnt_Toe_L.translate", -ToeTrans[0], ToeTrans[1], ToeTrans[2])

#Create the same function for the left arm

def mirrorJointArmLtoR():
    # Clavicle
    ClavicleTrans = cmds.getAttr("PlacementJnt_Clavicle_L.translate")
    cmds.setAttr("PlacementJnt_Clavicle_R.translate", -ClavicleTrans[0], -ClavicleTrans[1], -ClavicleTrans[2])
    ClavicleRot = cmds.getAttr("PlacementJnt_Clavicle_L.rotate")
    cmds.setAttr("PlacementJnt_Clavicle_R.rotate", ClavicleRot[0], ClavicleRot[1], ClavicleRot[2])
    #Arm
    ArmTrans = cmds.getAttr("PlacementJnt_Arm_L.translate")
    cmds.setAttr("PlacementJnt_Arm_R.translate", -ArmTrans[0], -ArmTrans[1], -ArmTrans[2])

    ArmRot = cmds.getAttr("PlacementJnt_Arm_L.rotate")
    cmds.setAttr("PlacementJnt_Arm_R.rotate", ArmRot[0], ArmRot[1], ArmRot[2])

    #Elbow
    ElbowTrans = cmds.getAttr("PlacementJnt_Elbow_L.translate")
    cmds.setAttr("PlacementJnt_Elbow_R.translate", -ElbowTrans[0], -ElbowTrans[1], -ElbowTrans[2])

    ElbowRot = cmds.getAttr("PlacementJnt_Elbow_L.rotate")
    cmds.setAttr("PlacementJnt_Elbow_R.rotate", ElbowRot[0], ElbowRot[1], ElbowRot[2])

    #Wrist
    WristTrans = cmds.getAttr("PlacementJnt_Wrist_L.translate")
    cmds.setAttr("PlacementJnt_Wrist_R.translate", -WristTrans[0], -WristTrans[1], -WristTrans[2])

    WristRot = cmds.getAttr("PlacementJnt_Wrist_L.rotate")
    cmds.setAttr("PlacementJnt_Wrist_R.rotate", WristRot[0], WristRot[1], WristRot[2])

    #Metacarpus Thumb
    MetacarpusThumbTrans = cmds.getAttr("PlacementJnt_Thumb_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Thumb_Metacarpus_R.translate", -MetacarpusThumbTrans[0], -MetacarpusThumbTrans[1], -MetacarpusThumbTrans[2])

    MetacarpusThumbRot = cmds.getAttr("PlacementJnt_Thumb_Metacarpus_L.rotate")
    cmds.setAttr("PlacementJnt_Thumb_Metacarpus_R.rotate", MetacarpusThumbRot[0], MetacarpusThumbRot[1], MetacarpusThumbRot[2])

    #Metacarpus Index
    MetacarpusIndexTrans = cmds.getAttr("PlacementJnt_Index_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Index_Metacarpus_R.translate", -MetacarpusIndexTrans[0], -MetacarpusIndexTrans[1], -MetacarpusIndexTrans[2])

    MetacarpusIndexRot = cmds.getAttr("PlacementJnt_Index_Metacarpus_L.rotate") 
    cmds.setAttr("PlacementJnt_Index_Metacarpus_R.rotate", MetacarpusIndexRot[0], MetacarpusIndexRot[1], MetacarpusIndexRot[2])

    #Metacarpus Middle
    MetacarpusMiddleTrans = cmds.getAttr("PlacementJnt_Middle_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Middle_Metacarpus_R.translate", -MetacarpusMiddleTrans[0], -MetacarpusMiddleTrans[1], -MetacarpusMiddleTrans[2])

    MetacarpusMiddleRot = cmds.getAttr("PlacementJnt_Middle_Metacarpus_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_Metacarpus_R.rotate", MetacarpusMiddleRot[0], MetacarpusMiddleRot[1], MetacarpusMiddleRot[2])

    #Metacarpus Ring
    MetacarpusRingTrans = cmds.getAttr("PlacementJnt_Ring_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Ring_Metacarpus_R.translate", -MetacarpusRingTrans[0], -MetacarpusRingTrans[1], -MetacarpusRingTrans[2])

    MetacarpusRingRot = cmds.getAttr("PlacementJnt_Ring_Metacarpus_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_Metacarpus_R.rotate", MetacarpusRingRot[0], MetacarpusRingRot[1], MetacarpusRingRot[2])

    #Metacarpus Pinky
    MetacarpusPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_Metacarpus_R.translate", -MetacarpusPinkyTrans[0], -MetacarpusPinkyTrans[1], -MetacarpusPinkyTrans[2])

    MetacarpusPinkyRot = cmds.getAttr("PlacementJnt_Pinky_Metacarpus_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_Metacarpus_R.rotate", MetacarpusPinkyRot[0], MetacarpusPinkyRot[1], MetacarpusPinkyRot[2])

    #One Thumb
    OneThumbTrans = cmds.getAttr("PlacementJnt_Thumb_01_L.translate")
    cmds.setAttr("PlacementJnt_Thumb_01_R.translate", -OneThumbTrans[0], -OneThumbTrans[1], -OneThumbTrans[2])

    OneThumbRot = cmds.getAttr("PlacementJnt_Thumb_01_L.rotate")
    cmds.setAttr("PlacementJnt_Thumb_01_R.rotate", OneThumbRot[0], OneThumbRot[1], OneThumbRot[2])

    #One Index
    OneIndexTrans = cmds.getAttr("PlacementJnt_Index_01_L.translate")
    cmds.setAttr("PlacementJnt_Index_01_R.translate", -OneIndexTrans[0], -OneIndexTrans[1], -OneIndexTrans[2])

    OneIndexRot = cmds.getAttr("PlacementJnt_Index_01_L.rotate")
    cmds.setAttr("PlacementJnt_Index_01_R.rotate", OneIndexRot[0], OneIndexRot[1], OneIndexRot[2])

    #One Middle
    OneMiddleTrans = cmds.getAttr("PlacementJnt_Middle_01_L.translate")
    cmds.setAttr("PlacementJnt_Middle_01_R.translate", -OneMiddleTrans[0], -OneMiddleTrans[1], -OneMiddleTrans[2])

    OneMiddleRot = cmds.getAttr("PlacementJnt_Middle_01_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_01_R.rotate", OneMiddleRot[0], OneMiddleRot[1], OneMiddleRot[2])

    #One Ring
    OneRingTrans = cmds.getAttr("PlacementJnt_Ring_01_L.translate")
    cmds.setAttr("PlacementJnt_Ring_01_R.translate", -OneRingTrans[0], -OneRingTrans[1], -OneRingTrans[2])

    OneRingRot = cmds.getAttr("PlacementJnt_Ring_01_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_01_R.rotate", OneRingRot[0], OneRingRot[1], OneRingRot[2])

    #One Pinky
    OnePinkyTrans = cmds.getAttr("PlacementJnt_Pinky_01_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_01_R.translate", -OnePinkyTrans[0], -OnePinkyTrans[1], -OnePinkyTrans[2])

    OnePinkyRot = cmds.getAttr("PlacementJnt_Pinky_01_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_01_R.rotate", OnePinkyRot[0], OnePinkyRot[1], OnePinkyRot[2])

    #Two Thumb
    TwoThumbTrans = cmds.getAttr("PlacementJnt_Thumb_02_L.translate")
    cmds.setAttr("PlacementJnt_Thumb_02_R.translate", -TwoThumbTrans[0], -TwoThumbTrans[1], -TwoThumbTrans[2])

    TwoThumbRot = cmds.getAttr("PlacementJnt_Thumb_02_L.rotate")
    cmds.setAttr("PlacementJnt_Thumb_02_R.rotate", TwoThumbRot[0], TwoThumbRot[1], TwoThumbRot[2])

    #Two Index
    TwoIndexTrans = cmds.getAttr("PlacementJnt_Index_02_L.translate")
    cmds.setAttr("PlacementJnt_Index_02_R.translate", -TwoIndexTrans[0], -TwoIndexTrans[1], -TwoIndexTrans[2])

    TwoIndexRot = cmds.getAttr("PlacementJnt_Index_02_L.rotate")
    cmds.setAttr("PlacementJnt_Index_02_R.rotate", TwoIndexRot[0], TwoIndexRot[1], TwoIndexRot[2])

    #Two Middle
    TwoMiddleTrans = cmds.getAttr("PlacementJnt_Middle_02_L.translate")
    cmds.setAttr("PlacementJnt_Middle_02_R.translate", -TwoMiddleTrans[0], -TwoMiddleTrans[1], -TwoMiddleTrans[2])

    TwoMiddleRot = cmds.getAttr("PlacementJnt_Middle_02_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_02_R.rotate", TwoMiddleRot[0], TwoMiddleRot[1], TwoMiddleRot[2])

    #Two Ring
    TwoRingTrans = cmds.getAttr("PlacementJnt_Ring_02_L.translate")
    cmds.setAttr("PlacementJnt_Ring_02_R.translate", -TwoRingTrans[0], -TwoRingTrans[1], -TwoRingTrans[2])

    TwoRingRot = cmds.getAttr("PlacementJnt_Ring_02_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_02_R.rotate", TwoRingRot[0], TwoRingRot[1], TwoRingRot[2])

    #Two Pinky
    TwoPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_02_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_02_R.translate", -TwoPinkyTrans[0], -TwoPinkyTrans[1], -TwoPinkyTrans[2])

    TwoPinkyRot = cmds.getAttr("PlacementJnt_Pinky_02_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_02_R.rotate", TwoPinkyRot[0], TwoPinkyRot[1], TwoPinkyRot[2])

    #Three Index
    ThreeIndexTrans = cmds.getAttr("PlacementJnt_Index_03_L.translate")
    cmds.setAttr("PlacementJnt_Index_03_R.translate", -ThreeIndexTrans[0], -ThreeIndexTrans[1], -ThreeIndexTrans[2])

    ThreeIndexRot = cmds.getAttr("PlacementJnt_Index_03_L.rotate")
    cmds.setAttr("PlacementJnt_Index_03_R.rotate", ThreeIndexRot[0], ThreeIndexRot[1], ThreeIndexRot[2])

    #Three Middle
    ThreeMiddleTrans = cmds.getAttr("PlacementJnt_Middle_03_L.translate")
    cmds.setAttr("PlacementJnt_Middle_03_R.translate", -ThreeMiddleTrans[0], -ThreeMiddleTrans[1], -ThreeMiddleTrans[2])

    ThreeMiddleRot = cmds.getAttr("PlacementJnt_Middle_03_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_03_R.rotate", ThreeMiddleRot[0], ThreeMiddleRot[1], ThreeMiddleRot[2])

    #Three Ring
    ThreeRingTrans = cmds.getAttr("PlacementJnt_Ring_03_L.translate")
    cmds.setAttr("PlacementJnt_Ring_03_R.translate", -ThreeRingTrans[0], -ThreeRingTrans[1], -ThreeRingTrans[2])

    ThreeRingRot = cmds.getAttr("PlacementJnt_Ring_03_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_03_R.rotate", ThreeRingRot[0], ThreeRingRot[1], ThreeRingRot[2])

    #Three Pinky
    ThreePinkyTrans = cmds.getAttr("PlacementJnt_Pinky_03_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_03_R.translate", -ThreePinkyTrans[0], -ThreePinkyTrans[1], -ThreePinkyTrans[2])

    ThreePinkyRot = cmds.getAttr("PlacementJnt_Pinky_03_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_03_R.rotate", ThreePinkyRot[0], ThreePinkyRot[1], ThreePinkyRot[2])

    #End Thumb
    EndThumbTrans = cmds.getAttr("PlacementJnt_Thumb_end_L.translate")
    cmds.setAttr("PlacementJnt_Thumb_end_R.translate", -EndThumbTrans[0], -EndThumbTrans[1], -EndThumbTrans[2])

    EndThumbRot = cmds.getAttr("PlacementJnt_Thumb_end_L.rotate")
    cmds.setAttr("PlacementJnt_Thumb_end_R.rotate", EndThumbRot[0], EndThumbRot[1], EndThumbRot[2])

    #End Index
    EndIndexTrans = cmds.getAttr("PlacementJnt_Index_end_L.translate")
    cmds.setAttr("PlacementJnt_Index_end_R.translate", -EndIndexTrans[0], -EndIndexTrans[1], -EndIndexTrans[2])

    EndIndexRot = cmds.getAttr("PlacementJnt_Index_end_L.rotate")
    cmds.setAttr("PlacementJnt_Index_end_R.rotate", EndIndexRot[0], EndIndexRot[1], EndIndexRot[2])

    #End Middle
    EndMiddleTrans = cmds.getAttr("PlacementJnt_Middle_end_L.translate")
    cmds.setAttr("PlacementJnt_Middle_end_R.translate", -EndMiddleTrans[0], -EndMiddleTrans[1], -EndMiddleTrans[2])

    EndMiddleRot = cmds.getAttr("PlacementJnt_Middle_end_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_end_R.rotate", EndMiddleRot[0], EndMiddleRot[1], EndMiddleRot[2])

    #End Ring
    EndRingTrans = cmds.getAttr("PlacementJnt_Ring_end_L.translate")
    cmds.setAttr("PlacementJnt_Ring_end_R.translate", -EndRingTrans[0], -EndRingTrans[1], -EndRingTrans[2])

    EndRingRot = cmds.getAttr("PlacementJnt_Ring_end_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_end_R.rotate", EndRingRot[0], EndRingRot[1], EndRingRot[2])

    #End Pinky
    EndPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_end_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_end_R.translate", -EndPinkyTrans[0], -EndPinkyTrans[1], -EndPinkyTrans[2])

    EndPinkyRot = cmds.getAttr("PlacementJnt_Pinky_end_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_end_R.rotate", EndPinkyRot[0], EndPinkyRot[1], EndPinkyRot[2])

def mirrorJointArmRtoL():
    # Clavicle
    ClavicleTrans = cmds.getAttr("PlacementJnt_Clavicle_R.translate")
    cmds.setAttr("PlacementJnt_Clavicle_L.translate", -ClavicleTrans[0], -ClavicleTrans[1], -ClavicleTrans[2])
    ClavicleRot = cmds.getAttr("PlacementJnt_Clavicle_R.rotate")
    cmds.setAttr("PlacementJnt_Clavicle_L.rotate", ClavicleRot[0], ClavicleRot[1], ClavicleRot[2])
    # Arm
    ArmTrans = cmds.getAttr("PlacementJnt_Arm_R.translate")
    cmds.setAttr("PlacementJnt_Arm_L.translate", -ArmTrans[0], -ArmTrans[1], -ArmTrans[2])
    ArmRot = cmds.getAttr("PlacementJnt_Arm_R.rotate")
    cmds.setAttr("PlacementJnt_Arm_L.rotate", ArmRot[0], ArmRot[1], ArmRot[2])
    # Elbow
    ElbowTrans = cmds.getAttr("PlacementJnt_Elbow_R.translate")
    cmds.setAttr("PlacementJnt_Elbow_L.translate", -ElbowTrans[0], -ElbowTrans[1], -ElbowTrans[2])
    ElbowRot = cmds.getAttr("PlacementJnt_Elbow_R.rotate")
    cmds.setAttr("PlacementJnt_Elbow_L.rotate", ElbowRot[0], ElbowRot[1], ElbowRot[2])
    # Wrist
    WristTrans = cmds.getAttr("PlacementJnt_Wrist_R.translate")
    cmds.setAttr("PlacementJnt_Wrist_L.translate", -WristTrans[0], -WristTrans[1], -WristTrans[2])
    WristRot = cmds.getAttr("PlacementJnt_Wrist_R.rotate")
    cmds.setAttr("PlacementJnt_Wrist_L.rotate", WristRot[0], WristRot[1], WristRot[2])
    # Metacarpus Thumb
    MetacarpusThumbTrans = cmds.getAttr("PlacementJnt_Thumb_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Thumb_Metacarpus_L.translate", -MetacarpusThumbTrans[0], -MetacarpusThumbTrans[1], -MetacarpusThumbTrans[2])
    MetacarpusThumbRot = cmds.getAttr("PlacementJnt_Thumb_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Thumb_Metacarpus_L.rotate", MetacarpusThumbRot[0], MetacarpusThumbRot[1], MetacarpusThumbRot[2])
    # Metacarpus Index
    MetacarpusIndexTrans = cmds.getAttr("PlacementJnt_Index_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Index_Metacarpus_L.translate", -MetacarpusIndexTrans[0], -MetacarpusIndexTrans[1], -MetacarpusIndexTrans[2])
    MetacarpusIndexRot = cmds.getAttr("PlacementJnt_Index_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Index_Metacarpus_L.rotate", MetacarpusIndexRot[0], MetacarpusIndexRot[1], MetacarpusIndexRot[2])
    # Metacarpus Middle
    MetacarpusMiddleTrans = cmds.getAttr("PlacementJnt_Middle_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Middle_Metacarpus_L.translate", -MetacarpusMiddleTrans[0], -MetacarpusMiddleTrans[1], -MetacarpusMiddleTrans[2])
    MetacarpusMiddleRot = cmds.getAttr("PlacementJnt_Middle_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_Metacarpus_L.rotate", MetacarpusMiddleRot[0], MetacarpusMiddleRot[1], MetacarpusMiddleRot[2])
    # Metacarpus Ring
    MetacarpusRingTrans = cmds.getAttr("PlacementJnt_Ring_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Ring_Metacarpus_L.translate", -MetacarpusRingTrans[0], -MetacarpusRingTrans[1], -MetacarpusRingTrans[2])
    MetacarpusRingRot = cmds.getAttr("PlacementJnt_Ring_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_Metacarpus_L.rotate", MetacarpusRingRot[0], MetacarpusRingRot[1], MetacarpusRingRot[2])
    # Metacarpus Pinky
    MetacarpusPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_Metacarpus_L.translate", -MetacarpusPinkyTrans[0], -MetacarpusPinkyTrans[1], -MetacarpusPinkyTrans[2])
    MetacarpusPinkyRot = cmds.getAttr("PlacementJnt_Pinky_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_Metacarpus_L.rotate", MetacarpusPinkyRot[0], MetacarpusPinkyRot[1], MetacarpusPinkyRot[2])
    # One Thumb
    OneThumbTrans = cmds.getAttr("PlacementJnt_Thumb_01_R.translate")
    cmds.setAttr("PlacementJnt_Thumb_01_L.translate", -OneThumbTrans[0], -OneThumbTrans[1], -OneThumbTrans[2])
    OneThumbRot = cmds.getAttr("PlacementJnt_Thumb_01_R.rotate")
    cmds.setAttr("PlacementJnt_Thumb_01_L.rotate", OneThumbRot[0], OneThumbRot[1], OneThumbRot[2])
    # One Index
    OneIndexTrans = cmds.getAttr("PlacementJnt_Index_01_R.translate")
    cmds.setAttr("PlacementJnt_Index_01_L.translate", -OneIndexTrans[0], -OneIndexTrans[1], -OneIndexTrans[2])
    OneIndexRot = cmds.getAttr("PlacementJnt_Index_01_R.rotate")
    cmds.setAttr("PlacementJnt_Index_01_L.rotate", OneIndexRot[0], OneIndexRot[1], OneIndexRot[2])
    # One Middle
    OneMiddleTrans = cmds.getAttr("PlacementJnt_Middle_01_R.translate")
    cmds.setAttr("PlacementJnt_Middle_01_L.translate", -OneMiddleTrans[0], -OneMiddleTrans[1], -OneMiddleTrans[2])
    OneMiddleRot = cmds.getAttr("PlacementJnt_Middle_01_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_01_L.rotate", OneMiddleRot[0], OneMiddleRot[1], OneMiddleRot[2])
    # One Ring
    OneRingTrans = cmds.getAttr("PlacementJnt_Ring_01_R.translate")
    cmds.setAttr("PlacementJnt_Ring_01_L.translate", -OneRingTrans[0], -OneRingTrans[1], -OneRingTrans[2])
    OneRingRot = cmds.getAttr("PlacementJnt_Ring_01_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_01_L.rotate", OneRingRot[0], OneRingRot[1], OneRingRot[2])
    # One Pinky
    OnePinkyTrans = cmds.getAttr("PlacementJnt_Pinky_01_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_01_L.translate", -OnePinkyTrans[0], -OnePinkyTrans[1], -OnePinkyTrans[2])
    OnePinkyRot = cmds.getAttr("PlacementJnt_Pinky_01_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_01_L.rotate", OnePinkyRot[0], OnePinkyRot[1], OnePinkyRot[2])
    # Two Thumb
    TwoThumbTrans = cmds.getAttr("PlacementJnt_Thumb_02_R.translate")
    cmds.setAttr("PlacementJnt_Thumb_02_L.translate", -TwoThumbTrans[0], -TwoThumbTrans[1], -TwoThumbTrans[2])
    TwoThumbRot = cmds.getAttr("PlacementJnt_Thumb_02_R.rotate")
    cmds.setAttr("PlacementJnt_Thumb_02_L.rotate", TwoThumbRot[0], TwoThumbRot[1], TwoThumbRot[2])
    # Two Index
    TwoIndexTrans = cmds.getAttr("PlacementJnt_Index_02_R.translate")
    cmds.setAttr("PlacementJnt_Index_02_L.translate", -TwoIndexTrans[0], -TwoIndexTrans[1], -TwoIndexTrans[2])
    TwoIndexRot = cmds.getAttr("PlacementJnt_Index_02_R.rotate")
    cmds.setAttr("PlacementJnt_Index_02_L.rotate", TwoIndexRot[0], TwoIndexRot[1], TwoIndexRot[2])
    # Two Middle
    TwoMiddleTrans = cmds.getAttr("PlacementJnt_Middle_02_R.translate")
    cmds.setAttr("PlacementJnt_Middle_02_L.translate", -TwoMiddleTrans[0], -TwoMiddleTrans[1], -TwoMiddleTrans[2])
    TwoMiddleRot = cmds.getAttr("PlacementJnt_Middle_02_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_02_L.rotate", TwoMiddleRot[0], TwoMiddleRot[1], TwoMiddleRot[2])
    # Two Ring
    TwoRingTrans = cmds.getAttr("PlacementJnt_Ring_02_R.translate")
    cmds.setAttr("PlacementJnt_Ring_02_L.translate", -TwoRingTrans[0], -TwoRingTrans[1], -TwoRingTrans[2])
    TwoRingRot = cmds.getAttr("PlacementJnt_Ring_02_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_02_L.rotate", TwoRingRot[0], TwoRingRot[1], TwoRingRot[2])
    # Two Pinky
    TwoPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_02_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_02_L.translate", -TwoPinkyTrans[0], -TwoPinkyTrans[1], -TwoPinkyTrans[2])
    TwoPinkyRot = cmds.getAttr("PlacementJnt_Pinky_02_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_02_L.rotate", TwoPinkyRot[0], TwoPinkyRot[1], TwoPinkyRot[2])
    # Three Index
    ThreeIndexTrans = cmds.getAttr("PlacementJnt_Index_03_R.translate")
    cmds.setAttr("PlacementJnt_Index_03_L.translate", -ThreeIndexTrans[0], -ThreeIndexTrans[1], -ThreeIndexTrans[2])
    ThreeIndexRot = cmds.getAttr("PlacementJnt_Index_03_R.rotate")
    cmds.setAttr("PlacementJnt_Index_03_L.rotate", ThreeIndexRot[0], ThreeIndexRot[1], ThreeIndexRot[2])
    # Three Middle
    ThreeMiddleTrans = cmds.getAttr("PlacementJnt_Middle_03_R.translate")
    cmds.setAttr("PlacementJnt_Middle_03_L.translate", -ThreeMiddleTrans[0], -ThreeMiddleTrans[1], -ThreeMiddleTrans[2])
    ThreeMiddleRot = cmds.getAttr("PlacementJnt_Middle_03_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_03_L.rotate", ThreeMiddleRot[0], ThreeMiddleRot[1], ThreeMiddleRot[2])
    # Three Ring
    ThreeRingTrans = cmds.getAttr("PlacementJnt_Ring_03_R.translate")
    cmds.setAttr("PlacementJnt_Ring_03_L.translate", -ThreeRingTrans[0], -ThreeRingTrans[1], -ThreeRingTrans[2])
    ThreeRingRot = cmds.getAttr("PlacementJnt_Ring_03_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_03_L.rotate", ThreeRingRot[0], ThreeRingRot[1], ThreeRingRot[2])
    # Three Pinky
    ThreePinkyTrans = cmds.getAttr("PlacementJnt_Pinky_03_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_03_L.translate", -ThreePinkyTrans[0], -ThreePinkyTrans[1], -ThreePinkyTrans[2])
    ThreePinkyRot = cmds.getAttr("PlacementJnt_Pinky_03_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_03_L.rotate", ThreePinkyRot[0], ThreePinkyRot[1], ThreePinkyRot[2])
    # End Thumb
    EndThumbTrans = cmds.getAttr("PlacementJnt_Thumb_end_R.translate")
    cmds.setAttr("PlacementJnt_Thumb_end_L.translate", -EndThumbTrans[0], -EndThumbTrans[1], -EndThumbTrans[2])
    EndThumbRot = cmds.getAttr("PlacementJnt_Thumb_end_R.rotate")
    cmds.setAttr("PlacementJnt_Thumb_end_L.rotate", EndThumbRot[0], EndThumbRot[1], EndThumbRot[2])
    # End Index
    EndIndexTrans = cmds.getAttr("PlacementJnt_Index_end_R.translate")
    cmds.setAttr("PlacementJnt_Index_end_L.translate", -EndIndexTrans[0], -EndIndexTrans[1], -EndIndexTrans[2])
    EndIndexRot = cmds.getAttr("PlacementJnt_Index_end_R.rotate")
    cmds.setAttr("PlacementJnt_Index_end_L.rotate", EndIndexRot[0], EndIndexRot[1], EndIndexRot[2])
    # End Middle
    EndMiddleTrans = cmds.getAttr("PlacementJnt_Middle_end_R.translate")
    cmds.setAttr("PlacementJnt_Middle_end_L.translate", -EndMiddleTrans[0], -EndMiddleTrans[1], -EndMiddleTrans[2])
    EndMiddleRot = cmds.getAttr("PlacementJnt_Middle_end_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_end_L.rotate", EndMiddleRot[0], EndMiddleRot[1], EndMiddleRot[2])
    # End Ring
    EndRingTrans = cmds.getAttr("PlacementJnt_Ring_end_R.translate")
    cmds.setAttr("PlacementJnt_Ring_end_L.translate", -EndRingTrans[0], -EndRingTrans[1], -EndRingTrans[2])
    EndRingRot = cmds.getAttr("PlacementJnt_Ring_end_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_end_L.rotate", EndRingRot[0], EndRingRot[1], EndRingRot[2])
    # End Pinky
    EndPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_end_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_end_L.translate", -EndPinkyTrans[0], -EndPinkyTrans[1], -EndPinkyTrans[2])
    EndPinkyRot = cmds.getAttr("PlacementJnt_Pinky_end_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_end_L.rotate", EndPinkyRot[0], EndPinkyRot[1], EndPinkyRot[2])
