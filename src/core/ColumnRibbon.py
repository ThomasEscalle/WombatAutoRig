import maya.cmds as cmds
from wombatAutoRig.src.core import Bookmark
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import Controllers


def ColumnRibbon(name="Default", height=2):
    #Create a nurbs plane
    RibbonLowDef = cmds.nurbsPlane(axis=[0,0,1], w=1, lr=height, u=1, v=2, p=[0,1,0], name=f"ColumnRibbon_{name}_LowDef")

    #region Hierarchy
    GrpAll = cmds.group(empty=True, n=f"Ribbon_Spine_{name}")
    cmds.group(empty=True, n="Global_Move_01")
    cmds.group(empty=True, n="CTRLs_01")
    cmds.group(empty=True, n="Joints_01")
    cmds.group(empty=True, n="ExtraNodes_01")
    cmds.group(empty=True, n="Grp_Locs")
    cmds.group(empty=True, n="Grp_Crvs")
    cmds.group(empty=True, n="Grp_Surfaces")

    cmds.parent("Global_Move_01", "|ExtraNodes_01", GrpAll)
    cmds.parent("|CTRLs_01", "|Joints_01", "Global_Move_01")
    cmds.parent("|Grp_Locs", "|Grp_Crvs", "|Grp_Surfaces", f"Ribbon_Spine_{name}|ExtraNodes_01")

    cmds.parent(RibbonLowDef, f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Surfaces")

    #region Node Editor part 01

    Bookmark.createBookmark("node_Ribbon_Spine")
    #ShapeRibbon
    ShapeRibbon = cmds.listRelatives(f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Surfaces|ColumnRibbon_{name}_LowDef", shapes=True)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine", ShapeRibbon[0], state=2)
    #RebuildSurface
    rebuildSurface = cmds.shadingNode("rebuildSurface", au=True, name=f"rebuildSurface_Ribbon_{name}")
    cmds.setAttr(rebuildSurface + ".degreeU", 1)
    cmds.setAttr(rebuildSurface + ".degreeV", 7)
    cmds.setAttr(rebuildSurface + ".direction", 1)
    cmds.setAttr(rebuildSurface + ".spansU", 1)
    cmds.setAttr(rebuildSurface + ".spansV", 2)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine", rebuildSurface, row=0, column=1, state=1)

    cmds.connectAttr(ShapeRibbon[0] + ".worldSpace[0]", rebuildSurface + ".inputSurface")
    #CurveFromSurfaceIso
    curveFromSurfaceIso = cmds.shadingNode("curveFromSurfaceIso", au=True, name=f"curveFromSurfaceIso_Ribbon_{name}") 
    cmds.setAttr(curveFromSurfaceIso + ".isoparmDirection", 1)
    cmds.setAttr(curveFromSurfaceIso + ".isoparmValue", 0.5)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine", curveFromSurfaceIso, row=0, column=2, state=1)

    cmds.connectAttr(rebuildSurface + ".outputSurface", curveFromSurfaceIso + ".inputSurface")

    #curve Shape
    Crv = cmds.curve(name=f"Crv_Ribbon_{name}_Isoparm", p=[(0,0,0), (0,height/3,0), (0,2*height/3,0), (0,height,0)], degree=3)
    CrvShape = cmds.listRelatives(Crv, s=True)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine", CrvShape[0], row=0, column=3, state=1)
    cmds.parent(Crv, f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Crvs")

    cmds.connectAttr(curveFromSurfaceIso + ".outputCurve", CrvShape[0] + ".create")

    #region Locators
    InitLenght = cmds.spaceLocator(n="Loc_Info_Init_Lenght")[0]
    SquashChest = cmds.spaceLocator(n="Loc_Info_Squash_Chest")[0]
    MovablePivot = cmds.spaceLocator(n="Loc_MovableRoatetPivot_Chest_Ik")[0]

    InitLenghtOffset = cmds.group(InitLenght, name="Loc_Info_Init_Lenght_Offset")
    cmds.setAttr(InitLenghtOffset + ".translateY", height)
    SquashChestOffset = cmds.group(SquashChest, name="Loc_Info_Squash_Chest_Offset")
    cmds.setAttr(SquashChestOffset + ".translateY", height)

    cmds.parent(InitLenghtOffset, f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Locs")
    cmds.parent(SquashChestOffset, f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Locs")

    #CTRL IK Chest
    CTRLIK = cmds.circle(center=[0,height,0], nr=[0,1,0], radius=height/2.5, name="CTRL_IK_Chest")
    cmds.matchTransform(CTRLIK, f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Locs|Loc_Info_Init_Lenght_Offset", piv=True)
    cmds.setAttr(MovablePivot + ".translateY", 7*height/8)
    cmds.parent(MovablePivot, CTRLIK)
    cmds.parent(CTRLIK, f"Ribbon_Spine_{name}")
    Offset.Offset(CTRLIK, nbr=1)
    cmds.connectAttr(MovablePivot + ".translate", CTRLIK[0] + ".rotatePivot")

    #Curve Squash Offset
    cmds.curve(p=[(0,0,0), (0,height,0)], degree=1, name="Crv_Squash_Offset")
    cmds.parent("Crv_Squash_Offset", f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Crvs")
    CurveSquashOffset = cmds.listRelatives("Crv_Squash_Offset", s=True)
    cmds.shadingNode("attachCurve", au=True, name="attachCurve_Ribbon")
    cmds.shadingNode("rebuildCurve", au=True, name="rebuildCurve_Ribbon")
    cmds.setAttr("rebuildCurve_Ribbon.spans", 6)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine", CurveSquashOffset[0], row=-2, column=0, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine", InitLenght, row=-2, column=-1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine", SquashChest, row=-2, column=-1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine", "attachCurve_Ribbon", row=-1, column=1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine", "rebuildCurve_Ribbon", row=-1, column=2, state=1)

    cmds.connectAttr(SquashChest + ".worldPosition[0]", CurveSquashOffset[0] + ".controlPoints[0]")
    cmds.connectAttr(InitLenght + ".worldPosition[0]", CurveSquashOffset[0] + ".controlPoints[1]")

    cmds.connectAttr(CrvShape[0] + ".worldSpace[0]", "attachCurve_Ribbon.inputCurve1")
    cmds.connectAttr(CurveSquashOffset[0] + ".worldSpace[0]", "attachCurve_Ribbon.inputCurve2")

    cmds.connectAttr("attachCurve_Ribbon.outputCurve", "rebuildCurve_Ribbon.inputCurve")

    #region FK CTRLs
    CtrlUpperBody = Controllers.createController("3D_Shapes/boat", "CTRL_UpperBody")
    Offset.Offset(CtrlUpperBody, nbr=1)
    CtrlFKMid = cmds.circle(center=[0,0,0], nr=[0,1,0], radius=height/2.5, name="CTRL_FK_Mid")
    Offset.Offset(CtrlFKMid, nbr=1)
    CtrlFKChest = Controllers.createController("3D_Shapes/corner", "CTRL_FK_Chest")
    Offset.Offset(CtrlFKChest, nbr=1)

    #Hierarchy
    cmds.parent(CtrlUpperBody + "_Offset", "CTRLs_01")
    cmds.parent(CtrlFKMid + "_Offset", CtrlUpperBody)
    cmds.parent(CtrlFKChest + "_Offset", CtrlFKMid)
    cmds.parent(CTRLIK + "_Offset", CtrlFKChest)

    #region Loc Axis mid Spine Info
    LocAxisMidSpine = cmds.spaceLocator(n="Loc_Axis_Mid_Spine_Info")[0]
    Offset.Offset(LocAxisMidSpine, nbr=2)

    cmds.parent(LocAxisMidSpine + "_Offset", "Grp_Locs")

    #Connection
    cmds.shadingNode("addDoubleLinear", au=True, name="add_tx_Mid_Chest")
    cmds.shadingNode("addDoubleLinear", au=True, name="add_ty_Mid_Chest")
    cmds.shadingNode("addDoubleLinear", au=True, name="add_tz_Mid_Chest")
    cmds.shadingNode("multDoubleLinear", au=True, name="mult_scaleY_Mid_UpperBody")

    Bookmark.createBookmark("node_Ribbon_Spine_LocAxisMidSpine")
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", LocAxisMidSpine, state=2)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", CtrlFKMid + "_Offset", row=-1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", CtrlFKChest + "_Offset",row=-2 ,state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", CtrlUpperBody, row=-3, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", "add_tx_Mid_Chest", row=-1, column=1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", "add_ty_Mid_Chest", row=-2, column=1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", "add_tz_Mid_Chest", row=-3, column=1, state=1)








    
ColumnRibbon("01")