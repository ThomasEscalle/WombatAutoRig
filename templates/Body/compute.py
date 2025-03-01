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
from wombatAutoRig.src.core import Bookmark
from wombatAutoRig.src.core import ColumnRibbon
from wombatAutoRig.src.core import SkinCage


#Faire les doigts (attentes CTRLs)
#SpaceFollow

def visibilityShape(CTRL, type):
    Shape = cmds.listRelatives(CTRL, s=True)
    for shape in Shape:
        cmds.connectAttr("CTRL_Settings_Spine" + f".{type}Visibility", shape + ".lodVisibility")

def compute(settings):

    # Bind skin set
    cmds.sets(n="Bind_JNTs", em=True)
    
    #CTRL global
    cmds.duplicate("PlacementCtrl_Global", n="CTRL_{}_Global".format(settings["name"]))
    cmds.parent("CTRL_{}_Global".format(settings["name"]), "{}".format(settings["name"]))
    cmds.makeIdentity("CTRL_{}_Global".format(settings["name"]), a=True, t=True, r=True, s=True)
    Global = ["CTRL_{}_Global".format(settings["name"])]
    MatrixConstrain.MatrixConstrain(Global, "{}|GlobalMove_01".format(settings["name"]), BookmarkName="MatX_Main")

    #Joint Root
    cmds.duplicate("PlacementJnt_Root", n="Bind_Root", po = True)
    cmds.duplicate("PlacementJnt_Root", n="Bind_Hip", po = True)


    cmds.parent(f"Bind_Hip", world=True)
    cmds.sets(f"Bind_Hip", add="Bind_JNTs")
    cmds.parent(f"Bind_Root", world=True)
    cmds.sets(f"Bind_Root", add="Bind_JNTs")
    Offset.offset("Bind_Root", nbr=3)
    cmds.parent("Bind_Root_Offset", "{}|GlobalMove_01|Joints_01".format(settings["name"]))
    cmds.parent("Bind_Hip", "Bind_Root")

    #CTRL Settings
    cmds.duplicate("PlacementCtrl_Settings", n="CTRL_Settings")
    cmds.parent("CTRL_Settings", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    cmds.makeIdentity("CTRL_Settings", a=True, t=True, r=True, s=True)






    createLeg(settings, "L")
    createLeg(settings, "R")

    createHand(settings, "L")
    createHand(settings, "R")

    createFinger(settings, side ="L", finger= "Thumb")
    createFinger(settings, side ="L", finger= "Index")
    createFinger(settings, side ="L", finger= "Middle")
    createFinger(settings, side ="L", finger= "Ring")
    createFinger(settings, side ="L", finger= "Pinky")

    createFinger(settings, side ="R", finger= "Thumb")
    createFinger(settings, side ="R", finger= "Index")
    createFinger(settings, side ="R", finger= "Middle")
    createFinger(settings, side ="R", finger= "Ring")
    createFinger(settings, side ="R", finger= "Pinky")

    createArm(settings, "L")
    createArm(settings, "R")

    createSpine(settings)

    if settings["bindSkin"] == True :
        joints = cmds.sets( "Bind_JNTs", q=True )
        body_mesh = settings["geo"]  
        #Create skin cage
        cage_meshes = SkinCage.SkinCage(settings=settings)

        #Transfer skin weights to the body mesh
        for geo in body_mesh:
            SkinCage.transfer_skin_weights(joints, cage_meshes, geo)

        #suppr cubes
        cmds.delete(cage_meshes)



def createLeg(settings, side = "L"):


    #region Leg 

    #region Creating the joints 
    
    cmds.duplicate(f"PlacementJnt_Hip_{side}", n=f"Bind_Hip_{side}", po = True)
    cmds.sets(f"Bind_Hip_{side}", add="Bind_JNTs")

    
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
    
    cmds.parent(f"Bind_Hip_{side}", f"Bind_Hip")
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

    #Create a locator that match the transform of the pole vector and parent it inside the fk Knee
    cmds.spaceLocator(n=f"Locator_PoleVector_Knee_{side}")[0]
    cmds.matchTransform(f"Locator_PoleVector_Knee_{side}", f"PV_Leg_{side}", pos=True)
    cmds.parent(f"Locator_PoleVector_Knee_{side}", f"FK_Knee_{side}")
    
    #region Attach Joints 
    Bind_Hip_L = [f"Bind_Hip_{side}"]
    DrvJnt_Leg_L = [f"DrvJnt_Leg_{side}"]

    BookmarkRowOffset = 0
    if side == "L":
        BookmarkRowOffset = -10

    MatrixConstrain.MatrixConstrain(Bind_Hip_L, f"DrvJnt_Leg_{side}_Hook", Offset=False, sX=False, sY=False, sZ=False, BookmarkName="MatX_Main", BookColumnOffset=BookmarkRowOffset, BookRowOffset = -1)
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, f"FK_Leg_{side}_Hook", Offset=False, sX=False, sY=False, sZ=False, BookmarkName="MatX_Main", BookColumnOffset=BookmarkRowOffset, BookRowOffset = -2)
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, f"Preserve_Knee_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False, BookmarkName="MatX_Main", BookColumnOffset=BookmarkRowOffset, BookRowOffset = -3)
    
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
    Ribbon.Ribbon(Name=f"Ribbon_Leg_{side}", Span=5, BindSet= "Bind_JNTs", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-2)
    Ribbon.Ribbon(Name=f"Ribbon_Knee_{side}", Span=5, BindSet= "Bind_JNTs", BookColumnOffset=BookmarkRowOffset, BookRowOffset=0)

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
    MatrixConstrain.MatrixConstrain((f"DrvJnt_Leg_{side}", f"DrvJnt_Knee_{side}"), f"CTRL_Global_Ribbon_Leg_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=0)
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs|Grp_Ribbon_Leg_{}|CTRL_Global_Ribbon_Leg_{}".format(settings["name"], side,side), Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-1)
    cmds.delete("{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs|Grp_Ribbon_Leg_{}|CTRL_Global_Ribbon_Leg_{}|IS_CONSTRAIN_BY___DrvJnt_Leg_{}__".format(settings["name"], side ,side ,side))
    cmds.rotate(90, 0, 0, f"CTRL_Global_Ribbon_Leg_{side}", r=True, os=True)
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, f"CTRL_Global_Ribbon_Leg_{side}", Offset=True, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-2)
    MatrixConstrain.MatrixConstrain(Global, f"CTRL_Global_Ribbon_Leg_{side}", Offset=True, rX=False, rY=False, rZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-3)
    CTRL_Shape_Leg = cmds.listRelatives(f"CTRL_Global_Ribbon_Knee_{side}", shapes=True)
    cmds.setAttr(CTRL_Shape_Leg[0] + ".lodVisibility", 0)
    
    cmds.parent(f"Grp_Ribbon_Knee_{side}|Grp_Extra_Nodes_Ribbon_Knee_{side}|Grp_Extra_Nodes_To_Hide_Ribbon_Knee_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01|Ribbons_Legs_Hide".format(settings["name"]))
    
    cmds.parent(f"Grp_Ribbon_Knee_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs".format(settings["name"]))
    
    DrvJnt_Knee_L = [f"DrvJnt_Knee_{side}"]
    MatrixConstrain.MatrixConstrain((f"DrvJnt_Knee_{side}", f"DrvJnt_Ankle_{side}"), f"CTRL_Global_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-4)
    MatrixConstrain.MatrixConstrain(DrvJnt_Knee_L, f"CTRL_Global_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-5)
    cmds.delete("{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Legs|Grp_Ribbon_Knee_{}|CTRL_Global_Ribbon_Knee_{}|IS_CONSTRAIN_BY___DrvJnt_Knee_{}__".format(settings["name"], side , side ,side))
    cmds.rotate(90, 0, 0, f"CTRL_Global_Ribbon_Knee_{side}", r=True, os=True)
    MatrixConstrain.MatrixConstrain(DrvJnt_Knee_L, f"CTRL_Global_Ribbon_Knee_{side}", Offset=True, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-6)
    MatrixConstrain.MatrixConstrain(Global, f"CTRL_Global_Ribbon_Knee_{side}", Offset=True, rX=False, rY=False, rZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-7)
    CTRL_Shape_Knee = cmds.listRelatives(f"CTRL_Global_Ribbon_Leg_{side}", shapes=True)
    cmds.setAttr(CTRL_Shape_Knee[0] + ".lodVisibility", 0)
    
    DrvJnt_Ankle_L = [f"DrvJnt_Ankle_{side}"]
    Preserve_Knee_L = [f"Preserve_Knee_{side}"]
    cmds.sets(f"Preserve_Knee_{side}", add="Bind_JNTs")
    MatrixConstrain.MatrixConstrain(DrvJnt_Leg_L, f"CTRL_End_Ribbon_Leg_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-8)
    MatrixConstrain.MatrixConstrain(DrvJnt_Ankle_L, f"CTRL_Start_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-9)
    MatrixConstrain.MatrixConstrain(Preserve_Knee_L, f"CTRL_End_Ribbon_Knee_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-10)
    MatrixConstrain.MatrixConstrain(Preserve_Knee_L, f"CTRL_Start_Ribbon_Leg_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-11)
    
    #Bend
    BendLeg = NewCTRL.Bend(f"PlacementCtrl_Ribbon_Leg_{side}", f"CTRL_Mid_Ribbon_Leg_{side}", name=f"CTRL_Mid_Ribbon_Leg_{side}")
    BendKnee = NewCTRL.Bend(f"PlacementCtrl_Ribbon_Knee_{side}", f"CTRL_Mid_Ribbon_Knee_{side}", name=f"CTRL_Mid_Ribbon_Knee_{side}")

    cmds.connectAttr(f"Settings_Leg_{side}.Vis_Bend", BendLeg + ".visibility")
    cmds.connectAttr(f"Settings_Leg_{side}.Vis_Bend", BendKnee + ".visibility")

    #endregion Leg 
    


    ############################################################################################################
    ############################################################################################################
    ################### C O M P U T E    L E G  T H O M A S  ##################################################
    ############################################################################################################
    ############################################################################################################

    computeThomas.createFoot(settings, side)
    
    ############################################################################################################
    ############################################################################################################
    ############################################################################################################
    ############################################################################################################
    ############################################################################################################


    
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
    MatrixConstrain.MatrixConstrain(FK_Leg, f"FK_Leg_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-12)
    MatrixConstrain.MatrixConstrain(FK_Knee, f"FK_Knee_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-13)
    MatrixConstrain.MatrixConstrain(FK_Ankle, f"FK_Ankle_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-14)
    MatrixConstrain.MatrixConstrain(FK_Ball, f"FK_Ball_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-15)

    Bind_Hip = [f"Bind_Hip_{side}"]
    MatrixConstrain.MatrixConstrain(Bind_Hip, f"CTRL_FK_Leg_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-16)


    
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
    MatrixConstrain.MatrixConstrain(CTRL_Foot_L, f"Locator_Ankle_{side}", Offset=True, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Leg", BookColumnOffset=BookmarkRowOffset, BookRowOffset=-17)
    
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

    #Bookmark
    Bookmark.createBookmark("IkFk_Leg")
    Bookmark.addNodeToBookmark("IkFk_Leg", f"Settings_Leg_{side}", column=BookmarkRowOffset, row=0, state=2)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"Locator_Hip_{side}", column=BookmarkRowOffset, row=1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"Locator_Ankle_{side}", column=BookmarkRowOffset, row=1.2, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"Distance_Leg_{side}", column=BookmarkRowOffset+1, row=1.1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", "GlobalMove_01", column=BookmarkRowOffset+1, row=1.3, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"MD_Distance_Leg_{side}_GlobalRelativeScale", column=BookmarkRowOffset+2, row=1.1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"MD_Distance_Leg_{side}_Divide", column=BookmarkRowOffset+3, row=1.1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"MD_Distance_Leg_{side}_Power", column=BookmarkRowOffset+4, row=1.1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"CTRL_Foot_{side}", column=BookmarkRowOffset+2, row=0, state=1)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"Cond_Distance_Leg_{side}", column=BookmarkRowOffset+3, row=0, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"Cond_Boolean_Leg_{side}", column=BookmarkRowOffset+4, row=0, state=0)

    Bookmark.addNodeToBookmark("IkFk_Leg", "Reverse_Leg_{}".format(side), column=BookmarkRowOffset+1, row=-0.2, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"IK_Leg_{side}", column=BookmarkRowOffset+1, row=-0.3, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"IK_Ball_{side}", column=BookmarkRowOffset+1, row=-0.4, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"IK_Toe_{side}", column=BookmarkRowOffset+1, row=-0.5, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"Bind_Foot_{side}", column=BookmarkRowOffset+1, row=-0.6, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"PV_Leg_{side}", column=BookmarkRowOffset+1, row=-0.7, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"CTRL_Pin_Knee_{side}", column=BookmarkRowOffset+1, row=-0.8, state=0)

    Bookmark.addNodeToBookmark("IkFk_Leg", f"FK_Leg_{side}", column=BookmarkRowOffset+5, row=-0.2, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"FK_Knee_{side}", column=BookmarkRowOffset+5, row=-0.4, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"FK_Ankle_{side}", column=BookmarkRowOffset+5, row=-0.6, state=0)

    Bookmark.addNodeToBookmark("IkFk_Leg", f"DrvJnt_Leg_{side}", column=BookmarkRowOffset+6, row=-0.2, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"DrvJnt_Knee_{side}", column=BookmarkRowOffset+6, row=-0.4, state=0)
    Bookmark.addNodeToBookmark("IkFk_Leg", f"DrvJnt_Ankle_{side}", column=BookmarkRowOffset+6, row=-0.6, state=0)

    #region Twist Ex 
    Twist_Leg = TwistExtractor.create_twist_extractor(f"Leg_{side}")
    Twist_Ankle = TwistExtractor.create_twist_extractor(f"Knee_{side}")

    cmds.duplicate(f"DrvJnt_Ankle_{side}", n=f"DrvJnt_Ankle_{side}_NonRoll", po=True)
    Color.setColor(f"DrvJnt_Ankle_{side}", "orange")
    cmds.createNode("multiplyDivide", n=f"Opposed_{side}")
    cmds.setAttr(f"Opposed_{side}.input2X", -1)
    cmds.setAttr(f"Opposed_{side}.input2Y", -1)

    OffsetBook = 0
    if side == "L":
        OffsetBook+=1
    NonRoll_Leg = NonRollMatrix.NonRollMatrix(f"Bind_Hip_{side}", f"DrvJnt_Leg_{side}", OffsetBookmark = OffsetBook)
    NonRoll_Foot = NonRollMatrix.NonRollMatrix(f"DrvJnt_Ankle_{side}_NonRoll", f"Bind_Foot_{side}", OffsetBookmark = OffsetBook+2)

    #Bookmark parenthese
    Bookmark.addNodeToBookmark("NonRoll", Twist_Leg, 5, OffsetBook, state = 1)
    Bookmark.addNodeToBookmark("NonRoll", f"Opposed_{side}", 4, OffsetBook, state = 1)
    Bookmark.addNodeToBookmark("NonRoll", f"CTRL_End_Ribbon_Leg_{side}", 6, OffsetBook, state = 1)
    Bookmark.addNodeToBookmark("NonRoll", Twist_Ankle, 4, OffsetBook+2, state = 1)
    Bookmark.addNodeToBookmark("NonRoll", f"CTRL_Start_Ribbon_Knee_{side}", 5, OffsetBook+2, state = 1)

    cmds.connectAttr(NonRoll_Foot + ".outputRotateZ", f"Opposed_{side}.input1X")
    cmds.connectAttr(f"Opposed_{side}.outputX", f"Twist_Knee_{side}_00.rotateX")
    cmds.connectAttr(NonRoll_Leg + ".outputRotateX", f"Opposed_{side}.input1Y")
    cmds.connectAttr(f"Opposed_{side}.outputY",f"Twist_Leg_{side}_00.rotateX")


    cmds.parent(f"Twist_Leg_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    cmds.parent(f"Twist_Knee_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    
    cmds.connectAttr(f"Twist_Leg_{side}_00.TwistEx", f"CTRL_End_Ribbon_Leg_{side}.rotateX")
    cmds.connectAttr(f"Twist_Knee_{side}_00.TwistEx", f"CTRL_Start_Ribbon_Knee_{side}.rotateX")

    #CTRL Hip
    if side == "L":
        CTRLhip = NewCTRL.NewCTRL("PlacementCtrl_Hip", "Bind_Hip", "CTRL_Hip", 2)
        cmds.parent(CTRLhip, "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))

        cmds.connectAttr("CTRL_Hip.t", "Bind_Hip.t")
        cmds.connectAttr("CTRL_Hip.r", "Bind_Hip.r")

#ajouter preserve au doigts

def createHand(settings, side = "L"):
    #region Creating the joints
    cmds.duplicate(f"PlacementJnt_Wrist_{side}", n=f"Bind_Hand_{side}", po=True)
    Color.setColor(f"Bind_Hand_{side}", "white")
    cmds.sets(f"Bind_Hand_{side}", add="Bind_JNTs")

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

    cmds.sets(f"Bind_{finger}_Metacarpus_{side}", add="Bind_JNTs")
    cmds.sets(f"Bind_{finger}_01_{side}", add="Bind_JNTs")
    cmds.sets(f"Bind_{finger}_02_{side}", add="Bind_JNTs")
    if finger == "Thumb":
        cmds.sets(f"Bind_{finger}_end_{side}", add="Bind_JNTs")
    else:
        cmds.sets(f"Bind_{finger}_03_{side}", add="Bind_JNTs")
        cmds.sets(f"Bind_{finger}_end_{side}", add="Bind_JNTs")

    
    #Create CTRLs
    
    NewCTRL.NewCTRL(f"PlacementCtrl_Finger_{finger}_Metacarpus_{side}", f"Bind_{finger}_Metacarpus_{side}", name=f"CTRL_Finger_{finger}_Metacarpus_{side}")
    NewCTRL.NewCTRL(f"PlacementCtrl_Finger_{finger}_01_{side}", f"Bind_{finger}_01_{side}", name=f"CTRL_Finger_{finger}_01_{side}")
    NewCTRL.NewCTRL(f"PlacementCtrl_Finger_{finger}_02_{side}", f"Bind_{finger}_02_{side}", name=f"CTRL_Finger_{finger}_02_{side}")

    if finger != "Thumb":
        NewCTRL.NewCTRL(f"PlacementCtrl_Finger_{finger}_03_{side}", f"Bind_{finger}_03_{side}", name=f"CTRL_Finger_{finger}_03_{side}")

    if not cmds.objExists("CTRLs_Hands"):
        cmds.group(n="CTRLs_Hands", em=True)
        cmds.parent("CTRLs_Hands", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))

    if not cmds.objExists(f"CTRLs_Hand_{side}"):
        cmds.group(empty=True, name=f"CTRLs_Hand_{side}")
        cmds.parent(f"CTRLs_Hand_{side}", "{}|GlobalMove_01|CTRLs_01|CTRLs_Hands".format(settings["name"]))
        Bind_Hand = [f"Bind_Hand_{side}"]
        MatrixConstrain.MatrixConstrain(Bind_Hand, f"CTRLs_Hand_{side}", Offset=True, sX=False, sY=False, sZ=False,)

    cmds.parent(f"CTRL_Finger_{finger}_Metacarpus_{side}_Offset", f"CTRLs_Hand_{side}")
    cmds.parent(f"CTRL_Finger_{finger}_01_{side}_Offset", f"CTRL_Finger_{finger}_Metacarpus_{side}")
    cmds.parent(f"CTRL_Finger_{finger}_02_{side}_Offset", f"CTRL_Finger_{finger}_01_{side}")

    if finger != "Thumb":
        cmds.parent(f"CTRL_Finger_{finger}_03_{side}_Offset", f"CTRL_Finger_{finger}_02_{side}")

    #Constraining 
    Metacarpus = [f"CTRL_Finger_{finger}_Metacarpus_{side}"]
    Finger01 = [f"CTRL_Finger_{finger}_01_{side}"]
    Finger02 = [f"CTRL_Finger_{finger}_02_{side}"]
    MatrixConstrain.MatrixConstrain(Metacarpus, f"Bind_{finger}_Metacarpus_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)
    MatrixConstrain.MatrixConstrain(Finger01, f"Bind_{finger}_01_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)
    MatrixConstrain.MatrixConstrain(Finger02, f"Bind_{finger}_02_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)

    if finger != "Thumb":
        Finger03 = [f"CTRL_Finger_{finger}_03_{side}"]
        MatrixConstrain.MatrixConstrain(Finger03, f"Bind_{finger}_03_{side}", Offset=True, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)

    
def createSpine(settings):
    #TO DO
    #savoir quelle hauteur doit faire la spine ===> un joitn de placement pour le chest
    Heigth = cmds.getAttr("PlacementJnt_Chest.translateY")
    #Savoir combien de CTRLFK                  ===> une option dans l'UI pour ecrire un attribut dans le dico settings
    NbrFK = int(settings["nbrCtrlFkSpine"])

    NbrJoints = int(settings["nbrJointsSpine"])

    OffsetCtrlRoot = ColumnRibbon.ColumnRibbon(name="{}".format(settings["name"]), height=Heigth, CTRLFK=NbrFK, JntNbr =NbrJoints ,BindSet="Bind_JNTs")

    #Placer la spine grace a son offset CTRL (match all transform of bind root)

    cmds.matchTransform(OffsetCtrlRoot, "Bind_Root", pos=True, rot=True)

    #COntraindre la spine au CTRL Global (all)

    MatrixConstrain.MatrixConstrain(["CTRL_{}_Global".format(settings["name"])], OffsetCtrlRoot)

    #Contraindre clavicle par BindChest

    MatrixConstrain.MatrixConstrain(["Bind_Chest"], "Bind_Clavicle_L_Hook", sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(["Bind_Chest"], "Bind_Clavicle_R_Hook", sX=False, sY=False, sZ=False)

    #Ctrl Clavicle a contraindre

    MatrixConstrain.MatrixConstrain(["Bind_Chest"], "CTRL_Clavicle_L_Move", sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(["Bind_Chest"], "CTRL_Clavicle_R_Move", sX=False, sY=False, sZ=False)

    #Contraindre BindRoot par BindRootSpine

    MatrixConstrain.MatrixConstrain(["Bind_Root_Spine"], "Bind_Root_Hook", sX=False, sY=False, sZ=False)

    #Ctrl Hip a contraindre

    MatrixConstrain.MatrixConstrain(["Bind_Root_Spine"], "CTRL_Hip_Move", sX=False, sY=False, sZ=False)

    #Hierarchiser Ribbon dans Extranodes

    cmds.parent("Ribbon_Spine_{}".format(settings["name"]), "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01".format(settings["name"]))

    #Shape CTRL a changer grace à NewCTRL.Bend
    
    NewCTRL.Bend("PlacementCtrl_Root", "CTRL_UpperBody", "CTRL_Root")
    NewCTRL.Bend("PlacementCtrl_Shoulder", "CTRL_FK_Chest", "CTRL_FK_Chest")
    NewCTRL.Bend("PlacementCtrl_Settings_Spine", "CTRL_Option", "CTRL_Settings_Spine")

    NewCTRL.Bend("PlacementCtrl_ShoulderIk", "CTRL_IK_Chest", "CTRL_IK_Chest")
    NewCTRL.Bend("PlacementCtrl_IkRoot", "CTRL_IK_Root", "CTRL_IK_Root")

    NewCTRL.Bend("PlacementCtrl_Tangent_Root", "CTRL_Tangent_Root", "CTRL_Tangent_Root")
    NewCTRL.Bend("PlacementCtrl_Tangent_Chest", "CTRL_Tangent_Chest", "CTRL_Tangent_Chest")

    if NbrFK == 1 :
        NewCTRL.Bend("PlacementCtrl_Spine_Ik_1", "CTRL_IK_Mid", "CTRL_IK_Mid")
        NewCTRL.Bend("PlacementCtrl_Spine_Fk_1", "CTRL_FK_Mid", "CTRL_FK_Mid")

    if NbrFK == int(3) :
        NewCTRL.Bend("PlacementCtrl_Spine_Ik_1", "CTRL_IK_Mid_Bottom", "CTRL_IK_Mid_Bottom")
        NewCTRL.Bend("PlacementCtrl_Spine_Fk_1", "CTRL_FK_Mid_Bottom", "CTRL_FK_Mid_Bottom")

        NewCTRL.Bend("PlacementCtrl_Spine_Ik_2", "CTRL_IK_Mid", "CTRL_IK_Mid")
        NewCTRL.Bend("PlacementCtrl_Spine_Fk_2", "CTRL_FK_Mid", "CTRL_FK_Mid")

        NewCTRL.Bend("PlacementCtrl_Spine_Ik_3", "CTRL_IK_Mid_Top", "CTRL_IK_Mid_Top")
        NewCTRL.Bend("PlacementCtrl_Spine_Fk_3", "CTRL_FK_Mid_Top", "CTRL_FK_Mid_Top")

    if NbrFK == 5 :
        NewCTRL.Bend("PlacementCtrl_Spine_Ik_1", "CTRL_IK_Mid1", "CTRL_IK_Mid1")
        NewCTRL.Bend("PlacementCtrl_Spine_Fk_1", "CTRL_FK_Mid1", "CTRL_FK_Mid1")

        NewCTRL.Bend("PlacementCtrl_Spine_Ik_2", "CTRL_IK_Mid2", "CTRL_IK_Mid2")
        NewCTRL.Bend("PlacementCtrl_Spine_Fk_2", "CTRL_FK_Mid2", "CTRL_FK_Mid2")

        NewCTRL.Bend("PlacementCtrl_Spine_Ik_3", "CTRL_IK_Mid", "CTRL_IK_Mid")
        NewCTRL.Bend("PlacementCtrl_Spine_Fk_3", "CTRL_FK_Mid", "CTRL_FK_Mid")

        NewCTRL.Bend("PlacementCtrl_Spine_Ik_4", "CTRL_IK_Mid3", "CTRL_IK_Mid3")
        NewCTRL.Bend("PlacementCtrl_Spine_Fk_4", "CTRL_FK_Mid3", "CTRL_FK_Mid3")

        NewCTRL.Bend("PlacementCtrl_Spine_Ik_5", "CTRL_IK_Mid4", "CTRL_IK_Mid4")
        NewCTRL.Bend("PlacementCtrl_Spine_Fk_5", "CTRL_FK_Mid4", "CTRL_FK_Mid4")
    
    for i in range(NbrJoints - 2):
        NewCTRL.Bend(f"PlacementCtrl_Spine_Ribbon_{i+1}", f"CTRL_RibbonSpine_0{i+1}", f"CTRL_RibbonSpine_0{i+1}")
        Shape = cmds.listRelatives(f"CTRL_RibbonSpine_0{i+1}", s=True)
        for shape in Shape:
            cmds.connectAttr("CTRL_Settings_Spine" + ".PinVisibility", shape + ".lodVisibility")

    visibilityShape("CTRL_FK_Mid", "Fk")
    visibilityShape("CTRL_FK_Chest", "Fk")

    visibilityShape("CTRL_IK_Root", "Ik")
    visibilityShape("CTRL_IK_Mid", "Ik")
    visibilityShape("CTRL_IK_Chest", "Ik")

    if NbrFK == 3:
        visibilityShape("CTRL_FK_Mid_Bottom", "Fk") 
        visibilityShape("CTRL_FK_Mid_Top", "Fk")
    
        visibilityShape("CTRL_IK_Mid_Bottom", "Ik")
        visibilityShape("CTRL_IK_Mid_Top", "Ik")

    if NbrFK == 5:
        visibilityShape("CTRL_IK_Mid1", "Ik")
        visibilityShape("CTRL_IK_Mid2", "Ik")
        visibilityShape("CTRL_IK_Mid3", "Ik")
        visibilityShape("CTRL_IK_Mid4", "Ik")
    
        visibilityShape("CTRL_FK_Mid1", "Fk")
        visibilityShape("CTRL_FK_Mid2", "Fk")
        visibilityShape("CTRL_FK_Mid3", "Fk")
        visibilityShape("CTRL_FK_Mid4", "Fk")

    #parent Ctrl Option into Ctrl Settings
    cmds.parent("CTRL_Settings_Spine", "CTRL_Settings")
    cmds.makeIdentity("CTRL_Settings_Spine", t=True, a=True)


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
    cmds.sets(f"Preserve_Elbow_{side}", add="Bind_JNTs")


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

    cmds.sets(f"Bind_Clavicle_{side}", add="Bind_JNTs")
    cmds.sets(f"Bind_Clavicle_end_{side}", add="Bind_JNTs")

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
    BookmarkColumnOffset =0
    if side == "L":
        BookmarkColumnOffset=-10
    cmds.ikHandle(n=f"IK_Arm_{side}", sj=f"DrvJnt_Arm_{side}", ee=f"DrvJnt_Wrist_{side}", sol="ikRPsolver")
    cmds.parent(f"IK_Arm_{side}", "{}|GlobalMove_01|IKs_01".format(settings["name"]))
    CTRL_Wrist_L = [f"CTRL_Wrist_{side}"]  
    MatrixConstrain.MatrixConstrain(CTRL_Wrist_L, f"IK_Arm_{side}", BookmarkName="MatX_Arm", BookRowOffset=0, BookColumnOffset=BookmarkColumnOffset)
    #pole vector
    #Locator = cmds.spaceLocator(n=f"PoleVector_Arm_{side}")
    #Color.setColor(f"PoleVector_Arm_{side}", "green")
    PoleVector.PoleVector(joint_1=f"DrvJnt_Arm_{side}", joint_2=f"DrvJnt_Elbow_{side}", joint_3=f"DrvJnt_Wrist_{side}", CTRL=f"PlacementCtrl_Pv_Arm_{side}")
    cmds.rename(f"PlacementCtrl_Pv_Arm_{side}", f"PV_Arm_{side}")
    Offset.offset(f"PV_Arm_{side}", nbr=1)
    cmds.poleVectorConstraint(f"PV_Arm_{side}", f"IK_Arm_{side}")
    cmds.parent(f"PV_Arm_{side}_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    #Create a locator that match the transform of the pole vector and parent it inside the fk Knee
    cmds.spaceLocator(n=f"Locator_PoleVector_Elbow_{side}")[0]
    cmds.matchTransform(f"Locator_PoleVector_Elbow_{side}", f"PV_Arm_{side}", pos=True)
    cmds.parent(f"Locator_PoleVector_Elbow_{side}", f"FK_Elbow_{side}")
    
    #region Attach Joints 
    DrvJnt_Arm_L = [f"DrvJnt_Arm_{side}"]
    Bind_Clavicle_end = [f"Bind_Clavicle_end_{side}"]
    MatrixConstrain.MatrixConstrain(Bind_Clavicle_end, f"FK_Arm_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-1, BookColumnOffset=BookmarkColumnOffset)
    MatrixConstrain.MatrixConstrain(Bind_Clavicle_end, f"DrvJnt_Arm_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-2, BookColumnOffset=BookmarkColumnOffset)
    MatrixConstrain.MatrixConstrain(DrvJnt_Arm_L, f"Preserve_Elbow_{side}_Hook", Offset=True, sX=False, sY=False, sZ=False, BookmarkName="MatX_Arm", BookRowOffset=-3, BookColumnOffset=BookmarkColumnOffset)
    
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
    Ribbon.Ribbon(Name=f"Ribbon_Arm_{side}", Span=5, BindSet = "Bind_JNTs", BookRowOffset=-6, BookColumnOffset=BookmarkColumnOffset)
    Ribbon.Ribbon(Name=f"Ribbon_Elbow_{side}", Span=5, BindSet = "Bind_JNTs", BookRowOffset=-4, BookColumnOffset=BookmarkColumnOffset)

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
    MatrixConstrain.MatrixConstrain((f"DrvJnt_Arm_{side}", f"DrvJnt_Elbow_{side}"), f"CTRL_Global_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-4, BookColumnOffset=BookmarkColumnOffset)
    MatrixConstrain.MatrixConstrain(DrvJnt_Arm_L, "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Arms|Grp_Ribbon_Arm_{}|CTRL_Global_Ribbon_Arm_{}".format(settings["name"], side,side), Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Arm", BookRowOffset=-5, BookColumnOffset=BookmarkColumnOffset)
    MatrixConstrain.MatrixConstrain(Global, "CTRL_Global_Ribbon_Arm_{}".format(side), Offset=False, rX=False, rY=False, rZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Arm", BookRowOffset=-6, BookColumnOffset=BookmarkColumnOffset)
    CTRL_Shape_Arm = cmds.listRelatives(f"CTRL_Global_Ribbon_Arm_{side}", shapes=True)
    cmds.setAttr(CTRL_Shape_Arm[0] + ".lodVisibility", 0)
    
    cmds.parent(f"Grp_Ribbon_Elbow_{side}|Grp_Extra_Nodes_Ribbon_Elbow_{side}|Grp_Extra_Nodes_To_Hide_Ribbon_Elbow_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01|Ribbons_Arms_Hide".format(settings["name"]))
    
    cmds.parent(f"Grp_Ribbon_Elbow_{side}", "{}|Extra_Nodes_01|Extra_Nodes_To_Show_01|Ribbons_Arms".format(settings["name"]))
    
    DrvJnt_Elbow_L = [f"DrvJnt_Elbow_{side}"]
    MatrixConstrain.MatrixConstrain((f"DrvJnt_Elbow_{side}", f"DrvJnt_Wrist_{side}"), f"CTRL_Global_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-7, BookColumnOffset=BookmarkColumnOffset)
    MatrixConstrain.MatrixConstrain(DrvJnt_Elbow_L, f"CTRL_Global_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Arm", BookRowOffset=-8, BookColumnOffset=BookmarkColumnOffset)
    MatrixConstrain.MatrixConstrain(Global, f"CTRL_Global_Ribbon_Elbow_{side}", Offset=False, rX=False, rY=False, rZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Arm", BookRowOffset=-9, BookColumnOffset=BookmarkColumnOffset)

    CTRL_Shape_Elbow = cmds.listRelatives(f"CTRL_Global_Ribbon_Elbow_{side}", shapes=True)
    cmds.setAttr(CTRL_Shape_Elbow[0] + ".lodVisibility", 0)
    
    DrvJnt_Wrist_L = [f"DrvJnt_Wrist_{side}"]
    Preserve_Elbow_L = [f"Preserve_Elbow_{side}"]
    if side =="L":
        MatrixConstrain.MatrixConstrain(DrvJnt_Arm_L, f"CTRL_End_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-10, BookColumnOffset=BookmarkColumnOffset)
        MatrixConstrain.MatrixConstrain(DrvJnt_Wrist_L, f"CTRL_Start_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-11, BookColumnOffset=BookmarkColumnOffset)
        MatrixConstrain.MatrixConstrain(Preserve_Elbow_L, f"CTRL_End_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-12, BookColumnOffset=BookmarkColumnOffset)
        MatrixConstrain.MatrixConstrain(Preserve_Elbow_L, f"CTRL_Start_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-13, BookColumnOffset=BookmarkColumnOffset)
    elif side =="R":
        MatrixConstrain.MatrixConstrain(DrvJnt_Arm_L, f"CTRL_Start_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-10, BookColumnOffset=BookmarkColumnOffset)
        MatrixConstrain.MatrixConstrain(DrvJnt_Wrist_L, f"CTRL_End_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-11, BookColumnOffset=BookmarkColumnOffset)
        MatrixConstrain.MatrixConstrain(Preserve_Elbow_L, f"CTRL_Start_Ribbon_Elbow_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-12, BookColumnOffset=BookmarkColumnOffset)
        MatrixConstrain.MatrixConstrain(Preserve_Elbow_L, f"CTRL_End_Ribbon_Arm_{side}", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-13, BookColumnOffset=BookmarkColumnOffset)
    
    #Bend
    BendArm = NewCTRL.Bend(f"PlacementCtrl_Ribbon_Arm_{side}", f"CTRL_Mid_Ribbon_Arm_{side}", name=f"CTRL_Mid_Ribbon_Arm_{side}")
    BendElbow = NewCTRL.Bend(f"PlacementCtrl_Ribbon_Elbow_{side}", f"CTRL_Mid_Ribbon_Elbow_{side}", name=f"CTRL_Mid_Ribbon_Elbow_{side}")

    cmds.connectAttr(f"Settings_Arm_{side}.Vis_Bend", BendArm + ".visibility")
    cmds.connectAttr(f"Settings_Arm_{side}.Vis_Bend", BendElbow + ".visibility")

    #endregion Arm 
    
    
    
    #region Connection IK/FK
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"IK_Arm_{side}.ikBlend")
    
    cmds.connectAttr(f"FK_Arm_{side}.rotate", f"DrvJnt_Arm_{side}.rotate")
    cmds.connectAttr(f"FK_Arm_{side}.t", f"DrvJnt_Arm_{side}.t")
    cmds.connectAttr(f"FK_Elbow_{side}.rotate", f"DrvJnt_Elbow_{side}.rotate")
    cmds.connectAttr(f"FK_Elbow_{side}.t", f"DrvJnt_Elbow_{side}.t")
    
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
    MatrixConstrain.MatrixConstrain(FK_Arm, f"FK_Arm_{side}", Offset=True, sX=False, sY=False, sZ=False, BookmarkName="MatX_Arm", BookRowOffset=-14, BookColumnOffset=BookmarkColumnOffset)
    MatrixConstrain.MatrixConstrain(FK_Elbow, f"FK_Elbow_{side}", Offset=True, sX=False, sY=False, sZ=False, BookmarkName="MatX_Arm", BookRowOffset=-15, BookColumnOffset=BookmarkColumnOffset)
    MatrixConstrain.MatrixConstrain(FK_Wrist, f"FK_Wrist_{side}", Offset=True, sX=False, sY=False, sZ=False, BookmarkName="MatX_Arm", BookRowOffset=-16, BookColumnOffset=BookmarkColumnOffset)

    Bind_Clavicle = [f"Bind_Clavicle_{side}"]
    MatrixConstrain.MatrixConstrain(Bind_Clavicle, f"CTRL_FK_Arm_{side}_Hook", Offset=True, rX=False, rY=False, rZ=False, sX=False, sY=False, sZ=False, BookmarkName="MatX_Arm", BookRowOffset=-17, BookColumnOffset=BookmarkColumnOffset)

    
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
    MatrixConstrain.MatrixConstrain(CTRL_Wrist_L, f"Locator_Wrist_{side}", Offset=True, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False, BookmarkName="MatX_Arm", BookRowOffset=-18, BookColumnOffset=BookmarkColumnOffset)
    
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
    MatrixConstrain.MatrixConstrain(DrvJntWrist, f"Bind_Hand_{side}_Hook", sX=False, sY=False, sZ=False, BookmarkName="MatX_Arm", BookRowOffset=-19, BookColumnOffset=BookmarkColumnOffset)

    #Node Conditon
    cmds.createNode("condition", n=f"Cond_ConstraintRotate_DrvJnt_{side}")
    cmds.createNode("condition", n=f"Cond_ConstraintTranslate_DrvJnt_{side}")
    CTRL_IK_Wrist = [f"CTRL_Wrist_{side}"]
    FK_Constraint = MatrixConstrain.MatrixConstrain(FK_Wrist, f"DrvJnt_Wrist_{side}", sX=False, sY=False, sZ=False, BookmarkName="MatX_Arm", BookRowOffset=-20, BookColumnOffset=BookmarkColumnOffset)
    cmds.disconnectAttr(f"{FK_Constraint[1]}.outputRotateX",f"DrvJnt_Wrist_{side}.rotateX")
    cmds.disconnectAttr(f"{FK_Constraint[1]}.outputRotateY",f"DrvJnt_Wrist_{side}.rotateY")
    cmds.disconnectAttr(f"{FK_Constraint[1]}.outputRotateZ",f"DrvJnt_Wrist_{side}.rotateZ")
    cmds.connectAttr(f"{FK_Constraint[1]}.outputRotate", f"Cond_ConstraintRotate_DrvJnt_{side}.colorIfTrue")
    cmds.disconnectAttr(f"{FK_Constraint[0]}.outputTranslateX",f"DrvJnt_Wrist_{side}.translateX")
    cmds.disconnectAttr(f"{FK_Constraint[0]}.outputTranslateY",f"DrvJnt_Wrist_{side}.translateY")
    cmds.disconnectAttr(f"{FK_Constraint[0]}.outputTranslateZ",f"DrvJnt_Wrist_{side}.translateZ")
    cmds.connectAttr(f"{FK_Constraint[0]}.outputTranslate", f"Cond_ConstraintTranslate_DrvJnt_{side}.colorIfTrue")
    IK_Constraint = MatrixConstrain.MatrixConstrain(CTRL_IK_Wrist, f"DrvJnt_Wrist_{side}", sX=False, sY=False, sZ=False, tX=False, tY=False, tZ=False, BookmarkName="MatX_Arm", BookRowOffset=-21, BookColumnOffset=BookmarkColumnOffset)
    cmds.disconnectAttr(f"{IK_Constraint[1]}.outputRotateX",f"DrvJnt_Wrist_{side}.rotateX")
    cmds.disconnectAttr(f"{IK_Constraint[1]}.outputRotateY",f"DrvJnt_Wrist_{side}.rotateY")
    cmds.disconnectAttr(f"{IK_Constraint[1]}.outputRotateZ",f"DrvJnt_Wrist_{side}.rotateZ") 
    cmds.connectAttr(f"{IK_Constraint[1]}.outputRotate", f"Cond_ConstraintRotate_DrvJnt_{side}.colorIfFalse")

    coloriffalseR = cmds.getAttr(f"DrvJnt_Wrist_{side}.translateX")
    cmds.setAttr(f"Cond_ConstraintTranslate_DrvJnt_{side}.colorIfFalseR", coloriffalseR)
    cmds.setAttr(f"Cond_ConstraintTranslate_DrvJnt_{side}.colorIfFalseG", 0)
    cmds.setAttr(f"Cond_ConstraintTranslate_DrvJnt_{side}.colorIfFalseB", 0)

    cmds.connectAttr(f"Cond_ConstraintRotate_DrvJnt_{side}.outColor", f"DrvJnt_Wrist_{side}.r")
    cmds.connectAttr(f"Cond_ConstraintTranslate_DrvJnt_{side}.outColor", f"DrvJnt_Wrist_{side}.t")
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"Cond_ConstraintRotate_DrvJnt_{side}.secondTerm")
    cmds.connectAttr(f"Settings_Arm_{side}.IK_FK", f"Cond_ConstraintTranslate_DrvJnt_{side}.secondTerm")

    #Bookmark
    Bookmark.createBookmark("IkFk_Arm")
    Bookmark.addNodeToBookmark("IkFk_Arm", f"Settings_Arm_{side}", column=BookmarkColumnOffset, row=0, state=2)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"Locator_Hip_{side}", column=BookmarkColumnOffset, row=1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"Locator_Ankle_{side}", column=BookmarkColumnOffset, row=1.2, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"Distance_Arm_{side}", column=BookmarkColumnOffset+1, row=1.1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", "GlobalMove_01", column=BookmarkColumnOffset+1, row=1.3, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"MD_Distance_Arm_{side}_GlobalRelativeScale", column=BookmarkColumnOffset+2, row=1.1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"MD_Distance_Arm_{side}_Divide", column=BookmarkColumnOffset+3, row=1.1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"MD_Distance_Arm_{side}_Power", column=BookmarkColumnOffset+4, row=1.1, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"CTRL_Foot_{side}", column=BookmarkColumnOffset+2, row=0, state=1)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"Cond_Distance_Arm_{side}", column=BookmarkColumnOffset+3, row=0, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"Cond_Boolean_Arm_{side}", column=BookmarkColumnOffset+4, row=0, state=0)

    Bookmark.addNodeToBookmark("IkFk_Arm", "Reverse_Arm_{}".format(side), column=BookmarkColumnOffset+1, row=-0.2, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"IK_Arm_{side}", column=BookmarkColumnOffset+1, row=-0.3, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"IK_Ball_{side}", column=BookmarkColumnOffset+1, row=-0.4, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"IK_Toe_{side}", column=BookmarkColumnOffset+1, row=-0.5, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"Bind_Foot_{side}", column=BookmarkColumnOffset+1, row=-0.6, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"PV_Arm_{side}", column=BookmarkColumnOffset+1, row=-0.7, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"CTRL_Pin_Knee_{side}", column=BookmarkColumnOffset+1, row=-0.8, state=0)

    Bookmark.addNodeToBookmark("IkFk_Arm", f"FK_Arm_{side}", column=BookmarkColumnOffset+5, row=-0.2, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"FK_Knee_{side}", column=BookmarkColumnOffset+5, row=-0.4, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"FK_Ankle_{side}", column=BookmarkColumnOffset+5, row=-0.6, state=0)

    Bookmark.addNodeToBookmark("IkFk_Arm", f"DrvJnt_Arm_{side}", column=BookmarkColumnOffset+6, row=-0.2, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"DrvJnt_Knee_{side}", column=BookmarkColumnOffset+6, row=-0.4, state=0)
    Bookmark.addNodeToBookmark("IkFk_Arm", f"DrvJnt_Ankle_{side}", column=BookmarkColumnOffset+6, row=-0.6, state=0)

    #region Twist Ex 
    TwistArm = TwistExtractor.create_twist_extractor(f"Arm_{side}")
    TwistWrist = TwistExtractor.create_twist_extractor(f"Wrist_{side}")

    cmds.duplicate(f"DrvJnt_Wrist_{side}", n=f"DrvJnt_Wrist_{side}_NonRoll", po=True)
    Color.setColor(f"DrvJnt_Wrist_{side}", "orange")

    cmds.createNode("multiplyDivide", n=f"OpposedArm_{side}")
    cmds.setAttr(f"OpposedArm_{side}.input2X", -1)

    OffsetBook = 4
    if side == "L":
        OffsetBook+=1
    NonRoll_Arm = NonRollMatrix.NonRollMatrix(f"Bind_Clavicle_{side}", f"DrvJnt_Arm_{side}", OffsetBookmark = OffsetBook)

    cmds.connectAttr(NonRoll_Arm + ".outputRotateX", f"OpposedArm_{side}.input1X")
    cmds.connectAttr(f"OpposedArm_{side}.outputX",f"Twist_Arm_{side}_00.rotateX")

    DrvJntNonRollWrist = cmds.duplicate(DrvJnt_Wrist_L[0], po=True, name=DrvJnt_Wrist_L[0] + "_NonRoll")
    NonRoll_Hand = NonRollMatrix.NonRollMatrix(DrvJntNonRollWrist, DrvJnt_Wrist_L[0], OffsetBookmark = OffsetBook+2)
    cmds.connectAttr(NonRoll_Hand + ".outputRotateX", f"Twist_Wrist_{side}_00.rotateX")

    #Bookmark parenthese
    Bookmark.addNodeToBookmark("NonRoll", TwistArm, 5, OffsetBook, state = 1)
    Bookmark.addNodeToBookmark("NonRoll", f"OpposedArm_{side}", 4, OffsetBook, state = 1)
    Bookmark.addNodeToBookmark("NonRoll", TwistWrist, 4, OffsetBook+2, state = 1)

    cmds.parent(f"Twist_Arm_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    cmds.parent(f"Twist_Wrist_{side}_grp", "{}|Extra_Nodes_01|Extra_Nodes_To_Hide_01".format(settings["name"]))
    
    if side == "L":
        cmds.connectAttr(f"Twist_Arm_{side}_00.TwistEx", f"CTRL_End_Ribbon_Arm_{side}.rotateX")
        cmds.connectAttr(f"Twist_Wrist_{side}_00.TwistEx", f"CTRL_Start_Ribbon_Elbow_{side}.rotateX")
        Bookmark.addNodeToBookmark("NonRoll", f"CTRL_End_Ribbon_Arm_{side}", 6, OffsetBook, state = 1)
        Bookmark.addNodeToBookmark("NonRoll", f"CTRL_Start_Ribbon_Elbow_{side}", 5, OffsetBook+2, state = 1)

    elif side == "R":
        cmds.connectAttr(f"Twist_Arm_{side}_00.TwistEx", f"CTRL_Start_Ribbon_Arm_{side}.rotateX")
        cmds.connectAttr(f"Twist_Wrist_{side}_00.TwistEx", f"CTRL_End_Ribbon_Elbow_{side}.rotateX")
        Bookmark.addNodeToBookmark("NonRoll", f"CTRL_Start_Ribbon_Arm_{side}", 6, OffsetBook, state = 1)
        Bookmark.addNodeToBookmark("NonRoll", f"CTRL_End_Ribbon_Elbow_{side}", 5, OffsetBook+2, state = 1)
    
    #Clavicle CTRLs
    CTRLclavicle = NewCTRL.NewCTRL(f"PlacementCtrl_Clavicle_{side}", f"Bind_Clavicle_{side}", f"CTRL_Clavicle_{side}", 2)
    cmds.parent(CTRLclavicle, "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))

    cmds.connectAttr(f"CTRL_Clavicle_{side}.t", f"Bind_Clavicle_{side}.t")
    cmds.connectAttr(f"CTRL_Clavicle_{side}.r", f"Bind_Clavicle_{side}.r")