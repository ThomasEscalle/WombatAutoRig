import maya.cmds as cmds
from wombatAutoRig.templates.Body import computeThomas
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import PoleVector
from wombatAutoRig.src.core import MatrixConstrain
from wombatAutoRig.src.core import Ribbon
from wombatAutoRig.src.core import NonRollMatrix
from wombatAutoRig.src.core import TwistExtractor
from wombatAutoRig.src.core import NewCTRL


#(Reprendre les twist parce que j'ai fait betise jsp a voir/ probleme surtout au niveau des pieds a cause de l'angle qui est different)
#Faire les doigts
#SpaceFollow



def compute(settings):
    #CTRL global
    cmds.duplicate("PlacementCtrl_Global", n="CTRL_{}_Global".format(settings["name"]))
    cmds.parent("CTRL_{}_Global".format(settings["name"]), "{}".format(settings["name"]))
    cmds.makeIdentity("CTRL_{}_Global".format(settings["name"]), a=True, t=True, r=True, s=True)
    Global = ["CTRL_{}_Global".format(settings["name"])]
    MatrixConstrain.MatrixConstrain(Global, "{}|GlobalMove_01".format(settings["name"]))

    #Joint Root
    cmds.duplicate("PlacementJnt_Root", n="Bind_Root", po = True)
    cmds.parent(f"Bind_Root", world=True)
    Offset.offset("Bind_Root", nbr=3)
    cmds.parent("Bind_Root_Offset", "{}|GlobalMove_01|Joints_01".format(settings["name"]))

    #CTRL Settings
    cmds.duplicate("PlacementCtrl_Settings", n="CTRL_Settings")
    cmds.parent("CTRL_Settings", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))


    createLeg(settings, "L")
    createLeg(settings, "R")

    createHand(settings, "L")
    createHand(settings, "R")

    createFinger(settings, side ="L", finger= "Thumb")
    createFinger(settings, side ="L", finger= "Index")
    createFinger(settings, side ="L", finger= "Middle")
    createFinger(settings, side ="L", finger= "Ring")
    createFinger(settings, side ="L", finger= "Pimky")

    createFinger(settings, side ="R", finger= "Thumb")
    createFinger(settings, side ="R", finger= "Index")
    createFinger(settings, side ="R", finger= "Middle")
    createFinger(settings, side ="R", finger= "Ring")
    createFinger(settings, side ="R", finger= "Pimky")

    createArm(settings, "L")
    createArm(settings, "R")




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
    cmds.parent(f"DrvJnt_Leg_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_{}".format(settings["name"], side))
    cmds.parent(f"FK_Leg_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_{}".format(settings["name"], side))
    cmds.parent(f"Preserve_Knee_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_{}".format(settings["name"], side))
    
    #region Creating CTRL Pin
    cmds.duplicate(f"PlacementCtrl_Pin_Knee_{side}", n=f"CTRL_Pin_Knee_{side}")
    cmds.parent(f"CTRL_Pin_Knee_{side}", "{}|GlobalMove_01|Joints_01|Joints_Legs|Joints_Leg_{}|Preserve_Knee_{}_Offset|Preserve_Knee_{}_Hook|Preserve_Knee_{}_Move".format(settings["name"], side, side, side, side))
    cmds.parent(f"Preserve_Knee_{side}", f"CTRL_Pin_Knee_{side}")
    cmds.makeIdentity(f"CTRL_Pin_Knee_{side}", a=True, t=True, r=True, s=True)
    cmds.createNode('multiplyDivide', n=f"MD_Preserve_Knee_{side}")
    cmds.connectAttr(f"DrvJnt_Knee_{side}.ry", f"MD_Preserve_Knee_{side}.input1X")
    cmds.connectAttr(f"MD_Preserve_Knee_{side}.outputX", f"Preserve_Knee_{side}_Move.ry")
    cmds.setAttr(f"MD_Preserve_Knee_{side}.input2X", 0.5)
    
    #region Creating the IK handle
    cmds.ikHandle(n=f"IK_Leg_{side}", sj=f"DrvJnt_Leg_{side}", ee=f"DrvJnt_Ankle_{side}", sol="ikRPsolver")
    cmds.parent(f"IK_Leg_{side}", "{}|GlobalMove_01|IKs_01".format(settings["name"]))
    #pole vector
    #Locator = cmds.spaceLocator(n=f"PoleVector_{side}")
    #Color.setColor(f"PoleVector_{side}", "green")
    PoleVector.PoleVector(joint_1=f"DrvJnt_Leg_{side}", joint_2=f"DrvJnt_Knee_{side}", joint_3=f"DrvJnt_Ankle_{side}", CTRL=f"PlacementCtrl_Pv_Leg_{side}")
    cmds.rename(f"PlacementCtrl_Pv_Leg_{side}", f"PV_Leg_{side}")
    Offset.offset(f"PV_Leg_{side}", nbr=1)
    cmds.poleVectorConstraint(f"PV_Leg_{side}", f"IK_Leg_{side}")
    cmds.parent(f"PV_Leg_{side}_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    
    #region Attach Joints 
    Bind_Hip_L = [f"Bind_Hip_{side}"]
    DrvJnt_Leg_L = [f"DrvJnt_Leg_{side}"]
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, f"DrvJnt_Leg_{side}_Hook", Offset=False, sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, f"FK_Leg_{side}_Hook", Offset=False, sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, f"Preserve_Knee_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False)
    
    #region switch IK FK 
    cmds.duplicate(f"PlacementCtrl_Settings_Leg_{side}", n=f"Settings_Leg_{side}")
    cmds.parent(f"Settings_Leg_{side}", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    cmds.addAttr(f"Settings_Leg_{side}", ln="IK_FK", at="enum", en="FK:IK", k=True)
    cmds.addAttr(f"Settings_Leg_{side}", ln="Vis_Bend", at="bool", nn="Vis Bend", k=True)
    cmds.addAttr(f"Settings_Leg_{side}", ln="Vis_Pin", at="bool", nn="Vis Pin", k=True)
    cmds.setAttr(f"Settings_Leg_{side}.tx", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Leg_{side}.ty", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Leg_{side}.tz", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Leg_{side}.rx", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Leg_{side}.ry", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Leg_{side}.rz", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Leg_{side}.sx", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Leg_{side}.sy", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Leg_{side}.sz", keyable=False, channelBox=False)
    Offset.offset(f"Settings_Leg_{side}", nbr=2)
    cmds.setAttr(f"Settings_Leg_{side}.IK_FK", 1)
    cmds.parent(f"Settings_Leg_{side}", 'CTRL_Settings')
    #A contraindre par le CTRL Global
    
    #region Ribbon
    Ribbon.Ribbon(Name=f"Ribbon_Leg_{side}", Span=5)
    Ribbon.Ribbon(Name=f"Ribbon_Knee_{side}", Span=5)

    Global = ["CTRL_{}_Global".format(settings["name"])]
    
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
    MatrixConstrain.MatrixConstrain(Global, f"CTRL_Global_Ribbon_Leg_{side}", Offset=True, rX=False, rY=False, rZ=False, tX=False, tY=False, tZ=False)
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
    MatrixConstrain.MatrixConstrain(Global, f"CTRL_Global_Ribbon_Knee_{side}", Offset=True, rX=False, rY=False, rZ=False, tX=False, tY=False, tZ=False)
    CTRL_Shape_Knee = cmds.listRelatives(f"CTRL_Global_Ribbon_Leg_{side}", shapes=True)
    cmds.setAttr(CTRL_Shape_Knee[0] + ".lodVisibility", 0)
    
    DrvJnt_Ankle_L = [f"DrvJnt_Ankle_{side}"]
    Preserve_Knee_L = [f"Preserve_Knee_{side}"]
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, f"CTRL_End_Ribbon_Leg_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Ankle_L, f"CTRL_Start_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(Preserve_Knee_L, f"CTRL_End_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(Preserve_Knee_L, f"CTRL_Start_Ribbon_Leg_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    
    #Bend
    BendLeg = NewCTRL.Bend(f"PlacementCtrl_Ribbon_Leg_{side}", f"CTRL_Mid_Ribbon_Leg_{side}", name=f"CTRL_Mid_Ribbon_Leg_{side}")
    BendKnee = NewCTRL.Bend(f"PlacementCtrl_Ribbon_Knee_{side}", f"CTRL_Mid_Ribbon_Knee_{side}", name=f"CTRL_Mid_Ribbon_Knee_{side}")

    cmds.connectAttr(f"Settings_Leg_{side}.Vis_Bend", BendLeg + ".visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.Vis_Bend", BendKnee + ".visibility")

    #endregion Leg 
    



    computeThomas.createFoot(settings, side)
    
    
    #region Connction IK/FK
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"IK_Leg_{side}.ikBlend")
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"IK_Ball_{side}.ikBlend")
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"IK_Toe_{side}.ikBlend")
    
    cmds.connectAttr(f"FK_Leg_{side}.rotate", f"DrvJnt_Leg_{side}.rotate")
    cmds.connectAttr(f"FK_Knee_{side}.rotate", f"DrvJnt_Knee_{side}.rotate")
    cmds.connectAttr(f"FK_Ankle_{side}.rotate", f"Bind_Foot_{side}.rotate")
    cmds.connectAttr(f"FK_Ball_{side}.rotate", f"Bind_Ball_{side}.rotate")
    cmds.connectAttr(f"FK_Toe_{side}.rotate", f"Bind_Toe_{side}.rotate")
    
    cmds.createNode("reverse", n="Reverse_Leg_{}".format(side))
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"Reverse_Leg_{side}.inputX")
    
    cmds.connectAttr(f"Reverse_Leg_{side}.outputX", f"FK_Leg_{side}.visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"IK_Leg_{side}.visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"IK_Ball_{side}.visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"IK_Toe_{side}.visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"Bind_Foot_{side}.visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"DrvJnt_Leg_{side}.visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"PV_Leg_{side}.visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"CTRL_Foot_{side}.visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.Vis_Pin", f"CTRL_Pin_Knee_{side}.visibility")

    #region CTRL FK Joints

    NewCTRL.NewCTRL(f"PlacementCtrl_Fk_Leg_{side}", f"FK_Leg_{side}", name=f"CTRL_FK_Leg_{side}", nbr=3)
    NewCTRL.NewCTRL(f"PlacementCtrl_Fk_Knee_{side}", f"FK_Knee_{side}", name=f"CTRL_FK_Knee_{side}")
    NewCTRL.NewCTRL(f"PlacementCtrl_Fk_Ankle_{side}", f"FK_Ankle_{side}", name=f"CTRL_FK_Ankle_{side}")
    NewCTRL.NewCTRL(f"PlacementCtrl_Fk_Ball_{side}", f"FK_Ball_{side}", name=f"CTRL_FK_Ball_{side}")

    cmds.parent(f"CTRL_FK_Leg_{side}_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    cmds.parent(f"CTRL_FK_Knee_{side}_Offset", f"CTRL_FK_Leg_{side}")
    cmds.parent(f"CTRL_FK_Ankle_{side}_Offset", f"CTRL_FK_Knee_{side}")
    cmds.parent(f"CTRL_FK_Ball_{side}_Offset", f"CTRL_FK_Ankle_{side}")
    #Connecting and constraining 
    cmds.connectAttr(f"Reverse_Leg_{side}.outputX", f"CTRL_FK_Leg_{side}_Offset.visibility")
    FK_Leg = [f"CTRL_FK_Leg_{side}"]
    FK_Knee = [f"CTRL_FK_Knee_{side}"]
    FK_Ankle = [f"CTRL_FK_Ankle_{side}"]
    FK_Ball = [f"CTRL_FK_Ball_{side}"]
    MatrixConstrain.MatrixConstrain(FK_Leg, f"FK_Leg_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)
    MatrixConstrain.MatrixConstrain(FK_Knee, f"FK_Knee_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)
    MatrixConstrain.MatrixConstrain(FK_Ankle, f"FK_Ankle_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)
    MatrixConstrain.MatrixConstrain(FK_Ball, f"FK_Ball_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)

    Bind_Hip = [f"Bind_Hip_{side}"]
    MatrixConstrain.MatrixConstrain(Bind_Hip, f"CTRL_FK_Leg_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False,)


    
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
    cmds.connectAttr(f"Settings_Leg_{side}.IK_FK", f"Cond_FK_Leg_{side}.firstTerm")
    cmds.setAttr(f"Cond_FK_Leg_{side}.secondTerm", 1)
    
    cmds.connectAttr(f"Cond_FK_Leg_{side}.outColor", f"DrvJnt_Knee_{side}.s")
    cmds.connectAttr(f"Cond_FK_Leg_{side}.outColor", f"DrvJnt_Leg_{side}.s")


    #region Twist Ex 
    TwistExtractor.create_twist_extractor(f"Leg_{side}")
    TwistExtractor.create_twist_extractor(f"Knee_{side}")

    cmds.duplicate(f"DrvJnt_Ankle_{side}", n=f"DrvJnt_Ankle_{side}_NonRoll", po=True)
    Color.setColor(f"DrvJnt_Ankle_{side}", "orange")
    cmds.createNode("multiplyDivide", n=f"Opposed_{side}")
    cmds.setAttr(f"Opposed_{side}.input2X", -1)
    cmds.setAttr(f"Opposed_{side}.input2Y", -1)

    NonRoll_Leg = NonRollMatrix.NonRollMatrix(f"Bind_Hip_{side}", f"DrvJnt_Leg_{side}")
    NonRoll_Foot = NonRollMatrix.NonRollMatrix(f"DrvJnt_Ankle_{side}_NonRoll", f"Bind_Foot_{side}")


    cmds.connectAttr(NonRoll_Foot + ".outputRotateZ", f"Opposed_{side}.input1X")
    cmds.connectAttr(f"Opposed_{side}.outputX", f"Twist_Knee_{side}_00.rotateX")
    cmds.connectAttr(NonRoll_Leg + ".outputRotateX", f"Opposed_{side}.input1Y")
    cmds.connectAttr(f"Opposed_{side}.outputY",f"Twist_Leg_{side}_00.rotateX")


    cmds.parent(f"Twist_Leg_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    cmds.parent(f"Twist_Knee_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    
    cmds.connectAttr(f"Twist_Leg_{side}_00.TwistEx", f"CTRL_End_Ribbon_Leg_{side}.rotateX")
    cmds.connectAttr(f"Twist_Knee_{side}_00.TwistEx", f"CTRL_Start_Ribbon_Knee_{side}.rotateX")

def createHand(settings, side = "L"):
    #region Creating the joints
    cmds.duplicate(f"PlacementJnt_Wrist_{side}", n=f"Bind_Hand_{side}", po=True)
    Color.setColor(f"Bind_Hand_{side}", "white")

    #freeze transform
    cmds.makeIdentity(f"Bind_Hand_{side}", a=True, t=True, r=True, s=True)

    #offset
    Offset.offset(f"Bind_Hand_{side}", nbr=3)

    # Check if "Joints_Hand" exists, if not create it
    if not cmds.objExists("Joints_Hands"):
        cmds.group(n="Joints_Hands", em=True)
        cmds.parent("Joints_Hands", "{}|GlobalMove_01|Joints_01".format(settings["name"]))

    #rangement
    cmds.parent(f"Bind_Hand_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Hands".format(settings["name"]))

def createFinger(settings, side ="L", finger= "Thumb"):
    #Duplicate Joint
    cmds.duplicate(f"PlacementJnt_{finger}_Metacarpus_{side}", n=f"Bind_{finger}_Metacarpus_{side}", po=True)
    Color.setColor(f"Bind_{finger}_Metacarpus_{side}", "white")
    cmds.makeIdentity(f"Bind_{finger}_Metacarpus_{side}", a=True, t=True, r=True, s=True)

    if finger == "Thumb":
        n=2
    else :
        n=3
    for i in range(n):
        cmds.duplicate(f"PlacementJnt_{finger}_0{i+1}_{side}", n=f"Bind_{finger}_0{i+1}_{side}", po=True)
        Color.setColor(f"Bind_{finger}_0{i+1}_{side}", "white")
        cmds.makeIdentity(f"Bind_{finger}_0{i+1}_{side}", a=True, t=True, r=True, s=True)

    cmds.duplicate(f"PlacementJnt_{finger}_end_{side}", n=f"Bind_{finger}_end_{side}", po=True)
    Color.setColor(f"Bind_{finger}_end_{side}", "white")
    cmds.makeIdentity(f"Bind_{finger}_end_{side}", a=True, t=True, r=True, s=True)

    #Rangement
    cmds.parent(f"Bind_{finger}_Metacarpus_{side}", f"Bind_Hand_{side}")
    cmds.parent(f"Bind_{finger}_01_{side}", f"Bind_{finger}_Metacarpus_{side}")
    cmds.parent(f"Bind_{finger}_02_{side}", f"Bind_{finger}_01_{side}")
    if finger == "Thumb":
        cmds.parent(f"Bind_{finger}_end_{side}", f"Bind_{finger}_02_{side}")
    else:
        cmds.parent(f"Bind_{finger}_03_{side}", f"Bind_{finger}_02_{side}")
        cmds.parent(f"Bind_{finger}_end_{side}", f"Bind_{finger}_03_{side}")

def createArm(settings, side = "L"):
    #region Creating the joints 
        
    cmds.duplicate(f"PlacementJnt_Clavicle_{side}", n=f"Bind_Clavicle_{side}", po=True)
    Color.setColor(f"Bind_Clavicle_{side}", "white")
    cmds.duplicate(f"PlacementJnt_Clavicle_end_{side}", n=f"Bind_Clavicle_end_{side}", po=True)
    Color.setColor(f"Bind_Clavicle_end_{side}", "white")

    cmds.duplicate(f"PlacementJnt_Arm_{side}", n=f"DrvJnt_Arm_{side}", po=True)
    Color.setColor(f"DrvJnt_Arm_{side}", "yellow")
    cmds.duplicate(f"PlacementJnt_Elbow_{side}", n=f"DrvJnt_Elbow_{side}", po=True)
    Color.setColor(f"DrvJnt_Elbow_{side}", "yellow")
    cmds.duplicate(f"PlacementJnt_Wrist_{side}", n=f"DrvJnt_Wrist_{side}", po=True)
    Color.setColor(f"DrvJnt_Wrist_{side}", "yellow")
    
    cmds.duplicate(f"PlacementJnt_Arm_{side}", n=f"FK_Arm_{side}", po=True)
    Color.setColor(f"FK_Arm_{side}", "blue")
    cmds.duplicate(f"PlacementJnt_Elbow_{side}", n=f"FK_Elbow_{side}", po=True)
    Color.setColor(f"FK_Elbow_{side}", "blue")
    cmds.duplicate(f"PlacementJnt_Wrist_{side}", n=f"FK_Wrist_{side}", po=True)
    Color.setColor(f"FK_Wrist_{side}", "blue")
    
    cmds.duplicate(f"PlacementJnt_Elbow_{side}", n=f"Preserve_Elbow_{side}", po=True)

    #Freeze the transform

    cmds.makeIdentity(f"Bind_Clavicle_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"Bind_Clavicle_end_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"DrvJnt_Elbow_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"DrvJnt_Arm_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"DrvJnt_Wrist_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"FK_Arm_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"FK_Elbow_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"FK_Wrist_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"Preserve_Elbow_{side}", a=True, t=True, r=True, s=True)

    #Unparenting the joints

    cmds.parent(f"Bind_Clavicle_{side}", world=True)
    cmds.parent(f"Bind_Clavicle_end_{side}", world=True)
    cmds.parent(f"DrvJnt_Arm_{side}", world=True)
    cmds.parent(f"DrvJnt_Elbow_{side}", world=True)
    cmds.parent(f"DrvJnt_Wrist_{side}", world=True)
    cmds.parent(f"FK_Arm_{side}", world=True)
    cmds.parent(f"FK_Elbow_{side}", world=True)
    cmds.parent(f"FK_Wrist_{side}", world=True)
    cmds.parent(f"Preserve_Elbow_{side}", world=True)
    
    #Reparenting the joints

    cmds.parent(f"Bind_Clavicle_end_{side}", f"Bind_Clavicle_{side}")
    cmds.parent(f"DrvJnt_Elbow_{side}", f"DrvJnt_Arm_{side}")
    cmds.parent(f"DrvJnt_Wrist_{side}", f"DrvJnt_Elbow_{side}")
    cmds.parent(f"FK_Elbow_{side}", f"FK_Arm_{side}")
    cmds.parent(f"FK_Wrist_{side}", f"FK_Elbow_{side}")
    
    #Offset for the joints
    
    Offset.offset(f"Bind_Clavicle_{side}", nbr=3)
    Offset.offset(f"DrvJnt_Arm_{side}", nbr=3)
    Offset.offset(f"FK_Arm_{side}", nbr=3)
    Offset.offset(f"Preserve_Elbow_{side}", nbr=3)
    
    #Rangement des joints dans un groupe

    # Check if "Joints_Arms" exists, if not create it
    if not cmds.objExists("Joints_Arms"):
        cmds.group(n="Joints_Arms", em=True)
        cmds.parent("Joints_Arms", "{}|GlobalMove_01|Joints_01".format(settings["name"]))

    cmds.group(n=f"Joints_Arm_{side}", em=True)
    cmds.parent(f"Joints_Arm_{side}", "Joints_Arms")
    cmds.parent(f"DrvJnt_Arm_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Arms|Joints_Arm_{}".format(settings["name"], side))
    cmds.parent(f"FK_Arm_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Arms|Joints_Arm_{}".format(settings["name"], side))
    cmds.parent(f"Preserve_Elbow_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Arms|Joints_Arm_{}".format(settings["name"], side))

    if not cmds.objExists("Joints_Clavicles"):
        cmds.group(n="Joints_Clavicles", em=True)
        cmds.parent("Joints_Clavicles", "{}|GlobalMove_01|Joints_01|Joints_Arms".format(settings["name"]))

    cmds.group(n=f"Joints_Clavicle_{side}", em=True)
    cmds.parent(f"Joints_Clavicle_{side}", "Joints_Clavicles")
    cmds.parent(f"Bind_Clavicle_{side}_Offset", "{}|GlobalMove_01|Joints_01|Joints_Arms|Joints_Clavicles|Joints_Clavicle_{}".format(settings["name"], side))
    
    #region Creating CTRL Pin
    cmds.duplicate(f"PlacementCtrl_Pin_Elbow_{side}", n=f"CTRL_Pin_Elbow_{side}")
    cmds.parent(f"CTRL_Pin_Elbow_{side}", "{}|GlobalMove_01|Joints_01|Joints_Arms|Joints_Arm_{}|Preserve_Elbow_{}_Offset|Preserve_Elbow_{}_Hook|Preserve_Elbow_{}_Move".format(settings["name"], side, side, side, side))
    cmds.parent(f"Preserve_Elbow_{side}", f"CTRL_Pin_Elbow_{side}")
    cmds.makeIdentity(f"CTRL_Pin_Elbow_{side}", a=True, t=True, r=True, s=True)
    cmds.createNode('multiplyDivide', n=f"MD_Preserve_Elbow_{side}")
    cmds.connectAttr(f"DrvJnt_Elbow_{side}.ry", f"MD_Preserve_Elbow_{side}.input1X")
    cmds.connectAttr(f"MD_Preserve_Elbow_{side}.outputX", f"Preserve_Elbow_{side}_Move.ry")
    cmds.setAttr(f"MD_Preserve_Elbow_{side}.input2X", 0.5)
    
    #region Creating The Wrist CTRL
    NewCTRL.NewCTRL(f"PlacementCtrl_Ik_Arm_{side}", f"DrvJnt_Wrist_{side}", name=f"CTRL_Wrist_{side}")
    cmds.parent(f"CTRL_Wrist_{side}_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    cmds.addAttr(f"CTRL_Wrist_{side}", ln=f"Stretch_Arm", at="bool", dv=False, k=True)


    #region Creating the IK handle
    cmds.ikHandle(n=f"IK_Arm_{side}", sj=f"DrvJnt_Arm_{side}", ee=f"DrvJnt_Wrist_{side}", sol="ikRPsolver")
    cmds.parent(f"IK_Arm_{side}", "{}|GlobalMove_01|IKs_01".format(settings["name"]))
    CTRL_Wrist_L = [f"CTRL_Wrist_{side}"]  
    MatrixConstrain.MatrixConstrain(CTRL_Wrist_L, f"IK_Arm_{side}")
    #pole vector
    #Locator = cmds.spaceLocator(n=f"PoleVector_Arm_{side}")
    #Color.setColor(f"PoleVector_Arm_{side}", "green")
    PoleVector.PoleVector(joint_1=f"DrvJnt_Arm_{side}", joint_2=f"DrvJnt_Elbow_{side}", joint_3=f"DrvJnt_Wrist_{side}", CTRL=f"PlacementCtrl_Pv_Arm_{side}")
    cmds.rename(f"PlacementCtrl_Pv_Arm_{side}", f"PV_Arm_{side}")
    Offset.offset(f"PV_Arm_{side}", nbr=1)
    cmds.poleVectorConstraint(f"PV_Arm_{side}", f"IK_Arm_{side}")
    cmds.parent(f"PV_Arm_{side}_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    
    #region Attach Joints 
    DrvJnt_Arm_L = [f"DrvJnt_Arm_{side}"]
    Bind_Clavicle_end = [f"Bind_Clavicle_end_{side}"]
    MatrixConstrain.MatrixConstrain(Bind_Clavicle_end, f"FK_Arm_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(Bind_Clavicle_end, f"DrvJnt_Arm_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Arm_L, f"Preserve_Elbow_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False)
    
    #region switch IK FK 
    cmds.duplicate(f"PlacementCtrl_Settings_Arm_{side}", n=f"Settings_Arm_{side}")
    cmds.parent(f"Settings_Arm_{side}", "{}|GlobalMove_01|CTRLs_01|CTRL_Settings".format(settings["name"]))
    cmds.addAttr(f"Settings_Arm_{side}", ln="IK_FK", at="enum", en="FK:IK", k=True)
    cmds.addAttr(f"Settings_Arm_{side}", ln="Vis_Bend", at="bool", nn="Vis Bend", k=True)
    cmds.addAttr(f"Settings_Arm_{side}", ln="Vis_Pin", at="bool", nn="Vis Pin", k=True)
    cmds.setAttr(f"Settings_Arm_{side}.tx", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Arm_{side}.ty", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Arm_{side}.tz", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Arm_{side}.rx", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Arm_{side}.ry", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Arm_{side}.rz", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Arm_{side}.sx", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Arm_{side}.sy", keyable=False, channelBox=False)
    cmds.setAttr(f"Settings_Arm_{side}.sz", keyable=False, channelBox=False)
    Offset.offset(f"Settings_Arm_{side}", nbr=2)
    
    #region Ribbon
    Ribbon.Ribbon(Name=f"Ribbon_Arm_{side}", Span=5)
    Ribbon.Ribbon(Name=f"Ribbon_Elbow_{side}", Span=5)

    Global = ["CTRL_{}_Global".format(settings["name"])]
    
    if not cmds.objExists("Ribbons_Arms_Hide"):
        cmds.group(n="Ribbons_Arms_Hide", em=True)
        cmds.parent("Ribbons_Arms_Hide", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))

    cmds.parent(f"Grp_Ribbon_Arm_{side}|Grp_Extra_Nodes_Ribbon_Arm_{side}|Grp_Extra_Nodes_To_Hide_Ribbon_Arm_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01|Ribbons_Arms_Hide".format(settings["name"]))
    

    if not cmds.objExists("Ribbons_Arms"):
        cmds.group(n="Ribbons_Arms", em=True)
        cmds.parent("Ribbons_Arms", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01".format(settings["name"]))
    cmds.parent(f"Grp_Ribbon_Arm_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Arms".format(settings["name"]))
    
    DrvJnt_Arm_L = [f"DrvJnt_Arm_{side}"]
    MatrixConstrain.MatrixConstrain((f"DrvJnt_Arm_{side}", f"DrvJnt_Elbow_{side}"), f"CTRL_Global_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Arm_L, "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Arms|Grp_Ribbon_Arm_{}|CTRL_Global_Ribbon_Arm_{}".format(settings["name"], side,side), Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    MatrixConstrain.MatrixConstrain(Global, "CTRL_Global_Ribbon_Arm_{}".format(side), Offset=False, rX=False, rY=False, rZ=False, tX=False, tY=False, tZ=False)
    CTRL_Shape_Arm = cmds.listRelatives(f"CTRL_Global_Ribbon_Arm_{side}", shapes=True)
    cmds.setAttr(CTRL_Shape_Arm[0] + ".lodVisibility", 0)
    
    cmds.parent(f"Grp_Ribbon_Elbow_{side}|Grp_Extra_Nodes_Ribbon_Elbow_{side}|Grp_Extra_Nodes_To_Hide_Ribbon_Elbow_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01|Ribbons_Arms_Hide".format(settings["name"]))
    
    cmds.parent(f"Grp_Ribbon_Elbow_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Arms".format(settings["name"]))
    
    DrvJnt_Elbow_L = [f"DrvJnt_Elbow_{side}"]
    MatrixConstrain.MatrixConstrain((f"DrvJnt_Elbow_{side}", f"DrvJnt_Wrist_{side}"), f"CTRL_Global_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Elbow_L, f"CTRL_Global_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    MatrixConstrain.MatrixConstrain(Global, f"CTRL_Global_Ribbon_Elbow_{side}", Offset=False, rX=False, rY=False, rZ=False, tX=False, tY=False, tZ=False)

    CTRL_Shape_Elbow = cmds.listRelatives(f"CTRL_Global_Ribbon_Elbow_{side}", shapes=True)
    cmds.setAttr(CTRL_Shape_Elbow[0] + ".lodVisibility", 0)
    
    DrvJnt_Wrist_L = [f"DrvJnt_Wrist_{side}"]
    Preserve_Elbow_L = [f"Preserve_Elbow_{side}"]
    if side =="L":
        MatrixConstrain.MatrixConstrain(DrvJnt_Arm_L, f"CTRL_End_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
        MatrixConstrain.MatrixConstrain(DrvJnt_Wrist_L, f"CTRL_Start_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
        MatrixConstrain.MatrixConstrain(Preserve_Elbow_L, f"CTRL_End_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
        MatrixConstrain.MatrixConstrain(Preserve_Elbow_L, f"CTRL_Start_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    elif side =="R":
        MatrixConstrain.MatrixConstrain(DrvJnt_Arm_L, f"CTRL_Start_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
        MatrixConstrain.MatrixConstrain(DrvJnt_Wrist_L, f"CTRL_End_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
        MatrixConstrain.MatrixConstrain(Preserve_Elbow_L, f"CTRL_Start_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
        MatrixConstrain.MatrixConstrain(Preserve_Elbow_L, f"CTRL_End_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    
    #Bend
    BendArm = NewCTRL.Bend(f"PlacementCtrl_Ribbon_Arm_{side}", f"CTRL_Mid_Ribbon_Arm_{side}", name=f"CTRL_Mid_Ribbon_Arm_{side}")
    BendElbow = NewCTRL.Bend(f"PlacementCtrl_Ribbon_Elbow_{side}", f"CTRL_Mid_Ribbon_Elbow_{side}", name=f"CTRL_Mid_Ribbon_Elbow_{side}")

    cmds.connectAttr(f"Settings_Arm_{side}.Vis_Bend", BendArm + ".visibility")
    cmds.connectAttr(f"Settings_Arm_{side}.Vis_Bend", BendElbow + ".visibility")

    #endregion Arm 
    
    
    
    #region Connection IK/FK
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"IK_Arm_{side}.ikBlend")
    
    cmds.connectAttr(f"FK_Arm_{side}.rotate", f"DrvJnt_Arm_{side}.rotate")
    cmds.connectAttr(f"FK_Elbow_{side}.rotate", f"DrvJnt_Elbow_{side}.rotate")
    
    cmds.createNode("reverse", n="Reverse_Arm_{}".format(side))
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"Reverse_Arm_{side}.inputX")
    
    cmds.connectAttr(f"Reverse_Arm_{side}.outputX", f"FK_Arm_{side}.visibility")
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"IK_Arm_{side}.visibility")
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"DrvJnt_Arm_{side}.visibility")
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"PV_Arm_{side}.visibility")
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"CTRL_Wrist_{side}.visibility")
    cmds.connectAttr(f"Settings_Arm_{side}.Vis_Pin", f"CTRL_Pin_Elbow_{side}.visibility")

    #region CTRL FK

    NewCTRL.NewCTRL(f"PlacementCtrl_Fk_Shoulder_{side}", f"FK_Arm_{side}", name=f"CTRL_FK_Arm_{side}", nbr=3)
    NewCTRL.NewCTRL(f"PlacementCtrl_Fk_Elbow_{side}", f"FK_Elbow_{side}", name=f"CTRL_FK_Elbow_{side}")
    NewCTRL.NewCTRL(f"PlacementCtrl_Fk_Wrist_{side}", f"FK_Wrist_{side}", name=f"CTRL_FK_Wrist_{side}")

    cmds.parent(f"CTRL_FK_Arm_{side}_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    cmds.parent(f"CTRL_FK_Elbow_{side}_Offset", f"CTRL_FK_Arm_{side}")
    cmds.parent(f"CTRL_FK_Wrist_{side}_Offset", f"CTRL_FK_Elbow_{side}")
    #Connecting and constraining 
    cmds.connectAttr(f"Reverse_Arm_{side}.outputX", f"CTRL_FK_Arm_{side}_Offset.visibility")
    FK_Arm = [f"CTRL_FK_Arm_{side}"]
    FK_Elbow = [f"CTRL_FK_Elbow_{side}"]
    FK_Wrist = [f"CTRL_FK_Wrist_{side}"]
    MatrixConstrain.MatrixConstrain(FK_Arm, f"FK_Arm_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)
    MatrixConstrain.MatrixConstrain(FK_Elbow, f"FK_Elbow_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)
    MatrixConstrain.MatrixConstrain(FK_Wrist, f"FK_Wrist_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)

    Bind_Clavicle = [f"Bind_Clavicle_{side}"]
    MatrixConstrain.MatrixConstrain(Bind_Clavicle, f"CTRL_FK_Arm_{side}_Hook", Offset=True, rX=False, rY=False, rZ=False, sX=False, sY=False, sZ=False,)

    
    #region Stretch Arm 
    
    #creatng locators for the stretch
    cmds.spaceLocator(n=f"Locator_Arm_{side}")
    cmds.setAttr(f"Locator_Arm_{side}.visibility", 0)
    cmds.spaceLocator(n=f"Locator_Wrist_{side}")
    cmds.setAttr(f"Locator_Wrist_{side}.visibility", 0)
    cmds.parent(f"Locator_Arm_{side}", f"Bind_Clavicle_{side}")
    cmds.parent(f"Locator_Wrist_{side}", f"Bind_Clavicle_{side}")
    cmds.matchTransform(f"Locator_Arm_{side}", f"Bind_Clavicle_end_{side}", pos=True)
    cmds.matchTransform(f"Locator_Wrist_{side}", f"DrvJnt_Wrist_{side}", pos=True)
    MatrixConstrain.MatrixConstrain(CTRL_Wrist_L, f"Locator_Wrist_{side}", Offset=True, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    
    #Creating the nodes for the stretch
    cmds.createNode("distanceBetween", n=f"Distance_Arm_{side}")
    cmds.createNode("multiplyDivide", n=f"MD_Distance_Arm_{side}_Divide")
    cmds.setAttr(f"MD_Distance_Arm_{side}_Divide.operation", 2)
    cmds.createNode("multiplyDivide", n=f"MD_Distance_Arm_{side}_Power")
    cmds.setAttr(f"MD_Distance_Arm_{side}_Power.operation", 3)
    cmds.setAttr(f"MD_Distance_Arm_{side}_Power.input2X", -0.5)
    cmds.createNode("multiplyDivide", n=f"MD_Distance_Arm_{side}_GlobalRelativeScale")
    cmds.createNode("condition", n=f"Cond_Distance_Arm_{side}")
    cmds.createNode("condition", n=f"Cond_Boolean_Arm_{side}")
    cmds.createNode("condition", n=f"Cond_FK_Arm_{side}")
    
    #Connecting the nodes
    cmds.connectAttr(f"Locator_Arm_{side}.translate", f"Distance_Arm_{side}.point1")
    cmds.connectAttr(f"Locator_Wrist_{side}.translate", f"Distance_Arm_{side}.point2")
    
    cmds.connectAttr(f"Distance_Arm_{side}.distance", f"MD_Distance_Arm_{side}_GlobalRelativeScale.input1X")
    cmds.connectAttr("GlobalMove_01.scaleY", f"MD_Distance_Arm_{side}_GlobalRelativeScale.input2X")
    cmds.connectAttr(f"MD_Distance_Arm_{side}_GlobalRelativeScale.outputX", f"MD_Distance_Arm_{side}_Divide.input1X")
    
    cmds.connectAttr("GlobalMove_01.scaleY", f"MD_Distance_Arm_{side}_GlobalRelativeScale.input2Y")
    Dist_Arm_Tendu = cmds.getAttr(f"DrvJnt_Elbow_{side}.translateX") +cmds.getAttr(f"DrvJnt_Wrist_{side}.translateX")
    cmds.setAttr(f"MD_Distance_Arm_{side}_GlobalRelativeScale.input1Y", Dist_Arm_Tendu)
    cmds.connectAttr(f"MD_Distance_Arm_{side}_GlobalRelativeScale.outputY", f"MD_Distance_Arm_{side}_Divide.input2X")
    
    cmds.connectAttr(f"MD_Distance_Arm_{side}_Divide.outputX", f"MD_Distance_Arm_{side}_Power.input1X")
    
    cmds.connectAttr(f"MD_Distance_Arm_{side}_Divide.outputX", f"Cond_Distance_Arm_{side}.firstTerm")
    cmds.setAttr(f"Cond_Distance_Arm_{side}.secondTerm", 1)
    cmds.setAttr(f"Cond_Distance_Arm_{side}.operation", 2)
    cmds.connectAttr(f"MD_Distance_Arm_{side}_Divide.outputX", f"Cond_Distance_Arm_{side}.colorIfTrueR")
    cmds.connectAttr(f"MD_Distance_Arm_{side}_Power.outputX", f"Cond_Distance_Arm_{side}.colorIfTrueG")
    cmds.connectAttr(f"MD_Distance_Arm_{side}_Power.outputX", f"Cond_Distance_Arm_{side}.colorIfTrueB")
    cmds.connectAttr(f"Cond_Distance_Arm_{side}.outColor", f"Cond_Boolean_Arm_{side}.colorIfTrue")
    cmds.connectAttr(f"CTRL_Wrist_{side}.Stretch_Arm", f"Cond_Boolean_Arm_{side}.firstTerm")
    cmds.setAttr(f"Cond_Boolean_Arm_{side}.secondTerm", 1)
    
    cmds.connectAttr(f"Cond_Boolean_Arm_{side}.outColor", f"Cond_FK_Arm_{side}.colorIfTrue")
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"Cond_FK_Arm_{side}.firstTerm")
    cmds.setAttr(f"Cond_FK_Arm_{side}.secondTerm", 1)
    
    cmds.connectAttr(f"Cond_FK_Arm_{side}.outColor", f"DrvJnt_Elbow_{side}.s")
    cmds.connectAttr(f"Cond_FK_Arm_{side}.outColor", f"DrvJnt_Arm_{side}.s")


    #DrvJnt wrsit constraint bind hand and is constraint by FK and IK
    DrvJntWrist = [f"DrvJnt_Wrist_{side}"]
    MatrixConstrain.MatrixConstrain(DrvJntWrist, f"Bind_Hand_{side}_Hook", sX=False, sY=False, sZ=False)

    #Node Conditon
    cmds.createNode("condition", n=f"Cond_Constraint_DrvJnt_{side}")
    CTRL_IK_Wrist = [f"CTRL_Wrist_{side}"]
    FK_Constraint = MatrixConstrain.MatrixConstrain(FK_Wrist, f"DrvJnt_Wrist_{side}", sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    cmds.disconnectAttr(f"{FK_Constraint}.outputRotateX",f"DrvJnt_Wrist_{side}.rotateX")
    cmds.disconnectAttr(f"{FK_Constraint}.outputRotateY",f"DrvJnt_Wrist_{side}.rotateY")
    cmds.disconnectAttr(f"{FK_Constraint}.outputRotateZ",f"DrvJnt_Wrist_{side}.rotateZ")
    cmds.connectAttr(f"{FK_Constraint}.outputRotate", f"Cond_Constraint_DrvJnt_{side}.colorIfTrue")
    IK_Constraint = MatrixConstrain.MatrixConstrain(CTRL_IK_Wrist, f"DrvJnt_Wrist_{side}", sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False)
    cmds.disconnectAttr(f"{IK_Constraint}.outputRotateX",f"DrvJnt_Wrist_{side}.rotateX")
    cmds.disconnectAttr(f"{IK_Constraint}.outputRotateY",f"DrvJnt_Wrist_{side}.rotateY")
    cmds.disconnectAttr(f"{IK_Constraint}.outputRotateZ",f"DrvJnt_Wrist_{side}.rotateZ") 
    cmds.connectAttr(f"{IK_Constraint}.outputRotate", f"Cond_Constraint_DrvJnt_{side}.colorIfFalse")

    cmds.connectAttr(f"Cond_Constraint_DrvJnt_{side}.outColor", f"DrvJnt_Wrist_{side}.r")
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"Cond_Constraint_DrvJnt_{side}.secondTerm")


    #region Twist Ex 
    TwistExtractor.create_twist_extractor(f"Arm_{side}")
    TwistExtractor.create_twist_extractor(f"Wrist_{side}")

    cmds.duplicate(f"DrvJnt_Wrist_{side}", n=f"DrvJnt_Wrist_{side}_NonRoll", po=True)
    Color.setColor(f"DrvJnt_Wrist_{side}", "orange")

    cmds.createNode("multiplyDivide", n=f"OpposedArm_{side}")
    cmds.setAttr(f"OpposedArm_{side}.input2X", -1)

    NonRoll_Arm = NonRollMatrix.NonRollMatrix(f"Bind_Clavicle_{side}", f"DrvJnt_Arm_{side}")

    cmds.connectAttr(NonRoll_Arm + ".outputRotateX", f"OpposedArm_{side}.input1X")
    cmds.connectAttr(f"OpposedArm_{side}.outputX",f"Twist_Arm_{side}_00.rotateX")

    cmds.connectAttr(DrvJnt_Wrist_L[0] + ".r", f"Twist_Wrist_{side}_00.r")

    cmds.parent(f"Twist_Arm_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    cmds.parent(f"Twist_Wrist_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    
    if side == "L":
        cmds.connectAttr(f"Twist_Arm_{side}_00.TwistEx", f"CTRL_End_Ribbon_Arm_{side}.rotateX")
        cmds.connectAttr(f"Twist_Wrist_{side}_00.TwistEx", f"CTRL_Start_Ribbon_Elbow_{side}.rotateX")

    elif side == "R":
        cmds.connectAttr(f"Twist_Arm_{side}_00.TwistEx", f"CTRL_Start_Ribbon_Arm_{side}.rotateX")
        cmds.connectAttr(f"Twist_Wrist_{side}_00.TwistEx", f"CTRL_End_Ribbon_Elbow_{side}.rotateX")