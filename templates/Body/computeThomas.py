from maya import cmds
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import MatrixConstrain

def compute(settings):
    # Create the foot (left)
    createFoot(settings, "L")

    createFoot(settings, "R")

# Compute the creation of the foot
def createFoot(settings, side = "L"):
    
    # Duplicate the joint "PlacementJnt_Ankle_{side}"
    foot = cmds.duplicate(f"PlacementJnt_Ankle_{side}", n=f"Bind_Foot_{side}")
    # Put the foot at the root of the scene
    cmds.parent(f"Bind_Foot_{side}", world=True)
    # Rename the joint "PlacementJnt_Toe_{side}" to "Bind_Toe_{side}"
    cmds.rename(f"Bind_Foot_{side}|PlacementJnt_Ball_{side}", f"Bind_Ball_{side}")
    # Rename the joint "PlacementJnt_ToeEnd_{side}" to "Bind_ToeEnd_{side}"
    cmds.rename(f"Bind_Foot_{side}|Bind_Ball_{side}|PlacementJnt_Toe_{side}", f"Bind_Toe_{side}")

    # Add the color to the foot
    Color.setColor(f"Bind_Foot_{side}", "white")
    Color.setColor(f"Bind_Ball_{side}", "white")
    Color.setColor(f"Bind_Toe_{side}", "white")

    # Freeze the transformation of the foot
    cmds.makeIdentity(f"Bind_Foot_{side}", a=True, t=True, r=True, s=True)

    # Add an offset and move group to the foot
    Offset.offset(f"Bind_Foot_{side}", 2 )

    # Group the Bind_Foot_{side}_Offset under the group "Joints_Feets"
    # Check if the group "Joints_Feets" exists
    if not cmds.objExists("Joints_Feets"):
        # Create the group "Joints_Feets"
        cmds.group(em=True, name="Joints_Feets")
    cmds.parent(f"Bind_Foot_{side}_Offset", "Joints_Feets") 


    # Duplicate the controller "AutoRig_Data|ControllersPlacement|IK_Controllers|PlacementCtrl_Foot_{side}"
    ctrl = cmds.duplicate(f"AutoRig_Data|ControllersPlacement|IK_Controllers|PlacementCtrl_Foot_{side}", n=f"CTRL_Foot_{side}")
    # Put the controller at the root of the scene
    cmds.parent(f"CTRL_Foot_{side}", world=True)
    # Freeze the transformation of the controller
    cmds.makeIdentity(f"CTRL_Foot_{side}", a=True, t=True, r=True, s=True)
    # Match the pivot of the controller with the pivot of the foot
    cmds.matchTransform(f"CTRL_Foot_{side}", f"Bind_Foot_{side}", pos=False, rot=False, scl=False, piv=True)

    #region Attributes

    # Add the necessary attributes to the controller
    #   _____ Separator ______
    #   Twist_Leg (float) (no min, no max)
    #   Foot_Roll (float) (min -1, max 1)
    #   Twist_Heel (float) (min -1, max 1)
    #   Twist_Toe (float) (min -1, max 1)
    #   Flex_Toe (float) (min -1, max 1)
    #   Bank (float) (min -30 , max 30)
    #   _____ Separator ______
    #   Stretch_Leg_Left (boolean)

    # Add a separator
    cmds.select(f"CTRL_Foot_{side}")
    cmds.addAttr( ln="_________",sn = "_________", at="enum", en="_________", keyable=True)

    # Add the attribute "Twist_Leg"
    cmds.select(f"CTRL_Foot_{side}")
    cmds.addAttr( ln="Twist_Leg", at="double", min=-360, max=360, dv=0, k=True)

    # Add the attribute "Foot_Roll"
    cmds.select(f"CTRL_Foot_{side}")
    cmds.addAttr( ln="Foot_Roll", at="double", min=-1, max=1, dv=0, k=True)

    # Add the attribute "Twist_Heel"
    cmds.select(f"CTRL_Foot_{side}")
    cmds.addAttr( ln="Twist_Heel", at="double", min=-1, max=1, dv=0, k=True)

    # Add the attribute "Twist_Toe"
    cmds.select(f"CTRL_Foot_{side}")
    cmds.addAttr( ln="Twist_Toe", at="double", min=-1, max=1, dv=0, k=True)

    # Add the attribute "Flex_Toe"
    cmds.select(f"CTRL_Foot_{side}")
    cmds.addAttr( ln="Flex_Toe", at="double", min=-1, max=1, dv=0, k=True)

    # Add the attribute "Bank" 
    cmds.select(f"CTRL_Foot_{side}")
    cmds.addAttr( ln="Bank", at="double", min=-30, max=30, dv=0, k=True)

    # Add a separator
    cmds.select(f"CTRL_Foot_{side}")
    cmds.addAttr( ln="__________",sn = "__________", at="enum", en="__________", keyable=True)

    # Add the attribute "Stretch_{side}eg_{side}eft"
    cmds.select(f"CTRL_Foot_{side}")
    cmds.addAttr( ln=f"Stretch_Leg_{side}", at="bool", dv=False, k=True)


    # endregion Attributes


    # Create Ik Single Chain from the foot to the ball
    IK_Ball_L = cmds.ikHandle( n=f"IK_Ball_{side}", sj=f"Bind_Foot_{side}", ee=f"Bind_Ball_{side}", sol="ikSCsolver")
    # Create Ik Single Chain from the ball to the toe
    IK_Toe_L = cmds.ikHandle( n=f"IK_Toe_{side}", sj=f"Bind_Ball_{side}", ee=f"Bind_Toe_{side}", sol="ikSCsolver")


    # region Hierarchie

    # Add five locators (Loc_Bank_Int_L, Loc_Bank_Ext_L, Loc_Ball_L, Loc_Heel_L, Loc_Toe_L)
    cmds.spaceLocator(n=f"Loc_Bank_Int_{side}")
    cmds.spaceLocator(n=f"Loc_Bank_Ext_{side}")
    cmds.spaceLocator(n=f"Loc_Ball_{side}")
    cmds.spaceLocator(n=f"Loc_Heel_{side}")
    cmds.spaceLocator(n=f"Loc_Toe_{side}")

    # Add three empty groups with no parents (Pivot_Ball_L, Pivot_Toe_L, Pivot_Toe_L_Offset)
    cmds.group(em=True, n=f"Pivot_Ball_{side}")
    cmds.group(em=True, n=f"Pivot_Toe_{side}")
    cmds.group(em=True, n=f"Pivot_Toe_{side}_Offset")

    # Place the Loc_Bank_Int_L at the position of the PlacementCtrl_Foot_Int_L
    cmds.matchTransform(f"Loc_Bank_Int_{side}", f"PlacementCtrl_Foot_Int_{side}", pos=True, rot=False, scl=False)
    # Place the Loc_Bank_Ext_L at the position of the PlacementCtrl_Foot_Ext_L
    cmds.matchTransform(f"Loc_Bank_Ext_{side}", f"PlacementCtrl_Foot_Ext_{side}", pos=True, rot=False, scl=False)
    # PLace the Loc_Ball_L at the position of the Bind_Ball_L
    cmds.matchTransform(f"Loc_Ball_{side}", f"Bind_Ball_{side}", pos=True, rot=False, scl=False)
    # Place the Loc_Toe_L at the position of the Bind_Toe_L
    cmds.matchTransform(f"Loc_Toe_{side}", f"Bind_Toe_{side}", pos=True, rot=False, scl=False)
    # Place the Loc_Heel_L at the position of the PlacementCtrl_Foot_Back_L
    cmds.matchTransform(f"Loc_Heel_{side}", f"PlacementCtrl_Foot_Back_{side}", pos=True, rot=False, scl=False)

    # Place the groups at the position of the Bind_Ball_L
    cmds.matchTransform(f"Pivot_Ball_{side}", f"Bind_Ball_{side}", pos=False, rot=False, scl=False, piv=True)
    cmds.matchTransform(f"Pivot_Toe_{side}", f"Bind_Ball_{side}", pos=False, rot=False, scl=False, piv=True)
    cmds.matchTransform(f"Pivot_Toe_{side}_Offset", f"Bind_Ball_{side}", pos=False, rot=False, scl=False, piv=True)

    # Freeze the transformation of the locators
    cmds.makeIdentity(f"Loc_Bank_Int_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"Loc_Bank_Ext_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"Loc_Ball_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"Loc_Heel_{side}", a=True, t=True, r=True, s=True)
    cmds.makeIdentity(f"Loc_Toe_{side}", a=True, t=True, r=True, s=True)

    # Parent the Loc_Bank_Int_{side} inside of CTRL_Foot_{side}
    cmds.parent(f"Loc_Bank_Int_{side}", f"CTRL_Foot_{side}")
    # Parent the Loc_Bank_Ext_{side} inside of CTRL_Foot_{side}|Loc_Bank_Int_{side}
    cmds.parent(f"Loc_Bank_Ext_{side}", f"CTRL_Foot_{side}|Loc_Bank_Int_{side}")
    # Parent the Loc_Ball_{side} inside of CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}
    cmds.parent(f"Loc_Ball_{side}", f"CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}")
    # Parent the Loc_Toe_{side} inside of CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}
    cmds.parent(f"Loc_Toe_{side}", f"CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}")
    # Parent the Loc_Heel_{side} inside of CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}|Loc_Toe_{side}
    cmds.parent(f"Loc_Heel_{side}", f"CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}|Loc_Toe_{side}")
    # Parent the Pivot_ball_{side} inside of CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}|Loc_Toe_{side}|Loc_Heel_{side}
    cmds.parent(f"Pivot_Ball_{side}", f"CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}|Loc_Toe_{side}|Loc_Heel_{side}")
    # Parent the Pivot_Toe_{side}_Offset inside of CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}|Loc_Toe_{side}|Loc_Heel_{side}
    cmds.parent(f"Pivot_Toe_{side}_Offset", f"CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}|Loc_Toe_{side}|Loc_Heel_{side}")
    # Parent the Pivot_toe_{side} inside of CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}|Loc_Toe_{side}|Loc_Heel_{side}|Pivot_Toe_{side}_Offset
    cmds.parent(f"Pivot_Toe_{side}", f"CTRL_Foot_{side}|Loc_Bank_Int_{side}|Loc_Bank_Ext_{side}|Loc_Ball_{side}|Loc_Toe_{side}|Loc_Heel_{side}|Pivot_Toe_{side}_Offset")

    # Parent the Ik_Toe_{side} inside of the Pivot_Toe_{side}
    cmds.parent(f"IK_Toe_{side}", f"Pivot_Toe_{side}")
    # Parent the Ik_Ball_{side} inside of the Loc_Heel_{side}
    cmds.parent(f"IK_Ball_{side}", f"Loc_Heel_{side}")

    # Hide the CTRL_Foot_{side}|Loc_Bank_Int_{side}
    cmds.setAttr(f"CTRL_Foot_{side}|Loc_Bank_Int_{side}.visibility", 0)
    









    # region Connections
    # Bank
    condBankInt = cmds.createNode("condition", n=f"Cond_Bank_Int_{side}")
    cmds.setAttr(condBankInt+".operation", 2)
    cmds.connectAttr(f"CTRL_Foot_{side}.Bank", condBankInt+".firstTerm", f=True)
    cmds.connectAttr(f"CTRL_Foot_{side}.Bank", condBankInt+".colorIfTrueR", f=True)
    cmds.connectAttr(condBankInt+".outColorR", f"Loc_Bank_Int_{side}.rotateZ", f=True)
    condBankExt = cmds.createNode("condition", n=f"Cond_Bank_Ext_{side}")
    cmds.setAttr(condBankExt+".operation", 4)
    cmds.connectAttr(f"CTRL_Foot_{side}.Bank", condBankExt+".firstTerm", f=True)
    cmds.connectAttr(f"CTRL_Foot_{side}.Bank", condBankExt+".colorIfTrueR", f=True)
    cmds.connectAttr(condBankExt+".outColorR", f"Loc_Bank_Ext_{side}.rotateZ", f=True)


    # Twist_{side}eg
    # Connect the CTRL_Foot_{side}.Twist_{side}eg to the IK_Leg_L.twist
    cmds.connectAttr(f"CTRL_Foot_{side}.Twist_Leg", f"IK_Leg_{side}.twist", f=True)

    # Twist Heel
    maxTwistHeel = 75
    remapValueTwistHeel = cmds.createNode("remapValue", n=f"RmV_Twist_Heel_{side}")
    cmds.setAttr(remapValueTwistHeel+".inputMin", -1)
    cmds.setAttr(remapValueTwistHeel+".inputMax", 1)
    cmds.setAttr(remapValueTwistHeel+".outputMin", -maxTwistHeel)
    cmds.setAttr(remapValueTwistHeel+".outputMax", maxTwistHeel)
    cmds.connectAttr(f"CTRL_Foot_{side}.Twist_Heel", remapValueTwistHeel+".inputValue", f=True)
    cmds.connectAttr(remapValueTwistHeel+".outValue", f"Loc_Heel_{side}.rotateY", f=True)

    # Twit Toe
    maxTwistToe = 75
    remapValueTwistToe = cmds.createNode("remapValue", n="RmV_Twist_Toe_L")
    cmds.setAttr(remapValueTwistToe+".inputMin", -1)
    cmds.setAttr(remapValueTwistToe+".inputMax", 1)
    cmds.setAttr(remapValueTwistToe+".outputMin", -maxTwistToe)
    cmds.setAttr(remapValueTwistToe+".outputMax", maxTwistToe)
    cmds.connectAttr(f"CTRL_Foot_{side}.Twist_Toe", remapValueTwistToe+".inputValue", f=True)
    cmds.connectAttr(remapValueTwistToe+".outValue", f"Loc_Toe_{side}.rotateY", f=True)

    # Flex Toe (rotate X axis of the Pivot_Toe_L)
    maxFlexToe = 55
    remapValueFlexToe = cmds.createNode("remapValue", n=f"RmV_Flex_Toe_{side}")
    cmds.setAttr(remapValueFlexToe+".inputMin", -1)
    cmds.setAttr(remapValueFlexToe+".inputMax", 1)
    cmds.setAttr(remapValueFlexToe+".outputMin", -maxFlexToe)
    cmds.setAttr(remapValueFlexToe+".outputMax", maxFlexToe)
    cmds.connectAttr(f"CTRL_Foot_{side}.Flex_Toe", remapValueFlexToe+".inputValue", f=True)
    cmds.connectAttr(remapValueFlexToe+".outValue", f"Pivot_Toe_{side}.rotateX", f=True)

    # Foot Roll
    maxFootRollHeel = -30
    remapValueFootRollHeel = cmds.createNode("remapValue", n=f"RmV_Foot_Roll_Heel_{side}")
    cmds.setAttr(remapValueFootRollHeel+".inputMin", -1)
    cmds.setAttr(remapValueFootRollHeel+".inputMax", 0)
    cmds.setAttr(remapValueFootRollHeel+".outputMin", 0)
    cmds.setAttr(remapValueFootRollHeel+".outputMax", maxFootRollHeel)
    cmds.setAttr(remapValueFootRollHeel+".value[0].value_FloatValue", 1)
    cmds.setAttr(remapValueFootRollHeel+".value[1].value_FloatValue", 0)
    cmds.connectAttr(f"CTRL_Foot_{side}.Foot_Roll", remapValueFootRollHeel+".inputValue", f=True)
    cmds.connectAttr(remapValueFootRollHeel+".outValue", f"Loc_Heel_{side}.rotateX", f=True)
    maxFootRollBall = 50
    remapValueFootRollBall = cmds.createNode("remapValue", n=f"RmV_Foot_Roll_Ball_{side}")
    cmds.setAttr(remapValueFootRollBall+".inputMin", 0)
    cmds.setAttr(remapValueFootRollBall+".inputMax", 1)
    cmds.setAttr(remapValueFootRollBall+".outputMin", 0)
    cmds.setAttr(remapValueFootRollBall+".outputMax", maxFootRollBall)
    cmds.setAttr(remapValueFootRollBall+".value[1].value_Position", 0.5)
    cmds.setAttr(remapValueFootRollBall+".value[2].value_Position", 1)
    cmds.setAttr(remapValueFootRollBall+".value[2].value_FloatValue", 0)
    cmds.connectAttr(f"CTRL_Foot_{side}.Foot_Roll", remapValueFootRollBall+".inputValue", f=True)
    cmds.connectAttr(remapValueFootRollBall+".outValue", f"Pivot_Ball_{side}.rotateX", f=True)
    maxFootRollToe = 60
    remapValueFootRollToe = cmds.createNode("remapValue", n=f"RmV_Foot_Roll_Toe_{side}")
    cmds.setAttr(remapValueFootRollToe+".inputMin", 0.5)
    cmds.setAttr(remapValueFootRollToe+".inputMax", 1)
    cmds.setAttr(remapValueFootRollToe+".outputMin", 0)
    cmds.setAttr(remapValueFootRollToe+".outputMax", maxFootRollToe)
    cmds.connectAttr(f"CTRL_Foot_{side}.Foot_Roll", remapValueFootRollToe+".inputValue", f=True)
    cmds.connectAttr(remapValueFootRollToe+".outValue", f"Loc_Toe_{side}.rotateX", f=True)





    # endregion Connections


    # Move the CTRL_Foot_L to the group CTRLs_01
    cmds.parent(f"CTRL_Foot_{side}", "CTRLs_01")
    # Move the Joints_Feets to the group Joints_01
    cmds.parent("Joints_Feets", "Joints_01")



    # Connect the DrvJnt_Ankle_L to the Bind_Foot_L
    drvAnkle = [f"DrvJnt_Ankle_{side}"]
    MatrixConstrain.MatrixConstrain(drvAnkle, f"Bind_Foot_{side}_Move", sX = False , sY = False, sZ = False , Offset = True)

    # Connect the Pivot_Ball_L to the IK_Leg_
    pvBall = [f"Pivot_Ball_{side}"]
    MatrixConstrain.MatrixConstrain(pvBall, f"IK_Leg_{side}", sX = False , sY = False, sZ = False , Offset = True, rX= False, rY= False, rZ= False)
    
