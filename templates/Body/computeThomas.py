from maya import cmds
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Offset


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



    return 42