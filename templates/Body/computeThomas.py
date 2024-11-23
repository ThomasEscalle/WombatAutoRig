from maya import cmds
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import MatrixConstrain


# Compute the creation of the foot (left)
def compute(settings):
    
    # Duplicate the joint "PlacementJnt_Ankle_L"
    foot = cmds.duplicate("PlacementJnt_Ankle_L", n="Bind_Foot_L")
    # Put the foot at the root of the scene
    cmds.parent("Bind_Foot_L", world=True)
    # Rename the joint "PlacementJnt_Toe_L" to "Bind_Toe_L"
    cmds.rename("Bind_Foot_L|PlacementJnt_Ball_L", "Bind_Ball_l")
    # Rename the joint "PlacementJnt_ToeEnd_L" to "Bind_ToeEnd_L"
    cmds.rename("Bind_Foot_L|Bind_Ball_l|PlacementJnt_Toe_L", "Bind_Toe_L")

    # Add the color to the foot
    Color.setColor("Bind_Foot_L", "white")
    Color.setColor("Bind_Ball_l", "white")
    Color.setColor("Bind_Toe_L", "white")

    # Freeze the transformation of the foot
    cmds.makeIdentity("Bind_Foot_L", a=True, t=True, r=True, s=True)

    # Add an offset and move group to the foot
    Offset.offset("Bind_Foot_L", 2 )

    # Group the Bind_Foot_L_Offset under the group "Joints_Feets"
    # Check if the group "Joints_Feets" exists
    if not cmds.objExists("Joints_Feets"):
        # Create the group "Joints_Feets"
        cmds.group(em=True, name="Joints_Feets")
    cmds.parent("Bind_Foot_L_Offset", "Joints_Feets") 


    # Duplicate the controller "AutoRig_Data|ControllersPlacement|IK_Controllers|PlacementCtrl_Foot_L"
    ctrl = cmds.duplicate("AutoRig_Data|ControllersPlacement|IK_Controllers|PlacementCtrl_Foot_L", n="CTRL_Foot_L")
    # Put the controller at the root of the scene
    cmds.parent("CTRL_Foot_L", world=True)
    # Freeze the transformation of the controller
    cmds.makeIdentity("CTRL_Foot_L", a=True, t=True, r=True, s=True)
    # Match the pivot of the controller with the pivot of the foot
    cmds.matchTransform("CTRL_Foot_L", "Bind_Foot_L", pos=False, rot=False, scl=False, piv=True)

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
    cmds.select("CTRL_Foot_L")
    cmds.addAttr( ln="_________",sn = "_________", at="enum", en="_________", keyable=True)

    # Add the attribute "Twist_Leg"
    cmds.select("CTRL_Foot_L")
    cmds.addAttr( ln="Twist_Leg", at="double", min=-360, max=360, dv=0, k=True)

    # Add the attribute "Foot_Roll"
    cmds.select("CTRL_Foot_L")
    cmds.addAttr( ln="Foot_Roll", at="double", min=-1, max=1, dv=0, k=True)

    # Add the attribute "Twist_Heel"
    cmds.select("CTRL_Foot_L")
    cmds.addAttr( ln="Twist_Heel", at="double", min=-1, max=1, dv=0, k=True)

    # Add the attribute "Twist_Toe"
    cmds.select("CTRL_Foot_L")
    cmds.addAttr( ln="Twist_Toe", at="double", min=-1, max=1, dv=0, k=True)

    # Add the attribute "Flex_Toe"
    cmds.select("CTRL_Foot_L")
    cmds.addAttr( ln="Flex_Toe", at="double", min=-1, max=1, dv=0, k=True)

    # Add the attribute "Bank" 
    cmds.select("CTRL_Foot_L")
    cmds.addAttr( ln="Bank", at="double", min=-30, max=30, dv=0, k=True)

    # Add a separator
    cmds.select("CTRL_Foot_L")
    cmds.addAttr( ln="__________",sn = "__________", at="enum", en="__________", keyable=True)

    # Add the attribute "Stretch_Leg_Left"
    cmds.select("CTRL_Foot_L")
    cmds.addAttr( ln="Stretch_Leg_Left", at="bool", dv=False, k=True)


    # endregion Attributes


    # Create Ik Single Chain from the foot to the ball
    IK_Ball_L = cmds.ikHandle( n="IK_Ball_L", sj="Bind_Foot_L", ee="Bind_Ball_l", sol="ikSCsolver")
    # Create Ik Single Chain from the ball to the toe
    IK_Toe_L = cmds.ikHandle( n="IK_Toe_L", sj="Bind_Ball_l", ee="Bind_Toe_L", sol="ikSCsolver")


    # region Hierarchie

    # Add five locators (Loc_Bank_Int_L, Loc_Bank_Ext_L, Loc_Ball_L, Loc_Heel_L, Loc_Toe_L)
    cmds.spaceLocator(n="Loc_Bank_Int_L")
    cmds.spaceLocator(n="Loc_Bank_Ext_L")
    cmds.spaceLocator(n="Loc_Ball_L")
    cmds.spaceLocator(n="Loc_Heel_L")
    cmds.spaceLocator(n="Loc_Toe_L")

    # Add three empty groups with no parents (Pivot_Ball_L, Pivot_Toe_L, Pivot_Toe_L_Offset)
    cmds.group(em=True, n="Pivot_Ball_L")
    cmds.group(em=True, n="Pivot_Toe_L")
    cmds.group(em=True, n="Pivot_Toe_L_Offset")

    # Place the Loc_Bank_Int_L at the position of the PlacementCtrl_Foot_Int_L
    cmds.matchTransform("Loc_Bank_Int_L", "PlacementCtrl_Foot_Int_L", pos=True, rot=False, scl=False)
    # Place the Loc_Bank_Ext_L at the position of the PlacementCtrl_Foot_Ext_L
    cmds.matchTransform("Loc_Bank_Ext_L", "PlacementCtrl_Foot_Ext_L", pos=True, rot=False, scl=False)
    # PLace the Loc_Ball_L at the position of the Bind_Ball_L
    cmds.matchTransform("Loc_Ball_L", "Bind_Ball_l", pos=True, rot=False, scl=False)
    # Place the Loc_Toe_L at the position of the Bind_Toe_L
    cmds.matchTransform("Loc_Toe_L", "Bind_Toe_L", pos=True, rot=False, scl=False)
    # Place the Loc_Heel_L at the position of the PlacementCtrl_Foot_Back_L
    cmds.matchTransform("Loc_Heel_L", "PlacementCtrl_Foot_Back_L", pos=True, rot=False, scl=False)

    # Place the groups at the position of the Bind_Ball_L
    cmds.matchTransform("Pivot_Ball_L", "Bind_Ball_l", pos=False, rot=False, scl=False, piv=True)
    cmds.matchTransform("Pivot_Toe_L", "Bind_Ball_l", pos=False, rot=False, scl=False, piv=True)
    cmds.matchTransform("Pivot_Toe_L_Offset", "Bind_Ball_l", pos=False, rot=False, scl=False, piv=True)

    # Freeze the transformation of the locators
    cmds.makeIdentity("Loc_Bank_Int_L", a=True, t=True, r=True, s=True)
    cmds.makeIdentity("Loc_Bank_Ext_L", a=True, t=True, r=True, s=True)
    cmds.makeIdentity("Loc_Ball_L", a=True, t=True, r=True, s=True)
    cmds.makeIdentity("Loc_Heel_L", a=True, t=True, r=True, s=True)
    cmds.makeIdentity("Loc_Toe_L", a=True, t=True, r=True, s=True)

    # Parent the Loc_Bank_Int_L inside of CTRL_Foot_L
    cmds.parent("Loc_Bank_Int_L", "CTRL_Foot_L")
    # Parent the Loc_Bank_Ext_L inside of CTRL_Foot_L|Loc_Bank_Int_L
    cmds.parent("Loc_Bank_Ext_L", "CTRL_Foot_L|Loc_Bank_Int_L")
    # Parent the Loc_Ball_L inside of CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L
    cmds.parent("Loc_Ball_L", "CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L")
    # Parent the Loc_Toe_L inside of CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L
    cmds.parent("Loc_Toe_L", "CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L")
    # Parent the Loc_Heel_L inside of CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L|Loc_Toe_L
    cmds.parent("Loc_Heel_L", "CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L|Loc_Toe_L")
    # Parent the Pivot_ball_L inside of CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L|Loc_Toe_L|Loc_Heel_L
    cmds.parent("Pivot_Ball_L", "CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L|Loc_Toe_L|Loc_Heel_L")
    # Parent the Pivot_Toe_L_Offset inside of CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L|Loc_Toe_L|Loc_Heel_L
    cmds.parent("Pivot_Toe_L_Offset", "CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L|Loc_Toe_L|Loc_Heel_L")
    # Parent the Pivot_toe_L inside of CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L|Loc_Toe_L|Loc_Heel_L|Pivot_Toe_L_Offset
    cmds.parent("Pivot_Toe_L", "CTRL_Foot_L|Loc_Bank_Int_L|Loc_Bank_Ext_L|Loc_Ball_L|Loc_Toe_L|Loc_Heel_L|Pivot_Toe_L_Offset")

    # Parent the Ik_Toe_L inside of the Pivot_Toe_L
    cmds.parent("IK_Toe_L", "Pivot_Toe_L")
    # Parent the Ik_Ball_L inside of the Loc_Heel_L
    cmds.parent("IK_Ball_L", "Loc_Heel_L")

    # Hide the CTRL_Foot_L|Loc_Bank_Int_L
    cmds.setAttr("CTRL_Foot_L|Loc_Bank_Int_L.visibility", 0)
    



    # Connect the Pivot_Ball_L to the IK_Leg_L
    pvBall = ["Pivot_Ball_L"]
    MatrixConstrain.MatrixConstrain(pvBall, "IK_Leg_L", sX = True , sY = True, sZ = True)
    # Connect the DrvJnt_Ankle_L to the Bind_Foot_L
    drvAnkle = ["DrvJnt_Ankle_L"]
    MatrixConstrain.MatrixConstrain(drvAnkle, "Bind_Foot_L", sX = True , sY = True, sZ = True)






    # region Connections
    # Bank
    condBankInt = cmds.createNode("condition", n="Cond_Bank_Int_L")
    cmds.setAttr(condBankInt+".operation", 2)
    cmds.connectAttr("CTRL_Foot_L.Bank", condBankInt+".firstTerm", f=True)
    cmds.connectAttr("CTRL_Foot_L.Bank", condBankInt+".colorIfTrueR", f=True)
    cmds.connectAttr(condBankInt+".outColorR", "Loc_Bank_Int_L.rotateZ", f=True)
    condBankExt = cmds.createNode("condition", n="Cond_Bank_Ext_L")
    cmds.setAttr(condBankExt+".operation", 4)
    cmds.connectAttr("CTRL_Foot_L.Bank", condBankExt+".firstTerm", f=True)
    cmds.connectAttr("CTRL_Foot_L.Bank", condBankExt+".colorIfTrueR", f=True)
    cmds.connectAttr(condBankExt+".outColorR", "Loc_Bank_Ext_L.rotateZ", f=True)


    # Twist_Leg
    # Connect the CTRL_Foot_L.Twist_Leg to the IK_Leg_L.twist
    cmds.connectAttr("CTRL_Foot_L.Twist_Leg", "IK_Leg_L.twist", f=True)

    # Twist Heel
    maxTwistHeel = 75
    remapValueTwistHeel = cmds.createNode("remapValue", n="RmV_Twist_Heel_L")
    cmds.setAttr(remapValueTwistHeel+".inputMin", -1)
    cmds.setAttr(remapValueTwistHeel+".inputMax", 1)
    cmds.setAttr(remapValueTwistHeel+".outputMin", -maxTwistHeel)
    cmds.setAttr(remapValueTwistHeel+".outputMax", maxTwistHeel)
    cmds.connectAttr("CTRL_Foot_L.Twist_Heel", remapValueTwistHeel+".inputValue", f=True)
    cmds.connectAttr(remapValueTwistHeel+".outValue", "Loc_Heel_L.rotateY", f=True)

    # Twit Toe
    maxTwistToe = 75
    remapValueTwistToe = cmds.createNode("remapValue", n="RmV_Twist_Toe_L")
    cmds.setAttr(remapValueTwistToe+".inputMin", -1)
    cmds.setAttr(remapValueTwistToe+".inputMax", 1)
    cmds.setAttr(remapValueTwistToe+".outputMin", -maxTwistToe)
    cmds.setAttr(remapValueTwistToe+".outputMax", maxTwistToe)
    cmds.connectAttr("CTRL_Foot_L.Twist_Toe", remapValueTwistToe+".inputValue", f=True)
    cmds.connectAttr(remapValueTwistToe+".outValue", "Loc_Toe_L.rotateY", f=True)

    # Flex Toe (rotate X axis of the Pivot_Toe_L)
    maxFlexToe = 55
    remapValueFlexToe = cmds.createNode("remapValue", n="RmV_Flex_Toe_L")
    cmds.setAttr(remapValueFlexToe+".inputMin", -1)
    cmds.setAttr(remapValueFlexToe+".inputMax", 1)
    cmds.setAttr(remapValueFlexToe+".outputMin", -maxFlexToe)
    cmds.setAttr(remapValueFlexToe+".outputMax", maxFlexToe)
    cmds.connectAttr("CTRL_Foot_L.Flex_Toe", remapValueFlexToe+".inputValue", f=True)
    cmds.connectAttr(remapValueFlexToe+".outValue", "Pivot_Toe_L.rotateX", f=True)

    # Foot Roll
    maxFootRollHeel = -30
    remapValueFootRollHeel = cmds.createNode("remapValue", n="RmV_Foot_Roll_Heel_L")
    cmds.setAttr(remapValueFootRollHeel+".inputMin", -1)
    cmds.setAttr(remapValueFootRollHeel+".inputMax", 0)
    cmds.setAttr(remapValueFootRollHeel+".outputMin", 0)
    cmds.setAttr(remapValueFootRollHeel+".outputMax", maxFootRollHeel)
    cmds.setAttr(remapValueFootRollHeel+".value[0].value_FloatValue", 1)
    cmds.setAttr(remapValueFootRollHeel+".value[1].value_FloatValue", 0)
    cmds.connectAttr("CTRL_Foot_L.Foot_Roll", remapValueFootRollHeel+".inputValue", f=True)
    cmds.connectAttr(remapValueFootRollHeel+".outValue", "Loc_Heel_L.rotateX", f=True)
    maxFootRollBall = 50
    remapValueFootRollBall = cmds.createNode("remapValue", n="RmV_Foot_Roll_Ball_L")
    cmds.setAttr(remapValueFootRollBall+".inputMin", 0)
    cmds.setAttr(remapValueFootRollBall+".inputMax", 1)
    cmds.setAttr(remapValueFootRollBall+".outputMin", 0)
    cmds.setAttr(remapValueFootRollBall+".outputMax", maxFootRollBall)
    cmds.setAttr(remapValueFootRollBall+".value[1].value_Position", 0.5)
    cmds.setAttr(remapValueFootRollBall+".value[2].value_Position", 1)
    cmds.setAttr(remapValueFootRollBall+".value[2].value_FloatValue", 0)
    cmds.connectAttr("CTRL_Foot_L.Foot_Roll", remapValueFootRollBall+".inputValue", f=True)
    cmds.connectAttr(remapValueFootRollBall+".outValue", "Pivot_Ball_L.rotateX", f=True)
    maxFootRollToe = 60
    remapValueFootRollToe = cmds.createNode("remapValue", n="RmV_Foot_Roll_Toe_L")
    cmds.setAttr(remapValueFootRollToe+".inputMin", 0.5)
    cmds.setAttr(remapValueFootRollToe+".inputMax", 1)
    cmds.setAttr(remapValueFootRollToe+".outputMin", 0)
    cmds.setAttr(remapValueFootRollToe+".outputMax", maxFootRollToe)
    cmds.connectAttr("CTRL_Foot_L.Foot_Roll", remapValueFootRollToe+".inputValue", f=True)
    cmds.connectAttr(remapValueFootRollToe+".outValue", "Loc_Toe_L.rotateX", f=True)





    # endregion Connections


    # Move the CTRL_Foot_L to the group CTRLs_01
    cmds.parent("CTRL_Foot_L", "CTRLs_01")
    # Move the Joints_Feets to the group Joints_01
    cmds.parent("Joints_Feets", "Joints_01")


    return 42