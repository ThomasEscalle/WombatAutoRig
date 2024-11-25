import maya.cmds as cmds
from wombatAutoRig.templates.Body import computeThomas
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import PoleVector
from wombatAutoRig.src.core import MatrixConstrain
from wombatAutoRig.src.core import Ribbon
from wombatAutoRig.src.core import TwistExtractor


def compute(settings):
    cmds.duplicate("PlacementJnt_Root", n="Bind_Root", po = True)
    cmds.parent(f"Bind_Root", world=True)
    Offset.offset("Bind_Root", nbr=3)


    createLeg(settings, "L")
    createLeg(settings, "R")

def createLeg(settings, side = "L"):


    #region Leg 

    #region Creating the joints 
    
    cmds.duplicate(f"PlacementJnt_Hip_{side}", n=f"Bind_Hip_{side}", po = True)
    
    cmds.duplicate(f"PlacementJnt_Hip_{side}", n=f"DrvJnt_Leg_{side}", po=True)
    Color.setColor(f"DrvJnt_Leg_{side}", "yellow")
    cmds.duplicate(f"PlacementJnt_Knee_{side}", n=f"DrvJnt_Knee_{side}", po=True)
    Color.setColor(f"DrvJnt_Knee_{side}", "yellow")
    cmds.duplicate(f"PlacementJnt_Ankle_{side}", n=f"DrvJnt_Ankle_{side}", po=True)
    Color.setColor(f"DrvJnt_Ankle_{side}", "yellow")
    
    cmds.duplicate(f"PlacementJnt_Hip_{side}", n=f"FK_Leg_{side}", po=True)
    Color.setColor(f"FK_Leg_{side}", "blue")
    cmds.duplicate(f"PlacementJnt_Knee_{side}", n=f"FK_Knee_{side}", po=True)
    Color.setColor(f"FK_Knee_{side}", "blue")
    cmds.duplicate(f"PlacementJnt_Ankle_{side}", n=f"FK_Ankle_{side}", po=True)
    Color.setColor(f"FK_Ankle_{side}", "blue")
    cmds.duplicate(f"PlacementJnt_Ball_{side}", n=f"FK_Ball_{side}", po=True)
    Color.setColor(f"FK_Ball_{side}", "blue")
    cmds.duplicate(f"PlacementJnt_Toe_{side}", n=f"FK_Toe_{side}", po=True)
    Color.setColor(f"FK_Toe_{side}", "blue")
    
    
    cmds.duplicate(f"PlacementJnt_Knee_{side}", n=f"Preserve_Knee_{side}", po=True)

    #Freeze the transform

    cmds.makeIdentity(f"Bind_Hip_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"DrvJnt_Leg_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"DrvJnt_Knee_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"DrvJnt_Ankle_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"FK_Leg_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"FK_Knee_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"FK_Ankle_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"FK_Ball_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"FK_Toe_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"Preserve_Knee_{side}", a=True, t=True, r=True, s=True)

    #Unparenting the joints
    
    
    cmds.parent(f"Bind_Hip_{side}", world=True)
    cmds.parent(f"DrvJnt_Leg_{side}", world=True)
    cmds.parent(f"DrvJnt_Knee_{side}", world=True)
    cmds.parent(f"DrvJnt_Ankle_{side}", world=True)
    cmds.parent(f"FK_Leg_{side}", world=True)
    cmds.parent(f"FK_Knee_{side}", world=True)
    cmds.parent(f"FK_Ankle_{side}", world=True)
    cmds.parent(f"Preserve_Knee_{side}", world=True)
    
    #Reparenting the joints
    
    cmds.parent(f"Bind_Hip_{side}", f"Bind_Root")
    cmds.parent(f"DrvJnt_Knee_{side}", f"DrvJnt_Leg_{side}")
    cmds.parent(f"DrvJnt_Ankle_{side}", f"DrvJnt_Knee_{side}")
    cmds.parent(f"FK_Knee_{side}", f"FK_Leg_{side}")
    cmds.parent(f"FK_Ankle_{side}", f"FK_Knee_{side}")
    cmds.parent(f"FK_Ball_{side}", f"FK_Ankle_{side}")
    cmds.parent(f"FK_Toe_{side}", f"FK_Ball_{side}")
    
    #Offset for the joints
    

    Offset.offset(f"DrvJnt_Leg_{side}", nbr=3)
    Offset.offset(f"FK_Leg_{side}", nbr=3)
    Offset.offset(f"Preserve_Knee_{side}", nbr=3)
    
    #Rangement des joints dans un groupe

    # Check if "Joints_Legs" exists, if not create it
    if not cmds.objExists("Joints_Legs"):
        cmds.group(n=f"Joints_Legs", em=True)
        cmds.parent("Joints_Legs", "{}|GlobalMove_01|Joints_01".format(settings["name"]))

    cmds.group(n=f"Joints_Leg_{side}", em=True)
    cmds.parent(f"Joints_Leg_{side}", "Joints_Legs")
    cmds.parent(f"Bind_Root_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_{}".format(settings["name"] , side))
    cmds.parent(f"DrvJnt_Leg_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_{}".format(settings["name"], side))
    cmds.parent(f"FK_Leg_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_{}".format(settings["name"], side))
    cmds.parent(f"Preserve_Knee_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_{}".format(settings["name"], side))
    
    #region Creating CTRL Pin
    cmds.duplicate(f"PlacementCtrl_knee_{side}", n=f"CTRL_Preserve_Knee_{side}")
    cmds.parent(f"CTRL_Preserve_Knee_{side}", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_{}|Preserve_Knee_{}_Offset|Preserve_Knee_{}_Hook|Preserve_Knee_{}_Move".format(settings["name"], side, side, side, side))
    cmds.parent(f"Preserve_Knee_{side}", f"CTRL_Preserve_Knee_{side}")
    cmds.createNode('multiplyDivide', n=f"MD_Preserve_Knee_{side}")
    cmds.connectAttr(f"DrvJnt_Knee_{side}.ry", f"MD_Preserve_Knee_{side}.input1X")
    cmds.connectAttr(f"MD_Preserve_Knee_{side}.outputX", f"Preserve_Knee_{side}_Move.ry")
    cmds.setAttr(f"MD_Preserve_Knee_{side}.input2X", 0.5)
    
    #region Creating the IK handle
    cmds.ikHandle(n=f"IK_Leg_{side}", sj=f"DrvJnt_Leg_{side}", ee=f"DrvJnt_Ankle_{side}", sol="ikRPsolver")
    cmds.parent(f"IK_Leg_{side}", "{}|GlobalMove_01|IKs_01".format(settings["name"]))
    Locator = cmds.spaceLocator(n=f"PoleVector_{side}")
    Color.setColor(f"PoleVector_{side}", "green")
    PoleVector.PoleVector(joint_1=f"DrvJnt_Leg_{side}", joint_2=f"DrvJnt_Knee_{side}", joint_3=f"DrvJnt_Ankle_{side}", CTRL=f"PoleVector_{side}")
    Offset.offset(f"PoleVector_{side}", nbr=1)
    cmds.poleVectorConstraint(Locator, f"IK_Leg_{side}")
    cmds.parent(f"PoleVector_{side}_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    
    #region Attach Joints 
    Bind_Hip_L = [f"Bind_Hip_{side}"]
    DrvJnt_Leg_L = [f"DrvJnt_Leg_{side}"]
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, f"DrvJnt_Leg_{side}_Hook", Offset=False, sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, f"FK_Leg_{side}_Hook", Offset=False, sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, f"Preserve_Knee_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False)
    
    #region switch IK FK 
    cmds.duplicate(f"PlacementCtrl_Switch_Leg_{side}", n=f"Switch_Leg_{side}")
    cmds.parent(f"Switch_Leg_{side}", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    cmds.addAttr(f"Switch_Leg_{side}", ln="IK_FK", at="enum", en="FK:IK", k=True)
    cmds.addAttr(f"Switch_Leg_{side}", ln="Vis_Bend", at="bool", nn="Vis Bend", k=True)
    cmds.addAttr(f"Switch_Leg_{side}", ln="Vis_Pin", at="bool", nn="Vis Pin", k=True)
    cmds.setAttr(f"Switch_Leg_{side}.tx", keyable=False, channelBox=False)
    cmds.setAttr(f"Switch_Leg_{side}.ty", keyable=False, channelBox=False)
    cmds.setAttr(f"Switch_Leg_{side}.tz", keyable=False, channelBox=False)
    cmds.setAttr(f"Switch_Leg_{side}.rx", keyable=False, channelBox=False)
    cmds.setAttr(f"Switch_Leg_{side}.ry", keyable=False, channelBox=False)
    cmds.setAttr(f"Switch_Leg_{side}.rz", keyable=False, channelBox=False)
    cmds.setAttr(f"Switch_Leg_{side}.sx", keyable=False, channelBox=False)
    cmds.setAttr(f"Switch_Leg_{side}.sy", keyable=False, channelBox=False)
    cmds.setAttr(f"Switch_Leg_{side}.sz", keyable=False, channelBox=False)
    Offset.offset(f"Switch_Leg_{side}", nbr=2)
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, f"Switch_Leg_{side}_Move", Offset=True, sX=False, sY=False, sZ=False)
    cmds.setAttr(f"Switch_Leg_{side}.IK_FK", 1)
    
    #region Ribbon
    Ribbon.Ribbon(Name=f"Ribbon_Leg_{side}", Span=5)
    Ribbon.Ribbon(Name=f"Ribbon_Knee_{side}", Span=5)
    
    if not cmds.objExists("Ribbons_Legs_Hide"):
        cmds.group(n="Ribbons_Legs_Hide", em=True)
        cmds.parent("Ribbons_Legs_Hide", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))

    cmds.parent(f"Grp_Ribbon_Leg_{side}|Grp_Extra_Nodes_Ribbon_Leg_{side}|Grp_Extra_Nodes_To_Hide_Ribbon_Leg_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01|Ribbons_Legs_Hide".format(settings["name"]))
    

    if not cmds.objExists("Ribbons_Legs"):
        cmds.group(n="Ribbons_Legs", em=True)
        cmds.parent("Ribbons_Legs", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01".format(settings["name"]))
    cmds.parent(f"Grp_Ribbon_Leg_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs".format(settings["name"]))
    
    DrvJnt_Leg_L = [f"DrvJnt_Leg_{side}"]
    MatrixConstrain.MatrixConstrain((f"DrvJnt_Leg_{side}", f"DrvJnt_Knee_{side}"), f"CTRL_Global_Ribbon_Leg_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs|Grp_Ribbon_Leg_{}|CTRL_Global_Ribbon_Leg_{}".format(settings["name"], side,side), Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    cmds.delete("{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs|Grp_Ribbon_Leg_{}|CTRL_Global_Ribbon_Leg_{}|IS_CONSTRAIN_BY___DrvJnt_Leg_{}__".format(settings["name"], side ,side ,side))
    cmds.rotate(90, 0, 0, f"CTRL_Global_Ribbon_Leg_{side}", r=True, os=True)
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, f"CTRL_Global_Ribbon_Leg_{side}", Offset=True, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    CTRL_Shape_Leg = cmds.listRelatives(f"CTRL_Global_Ribbon_Knee_{side}", shapes=True)
    cmds.setAttr(CTRL_Shape_Leg[0] + ".lodVisibility", 0)
    
    cmds.parent(f"Grp_Ribbon_Knee_{side}|Grp_Extra_Nodes_Ribbon_Knee_{side}|Grp_Extra_Nodes_To_Hide_Ribbon_Knee_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01|Ribbons_Legs_Hide".format(settings["name"]))
    
    cmds.parent(f"Grp_Ribbon_Knee_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs".format(settings["name"]))
    
    DrvJnt_Knee_L = [f"DrvJnt_Knee_{side}"]
    MatrixConstrain.MatrixConstrain((f"DrvJnt_Knee_{side}", f"DrvJnt_Ankle_{side}"), f"CTRL_Global_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Knee_L, f"CTRL_Global_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    cmds.delete("{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs|Grp_Ribbon_Knee_{}|CTRL_Global_Ribbon_Knee_{}|IS_CONSTRAIN_BY___DrvJnt_Knee_{}__".format(settings["name"], side , side ,side))
    cmds.rotate(90, 0, 0, f"CTRL_Global_Ribbon_Knee_{side}", r=True, os=True)
    MatrixConstrain.MatrixConstrain(DrvJnt_Knee_L, f"CTRL_Global_Ribbon_Knee_{side}", Offset=True, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    CTRL_Shape_Knee = cmds.listRelatives(f"CTRL_Global_Ribbon_Leg_{side}", shapes=True)
    cmds.setAttr(CTRL_Shape_Knee[0] + ".lodVisibility", 0)
    
    DrvJnt_Ankle_L = [f"DrvJnt_Ankle_{side}"]
    Preserve_Knee_L = [f"Preserve_Knee_{side}"]
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, f"CTRL_End_Ribbon_Leg_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Ankle_L, f"CTRL_Start_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(Preserve_Knee_L, f"CTRL_End_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(Preserve_Knee_L, f"CTRL_Start_Ribbon_Leg_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    

    #endregion Leg 
    



    computeThomas.createFoot(settings, side)
    
    
    #region Connction IK/FK
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"IK_Leg_{side}.ikBlend")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"IK_Ball_{side}.ikBlend")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"IK_Toe_{side}.ikBlend")
    
    cmds.connectAttr(f"FK_Leg_{side}.rotate", f"DrvJnt_Leg_{side}.rotate")
    cmds.connectAttr(f"FK_Knee_{side}.rotate", f"DrvJnt_Knee_{side}.rotate")
    cmds.connectAttr(f"FK_Ankle_{side}.rotate", f"Bind_Foot_{side}.rotate")
    cmds.connectAttr(f"FK_Ball_{side}.rotate", f"Bind_Ball_{side}.rotate")
    cmds.connectAttr(f"FK_Toe_{side}.rotate", f"Bind_Toe_{side}.rotate")
    
    cmds.createNode("reverse", n="Reverse_Leg_{}".format(side))
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"Reverse_Leg_{side}.inputX")
    
    cmds.connectAttr(f"Reverse_Leg_{side}.outputX", f"FK_Leg_{side}.visibility")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"IK_Leg_{side}.visibility")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"IK_Ball_{side}.visibility")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"IK_Toe_{side}.visibility")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"Bind_Foot_{side}.visibility")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"DrvJnt_Leg_{side}.visibility")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"PoleVector_{side}.visibility")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"CTRL_Foot_{side}.visibility")
    cmds.connectAttr(f"Switch_Leg_{side}.Vis_Pin", f"CTRL_Preserve_Knee_{side}.visibility")

    #region CTRL FK Joints
    cmds.duplicate(f"PlacementCtrl_hip_{side}", n=f"CTRL_FK_Leg_{side}")
    cmds.duplicate(f"PlacementCtrl_knee_{side}", n=f"CTRL_FK_Knee_{side}")
    cmds.duplicate(f"PlacementCtrl_ankle_{side}", n=f"CTRL_FK_Ankle_{side}")
    #Hierachy
    Offset.offset(f"CTRL_FK_Leg_{side}", nbr=1)
    Offset.offset(f"CTRL_FK_Knee_{side}", nbr=1)
    Offset.offset(f"CTRL_FK_Ankle_{side}", nbr=1)
    cmds.parent(f"CTRL_FK_Leg_{side}_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    cmds.parent(f"CTRL_FK_Knee_{side}_Offset", f"CTRL_FK_Leg_{side}")
    cmds.parent(f"CTRL_FK_Ankle_{side}_Offset", f"CTRL_FK_Knee_{side}")
    #Connecting and constraining 
    cmds.connectAttr(f"Reverse_Leg_{side}.outputX", f"CTRL_FK_Leg_{side}_Offset.visibility")
    FK_Leg = [f"CTRL_FK_Leg_{side}"]
    FK_Knee = [f"CTRL_FK_Knee_{side}"]
    FK_Ankle = [f"CTRL_FK_Ankle_{side}"]
    MatrixConstrain.MatrixConstrain(FK_Leg, f"FK_Leg_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)
    MatrixConstrain.MatrixConstrain(FK_Knee, f"FK_Knee_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)
    MatrixConstrain.MatrixConstrain(FK_Ankle, f"FK_Ankle_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)

    
    #region Stretch Leg 
    
    #creatng locators for the stretch
    cmds.spaceLocator(n=f"Locator_Hip_{side}")
    cmds.setAttr(f"Locator_Hip_{side}.visibility", 0)
    cmds.spaceLocator(n=f"Locator_Ankle_{side}")
    cmds.setAttr(f"Locator_Ankle_{side}.visibility", 0)
    cmds.parent(f"Locator_Hip_{side}", f"Bind_Hip_{side}")
    cmds.parent(f"Locator_Ankle_{side}", f"Bind_Hip_{side}")
    cmds.matchTransform(f"Locator_Hip_{side}", f"Bind_Hip_{side}", pos=True)
    cmds.matchTransform(f"Locator_Ankle_{side}", f"Bind_Foot_{side}", pos=True)
    cmds.matchTransform(f"Locator_Ankle_{side}", f"Bind_Foot_{side}", pos=True)
    cmds.matchTransform(f"Locator_Ankle_{side}", f"Bind_Foot_{side}", pos=True)
    CTRL_Foot_L = [f"CTRL_Foot_{side}"]
    MatrixConstrain.MatrixConstrain(CTRL_Foot_L, f"Locator_Ankle_{side}", Offset=True, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    
    #Creating the nodes for the stretch
    cmds.createNode("distanceBetween", n=f"Distance_Leg_{side}")
    cmds.createNode("multiplyDivide", n=f"MD_Distance_Leg_{side}_Divide")
    cmds.setAttr(f"MD_Distance_Leg_{side}_Divide.operation", 2)
    cmds.createNode("multiplyDivide", n=f"MD_Distance_Leg_{side}_Power")
    cmds.setAttr(f"MD_Distance_Leg_{side}_Power.operation", 3)
    cmds.setAttr(f"MD_Distance_Leg_{side}_Power.input2X", -0.5)
    cmds.createNode("multiplyDivide", n=f"MD_Distance_Leg_{side}_GlobalRelativeScale")
    cmds.createNode("condition", n=f"Cond_Distance_Leg_{side}")
    cmds.createNode("condition", n=f"Cond_Boolean_Leg_{side}")
    cmds.createNode("condition", n=f"Cond_FK_Leg_{side}")
    
    #Connecting the nodes
    cmds.connectAttr(f"Locator_Hip_{side}.translate", f"Distance_Leg_{side}.point1")
    cmds.connectAttr(f"Locator_Ankle_{side}.translate", f"Distance_Leg_{side}.point2")
    
    cmds.connectAttr(f"Distance_Leg_{side}.distance", f"MD_Distance_Leg_{side}_GlobalRelativeScale.input1X")
    cmds.connectAttr("GlobalMove_01.scaleY", f"MD_Distance_Leg_{side}_GlobalRelativeScale.input2X")
    cmds.connectAttr(f"MD_Distance_Leg_{side}_GlobalRelativeScale.outputX", f"MD_Distance_Leg_{side}_Divide.input1X")
    
    cmds.connectAttr("GlobalMove_01.scaleY", f"MD_Distance_Leg_{side}_GlobalRelativeScale.input2Y")
    Dist_Leg_Tendu = cmds.getAttr(f"DrvJnt_Knee_{side}.translateX") +cmds.getAttr(f"DrvJnt_Ankle_{side}.translateX")
    cmds.setAttr(f"MD_Distance_Leg_{side}_GlobalRelativeScale.input1Y", Dist_Leg_Tendu)
    cmds.connectAttr(f"MD_Distance_Leg_{side}_GlobalRelativeScale.outputY", f"MD_Distance_Leg_{side}_Divide.input2X")
    
    cmds.connectAttr(f"MD_Distance_Leg_{side}_Divide.outputX", f"MD_Distance_Leg_{side}_Power.input1X")
    
    cmds.connectAttr(f"MD_Distance_Leg_{side}_Divide.outputX", f"Cond_Distance_Leg_{side}.firstTerm")
    cmds.setAttr(f"Cond_Distance_Leg_{side}.secondTerm", 1)
    cmds.setAttr(f"Cond_Distance_Leg_{side}.operation", 2)
    cmds.connectAttr(f"MD_Distance_Leg_{side}_Divide.outputX", f"Cond_Distance_Leg_{side}.colorIfTrueR")
    cmds.connectAttr(f"MD_Distance_Leg_{side}_Power.outputX", f"Cond_Distance_Leg_{side}.colorIfTrueG")
    cmds.connectAttr(f"MD_Distance_Leg_{side}_Power.outputX", f"Cond_Distance_Leg_{side}.colorIfTrueB")
    cmds.connectAttr(f"Cond_Distance_Leg_{side}.outColor", f"Cond_Boolean_Leg_{side}.colorIfTrue")
    cmds.connectAttr(f"CTRL_Foot_{side}.Stretch_Leg", f"Cond_Boolean_Leg_{side}.firstTerm")
    cmds.setAttr(f"Cond_Boolean_Leg_{side}.secondTerm", 1)
    
    cmds.connectAttr(f"Cond_Boolean_Leg_{side}.outColor", f"Cond_FK_Leg_{side}.colorIfTrue")
    cmds.connectAttr(f"Switch_Leg_{side}.IK_FK", f"Cond_FK_Leg_{side}.firstTerm")
    cmds.setAttr(f"Cond_FK_Leg_{side}.secondTerm", 1)
    
    cmds.connectAttr(f"Cond_FK_Leg_{side}.outColor", f"DrvJnt_Knee_{side}.s")
    cmds.connectAttr(f"Cond_FK_Leg_{side}.outColor", f"DrvJnt_Leg_{side}.s")


    #region Twist Ex 
    TwistExtractor.create_twist_extractor(f"Leg_{side}")
    TwistExtractor.create_twist_extractor(f"Knee_{side}")

    cmds.parent(f"Twist_Leg_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    cmds.parent(f"Twist_Knee_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))

    cmds.createNode("multiplyDivide", n=f"Opposed_{side}")
    cmds.setAttr(f"Opposed_{side}.input2X", -1)
    cmds.setAttr(f"Opposed_{side}.input2Y", -1)
    
    cmds.connectAttr(f"Bind_Foot_{side}.rotateZ", f"Opposed_{side}.input1X")
    cmds.connectAttr(f"DrvJnt_Leg_{side}.rotateX", f"Opposed_{side}.input1Y")
    cmds.connectAttr(f"Opposed_{side}.outputY", f"Twist_Leg_{side}_00.rotateX")
    cmds.connectAttr(f"DrvJnt_Leg_{side}.rotateY", f"Twist_Leg_{side}_00.rotateY")
    cmds.connectAttr(f"DrvJnt_Leg_{side}.rotateZ", f"Twist_Leg_{side}_00.rotateZ")
    cmds.connectAttr(f"Twist_Leg_{side}_00.TwistEx", f"CTRL_End_Ribbon_Leg_{side}.rotateX")
    cmds.connectAttr(f"Twist_Knee_{side}_00.TwistEx", f"CTRL_Start_Ribbon_Knee_{side}.rotateX")

    cmds.connectAttr(f"DrvJnt_Leg_{side}.r", f"Twist_Leg_{side}_00.r")

    cmds.connectAttr(f"Opposed_{side}.outputX", f"Twist_Knee_{side}_00.rotateX")
    cmds.connectAttr(f"Bind_Foot_{side}.rotateY", f"Twist_Knee_{side}_00.rotateZ")
    cmds.connectAttr(f"Bind_Foot_{side}.rotateX", f"Twist_Knee_{side}_00.rotateY")

    
    
    