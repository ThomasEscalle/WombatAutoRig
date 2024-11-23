from maya import cmds
from wombatAutoRig.src.core import Color


def placeControllers(settings):
    print("Place the controllers")

    # PlacementCtrl_hip_L
    cmds.select(clear=True)
    PlacementCtrl_hip_L = cmds.circle(name="PlacementCtrl_hip_L", normal=[0, 1, 0], radius=9)
    cmds.matchTransform(PlacementCtrl_hip_L, "PlacementJnt_Hip_L", pos=True, rot=False, scl=False)
    cmds.parent(PlacementCtrl_hip_L, "AutoRig_Data|ControllersPlacement|FK_Controllers")
    Color.setColor("PlacementCtrl_hip_L", "yellow")


    # PlacementCtrl_knee_L
    cmds.select(clear=True)
    PlacementCtrl_knee_L = cmds.circle(name="PlacementCtrl_knee_L", normal=[0, 1, 0], radius=6)
    cmds.matchTransform(PlacementCtrl_knee_L, "PlacementJnt_Knee_L", pos=True, rot=False, scl=False)
    cmds.parent(PlacementCtrl_knee_L, "AutoRig_Data|ControllersPlacement|FK_Controllers")
    Color.setColor("PlacementCtrl_knee_L", "yellow")

    # PlacementCtrl_ankle_L
    cmds.select(clear=True)
    PlacementCtrl_ankle_L = cmds.circle(name="PlacementCtrl_ankle_L", normal=[0, 1, 0], radius=6)
    cmds.matchTransform(PlacementCtrl_ankle_L, "PlacementJnt_Ankle_L", pos=True, rot=False, scl=False)
    cmds.parent(PlacementCtrl_ankle_L, "AutoRig_Data|ControllersPlacement|FK_Controllers")
    Color.setColor("PlacementCtrl_ankle_L", "yellow")

    # PlacementCtrl_Foot
    cmds.select(clear=True)
    PlacementCtrl_Foot = cmds.circle(name="PlacementCtrl_Foot_L", normal=[0, 1, 0], radius=8)
    cmds.matchTransform(PlacementCtrl_Foot, "PlacementJnt_Ball_L", pos=True, rotationY=False, scl=False)
    cmds.setAttr(PlacementCtrl_Foot[0] + ".translateY", 0)
    cmds.parent(PlacementCtrl_Foot, "AutoRig_Data|ControllersPlacement|IK_Controllers")
    Color.setColor("PlacementCtrl_Foot_L", "yellow")

    # PlacementCtrl_Switch_Leg_L
    cmds.select(clear=True)
    PlacementCtrl_Switch_Leg_L = cmds.circle(name="PlacementCtrl_Switch_Leg_L", normal=[0, 1, 0], radius=6)
    cmds.move(24, 78, 0, PlacementCtrl_Switch_Leg_L)
    cmds.parent(PlacementCtrl_Switch_Leg_L, "AutoRig_Data|ControllersPlacement|Global_Controllers")
    Color.setColor("PlacementCtrl_Switch_Leg_L", "yellow")