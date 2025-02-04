#create a function that match the Ik and Fk CTRL to the same position

import maya.cmds as cmds
import maya.api.OpenMaya as om
import math

def PoleVector(joint_1, joint_2, joint_3, CTRL):
    a = om.MVector(cmds.xform(joint_1, q=True, rp=True, ws=True))
    b = om.MVector(cmds.xform(joint_2, q=True, rp=True, ws=True))
    c = om.MVector(cmds.xform(joint_3, q=True, rp=True, ws=True))
    
    start_to_end = c-a
    mid_to_end = c-b
    start_to_mid = b-a
    
    len_start_to_mid= om.MVector.length(start_to_mid)
    len_mid_to_end= om.MVector.length(mid_to_end)
    len_start_to_end= om.MVector.length(start_to_end)
    angle_BAC = om.MVector.angle(start_to_end,start_to_mid)
        
    mid_point = math.cos(angle_BAC) * len_start_to_mid * (start_to_end/len_start_to_end)
    
    mid = mid_point + a
    
    projection = b - mid
    len_projection = om.MVector.length(projection)
    mult = ((len_start_to_mid+len_mid_to_end)/2)/len_projection
    projection *= mult
    projection += b


    cmds.setAttr('{}.translateX'.format(CTRL), projection.x)
    cmds.setAttr('{}.translateY'.format(CTRL), projection.y)
    cmds.setAttr('{}.translateZ'.format(CTRL), projection.z)

def matchIkFk(CTRL, Member):
    if Member == "Arm L":
        BaseJnt = "FK_Arm_L"
        MediumJnt = "FK_Elbow_L"
        EndJnt = "FK_Wrist_L"

        BaseIKCTRL = "CTRL_Wrist_L"

        BaseCTRL = "CTRL_FK_Arm_L"
        MediumCTRL = "CTRL_FK_Elbow_L"
        EndCTRL = "CTRL_FK_Wrist_L"

        PV = "PV_Arm_L"
    if Member == "Arm R":
        BaseJnt = "FK_Arm_R"
        MediumJnt = "FK_Elbow_R"
        EndJnt = "FK_Wrist_R"

        BaseIKCTRL = "CTRL_Wrist_R"

        BaseCTRL = "CTRL_FK_Arm_R"
        MediumCTRL = "CTRL_FK_Elbow_R"
        EndCTRL = "CTRL_FK_Wrist_R"

        PV = "PV_Arm_R"
    if Member == "Leg L":
        BaseJnt = "FK_Leg_L"
        MediumJnt = "FK_Knee_L"
        EndJnt = "FK_Ankle_L"

        BaseIKCTRL = "CTRL_Foot_L"

        BaseCTRL = "CTRL_FK_Leg_L"
        MediumCTRL = "CTRL_FK_Knee_L"
        EndCTRL = "CTRL_FK_Ankle_L"

        PV = "PV_Leg_L"
    if Member == "Leg R":
        BaseJnt = "FK_Leg_R"
        MediumJnt = "FK_Knee_R"
        EndJnt = "FK_Ankle_R"

        BaseIKCTRL = "CTRL_Foot_R"

        BaseCTRL = "CTRL_FK_Leg_R"
        MediumCTRL = "CTRL_FK_Knee_R"
        EndCTRL = "CTRL_FK_Ankle_R"

        PV = "PV_Leg_R"

    #get the relative path of the CTRLs
    AllPath = cmds.listRelatives(CTRL, f=True)
    AllPath = AllPath[0]
    Split = AllPath.split("|")
    name = Split[1]
    print(name)
    print(Split)

    # get the rotation of the DrvJnt and apply it to the corresponding FK CTRL 
    if "Leg" in Member:
        grp = Member.replace(" ", "_")
        BaseDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Legs|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}'
        MediumDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Legs|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}|{MediumJnt}'
        EndDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Legs|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}|{MediumJnt}|{EndJnt}'
    if "Arm" in Member:
        grp = Member.replace(" ", "_")
        BaseDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Arms|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}'
        MediumDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Arms|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}|{MediumJnt}'
        EndDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Arms|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}|{MediumJnt}|{EndJnt}'

    EndFK = f'|{name}|GlobalMove_01|CTRLs_01|{BaseCTRL}_Offset|{BaseCTRL}_Hook|{BaseCTRL}_Move|{BaseCTRL}|{MediumCTRL}_Offset|{MediumCTRL}|{EndCTRL}_Offset|{EndCTRL}'
    PoleVec = f'|{name}|GlobalMove_01|CTRLs_01|{PV}_Offset|{PV}'

    if "Leg" in Member:
        CtrlIK = f'|{name}|GlobalMove_01|CTRLs_01|{BaseIKCTRL}'
    else:
        CtrlIK = f'|{name}|GlobalMove_01|CTRLs_01|{BaseIKCTRL}_Offset|{BaseIKCTRL}'

    # Replace the pole vector 
    Loc = cmds.spaceLocator(n="TempLoc")[0]
    PoleVector(BaseDrvJnt, MediumDrvJnt, EndDrvJnt, Loc)

    cmds.matchTransform(PoleVec, Loc)
    cmds.delete(Loc)

    #get the position of the FK CTRL and apply it to the corresponding IK CTRL
    cmds.matchTransform(CtrlIK, EndFK)

def matchFkIk(CTRL, Member):
    if Member == "Arm L":
        BaseJnt = "DrvJnt_Arm_L"
        MediumJnt = "DrvJnt_Elbow_L"
        EndJnt = "DrvJnt_Wrist_L"

        BaseCTRL = "CTRL_FK_Arm_L"
        MediumCTRL = "CTRL_FK_Elbow_L"
        EndCTRL = "CTRL_FK_Wrist_L"
    if Member == "Arm R":
        BaseJnt = "DrvJnt_Arm_R"
        MediumJnt = "DrvJnt_Elbow_R"
        EndJnt = "DrvJnt_Wrist_R"

        BaseCTRL = "CTRL_FK_Arm_R"
        MediumCTRL = "CTRL_FK_Elbow_R"
        EndCTRL = "CTRL_FK_Wrist_R"
    if Member == "Leg L":
        BaseJnt = "DrvJnt_Leg_L"
        MediumJnt = "DrvJnt_Knee_L"
        EndJnt = "DrvJnt_Ankle_L"

        BaseCTRL = "CTRL_FK_Leg_L"
        MediumCTRL = "CTRL_FK_Knee_L"
        EndCTRL = "CTRL_FK_Ankle_L"
    if Member == "Leg R":
        BaseJnt = "DrvJnt_Leg_R"
        MediumJnt = "DrvJnt_Knee_R"
        EndJnt = "DrvJnt_Ankle_R"

        BaseCTRL = "CTRL_FK_Leg_R"
        MediumCTRL = "CTRL_FK_Knee_R"
        EndCTRL = "CTRL_FK_Ankle_R"

    #get the relative path of the CTRLs
    AllPath = cmds.listRelatives(CTRL, f=True)
    AllPath = AllPath[0]
    Split = AllPath.split("|")
    name = Split[1]
    print(name)
    print(Split)

    # get the rotation of the DrvJnt and apply it to the corresponding FK CTRL 
    if "Leg" in Member:
        grp = Member.replace(" ", "_")
        BaseDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Legs|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}'
        MediumDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Legs|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}|{MediumJnt}'
        EndDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Legs|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}|{MediumJnt}|{EndJnt}'
    if "Arm" in Member:
        grp = Member.replace(" ", "_")
        BaseDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Arms|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}'
        MediumDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Arms|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}|{MediumJnt}'
        EndDrvJnt = f'|{name}|GlobalMove_01|Joints_01|Joints_Arms|Joints_{grp}|{BaseJnt}_Offset|{BaseJnt}_Hook|{BaseJnt}_Move|{BaseJnt}|{MediumJnt}|{EndJnt}'
    #get the rotation of the DrvJnt and apply it to the corresponding FK CTRL
    BaseDrvJntRot = cmds.xform(BaseDrvJnt, q=True, ro=True)
    MediumDrvJntRot = cmds.xform(MediumDrvJnt, q=True, ro=True)
    EndDrvJntRot = cmds.xform(EndDrvJnt, q=True, ro=True)

    BaseFK = f'|{name}|GlobalMove_01|CTRLs_01|{BaseCTRL}_Offset|{BaseCTRL}_Hook|{BaseCTRL}_Move|{BaseCTRL}'
    MediumFK = f'|{name}|GlobalMove_01|CTRLs_01|{BaseCTRL}_Offset|{BaseCTRL}_Hook|{BaseCTRL}_Move|{BaseCTRL}|{MediumCTRL}_Offset|{MediumCTRL}'
    EndFK = f'|{name}|GlobalMove_01|CTRLs_01|{BaseCTRL}_Offset|{BaseCTRL}_Hook|{BaseCTRL}_Move|{BaseCTRL}|{MediumCTRL}_Offset|{MediumCTRL}|{EndCTRL}_Offset|{EndCTRL}'

    cmds.setAttr(f'{BaseFK}.rotateX', BaseDrvJntRot[0])
    cmds.setAttr(f'{BaseFK}.rotateY', BaseDrvJntRot[1])
    cmds.setAttr(f'{BaseFK}.rotateZ', BaseDrvJntRot[2])

    cmds.setAttr(f'{MediumFK}.rotateX', MediumDrvJntRot[0])
    cmds.setAttr(f'{MediumFK}.rotateY', MediumDrvJntRot[1])
    cmds.setAttr(f'{MediumFK}.rotateZ', MediumDrvJntRot[2])

    cmds.setAttr(f'{EndFK}.rotateX', EndDrvJntRot[0])
    cmds.setAttr(f'{EndFK}.rotateY', EndDrvJntRot[1])
    cmds.setAttr(f'{EndFK}.rotateZ', EndDrvJntRot[2])