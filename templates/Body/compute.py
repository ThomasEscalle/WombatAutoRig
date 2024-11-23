import maya.cmds as cmds
from wombatAutoRig.templates.Body import computeThomas
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import PoleVector
from wombatAutoRig.src.core import MatrixConstrain
from wombatAutoRig.src.core import Ribbon



def compute(settings):


    #region Leg L

    #Creating the joints 
    cmds.duplicate("PlacementJnt_Root", n="Bind_Root", po = True)
    cmds.duplicate("PlacementJnt_Hip_L", n="Bind_Hip_L", po = True)
    
    cmds.duplicate("PlacementJnt_Hip_L", n="DrvJnt_Leg_L", po=True)
    Color.setColor("DrvJnt_Leg_L", "yellow")
    cmds.duplicate("PlacementJnt_Knee_L", n="DrvJnt_Knee_L", po=True)
    Color.setColor("DrvJnt_Knee_L", "yellow")
    cmds.duplicate("PlacementJnt_Ankle_L", n="DrvJnt_Ankle_L", po=True)
    Color.setColor("DrvJnt_Ankle_L", "yellow")
    
    cmds.duplicate("PlacementJnt_Hip_L", n="FK_Leg_L", po=True)
    Color.setColor("FK_Leg_L", "blue")
    cmds.duplicate("PlacementJnt_Knee_L", n="FK_Knee_L", po=True)
    Color.setColor("FK_Knee_L", "blue")
    cmds.duplicate("PlacementJnt_Ankle_L", n="FK_Ankle_L", po=True)
    Color.setColor("FK_Ankle_L", "blue")
    cmds.duplicate("PlacementJnt_Ball_L", n="FK_Ball_L", po=True)
    Color.setColor("FK_Ball_L", "blue")
    cmds.duplicate("PlacementJnt_Toe_L", n="FK_Toe_L", po=True)
    Color.setColor("FK_Toe_L", "blue")
    
    
    cmds.duplicate("PlacementJnt_Knee_L", n="Preserve_Knee_L", po=True)
    
    #Unparenting the joints
    
    cmds.parent("Bind_Root", world=True)
    cmds.parent("Bind_Hip_L", world=True)
    cmds.parent("DrvJnt_Leg_L", world=True)
    cmds.parent("DrvJnt_Knee_L", world=True)
    cmds.parent("DrvJnt_Ankle_L", world=True)
    cmds.parent("FK_Leg_L", world=True)
    cmds.parent("FK_Knee_L", world=True)
    cmds.parent("FK_Ankle_L", world=True)
    cmds.parent("Preserve_Knee_L", world=True)
    
    #Reparenting the joints
    
    cmds.parent("Bind_Hip_L", "Bind_Root")
    cmds.parent("DrvJnt_Knee_L", "DrvJnt_Leg_L")
    cmds.parent("DrvJnt_Ankle_L", "DrvJnt_Knee_L")
    cmds.parent("FK_Knee_L", "FK_Leg_L")
    cmds.parent("FK_Ankle_L", "FK_Knee_L")
    
    #Offset for the joints
    
    Offset.offset("Bind_Root", nbr=3)
    Offset.offset("DrvJnt_Leg_L", nbr=3)
    Offset.offset("FK_Leg_L", nbr=3)
    Offset.offset("Preserve_Knee_L", nbr=3)
    
    #Rangement des joints dans un groupe
    cmds.group(n="Joints_Legs", em=True)
    cmds.group(n="Joints_Leg_L", em=True)
    cmds.parent("Joints_Leg_L", "Joints_Legs")
    cmds.parent("Joints_Legs", "{}|GlobalMove_01|Joints_01".format(settings["name"]))
    cmds.parent("Bind_Root_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_L".format(settings["name"]))
    cmds.parent("DrvJnt_Leg_L_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_L".format(settings["name"]))
    cmds.parent("FK_Leg_L_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_L".format(settings["name"]))
    cmds.parent("Preserve_Knee_L_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_L".format(settings["name"]))
    
    #Creating a controller for the preserve Knee to be in
    cmds.duplicate("PlacementCtrl_knee_L", n="CTRL_Preserve_Knee_L")
    cmds.parent("CTRL_Preserve_Knee_L", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_L|Preserve_Knee_L_Offset|Preserve_Knee_L_Hook|Preserve_Knee_L_Move".format(settings["name"]))
    cmds.parent("Preserve_Knee_L", "CTRL_Preserve_Knee_L")
    
    #Creating the IK handle
    cmds.ikHandle(n="IK_Leg_L", sj="DrvJnt_Leg_L", ee="DrvJnt_Ankle_L", sol="ikRPsolver")
    cmds.parent("IK_Leg_L", "{}|GlobalMove_01|IKs_01".format(settings["name"]))
    Locator = cmds.spaceLocator(n="PoleVector_L")
    Color.setColor("PoleVector_L", "green")
    PoleVector.PoleVector(joint_1="DrvJnt_Leg_L", joint_2="DrvJnt_Knee_L", joint_3="DrvJnt_Ankle_L", CTRL="PoleVector_L")
    Offset.offset("PoleVector_L", nbr=1)
    cmds.poleVectorConstraint(Locator, "IK_Leg_L")
    cmds.parent("PoleVector_L_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    
    #Attach Joints chain To Hip
    Bind_Hip_L = ["Bind_Hip_L"]
    DrvJnt_Knee_L = ["DrvJnt_Knee_L"]
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, "DrvJnt_Leg_L_Hook", Offset=False, sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, "FK_Leg_L_Hook", Offset=False, sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Knee_L, "Preserve_Knee_L_Hook", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    
    #Creating a switch for the IK FK
    cmds.duplicate("PlacementCtrl_Switch_Leg_L", n="Switch_Leg_L")
    cmds.parent("Switch_Leg_L", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    cmds.addAttr("Switch_Leg_L", ln="IK_FK", at="enum", en="FK:IK", k=True)
    cmds.setAttr("Switch_Leg_L.tx", keyable=False, channelBox=False)
    cmds.setAttr("Switch_Leg_L.ty", keyable=False, channelBox=False)
    cmds.setAttr("Switch_Leg_L.tz", keyable=False, channelBox=False)
    cmds.setAttr("Switch_Leg_L.rx", keyable=False, channelBox=False)
    cmds.setAttr("Switch_Leg_L.ry", keyable=False, channelBox=False)
    cmds.setAttr("Switch_Leg_L.rz", keyable=False, channelBox=False)
    cmds.setAttr("Switch_Leg_L.sx", keyable=False, channelBox=False)
    cmds.setAttr("Switch_Leg_L.sy", keyable=False, channelBox=False)
    cmds.setAttr("Switch_Leg_L.sz", keyable=False, channelBox=False)
    Color.setColor("Switch_Leg_L", "yellow")
    Offset.offset("Switch_Leg_L", nbr=2)
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, "Switch_Leg_L_Move", Offset=True, sX=False, sY=False, sZ=False)
    
    #Attach Ribbon to DrvJnt
    Ribbon.Ribbon(Name="Ribbon_Leg_L", Span=5)
    Ribbon.Ribbon(Name="Ribbon_Knee_L", Span=5)
    
    cmds.group(n="Ribbons_Legs_Hide", em=True)
    cmds.parent("Ribbons_Legs_Hide", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    cmds.parent("Grp_Ribbon_Leg_L|Grp_Extra_Nodes_Ribbon_Leg_L|Grp_Extra_Nodes_To_Hide_Ribbon_Leg_L", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01|Ribbons_Legs_Hide".format(settings["name"]))
    
    cmds.group(n="Ribbons_Legs", em=True)
    cmds.parent("Ribbons_Legs", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01".format(settings["name"]))
    cmds.parent("Grp_Ribbon_Leg_L", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs".format(settings["name"]))
    
    DrvJnt_Leg_L = ["DrvJnt_Leg_L"]
    MatrixConstrain.MatrixConstrain(("DrvJnt_Leg_L", "DrvJnt_Knee_L"), "CTRL_Global_Ribbon_Leg_L", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, "CTRL_Global_Ribbon_Leg_L", Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    cmds.delete("IS_CONSTRAIN_BY___DrvJnt_Leg_L__")
    cmds.rotate(90, 0, 0, "CTRL_Global_Ribbon_Leg_L", r=True, os=True)
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, "CTRL_Global_Ribbon_Leg_L", Offset=True, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    
    cmds.parent("Grp_Ribbon_Knee_L|Grp_Extra_Nodes_Ribbon_Knee_L|Grp_Extra_Nodes_To_Hide_Ribbon_Knee_L", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01|Ribbons_Legs_Hide".format(settings["name"]))
    
    cmds.parent("Grp_Ribbon_Knee_L", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs".format(settings["name"]))
    
    DrvJnt_Knee_L_Ribbon = ["DrvJnt_Knee_L"]
    MatrixConstrain.MatrixConstrain(("DrvJnt_Knee_L", "DrvJnt_Ankle_L"), "CTRL_Global_Ribbon_Knee_L", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Knee_L, "CTRL_Global_Ribbon_Knee_L", Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    cmds.delete("{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs|Grp_Ribbon_Knee_L|CTRL_Global_Ribbon_Knee_L|IS_CONSTRAIN_BY___DrvJnt_Knee_L__".format(settings["name"]))
    cmds.rotate(90, 0, 0, "CTRL_Global_Ribbon_Knee_L", r=True, os=True)
    MatrixConstrain.MatrixConstrain(DrvJnt_Knee_L_Ribbon, "CTRL_Global_Ribbon_Knee_L", Offset=True, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    
    DrvJnt_Ankle_L = ["DrvJnt_Ankle_L"]
    Preserve_Knee_L = ["Preserve_Knee_L"]
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, "CTRL_End_Ribbon_Leg_L", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Ankle_L, "CTRL_Start_Ribbon_Knee_L", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(Preserve_Knee_L, "CTRL_End_Ribbon_Knee_L", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(Preserve_Knee_L, "CTRL_Start_Ribbon_Leg_L", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    

    #endregion Leg L 
    
    computeThomas.compute(settings)
    
    
    #Connecting the FK and IK to the switch (FK rotate into DrvJnt rotate)
    cmds.connectAttr("Switch_Leg_L.IK_FK", "IK_Leg_L.ikBlend")
    cmds.connectAttr("Switch_Leg_L.IK_FK", "IK_Ball_L.ikBlend")
    cmds.connectAttr("Switch_Leg_L.IK_FK", "IK_Toe_L.ikBlend")
    
    cmds.connectAttr("FK_Leg_L.rotate", "DrvJnt_Leg_L.rotate")
    cmds.connectAttr("FK_Knee_L.rotate", "DrvJnt_Knee_L.rotate")
    cmds.connectAttr("FK_Ankle_L.rotate", "DrvJnt_Ankle_L.rotate")
    cmds.connectAttr("FK_Ball_L.rotate", "Bind_Ball_L.rotate")
    cmds.connectAttr("FK_Toe_L.rotate", "Bind_Toe_L.rotate")
    
    cmds.createNode("reverse", asUtility=True, n="Reverse_Leg_L")
    cmds.connectAttr("Switch_Leg_L.IK_FK", "Reverse_Leg_L.inputX")