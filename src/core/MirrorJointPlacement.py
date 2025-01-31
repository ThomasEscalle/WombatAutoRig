import maya.cmds as cmds


def mirrorJointLegLtoR():
    #Hip
    HipTrans = cmds.getAttr("PlacementJnt_Hip_L.translate")
    cmds.setAttr("PlacementJnt_Hip_R.translate", -1*HipTrans[0][0], HipTrans[0][1], HipTrans[0][2])

    HipRot = cmds.getAttr("PlacementJnt_Hip_L.rotate")
    cmds.setAttr("PlacementJnt_Hip_R.rotate", -1*HipRot[0][0], HipRot[0][1], -1*HipRot[0][2])

    #Knee
    KneeTrans = cmds.getAttr("PlacementJnt_Knee_L.translate")
    cmds.setAttr("PlacementJnt_Knee_R.translate", KneeTrans[0][0], -1*KneeTrans[0][1], KneeTrans[0][2])

    KneeRot = cmds.getAttr("PlacementJnt_Knee_L.rotate")
    cmds.setAttr("PlacementJnt_Knee_R.rotate", -1*KneeRot[0][0], KneeRot[0][1], -1*KneeRot[0][2])

    #Ankle
    AnkleTrans = cmds.getAttr("PlacementJnt_Ankle_L.translate")
    cmds.setAttr("PlacementJnt_Ankle_R.translate", AnkleTrans[0][0], -1*AnkleTrans[0][1], AnkleTrans[0][2])

    AnkleRot = cmds.getAttr("PlacementJnt_Ankle_L.rotate")
    cmds.setAttr("PlacementJnt_Ankle_R.rotate", -1*AnkleRot[0][0], AnkleRot[0][1], -1*AnkleRot[0][2])

    #Ball
    BallTrans = cmds.getAttr("PlacementJnt_Ball_L.translate")
    cmds.setAttr("PlacementJnt_Ball_R.translate", BallTrans[0][0], -1*BallTrans[0][1], BallTrans[0][2])

    BallRot = cmds.getAttr("PlacementJnt_Ball_L.rotate")
    cmds.setAttr("PlacementJnt_Ball_R.rotate", -1*BallRot[0][0], BallRot[0][1], -1*BallRot[0][2])

    #Toe
    ToeTrans = cmds.getAttr("PlacementJnt_Toe_L.translate")
    cmds.setAttr("PlacementJnt_Toe_R.translate", ToeTrans[0][0], -1*ToeTrans[0][1], ToeTrans[0][2])

    ToeRot = cmds.getAttr("PlacementJnt_Toe_L.rotate")
    cmds.setAttr("PlacementJnt_Toe_R.rotate", -1*ToeRot[0][0], ToeRot[0][1], -1*ToeRot[0][2])


    #PlacementCTRL
    PlacementFrontTrans = cmds.getAttr("PlacementCtrl_Foot_Front_L.translate")
    cmds.setAttr("PlacementCtrl_Foot_Front_R.translate", -1*PlacementFrontTrans[0][0], PlacementFrontTrans[0][1], PlacementFrontTrans[0][2])
    
    PlacementIntTrans = cmds.getAttr("PlacementCtrl_Foot_Int_L.translate")
    cmds.setAttr("PlacementCtrl_Foot_Int_R.translate", -1*PlacementIntTrans[0][0], PlacementIntTrans[0][1], PlacementIntTrans[0][2])

    PlacementExtTrans = cmds.getAttr("PlacementCtrl_Foot_Ext_L.translate")
    cmds.setAttr("PlacementCtrl_Foot_Ext_R.translate", -1*PlacementExtTrans[0][0], PlacementExtTrans[0][1], PlacementExtTrans[0][2])

    PlacementBackTrans = cmds.getAttr("PlacementCtrl_Foot_Back_L.translate")
    cmds.setAttr("PlacementCtrl_Foot_Back_R.translate", -1*PlacementBackTrans[0][0], PlacementBackTrans[0][1], PlacementBackTrans[0][2])


#Create the same function for the right leg

def mirrorJointLegRtoL():
    #Hip
    HipTrans = cmds.getAttr("PlacementJnt_Hip_R.translate")
    cmds.setAttr("PlacementJnt_Hip_L.translate", -1*HipTrans[0][0], HipTrans[0][1], HipTrans[0][2])

    HipRot = cmds.getAttr("PlacementJnt_Hip_R.rotate")
    cmds.setAttr("PlacementJnt_Hip_L.rotate", -1*HipRot[0][0], HipRot[0][1], -1*HipRot[0][2])

    #Knee
    KneeTrans = cmds.getAttr("PlacementJnt_Knee_R.translate")
    cmds.setAttr("PlacementJnt_Knee_L.translate", KneeTrans[0][0], -1*KneeTrans[0][1], KneeTrans[0][2])

    KneeRot = cmds.getAttr("PlacementJnt_Knee_R.rotate")
    cmds.setAttr("PlacementJnt_Knee_L.rotate", -1*KneeRot[0][0], KneeRot[0][1], -1*KneeRot[0][2])

    #Ankle
    AnkleTrans = cmds.getAttr("PlacementJnt_Ankle_R.translate")
    cmds.setAttr("PlacementJnt_Ankle_L.translate", AnkleTrans[0][0], -1*AnkleTrans[0][1], AnkleTrans[0][2])

    AnkleRot = cmds.getAttr("PlacementJnt_Ankle_R.rotate")
    cmds.setAttr("PlacementJnt_Ankle_L.rotate", -1*AnkleRot[0][0], AnkleRot[0][1], -1*AnkleRot[0][2])

    #Ball
    BallTrans = cmds.getAttr("PlacementJnt_Ball_R.translate")
    cmds.setAttr("PlacementJnt_Ball_L.translate", BallTrans[0][0], -1*BallTrans[0][1], BallTrans[0][2])

    BallRot = cmds.getAttr("PlacementJnt_Ball_R.rotate")
    cmds.setAttr("PlacementJnt_Ball_L.rotate", -1*BallRot[0][0], BallRot[0][1], -1*BallRot[0][2])

    #Toe
    ToeTrans = cmds.getAttr("PlacementJnt_Toe_R.translate")
    cmds.setAttr("PlacementJnt_Toe_L.translate", ToeTrans[0][0], -1*ToeTrans[0][1], ToeTrans[0][2])

    ToeRot = cmds.getAttr("PlacementJnt_Toe_R.rotate")
    cmds.setAttr("PlacementJnt_Toe_L.rotate", -1*ToeRot[0][0], ToeRot[0][1], -1*ToeRot[0][2])

    #PlacementCTRL
    PlacementFrontTrans = cmds.getAttr("PlacementCtrl_Foot_Front_R.translate")
    cmds.setAttr("PlacementCtrl_Foot_Front_L.translate", -1*PlacementFrontTrans[0][0], PlacementFrontTrans[0][1], PlacementFrontTrans[0][2])
    
    PlacementIntTrans = cmds.getAttr("PlacementCtrl_Foot_Int_R.translate")
    cmds.setAttr("PlacementCtrl_Foot_Int_L.translate", -1*PlacementIntTrans[0][0], PlacementIntTrans[0][1], PlacementIntTrans[0][2])

    PlacementExtTrans = cmds.getAttr("PlacementCtrl_Foot_Ext_R.translate")
    cmds.setAttr("PlacementCtrl_Foot_Ext_L.translate", -1*PlacementExtTrans[0][0], PlacementExtTrans[0][1], PlacementExtTrans[0][2])

    PlacementBackTrans = cmds.getAttr("PlacementCtrl_Foot_Back_R.translate")
    cmds.setAttr("PlacementCtrl_Foot_Back_L.translate", -1*PlacementBackTrans[0][0], PlacementBackTrans[0][1], PlacementBackTrans[0][2])

#Create the same function for the left arm

def mirrorJointArmLtoR():
    # Clavicle
    ClavicleTrans = cmds.getAttr("PlacementJnt_Clavicle_L.translate")
    cmds.setAttr("PlacementJnt_Clavicle_R.translate", -1*ClavicleTrans[0][0], ClavicleTrans[0][1], ClavicleTrans[0][2])
    ClavicleRot = cmds.getAttr("PlacementJnt_Clavicle_L.rotate")
    cmds.setAttr("PlacementJnt_Clavicle_R.rotate", ClavicleRot[0][0], ClavicleRot[0][1], ClavicleRot[0][2])
    #Clevicle end
    ClavicleEndTrans = cmds.getAttr("PlacementJnt_Clavicle_end_L.translate")
    cmds.setAttr("PlacementJnt_Clavicle_end_R.translate", -1*ClavicleEndTrans[0][0], ClavicleEndTrans[0][1], -1*ClavicleEndTrans[0][2])
    ClavicleEndRot = cmds.getAttr("PlacementJnt_Clavicle_end_L.rotate")
    cmds.setAttr("PlacementJnt_Clavicle_end_R.rotate", ClavicleEndRot[0][0], ClavicleEndRot[0][1], ClavicleEndRot[0][2])
    #Arm
    ArmTrans = cmds.getAttr("PlacementJnt_Arm_L.translate")
    cmds.setAttr("PlacementJnt_Arm_R.translate", -1*ArmTrans[0][0], -1*ArmTrans[0][1], -1*ArmTrans[0][2])

    ArmRot = cmds.getAttr("PlacementJnt_Arm_L.rotate")
    cmds.setAttr("PlacementJnt_Arm_R.rotate", ArmRot[0][0], ArmRot[0][1], ArmRot[0][2])

    #Elbow
    ElbowTrans = cmds.getAttr("PlacementJnt_Elbow_L.translate")
    cmds.setAttr("PlacementJnt_Elbow_R.translate", -1*ElbowTrans[0][0], -1*ElbowTrans[0][1], -1*ElbowTrans[0][2])

    ElbowRot = cmds.getAttr("PlacementJnt_Elbow_L.rotate")
    cmds.setAttr("PlacementJnt_Elbow_R.rotate", ElbowRot[0][0], ElbowRot[0][1], ElbowRot[0][2])

    #Wrist
    WristTrans = cmds.getAttr("PlacementJnt_Wrist_L.translate")
    cmds.setAttr("PlacementJnt_Wrist_R.translate", -1*WristTrans[0][0], -1*WristTrans[0][1], -1*WristTrans[0][2])

    WristRot = cmds.getAttr("PlacementJnt_Wrist_L.rotate")
    cmds.setAttr("PlacementJnt_Wrist_R.rotate", WristRot[0][0], WristRot[0][1], WristRot[0][2])

    #Metacarpus Thumb
    MetacarpusThumbTrans = cmds.getAttr("PlacementJnt_Thumb_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Thumb_Metacarpus_R.translate", -1*MetacarpusThumbTrans[0][0], -1*MetacarpusThumbTrans[0][1], -1*MetacarpusThumbTrans[0][2])

    MetacarpusThumbRot = cmds.getAttr("PlacementJnt_Thumb_Metacarpus_L.rotate")
    cmds.setAttr("PlacementJnt_Thumb_Metacarpus_R.rotate", MetacarpusThumbRot[0][0], MetacarpusThumbRot[0][1], MetacarpusThumbRot[0][2])

    #Metacarpus Index
    MetacarpusIndexTrans = cmds.getAttr("PlacementJnt_Index_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Index_Metacarpus_R.translate", -1*MetacarpusIndexTrans[0][0], -1*MetacarpusIndexTrans[0][1], -1*MetacarpusIndexTrans[0][2])

    MetacarpusIndexRot = cmds.getAttr("PlacementJnt_Index_Metacarpus_L.rotate") 
    cmds.setAttr("PlacementJnt_Index_Metacarpus_R.rotate", MetacarpusIndexRot[0][0], MetacarpusIndexRot[0][1], MetacarpusIndexRot[0][2])

    #Metacarpus Middle
    MetacarpusMiddleTrans = cmds.getAttr("PlacementJnt_Middle_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Middle_Metacarpus_R.translate", -1*MetacarpusMiddleTrans[0][0], -1*MetacarpusMiddleTrans[0][1], -1*MetacarpusMiddleTrans[0][2])

    MetacarpusMiddleRot = cmds.getAttr("PlacementJnt_Middle_Metacarpus_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_Metacarpus_R.rotate", MetacarpusMiddleRot[0][0], MetacarpusMiddleRot[0][1], MetacarpusMiddleRot[0][2])

    #Metacarpus Ring
    MetacarpusRingTrans = cmds.getAttr("PlacementJnt_Ring_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Ring_Metacarpus_R.translate", -1*MetacarpusRingTrans[0][0], -1*MetacarpusRingTrans[0][1], -1*MetacarpusRingTrans[0][2])

    MetacarpusRingRot = cmds.getAttr("PlacementJnt_Ring_Metacarpus_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_Metacarpus_R.rotate", MetacarpusRingRot[0][0], MetacarpusRingRot[0][1], MetacarpusRingRot[0][2])

    #Metacarpus Pinky
    MetacarpusPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_Metacarpus_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_Metacarpus_R.translate", -1*MetacarpusPinkyTrans[0][0], -1*MetacarpusPinkyTrans[0][1], -1*MetacarpusPinkyTrans[0][2])

    MetacarpusPinkyRot = cmds.getAttr("PlacementJnt_Pinky_Metacarpus_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_Metacarpus_R.rotate", MetacarpusPinkyRot[0][0], MetacarpusPinkyRot[0][1], MetacarpusPinkyRot[0][2])

    #One Thumb
    OneThumbTrans = cmds.getAttr("PlacementJnt_Thumb_01_L.translate")
    cmds.setAttr("PlacementJnt_Thumb_01_R.translate", -1*OneThumbTrans[0][0], -1*OneThumbTrans[0][1], -1*OneThumbTrans[0][2])

    OneThumbRot = cmds.getAttr("PlacementJnt_Thumb_01_L.rotate")
    cmds.setAttr("PlacementJnt_Thumb_01_R.rotate", OneThumbRot[0][0], OneThumbRot[0][1], OneThumbRot[0][2])

    #One Index
    OneIndexTrans = cmds.getAttr("PlacementJnt_Index_01_L.translate")
    cmds.setAttr("PlacementJnt_Index_01_R.translate", -1*OneIndexTrans[0][0], -1*OneIndexTrans[0][1], -1*OneIndexTrans[0][2])

    OneIndexRot = cmds.getAttr("PlacementJnt_Index_01_L.rotate")
    cmds.setAttr("PlacementJnt_Index_01_R.rotate", OneIndexRot[0][0], OneIndexRot[0][1], OneIndexRot[0][2])

    #One Middle
    OneMiddleTrans = cmds.getAttr("PlacementJnt_Middle_01_L.translate")
    cmds.setAttr("PlacementJnt_Middle_01_R.translate", -1*OneMiddleTrans[0][0], -1*OneMiddleTrans[0][1], -1*OneMiddleTrans[0][2])

    OneMiddleRot = cmds.getAttr("PlacementJnt_Middle_01_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_01_R.rotate", OneMiddleRot[0][0], OneMiddleRot[0][1], OneMiddleRot[0][2])

    #One Ring
    OneRingTrans = cmds.getAttr("PlacementJnt_Ring_01_L.translate")
    cmds.setAttr("PlacementJnt_Ring_01_R.translate", -1*OneRingTrans[0][0], -1*OneRingTrans[0][1], -1*OneRingTrans[0][2])

    OneRingRot = cmds.getAttr("PlacementJnt_Ring_01_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_01_R.rotate", OneRingRot[0][0], OneRingRot[0][1], OneRingRot[0][2])

    #One Pinky
    OnePinkyTrans = cmds.getAttr("PlacementJnt_Pinky_01_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_01_R.translate", -1*OnePinkyTrans[0][0], -1*OnePinkyTrans[0][1], -1*OnePinkyTrans[0][2])

    OnePinkyRot = cmds.getAttr("PlacementJnt_Pinky_01_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_01_R.rotate", OnePinkyRot[0][0], OnePinkyRot[0][1], OnePinkyRot[0][2])

    #Two Thumb
    TwoThumbTrans = cmds.getAttr("PlacementJnt_Thumb_02_L.translate")
    cmds.setAttr("PlacementJnt_Thumb_02_R.translate", -1*TwoThumbTrans[0][0], -1*TwoThumbTrans[0][1], -1*TwoThumbTrans[0][2])

    TwoThumbRot = cmds.getAttr("PlacementJnt_Thumb_02_L.rotate")
    cmds.setAttr("PlacementJnt_Thumb_02_R.rotate", TwoThumbRot[0][0], TwoThumbRot[0][1], TwoThumbRot[0][2])

    #Two Index
    TwoIndexTrans = cmds.getAttr("PlacementJnt_Index_02_L.translate")
    cmds.setAttr("PlacementJnt_Index_02_R.translate", -1*TwoIndexTrans[0][0], -1*TwoIndexTrans[0][1], -1*TwoIndexTrans[0][2])

    TwoIndexRot = cmds.getAttr("PlacementJnt_Index_02_L.rotate")
    cmds.setAttr("PlacementJnt_Index_02_R.rotate", TwoIndexRot[0][0], TwoIndexRot[0][1], TwoIndexRot[0][2])

    #Two Middle
    TwoMiddleTrans = cmds.getAttr("PlacementJnt_Middle_02_L.translate")
    cmds.setAttr("PlacementJnt_Middle_02_R.translate", -1*TwoMiddleTrans[0][0], -1*TwoMiddleTrans[0][1], -1*TwoMiddleTrans[0][2])

    TwoMiddleRot = cmds.getAttr("PlacementJnt_Middle_02_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_02_R.rotate", TwoMiddleRot[0][0], TwoMiddleRot[0][1], TwoMiddleRot[0][2])

    #Two Ring
    TwoRingTrans = cmds.getAttr("PlacementJnt_Ring_02_L.translate")
    cmds.setAttr("PlacementJnt_Ring_02_R.translate", -1*TwoRingTrans[0][0], -1*TwoRingTrans[0][1], -1*TwoRingTrans[0][2])

    TwoRingRot = cmds.getAttr("PlacementJnt_Ring_02_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_02_R.rotate", TwoRingRot[0][0], TwoRingRot[0][1], TwoRingRot[0][2])

    #Two Pinky
    TwoPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_02_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_02_R.translate", -1*TwoPinkyTrans[0][0], -1*TwoPinkyTrans[0][1], -1*TwoPinkyTrans[0][2])

    TwoPinkyRot = cmds.getAttr("PlacementJnt_Pinky_02_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_02_R.rotate", TwoPinkyRot[0][0], TwoPinkyRot[0][1], TwoPinkyRot[0][2])

    #Three Index
    ThreeIndexTrans = cmds.getAttr("PlacementJnt_Index_03_L.translate")
    cmds.setAttr("PlacementJnt_Index_03_R.translate", -1*ThreeIndexTrans[0][0], -1*ThreeIndexTrans[0][1], -1*ThreeIndexTrans[0][2])

    ThreeIndexRot = cmds.getAttr("PlacementJnt_Index_03_L.rotate")
    cmds.setAttr("PlacementJnt_Index_03_R.rotate", ThreeIndexRot[0][0], ThreeIndexRot[0][1], ThreeIndexRot[0][2])

    #Three Middle
    ThreeMiddleTrans = cmds.getAttr("PlacementJnt_Middle_03_L.translate")
    cmds.setAttr("PlacementJnt_Middle_03_R.translate", -1*ThreeMiddleTrans[0][0], -1*ThreeMiddleTrans[0][1], -1*ThreeMiddleTrans[0][2])

    ThreeMiddleRot = cmds.getAttr("PlacementJnt_Middle_03_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_03_R.rotate", ThreeMiddleRot[0][0], ThreeMiddleRot[0][1], ThreeMiddleRot[0][2])

    #Three Ring
    ThreeRingTrans = cmds.getAttr("PlacementJnt_Ring_03_L.translate")
    cmds.setAttr("PlacementJnt_Ring_03_R.translate", -1*ThreeRingTrans[0][0], -1*ThreeRingTrans[0][1], -1*ThreeRingTrans[0][2])

    ThreeRingRot = cmds.getAttr("PlacementJnt_Ring_03_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_03_R.rotate", ThreeRingRot[0][0], ThreeRingRot[0][1], ThreeRingRot[0][2])

    #Three Pinky
    ThreePinkyTrans = cmds.getAttr("PlacementJnt_Pinky_03_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_03_R.translate", -1*ThreePinkyTrans[0][0], -1*ThreePinkyTrans[0][1], -1*ThreePinkyTrans[0][2])

    ThreePinkyRot = cmds.getAttr("PlacementJnt_Pinky_03_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_03_R.rotate", ThreePinkyRot[0][0], ThreePinkyRot[0][1], ThreePinkyRot[0][2])

    #End Thumb
    EndThumbTrans = cmds.getAttr("PlacementJnt_Thumb_end_L.translate")
    cmds.setAttr("PlacementJnt_Thumb_end_R.translate", -1*EndThumbTrans[0][0], -1*EndThumbTrans[0][1], -1*EndThumbTrans[0][2])

    EndThumbRot = cmds.getAttr("PlacementJnt_Thumb_end_L.rotate")
    cmds.setAttr("PlacementJnt_Thumb_end_R.rotate", EndThumbRot[0][0], EndThumbRot[0][1], EndThumbRot[0][2])

    #End Index
    EndIndexTrans = cmds.getAttr("PlacementJnt_Index_end_L.translate")
    cmds.setAttr("PlacementJnt_Index_end_R.translate", -1*EndIndexTrans[0][0], -1*EndIndexTrans[0][1], -1*EndIndexTrans[0][2])

    EndIndexRot = cmds.getAttr("PlacementJnt_Index_end_L.rotate")
    cmds.setAttr("PlacementJnt_Index_end_R.rotate", EndIndexRot[0][0], EndIndexRot[0][1], EndIndexRot[0][2])

    #End Middle
    EndMiddleTrans = cmds.getAttr("PlacementJnt_Middle_end_L.translate")
    cmds.setAttr("PlacementJnt_Middle_end_R.translate", -1*EndMiddleTrans[0][0], -1*EndMiddleTrans[0][1], -1*EndMiddleTrans[0][2])

    EndMiddleRot = cmds.getAttr("PlacementJnt_Middle_end_L.rotate")
    cmds.setAttr("PlacementJnt_Middle_end_R.rotate", EndMiddleRot[0][0], EndMiddleRot[0][1], EndMiddleRot[0][2])

    #End Ring
    EndRingTrans = cmds.getAttr("PlacementJnt_Ring_end_L.translate")
    cmds.setAttr("PlacementJnt_Ring_end_R.translate", -1*EndRingTrans[0][0], -1*EndRingTrans[0][1], -1*EndRingTrans[0][2])

    EndRingRot = cmds.getAttr("PlacementJnt_Ring_end_L.rotate")
    cmds.setAttr("PlacementJnt_Ring_end_R.rotate", EndRingRot[0][0], EndRingRot[0][1], EndRingRot[0][2])

    #End Pinky
    EndPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_end_L.translate")
    cmds.setAttr("PlacementJnt_Pinky_end_R.translate", -1*EndPinkyTrans[0][0], -1*EndPinkyTrans[0][1], -1*EndPinkyTrans[0][2])

    EndPinkyRot = cmds.getAttr("PlacementJnt_Pinky_end_L.rotate")
    cmds.setAttr("PlacementJnt_Pinky_end_R.rotate", EndPinkyRot[0][0], EndPinkyRot[0][1], EndPinkyRot[0][2])

def mirrorJointArmRtoL():
    # Clavicle
    ClavicleTrans = cmds.getAttr("PlacementJnt_Clavicle_R.translate")
    cmds.setAttr("PlacementJnt_Clavicle_L.translate", -1*ClavicleTrans[0][0], ClavicleTrans[0][1], ClavicleTrans[0][2])
    ClavicleRot = cmds.getAttr("PlacementJnt_Clavicle_R.rotate")
    cmds.setAttr("PlacementJnt_Clavicle_L.rotate", ClavicleRot[0][0], ClavicleRot[0][1], ClavicleRot[0][2])
    #Clevicle end
    ClavicleEndTrans = cmds.getAttr("PlacementJnt_Clavicle_end_R.translate")
    cmds.setAttr("PlacementJnt_Clavicle_end_L.translate", -1*ClavicleEndTrans[0][0], ClavicleEndTrans[0][1], -1*ClavicleEndTrans[0][2])
    ClavicleEndRot = cmds.getAttr("PlacementJnt_Clavicle_end_R.rotate")
    cmds.setAttr("PlacementJnt_Clavicle_end_L.rotate", ClavicleEndRot[0][0], ClavicleEndRot[0][1], ClavicleEndRot[0][2])
    # Arm
    ArmTrans = cmds.getAttr("PlacementJnt_Arm_R.translate")
    cmds.setAttr("PlacementJnt_Arm_L.translate", -1*ArmTrans[0][0], -1*ArmTrans[0][1], -1*ArmTrans[0][2])
    ArmRot = cmds.getAttr("PlacementJnt_Arm_R.rotate")
    cmds.setAttr("PlacementJnt_Arm_L.rotate", ArmRot[0][0], ArmRot[0][1], ArmRot[0][2])
    # Elbow
    ElbowTrans = cmds.getAttr("PlacementJnt_Elbow_R.translate")
    cmds.setAttr("PlacementJnt_Elbow_L.translate", -1*ElbowTrans[0][0], -1*ElbowTrans[0][1], -1*ElbowTrans[0][2])
    ElbowRot = cmds.getAttr("PlacementJnt_Elbow_R.rotate")
    cmds.setAttr("PlacementJnt_Elbow_L.rotate", ElbowRot[0][0], ElbowRot[0][1], ElbowRot[0][2])
    # Wrist
    WristTrans = cmds.getAttr("PlacementJnt_Wrist_R.translate")
    cmds.setAttr("PlacementJnt_Wrist_L.translate", -1*WristTrans[0][0], -1*WristTrans[0][1], -1*WristTrans[0][2])
    WristRot = cmds.getAttr("PlacementJnt_Wrist_R.rotate")
    cmds.setAttr("PlacementJnt_Wrist_L.rotate", WristRot[0][0], WristRot[0][1], WristRot[0][2])
    # Metacarpus Thumb
    MetacarpusThumbTrans = cmds.getAttr("PlacementJnt_Thumb_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Thumb_Metacarpus_L.translate", -1*MetacarpusThumbTrans[0][0], -1*MetacarpusThumbTrans[0][1], -1*MetacarpusThumbTrans[0][2])
    MetacarpusThumbRot = cmds.getAttr("PlacementJnt_Thumb_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Thumb_Metacarpus_L.rotate", MetacarpusThumbRot[0][0], MetacarpusThumbRot[0][1], MetacarpusThumbRot[0][2])
    # Metacarpus Index
    MetacarpusIndexTrans = cmds.getAttr("PlacementJnt_Index_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Index_Metacarpus_L.translate", -1*MetacarpusIndexTrans[0][0], -1*MetacarpusIndexTrans[0][1], -1*MetacarpusIndexTrans[0][2])
    MetacarpusIndexRot = cmds.getAttr("PlacementJnt_Index_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Index_Metacarpus_L.rotate", MetacarpusIndexRot[0][0], MetacarpusIndexRot[0][1], MetacarpusIndexRot[0][2])
    # Metacarpus Middle
    MetacarpusMiddleTrans = cmds.getAttr("PlacementJnt_Middle_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Middle_Metacarpus_L.translate", -1*MetacarpusMiddleTrans[0][0], -1*MetacarpusMiddleTrans[0][1], -1*MetacarpusMiddleTrans[0][2])
    MetacarpusMiddleRot = cmds.getAttr("PlacementJnt_Middle_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_Metacarpus_L.rotate", MetacarpusMiddleRot[0][0], MetacarpusMiddleRot[0][1], MetacarpusMiddleRot[0][2])
    # Metacarpus Ring
    MetacarpusRingTrans = cmds.getAttr("PlacementJnt_Ring_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Ring_Metacarpus_L.translate", -1*MetacarpusRingTrans[0][0], -1*MetacarpusRingTrans[0][1], -1*MetacarpusRingTrans[0][2])
    MetacarpusRingRot = cmds.getAttr("PlacementJnt_Ring_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_Metacarpus_L.rotate", MetacarpusRingRot[0][0], MetacarpusRingRot[0][1], MetacarpusRingRot[0][2])
    # Metacarpus Pinky
    MetacarpusPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_Metacarpus_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_Metacarpus_L.translate", -1*MetacarpusPinkyTrans[0][0], -1*MetacarpusPinkyTrans[0][1], -1*MetacarpusPinkyTrans[0][2])
    MetacarpusPinkyRot = cmds.getAttr("PlacementJnt_Pinky_Metacarpus_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_Metacarpus_L.rotate", MetacarpusPinkyRot[0][0], MetacarpusPinkyRot[0][1], MetacarpusPinkyRot[0][2])
    # One Thumb
    OneThumbTrans = cmds.getAttr("PlacementJnt_Thumb_01_R.translate")
    cmds.setAttr("PlacementJnt_Thumb_01_L.translate", -1*OneThumbTrans[0][0], -1*OneThumbTrans[0][1], -1*OneThumbTrans[0][2])
    OneThumbRot = cmds.getAttr("PlacementJnt_Thumb_01_R.rotate")
    cmds.setAttr("PlacementJnt_Thumb_01_L.rotate", OneThumbRot[0][0], OneThumbRot[0][1], OneThumbRot[0][2])
    # One Index
    OneIndexTrans = cmds.getAttr("PlacementJnt_Index_01_R.translate")
    cmds.setAttr("PlacementJnt_Index_01_L.translate", -1*OneIndexTrans[0][0], -1*OneIndexTrans[0][1], -1*OneIndexTrans[0][2])
    OneIndexRot = cmds.getAttr("PlacementJnt_Index_01_R.rotate")
    cmds.setAttr("PlacementJnt_Index_01_L.rotate", OneIndexRot[0][0], OneIndexRot[0][1], OneIndexRot[0][2])
    # One Middle
    OneMiddleTrans = cmds.getAttr("PlacementJnt_Middle_01_R.translate")
    cmds.setAttr("PlacementJnt_Middle_01_L.translate", -1*OneMiddleTrans[0][0], -1*OneMiddleTrans[0][1], -1*OneMiddleTrans[0][2])
    OneMiddleRot = cmds.getAttr("PlacementJnt_Middle_01_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_01_L.rotate", OneMiddleRot[0][0], OneMiddleRot[0][1], OneMiddleRot[0][2])
    # One Ring
    OneRingTrans = cmds.getAttr("PlacementJnt_Ring_01_R.translate")
    cmds.setAttr("PlacementJnt_Ring_01_L.translate", -1*OneRingTrans[0][0], -1*OneRingTrans[0][1], -1*OneRingTrans[0][2])
    OneRingRot = cmds.getAttr("PlacementJnt_Ring_01_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_01_L.rotate", OneRingRot[0][0], OneRingRot[0][1], OneRingRot[0][2])
    # One Pinky
    OnePinkyTrans = cmds.getAttr("PlacementJnt_Pinky_01_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_01_L.translate", -1*OnePinkyTrans[0][0], -1*OnePinkyTrans[0][1], -1*OnePinkyTrans[0][2])
    OnePinkyRot = cmds.getAttr("PlacementJnt_Pinky_01_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_01_L.rotate", OnePinkyRot[0][0], OnePinkyRot[0][1], OnePinkyRot[0][2])
    # Two Thumb
    TwoThumbTrans = cmds.getAttr("PlacementJnt_Thumb_02_R.translate")
    cmds.setAttr("PlacementJnt_Thumb_02_L.translate", -1*TwoThumbTrans[0][0], -1*TwoThumbTrans[0][1], -1*TwoThumbTrans[0][2])
    TwoThumbRot = cmds.getAttr("PlacementJnt_Thumb_02_R.rotate")
    cmds.setAttr("PlacementJnt_Thumb_02_L.rotate", TwoThumbRot[0][0], TwoThumbRot[0][1], TwoThumbRot[0][2])
    # Two Index
    TwoIndexTrans = cmds.getAttr("PlacementJnt_Index_02_R.translate")
    cmds.setAttr("PlacementJnt_Index_02_L.translate", -1*TwoIndexTrans[0][0], -1*TwoIndexTrans[0][1], -1*TwoIndexTrans[0][2])
    TwoIndexRot = cmds.getAttr("PlacementJnt_Index_02_R.rotate")
    cmds.setAttr("PlacementJnt_Index_02_L.rotate", TwoIndexRot[0][0], TwoIndexRot[0][1], TwoIndexRot[0][2])
    # Two Middle
    TwoMiddleTrans = cmds.getAttr("PlacementJnt_Middle_02_R.translate")
    cmds.setAttr("PlacementJnt_Middle_02_L.translate", -1*TwoMiddleTrans[0][0], -1*TwoMiddleTrans[0][1], -1*TwoMiddleTrans[0][2])
    TwoMiddleRot = cmds.getAttr("PlacementJnt_Middle_02_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_02_L.rotate", TwoMiddleRot[0][0], TwoMiddleRot[0][1], TwoMiddleRot[0][2])
    # Two Ring
    TwoRingTrans = cmds.getAttr("PlacementJnt_Ring_02_R.translate")
    cmds.setAttr("PlacementJnt_Ring_02_L.translate", -1*TwoRingTrans[0][0], -1*TwoRingTrans[0][1], -1*TwoRingTrans[0][2])
    TwoRingRot = cmds.getAttr("PlacementJnt_Ring_02_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_02_L.rotate", TwoRingRot[0][0], TwoRingRot[0][1], TwoRingRot[0][2])
    # Two Pinky
    TwoPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_02_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_02_L.translate", -1*TwoPinkyTrans[0][0], -1*TwoPinkyTrans[0][1], -1*TwoPinkyTrans[0][2])
    TwoPinkyRot = cmds.getAttr("PlacementJnt_Pinky_02_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_02_L.rotate", TwoPinkyRot[0][0], TwoPinkyRot[0][1], TwoPinkyRot[0][2])
    # Three Index
    ThreeIndexTrans = cmds.getAttr("PlacementJnt_Index_03_R.translate")
    cmds.setAttr("PlacementJnt_Index_03_L.translate", -1*ThreeIndexTrans[0][0], -1*ThreeIndexTrans[0][1], -1*ThreeIndexTrans[0][2])
    ThreeIndexRot = cmds.getAttr("PlacementJnt_Index_03_R.rotate")
    cmds.setAttr("PlacementJnt_Index_03_L.rotate", ThreeIndexRot[0][0], ThreeIndexRot[0][1], ThreeIndexRot[0][2])
    # Three Middle
    ThreeMiddleTrans = cmds.getAttr("PlacementJnt_Middle_03_R.translate")
    cmds.setAttr("PlacementJnt_Middle_03_L.translate", -1*ThreeMiddleTrans[0][0], -1*ThreeMiddleTrans[0][1], -1*ThreeMiddleTrans[0][2])
    ThreeMiddleRot = cmds.getAttr("PlacementJnt_Middle_03_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_03_L.rotate", ThreeMiddleRot[0][0], ThreeMiddleRot[0][1], ThreeMiddleRot[0][2])
    # Three Ring
    ThreeRingTrans = cmds.getAttr("PlacementJnt_Ring_03_R.translate")
    cmds.setAttr("PlacementJnt_Ring_03_L.translate", -1*ThreeRingTrans[0][0], -1*ThreeRingTrans[0][1], -1*ThreeRingTrans[0][2])
    ThreeRingRot = cmds.getAttr("PlacementJnt_Ring_03_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_03_L.rotate", ThreeRingRot[0][0], ThreeRingRot[0][1], ThreeRingRot[0][2])
    # Three Pinky
    ThreePinkyTrans = cmds.getAttr("PlacementJnt_Pinky_03_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_03_L.translate", -1*ThreePinkyTrans[0][0], -1*ThreePinkyTrans[0][1], -1*ThreePinkyTrans[0][2])
    ThreePinkyRot = cmds.getAttr("PlacementJnt_Pinky_03_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_03_L.rotate", ThreePinkyRot[0][0], ThreePinkyRot[0][1], ThreePinkyRot[0][2])
    # End Thumb
    EndThumbTrans = cmds.getAttr("PlacementJnt_Thumb_end_R.translate")
    cmds.setAttr("PlacementJnt_Thumb_end_L.translate", -1*EndThumbTrans[0][0], -1*EndThumbTrans[0][1], -1*EndThumbTrans[0][2])
    EndThumbRot = cmds.getAttr("PlacementJnt_Thumb_end_R.rotate")
    cmds.setAttr("PlacementJnt_Thumb_end_L.rotate", EndThumbRot[0][0], EndThumbRot[0][1], EndThumbRot[0][2])
    # End Index
    EndIndexTrans = cmds.getAttr("PlacementJnt_Index_end_R.translate")
    cmds.setAttr("PlacementJnt_Index_end_L.translate", -1*EndIndexTrans[0][0], -1*EndIndexTrans[0][1], -1*EndIndexTrans[0][2])
    EndIndexRot = cmds.getAttr("PlacementJnt_Index_end_R.rotate")
    cmds.setAttr("PlacementJnt_Index_end_L.rotate", EndIndexRot[0][0], EndIndexRot[0][1], EndIndexRot[0][2])
    # End Middle
    EndMiddleTrans = cmds.getAttr("PlacementJnt_Middle_end_R.translate")
    cmds.setAttr("PlacementJnt_Middle_end_L.translate", -1*EndMiddleTrans[0][0], -1*EndMiddleTrans[0][1], -1*EndMiddleTrans[0][2])
    EndMiddleRot = cmds.getAttr("PlacementJnt_Middle_end_R.rotate")
    cmds.setAttr("PlacementJnt_Middle_end_L.rotate", EndMiddleRot[0][0], EndMiddleRot[0][1], EndMiddleRot[0][2])
    # End Ring
    EndRingTrans = cmds.getAttr("PlacementJnt_Ring_end_R.translate")
    cmds.setAttr("PlacementJnt_Ring_end_L.translate", -1*EndRingTrans[0][0], -1*EndRingTrans[0][1], -1*EndRingTrans[0][2])
    EndRingRot = cmds.getAttr("PlacementJnt_Ring_end_R.rotate")
    cmds.setAttr("PlacementJnt_Ring_end_L.rotate", EndRingRot[0][0], EndRingRot[0][1], EndRingRot[0][2])
    # End Pinky
    EndPinkyTrans = cmds.getAttr("PlacementJnt_Pinky_end_R.translate")
    cmds.setAttr("PlacementJnt_Pinky_end_L.translate", -1*EndPinkyTrans[0][0], -1*EndPinkyTrans[0][1], -1*EndPinkyTrans[0][2])
    EndPinkyRot = cmds.getAttr("PlacementJnt_Pinky_end_R.rotate")
    cmds.setAttr("PlacementJnt_Pinky_end_L.rotate", EndPinkyRot[0][0], EndPinkyRot[0][1], EndPinkyRot[0][2])


