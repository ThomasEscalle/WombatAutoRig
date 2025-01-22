import maya.cmds as cmds
from wombatAutoRig.src.core import Bookmark
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import Controllers


#Offset t sur tangent CTRL
#Connection CTRL point surface (moment de verite sur la surface pb ou ps pb)

def MatrixConstraint(Master, Slave, mode=1, t=True, r=True, s=False):
    #creation des nodes
    MultMatX = cmds.shadingNode("multMatrix", au=True, name=f"MultMatX_{Slave}")
    DecMatX = cmds.shadingNode("decomposeMatrix", au=True, name=f"DecMatX_{Slave}")

    #connection
    cmds.connectAttr(Master + ".worldMatrix[0]", MultMatX + ".matrixIn[0]")
    cmds.connectAttr(Slave + ".parentInverseMatrix[0]", MultMatX + ".matrixIn[1]")

    cmds.connectAttr(MultMatX + ".matrixSum", DecMatX + ".inputMatrix")

    if t == True :
        cmds.connectAttr(DecMatX + ".outputTranslate", Slave + ".t")
    if r == True :
        cmds.connectAttr(DecMatX + ".outputRotate", Slave + ".r")
    if s == True :
        cmds.connectAttr(DecMatX + ".outputScale", Slave + ".s")

def MatrixInputRibbon(CTRL, side, point, surface):
    # creation Node
    Mult = cmds.shadingNode("multMatrix", au=True, name=f"MultMatX_{CTRL}_{side}")
    Decompose = cmds.shadingNode("decomposeMatrix", au=True, name=f"DecMatX_{CTRL}_{side}")
    MultPiv = cmds.shadingNode("multMatrix", au=True, name=f"MultPivMatX_{CTRL}_{side}")
    ComPiv = cmds.shadingNode("composeMatrix", au=True, name=f"ComPivMatX_{CTRL}_{side}")

    #connection
    cmds.connectAttr(CTRL + ".scalePivot", ComPiv + ".inputTranslate")

    cmds.connectAttr(ComPiv + ".outputMatrix", MultPiv + ".matrixIn[0]")
    cmds.connectAttr(CTRL + ".worldMatrix[0]", MultPiv + ".matrixIn[1]")
    
    cmds.connectAttr(side + ".outputMatrix", Mult + ".matrixIn[0]")
    cmds.connectAttr(MultPiv + ".matrixSum", Mult + ".matrixIn[1]")

    cmds.connectAttr(Mult + ".matrixSum", Decompose + ".inputMatrix")

    cmds.connectAttr(Decompose + ".outputTranslate", surface + f".controlPoints[{point}]")

    #Bookmark
    Bookmark.addNodeToBookmark("Ribbon_input", Mult, row=point, column=0, state=0)
    Bookmark.addNodeToBookmark("Ribbon_input", Decompose, row=point, column=1, state=0)
    Bookmark.addNodeToBookmark("Ribbon_input", MultPiv, row=point-0.1, column=-0.5, state=0)
    Bookmark.addNodeToBookmark("Ribbon_input", ComPiv, row=point-0.1, column=-1, state=0)

def ColumnRibbon(name="Default", height=2, JntNbr=7):
    #Create a nurbs plane
    RibbonLowDef = cmds.surface( dv=3, du=1, fu='open', fv='open', kv=(0, 0, 0, 0.5, 1, 1, 1), ku=(0, 1), pw=((-0.5, 0, 0,1), (-0.5, height/3,0,1), (-0.5, height/2,0,1), (-0.5, 2*height/3,0,1), (-0.5, height,0,1), (0.5, 0,0,1), (0.5, height/3, 0,1), (-0.5, height/2,0,1), (0.5, 2*height/3, 0,1), (0.5, height, 0,1)), name=f"ColumnRibbon_{name}_LowDef")
    #cmds.nurbsPlane(axis=[0,0,1], w=1, lr=height, u=1, v=2, p=[0,1,0], name=f"ColumnRibbon_{name}_LowDef")
    LambertBlue = cmds.shadingNode("lambert", asShader=True, name="Lambert_Ribbon")
    cmds.setAttr(LambertBlue + ".color", 0, 0, 1)
    cmds.setAttr(LambertBlue + ".transparency", 0.3, 0.3, 0.3)
    cmds.select(RibbonLowDef)
    cmds.hyperShade(assign=LambertBlue)

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
    cmds.setAttr(rebuildSurface + ".degreeU", 3)
    cmds.setAttr(rebuildSurface + ".degreeV", 7)
    cmds.setAttr(rebuildSurface + ".direction", 1)
    cmds.setAttr(rebuildSurface + ".spansU", 1)
    cmds.setAttr(rebuildSurface + ".spansV", 2)
    cmds.setAttr(rebuildSurface + ".endKnots", 1)
    cmds.setAttr(rebuildSurface + ".keepRange", 0)
    cmds.setAttr(rebuildSurface + ".keepCorners", False)
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
    SquashChestOffset = cmds.group(SquashChest, name="Loc_Info_Squash_Chest_Offset")

    cmds.parent(InitLenghtOffset, f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Locs")
    cmds.parent(SquashChestOffset, f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Locs")

    #CTRL IK Chest
    ComOffset = cmds.shadingNode("composeMatrix", au=True, name="Offset")
    CTRLIK = cmds.circle(nr=[0,1,0], radius=height/2.5, name="CTRL_IK_Chest")
    cmds.parent(CTRLIK[0], f"Ribbon_Spine_{name}")
    Offset.offset(CTRLIK[0], nbr=1)
    

    #Constraining Loc Squash By CTRL IK
    MatrixConstraint(CTRLIK[0], SquashChestOffset, s=True)

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
    CtrlUpperBody = cmds.curve(p=[(1,0,1),(-1,0,1),(-1,0,-1),(1,0,-1),(1,0,1)], d=1, name = "CTRL_UpperBody")                        #Controllers.createController("3D_Shapes/boat", "CTRL_UpperBody")
    Offset.offset(CtrlUpperBody, nbr=1)
    cmds.addAttr(CtrlUpperBody, ln="TangentFactorDwn", at="double", min=0.005, max=0.75, dv=0, k=True)
    CtrlFKMid = cmds.circle(nr=[0,1,0], radius=height/2.5, name="CTRL_FK_Mid")
    cmds.setAttr(CtrlFKMid[0] + ".translateY", height/2)
    Offset.offset("CTRL_FK_Mid", nbr=1)
    CtrlFKChest = cmds.curve(p=[(1,0,1),(-1,0,1),(-1,0,-1),(1,0,-1),(1,0,1)], d=1, name = "CTRL_FK_Chest")                          #Controllers.createController("3D_Shapes/corner", "CTRL_FK_Chest")
    cmds.setAttr("CTRL_FK_Chest.translateY", 2)
    cmds.addAttr(CtrlFKChest, ln="TangentFactorUp", at="double", min=0.005, max=0.75, dv=0, k=True)
    Offset.offset(CtrlFKChest, nbr=1)

    #Hierarchy
    cmds.parent(CtrlUpperBody + "_Offset", "CTRLs_01")
    cmds.parent(CtrlFKMid[0] + "_Offset", CtrlUpperBody)
    cmds.parent(CtrlFKChest + "_Offset", CtrlFKMid)
    cmds.parent(CTRLIK[0] + "_Offset", CtrlFKChest)
    cmds.setAttr(CTRLIK[0] + "_Offset.translateY", 0)
    cmds.parent(MovablePivot, CTRLIK[0])
    cmds.setAttr(MovablePivot + ".translateY", -height/8)
    cmds.connectAttr(MovablePivot + ".translate", CTRLIK[0] + ".rotatePivot")


    #region Loc Axis mid Spine Info
    LocAxisMidSpine = cmds.spaceLocator(n="Loc_Axis_Mid_Spine_Info")[0]
    Offset.offset(LocAxisMidSpine, nbr=2)

    cmds.parent(LocAxisMidSpine + "_Offset", "Grp_Locs")

    MatrixConstraint(CtrlUpperBody, LocAxisMidSpine + "_Offset")

    #Connection
    cmds.shadingNode("addDoubleLinear", au=True, name="add_tx_Mid_Chest")
    cmds.shadingNode("addDoubleLinear", au=True, name="add_ty_Mid_Chest")
    cmds.shadingNode("addDoubleLinear", au=True, name="add_tz_Mid_Chest")
    cmds.shadingNode("multDoubleLinear", au=True, name="mult_scaleY_Mid_UpperBody")
    cmds.shadingNode("addDoubleLinear", au=True, name="add_tx_Chest_Chest")
    cmds.shadingNode("addDoubleLinear", au=True, name="add_ty_Chest_Chest")
    cmds.shadingNode("addDoubleLinear", au=True, name="add_tz_Chest_Chest")


    Bookmark.createBookmark("node_Ribbon_Spine_LocAxisMidSpine")
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", LocAxisMidSpine + "_Move", row=-2, column=4, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", LocAxisMidSpine + "_Offset", row=-1, column=4, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", CtrlFKMid[0] + "_Offset", row=-1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", CtrlFKChest + "_Offset",row=-2 ,state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", CtrlUpperBody, row=-3, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", "add_tx_Mid_Chest", row=-1, column=1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", "add_ty_Mid_Chest", row=-2, column=1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", "add_tz_Mid_Chest", row=-3, column=1, state=1)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", "mult_scaleY_Mid_UpperBody", row=-2, column=2, state=1)

    cmds.connectAttr(CtrlFKMid[0] + "_Offset.translateX", "add_tx_Mid_Chest.input1")
    cmds.connectAttr(CtrlFKChest + "_Offset.translateX", "add_tx_Mid_Chest.input2")

    cmds.connectAttr(CtrlFKMid[0] + "_Offset.translateY", "add_ty_Mid_Chest.input1")
    cmds.connectAttr(CtrlFKChest + "_Offset.translateY", "add_ty_Mid_Chest.input2")

    cmds.connectAttr(CtrlFKMid[0] + "_Offset.translateZ", "add_tz_Mid_Chest.input1")
    cmds.connectAttr(CtrlFKChest + "_Offset.translateZ", "add_tz_Mid_Chest.input2")

    cmds.connectAttr("add_ty_Mid_Chest.output", "mult_scaleY_Mid_UpperBody.input1")
    cmds.connectAttr(CtrlUpperBody + ".scaleY", "mult_scaleY_Mid_UpperBody.input2")

    cmds.connectAttr("add_tx_Mid_Chest.output", LocAxisMidSpine + "_Move.translateX")
    cmds.connectAttr("mult_scaleY_Mid_UpperBody.output", LocAxisMidSpine + "_Move.translateY")
    cmds.connectAttr("add_tz_Mid_Chest.output", LocAxisMidSpine + "_Move.translateZ")

    cmds.connectAttr(CtrlUpperBody + ".scale", LocAxisMidSpine + "_Move.scale")

    cmds.connectAttr(CtrlFKChest + ".translateX", "add_tx_Chest_Chest.input1")
    cmds.connectAttr(CtrlFKChest + ".translateY", "add_ty_Chest_Chest.input1")
    cmds.connectAttr(CtrlFKChest + ".translateZ", "add_tz_Chest_Chest.input1")
    cmds.connectAttr(CTRLIK[0] + ".translateX", "add_tx_Chest_Chest.input2")
    cmds.connectAttr(CTRLIK[0] + ".translateY", "add_ty_Chest_Chest.input2")
    cmds.connectAttr(CTRLIK[0] + ".translateZ", "add_tz_Chest_Chest.input2")

    cmds.connectAttr("add_tz_Chest_Chest.output", LocAxisMidSpine + ".translateZ")
    cmds.connectAttr("add_ty_Chest_Chest.output", LocAxisMidSpine + ".translateY")
    cmds.connectAttr("add_tx_Chest_Chest.output", LocAxisMidSpine + ".translateX")


    #region CTRL Option
    CtrlOption = Controllers.createController("2D_Shapes/star", "CTRL_Option")
    cmds.setAttr(CtrlOption + ".tx", keyable=False, channelBox=False)
    cmds.setAttr(CtrlOption + ".ty", keyable=False, channelBox=False)
    cmds.setAttr(CtrlOption + ".tz", keyable=False, channelBox=False)
    cmds.setAttr(CtrlOption + ".rx", keyable=False, channelBox=False)
    cmds.setAttr(CtrlOption + ".ry", keyable=False, channelBox=False)
    cmds.setAttr(CtrlOption + ".rz", keyable=False, channelBox=False)
    cmds.setAttr(CtrlOption + ".sx", keyable=False, channelBox=False)
    cmds.setAttr(CtrlOption + ".sy", keyable=False, channelBox=False)
    cmds.setAttr(CtrlOption + ".sz", keyable=False, channelBox=False)

    cmds.addAttr(CtrlOption, ln="STRETCH", at="double", min=0, max=1, dv=1, k=True)
    cmds.addAttr(CtrlOption, ln="SQUASH", at="double", min=0, max=1, dv=1, k=True)
    cmds.addAttr(CtrlOption, ln="_________",sn = "_________", at="enum", en="_________", keyable=True)
    cmds.addAttr(CtrlOption, ln=f"IkVisibility", at="bool", dv=False, k=True)
    cmds.addAttr(CtrlOption, ln=f"FkVisibility", at="bool", dv=False, k=True)
    cmds.addAttr(CtrlOption, ln="________",sn = "________", at="enum", en="________", keyable=True)
    cmds.addAttr(CtrlOption, ln="TwistChest", at="double", dv=0, k=True)
    cmds.addAttr(CtrlOption, ln="TwistMid", at="double", dv=0, k=True)
    cmds.addAttr(CtrlOption, ln="TwistRoot", at="double", dv=0, k=True)
    cmds.addAttr(CtrlOption, ln="__________",sn = "__________", at="enum", en="__________", keyable=True)
    cmds.addAttr(CtrlOption, ln=f"VolumeActivation", at="bool", dv=True, k=True)
    cmds.addAttr(CtrlOption, ln="VolumeFactor", at="double", min=0, max=10, dv=1, k=True)
    cmds.addAttr(CtrlOption, ln="VolumeOffset", at="double", min=-1, max=1, dv=0, k=True)
    cmds.addAttr(CtrlOption, ln="VolumeIntensity", at="double", min=0, max=1, dv=1, k=True)
    cmds.addAttr(CtrlOption, ln="___________",sn = "___________", at="enum", en="___________", keyable=True)
    cmds.addAttr(CtrlOption, ln=f"StretchVolume", at="bool", dv=True, k=True)
    cmds.addAttr(CtrlOption, ln=f"SquashVolume", at="bool", dv=True, k=True)

    Offset.offset(CtrlOption, nbr=1)
    cmds.parent(CtrlOption + "_Offset", CtrlFKMid)


    #region Translate point with NoStretch posibility
    CurveInfoIso = cmds.shadingNode("curveInfo", au=True, name="curveInfo_Ribbon_Iso")
    cmds.connectAttr(curveFromSurfaceIso + ".outputCurve", CurveInfoIso +".inputCurve")
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", CurveInfoIso, row=-1, column=4, state=0)
    Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", "rebuildCurve_Ribbon", row=-1, column=5, state=0)
    

    for i in range(JntNbr):
        #Creation des joints
        if i == 0:
            cmds.joint(n="Bind_Root")
        elif i == JntNbr-1 :
            cmds.joint(n="Bind_Chest")
        else :
            cmds.joint(n=f"Bind_RibbonSpine_0{i}")

        #creation CTRLS
        if i !=0 and i !=JntNbr-1:
            cmds.circle(radius=height/4, name=f"CTRL_RibbonSpine_0{i}", nr=[0,1,0])
            cmds.group(empty=True, name=f"TwistScale_RibbonSpine_0{i}")
            cmds.group(empty=True, name=f"Offset_RibbonSpine_0{i}")
        
        if i == JntNbr-1:
            cmds.group(empty=True, name="Offset_Bind_Chest")
        if i == 0 :
            cmds.group(empty=True, name="Offset_Bind_Root")
        
        #Hierarchy
        if i !=0 and i !=JntNbr-1:
            cmds.parent(f"Bind_RibbonSpine_0{i}", f"CTRL_RibbonSpine_0{i}")
            cmds.parent(f"CTRL_RibbonSpine_0{i}", f"TwistScale_RibbonSpine_0{i}")
            cmds.parent(f"TwistScale_RibbonSpine_0{i}", f"Offset_RibbonSpine_0{i}")
            cmds.parent(f"Offset_RibbonSpine_0{i}", f"Ribbon_Spine_{name}|Global_Move_01|Joints_01")
        
        if i == JntNbr-1:
            cmds.parent("Bind_Chest", "Offset_Bind_Chest")
            cmds.group("Bind_Chest", name=f"TwistScale_RibbonSpine_0{i}")
            cmds.parent("Offset_Bind_Chest", f"Ribbon_Spine_{name}|Global_Move_01|Joints_01")
        if i == 0 :
            cmds.parent("Bind_Root", "Offset_Bind_Root")
            cmds.group("Bind_Root", name=f"TwistScale_RibbonSpine_0{i}")
            cmds.parent("Offset_Bind_Root", f"Ribbon_Spine_{name}|Global_Move_01|Joints_01")

        #Creation nodes
        MultNoStretch = cmds.shadingNode("multDoubleLinear", au=True, name=f"mult_Param_0{i}_NoStretch_Defaut")
        cmds.setAttr(MultNoStretch + ".input1", i/(JntNbr-1))
        DivLength = cmds.shadingNode("multiplyDivide", au=True, name=f"Div_Param_Point_0{i}_by_arcLength")
        cmds.setAttr(DivLength + ".operation", 2)
        Cond_NoStretch = cmds.shadingNode("condition", au=True, name=f"cond_StretchFactor_negativeValues_0{i}")
        cmds.setAttr(Cond_NoStretch + ".operation", 4)
        blendColors = cmds.shadingNode("blendColors", au=True, name=f"Blend_StretchFactor_0{i}")
        pointOnCurveInfo = cmds.shadingNode("pointOnCurveInfo", au=True, name=f"pointCrvInf_First_Joint_0{i}")
        cmds.setAttr(pointOnCurveInfo + ".turnOnPercentage", 1)

        #Connection Nodes
        cmds.connectAttr(LocAxisMidSpine + "_Move.translateY", MultNoStretch + ".input2")

        cmds.connectAttr(MultNoStretch + ".output", DivLength + ".input1X")
        cmds.connectAttr(CurveInfoIso + ".arcLength", DivLength + ".input2X")

        cmds.connectAttr(DivLength + ".outputX" , Cond_NoStretch + ".firstTerm")
        cmds.connectAttr(DivLength + ".outputX" , Cond_NoStretch + ".colorIfTrueR")
        cmds.connectAttr(MultNoStretch + ".input1" , Cond_NoStretch + ".secondTerm")
        cmds.connectAttr(MultNoStretch + ".input1" , Cond_NoStretch + ".colorIfFalseR")

        cmds.connectAttr(MultNoStretch + ".input1", blendColors + ".color1R")
        cmds.connectAttr(Cond_NoStretch + ".outColorR", blendColors + ".color2R")
        cmds.connectAttr(CtrlOption + ".STRETCH", blendColors + ".blender")

        cmds.connectAttr(blendColors+ ".outputR", pointOnCurveInfo + ".parameter")
        cmds.connectAttr("rebuildCurve_Ribbon.outputCurve", pointOnCurveInfo + ".inputCurve")

        if i !=0 and i !=JntNbr-1:
            cmds.connectAttr(pointOnCurveInfo + ".position", f"Offset_RibbonSpine_0{i}.t")
        
        if i == JntNbr-1:
            cmds.connectAttr(pointOnCurveInfo + ".position", "Offset_Bind_Chest.t")

        if i == 0 :
            cmds.connectAttr(pointOnCurveInfo + ".position", "Offset_Bind_Root.t")

        #region Rotation

        #Creation nodes
        PointSurfaceInfo = cmds.shadingNode("pointOnSurfaceInfo", au=True, name=f"pointSurfInfo_Point_0{i}")
        cmds.setAttr(PointSurfaceInfo + ".parameterU", 0.5)
        cmds.setAttr(PointSurfaceInfo + ".turnOnPercentage", 1)
        VectorProduct = cmds.shadingNode("vectorProduct", au=True, name=f"vP_mTx_Rotation_Point_0{i}")
        cmds.setAttr(VectorProduct + ".operation", 2)
        FourByFour = cmds.shadingNode("fourByFourMatrix", au=True, name=f"mtx_Rotation_Point_0{i}")
        DecMatX = cmds.shadingNode("decomposeMatrix", au=True, name=f"dM_Rotation_Point_0{i}")

        #connection
        cmds.connectAttr(blendColors+ ".outputR", PointSurfaceInfo + ".parameterV")
        cmds.connectAttr(rebuildSurface+ ".outputSurface", PointSurfaceInfo + ".inputSurface")

        cmds.connectAttr(PointSurfaceInfo + ".normal", VectorProduct + ".input1")
        cmds.connectAttr(PointSurfaceInfo + ".tangentV", VectorProduct + ".input2")

        cmds.connectAttr(PointSurfaceInfo + ".normalX", FourByFour + ".in00")
        cmds.connectAttr(PointSurfaceInfo + ".normalY", FourByFour + ".in01")
        cmds.connectAttr(PointSurfaceInfo + ".normalZ", FourByFour + ".in02")

        cmds.connectAttr(PointSurfaceInfo + ".tangentVx", FourByFour + ".in10")
        cmds.connectAttr(PointSurfaceInfo + ".tangentVy", FourByFour + ".in11")
        cmds.connectAttr(PointSurfaceInfo + ".tangentVz", FourByFour + ".in12")

        cmds.connectAttr(VectorProduct + ".outputX", FourByFour + ".in20")
        cmds.connectAttr(VectorProduct + ".outputY", FourByFour + ".in21")
        cmds.connectAttr(VectorProduct + ".outputZ", FourByFour + ".in22")

        cmds.connectAttr(PointSurfaceInfo + ".positionX", FourByFour + ".in30")
        cmds.connectAttr(PointSurfaceInfo + ".positionY", FourByFour + ".in31")
        cmds.connectAttr(PointSurfaceInfo + ".positionZ", FourByFour + ".in32")

        cmds.connectAttr(FourByFour + ".output", DecMatX + ".inputMatrix")

        if i !=0 and i !=JntNbr-1:
            cmds.connectAttr(DecMatX + ".outputRotate", f"Offset_RibbonSpine_0{i}.r")
        
        if i == JntNbr-1:
            cmds.connectAttr(DecMatX + ".outputRotate", "Offset_Bind_Chest.r")

        if i == 0 :
            cmds.connectAttr(DecMatX + ".outputRotate", "Offset_Bind_Root.r")


        #region Bookmark
        BookRowOffset = 2*i
        Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", MultNoStretch, row=BookRowOffset-2, column=5, state=1)
        Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", DivLength, row=BookRowOffset-2, column=6, state=1)
        Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", Cond_NoStretch, row=BookRowOffset-2, column=6, state=1)
        Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", blendColors, row=BookRowOffset-2, column=7, state=1)
        Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", pointOnCurveInfo, row=BookRowOffset-1, column=8, state=1)

        Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", PointSurfaceInfo, row=BookRowOffset-2, column=8, state=0)
        Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", VectorProduct, row=BookRowOffset-1, column=9, state=0)
        Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", FourByFour, row=BookRowOffset-1, column=10, state=0)
        Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", DecMatX, row=BookRowOffset-1, column=11, state=0)

        if i !=0 and i !=JntNbr-1:
            Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", f"Offset_RibbonSpine_0{i}", row=BookRowOffset-1, column=12, state=1)
        
        if i == JntNbr-1:
            Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", "Offset_Bind_Chest", row=BookRowOffset-1, column=12, state=1)

        if i == 0 :
            Bookmark.addNodeToBookmark("node_Ribbon_Spine_LocAxisMidSpine", f"Offset_Bind_Root", row=BookRowOffset-1, column=12, state=1)


    #region CTRL IK
    CTRLIKRoot = cmds.circle(nr=[0,1,0], radius=height/2.5, name="CTRL_IK_Root")
    cmds.parent(CTRLIKRoot[0], CtrlUpperBody)
    Offset.offset(CTRLIKRoot[0], nbr=1)

    CtrlIkMid =  cmds.circle(nr=[0,1,0], radius=height/2.5, name="CTRL_IK_Mid")
    cmds.addAttr(CtrlIkMid[0], ln="RotationFactor", at="double", min=-1, max=1, dv=0, k=True)
    cmds.setAttr(CtrlIkMid[0] + ".translateY", height/2)
    cmds.parent(CtrlIkMid[0], CtrlUpperBody)
    Offset.offset(CtrlIkMid[0], nbr=1)
    cmds.group(CtrlIkMid[0], name="cstr_Ik_Mid")
    cmds.group(CtrlIkMid[0], name="Offset_Rotation_Ik_Mid")

    #Loc Axis Mid IK Pelvis
    LocAxisMidPelvis = cmds.spaceLocator(n="Loc_axis_Mid_Ik_Pelvis")[0]
    cmds.parent(LocAxisMidPelvis, f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Locs")
    Offset.offset(LocAxisMidPelvis, nbr=1)
    MatrixConstraint(CTRLIKRoot[0], LocAxisMidPelvis + "_Offset")
    cmds.aimConstraint(LocAxisMidSpine, LocAxisMidPelvis, aim=(0,1,0), wuo=CTRLIKRoot[0], wut=2, u=(1,0,0), wu=(1,0,0))

    #MatrixConstraint(CtrlFKMid[0] + "_Offset", "cstr_Ik_Mid") Creation nodes
    MultMatX = cmds.shadingNode("multMatrix", au=True, name=f"MultMatX_cstr_Ik_Mid")
    DecMatX = cmds.shadingNode("decomposeMatrix", au=True, name=f"DecMatX_cstr_Ik_Mid")
    ComMatX = cmds.shadingNode("composeMatrix", au=True, name=f"ComMatX_FK_Mid_Offset")

    #connection
    cmds.connectAttr(CtrlFKMid[0] + "_Offset" + ".translateY", ComMatX + ".inputTranslateY")
    cmds.connectAttr(ComMatX + ".outputMatrix", MultMatX + ".matrixIn[0]")
    cmds.connectAttr(LocAxisMidPelvis + ".worldMatrix[0]", MultMatX + ".matrixIn[1]")
    cmds.connectAttr("cstr_Ik_Mid.parentInverseMatrix[0]", MultMatX + ".matrixIn[2]")

    cmds.connectAttr(MultMatX + ".matrixSum", DecMatX + ".inputMatrix")

    cmds.connectAttr(DecMatX + ".outputTranslate", "cstr_Ik_Mid.t")
    cmds.connectAttr(DecMatX + ".outputRotate", "cstr_Ik_Mid.r")

    cmds.connectAttr(CtrlFKMid[0] + ".t", "Offset_Rotation_Ik_Mid.t")
    cmds.connectAttr(CtrlFKMid[0] + ".rotateY", "Offset_Rotation_Ik_Mid.rotateY")

    #CTRL Tangent
    CtrlTanChest = cmds.curve(name="CTRL_Tangent_Chest", p=[(1,0,0),(1.05,0.18,0),(1.25,0.25,0),(1.45,0.18,0),(1.5,0,0),(1.45,-0.18,0),(1.25,-0.25,0),(1.05,-0.18,0),(1,0,0)])
    cmds.parent(CtrlTanChest, CTRLIK[0])
    Offset.offset(CtrlTanChest, nbr=1)
    cmds.setAttr(ComOffset + ".inputTranslateY", -height/8)
    cmds.connectAttr(ComOffset + ".outputMatrix", CtrlTanChest + "_Offset.offsetParentMatrix")
    cmds.disconnectAttr(ComOffset + ".outputMatrix", CtrlTanChest + "_Offset.offsetParentMatrix")

    CtrlTanRoot = cmds.curve(name="CTRL_Tangent_Root", p=[(1,0,0),(1.05,0.18,0),(1.25,0.25,0),(1.45,0.18,0),(1.5,0,0),(1.45,-0.18,0),(1.25,-0.25,0),(1.05,-0.18,0),(1,0,0)])
    cmds.parent(CtrlTanRoot, CTRLIKRoot[0])
    Offset.offset(CtrlTanRoot, nbr=1)
    cmds.group(CtrlTanRoot, name="Offset_Rotation_Tangent_Root")
    cmds.setAttr(ComOffset + ".inputTranslateY", height/8)
    cmds.connectAttr(ComOffset + ".outputMatrix", CtrlTanRoot + "_Offset.offsetParentMatrix")
    cmds.disconnectAttr(ComOffset + ".outputMatrix", CtrlTanRoot + "_Offset.offsetParentMatrix")

    #Offset Input
    LocInfoPelvis = cmds.spaceLocator(n="Loc_Info_Pelvis")[0]
    cmds.parent(LocInfoPelvis, f"Ribbon_Spine_{name}|ExtraNodes_01|Grp_Locs")
    Offset.offset(LocInfoPelvis, nbr=1)
    MatrixConstraint(CTRLIKRoot[0], LocInfoPelvis + "_Offset", s=True)
    #Creation Nodes
    FactorTangentChest = cmds.shadingNode("multDoubleLinear", au=True, name="Factor_Tangent_Chest")
    cmds.setAttr(FactorTangentChest + ".input2",-1)
    DistB = cmds.shadingNode("distanceBetween", au=True, name="DistB_Root_To_Chest")
    ArcLengthChest = cmds.shadingNode("multDoubleLinear", au=True, name="ArcLength_by_factor_Tangent_Chest")
    Div_Scale_Root = cmds.shadingNode("multiplyDivide", au=True, name="Div_Scale_UpperBody_TangentRoot")
    cmds.setAttr(Div_Scale_Root + ".operation", 2)
    Div_Scale_Chest = cmds.shadingNode("multiplyDivide", au=True, name="Div_Scale_UpperBody_TangentChest")
    cmds.setAttr(Div_Scale_Chest + ".operation", 2)
    OpposedFactorMid = cmds.shadingNode("multDoubleLinear", au=True, name="Opposed_Factor_Z_Rot_Mid_Ik")
    MDL_X_01 = cmds.shadingNode("multDoubleLinear", au=True, name="mult_Rotation_X_Ik_Mid_01")
    MDL_Z_01 = cmds.shadingNode("multDoubleLinear", au=True, name="mult_Rotation_Z_Ik_Mid_01")
    MDL_X_02 = cmds.shadingNode("multDoubleLinear", au=True, name="mult_Rotation_X_Ik_Mid_02")
    MDL_Z_02 = cmds.shadingNode("multDoubleLinear", au=True, name="mult_Rotation_Z_Ik_Mid_02")

    #Connection
    LocAxisMidSpineShape = cmds.listRelatives(LocAxisMidSpine, s=True)
    LocAxisMidPelvisShape = cmds.listRelatives(LocInfoPelvis, s=True)

    cmds.connectAttr(LocAxisMidSpineShape[0] + ".worldPosition[0]", DistB + ".point1")
    cmds.connectAttr(LocAxisMidPelvisShape[0] + ".worldPosition[0]", DistB + ".point2")

    cmds.connectAttr(CtrlFKChest + ".TangentFactorUp", FactorTangentChest + ".input1")

    cmds.connectAttr(CtrlUpperBody + ".TangentFactorDwn", ArcLengthChest + ".input1")
    cmds.connectAttr(DistB + ".distance", ArcLengthChest + ".input2")
    
    cmds.connectAttr(ArcLengthChest + ".output", Div_Scale_Root + ".input1X")
    cmds.connectAttr(ArcLengthChest + ".output", Div_Scale_Chest + ".input1X")
    cmds.connectAttr(CtrlUpperBody + ".scaleY", Div_Scale_Root + ".input2X")
    cmds.connectAttr(CtrlUpperBody + ".scaleY", Div_Scale_Chest + ".input2X")

    cmds.connectAttr(Div_Scale_Root + ".outputX", CtrlTanRoot + "_Offset.translateY")
    cmds.connectAttr(Div_Scale_Chest + ".outputX", CtrlTanChest + "_Offset.translateY")

    cmds.connectAttr(CtrlIkMid[0] + ".RotationFactor", OpposedFactorMid + ".input1")

    cmds.connectAttr(CtrlIkMid[0] + ".rotateX", MDL_X_01 + ".input1")
    cmds.connectAttr(CtrlIkMid[0] + ".rotateX", MDL_X_02 + ".input1")
    cmds.connectAttr(CtrlIkMid[0] + ".rotateZ", MDL_Z_01 + ".input1")
    cmds.connectAttr(CtrlIkMid[0] + ".rotateZ", MDL_Z_02 + ".input1")

    cmds.connectAttr(CtrlIkMid[0] + ".RotationFactor", MDL_Z_02 + ".input2")
    cmds.connectAttr(CtrlIkMid[0] + ".RotationFactor", MDL_X_01 + ".input2")
    cmds.connectAttr(OpposedFactorMid + ".output", MDL_X_02 + ".input2")
    cmds.connectAttr(OpposedFactorMid + ".output", MDL_Z_01 + ".input2")

    cmds.connectAttr(MDL_X_01 + ".output", CtrlTanChest + "_Offset.translateX")
    cmds.connectAttr(MDL_Z_01 + ".output", CtrlTanChest + "_Offset.translateZ")
    cmds.connectAttr(MDL_X_02 + ".output", CtrlTanRoot + "_Offset.translateX")
    cmds.connectAttr(MDL_Z_02 + ".output", CtrlTanRoot + "_Offset.translateZ")


    #ScaleY LocAxisPelvis
    DivByLength = cmds.shadingNode("multiplyDivide", au=True, name="Div_y_InitLength")
    cmds.setAttr(DivByLength + ".operation", 2)

    cmds.connectAttr(DistB + ".distance", DivByLength + ".input1X")
    cmds.connectAttr(LocAxisMidSpine + "_Move" + ".translateY", DivByLength + ".input2X")
    cmds.connectAttr(DivByLength + ".outputX", LocAxisMidPelvis + ".scaleY")


    #region connect control point 
    Bookmark.createBookmark("Ribbon_input")
    #compose Matrix side
    cM_L = cmds.shadingNode("composeMatrix", au=True, name="cM_Side_Offset_L")
    cmds.setAttr(cM_L + ".inputTranslateX", -0.5)
    cM_R = cmds.shadingNode("composeMatrix", au=True, name="cM_Side_Offset_R")
    cmds.setAttr(cM_R + ".inputTranslateX", 0.5)

    MatrixInputRibbon(CTRL=CTRLIKRoot[0], side=cM_R, point=0, surface=ShapeRibbon[0])
    MatrixInputRibbon(CTRL=CtrlTanRoot, side=cM_R, point=1, surface=ShapeRibbon[0])
    MatrixInputRibbon(CTRL=CtrlIkMid[0], side=cM_R, point=2, surface=ShapeRibbon[0])
    MatrixInputRibbon(CTRL=CtrlTanChest, side=cM_R, point=3, surface=ShapeRibbon[0])
    MatrixInputRibbon(CTRL=CTRLIK[0], side=cM_R, point=4, surface=ShapeRibbon[0])
    MatrixInputRibbon(CTRL=CTRLIKRoot[0], side=cM_L, point=5, surface=ShapeRibbon[0])
    MatrixInputRibbon(CTRL=CtrlTanRoot, side=cM_L, point=6, surface=ShapeRibbon[0])
    MatrixInputRibbon(CTRL=CtrlIkMid[0], side=cM_L, point=7, surface=ShapeRibbon[0])
    MatrixInputRibbon(CTRL=CtrlTanChest, side=cM_L, point=8, surface=ShapeRibbon[0])
    MatrixInputRibbon(CTRL=CTRLIK[0], side=cM_L, point=9, surface=ShapeRibbon[0])

    #Bookmark
    Bookmark.addNodeToBookmark("Ribbon_input", CTRLIKRoot[0], row=0, column=-2, state=0)
    Bookmark.addNodeToBookmark("Ribbon_input", CtrlTanRoot, row=2.25, column=-2, state=0)
    Bookmark.addNodeToBookmark("Ribbon_input", CtrlIkMid[0], row=4.5, column=-2, state=0)
    Bookmark.addNodeToBookmark("Ribbon_input", CtrlTanChest, row=6.75, column=-2, state=0)
    Bookmark.addNodeToBookmark("Ribbon_input", CTRLIK[0], row=9, column=-2, state=0)

    Bookmark.addNodeToBookmark("Ribbon_input", cM_L, row=1.125, column=-1, state=0)
    Bookmark.addNodeToBookmark("Ribbon_input", cM_R, row=7.875, column=-1, state=0)

    Bookmark.addNodeToBookmark("Ribbon_input", ShapeRibbon[0], row=4.5, column=2, state=0)


    #Constraint Offset Info Init Length
    #Creation Nodes
    Negative = cmds.shadingNode("multDoubleLinear", au=True, name="Negative_Arc_Length_Ribbon")
    MultOffsetInitLength = cmds.shadingNode("multDoubleLinear", au=True, name="mult_Squash_Value")
    MultCondOffsetInitLength = cmds.shadingNode("multDoubleLinear", au=True, name="mult_By_0_If")
    DifferenceBtw = cmds.shadingNode("addDoubleLinear", au=True, name="Diff_InitLength_ArcLength")
    Reverse = cmds.shadingNode("reverse", au=True, name="reverseSquashValue")
    CondOffsetInitLength = cmds.shadingNode("condition", au=True, name="cond_if_Squash_maxValue")
    cMOffsetInitLength = cmds.shadingNode("composeMatrix", au=True, name="cM_Offset_InitLength")
    MultMatXOffsetInitLength = cmds.shadingNode("multMatrix", au=True, name="mult_MTX_Chest_info_Length_Squash")
    DecMatXOffsetInitLength = cmds.shadingNode("decomposeMatrix", au=True, name="dM_Chest_info_Length_Squash")

    #setAttr
    cmds.setAttr(Negative + ".input2", -1)
    cmds.setAttr(CondOffsetInitLength + ".operation", 3)

    #connection
    cmds.connectAttr(CurveInfoIso + ".arcLength", Negative + ".input1")

    cmds.connectAttr(LocAxisMidSpine + "_Move.translateY", DifferenceBtw + ".input1")
    cmds.connectAttr(LocAxisMidSpine + "_Move.translateY", CondOffsetInitLength + ".secondTerm")
    cmds.connectAttr(CurveInfoIso + ".arcLength", CondOffsetInitLength + ".firstTerm")
    cmds.connectAttr(Negative + ".output", DifferenceBtw + ".input2")

    cmds.connectAttr(CtrlOption + ".SQUASH", Reverse + ".inputX")

    cmds.connectAttr(DifferenceBtw + ".output", MultCondOffsetInitLength + ".input1")

    cmds.connectAttr(MultCondOffsetInitLength + ".output", MultOffsetInitLength + ".input1")
    cmds.connectAttr(Reverse + ".outputX", MultOffsetInitLength + ".input2")

    cmds.connectAttr(MultOffsetInitLength + ".output", cMOffsetInitLength + ".inputTranslateY")

    cmds.connectAttr(cMOffsetInitLength + ".outputMatrix", MultMatXOffsetInitLength + ".matrixIn[0]")
    cmds.connectAttr(CTRLIK[0] + ".worldMatrix[0]", MultMatXOffsetInitLength + ".matrixIn[1]")
    cmds.connectAttr(InitLenght + "_Offset.parentInverseMatrix[0]", MultMatXOffsetInitLength + ".matrixIn[2]")

    cmds.connectAttr(MultMatXOffsetInitLength + ".matrixSum", DecMatXOffsetInitLength + ".inputMatrix")

    cmds.connectAttr(DecMatXOffsetInitLength + ".outputTranslate", InitLenght + "_Offset.t")
    cmds.connectAttr(DecMatXOffsetInitLength + ".outputRotate", InitLenght + "_Offset.r")
    cmds.connectAttr(DecMatXOffsetInitLength + ".outputScale", InitLenght + "_Offset.s")

    cmds.setAttr(ComOffset + ".inputTranslateY", height)
    cmds.connectAttr(ComOffset + ".outputMatrix", InitLenght + "_Offset.offsetParentMatrix")
    cmds.disconnectAttr(ComOffset + ".outputMatrix", InitLenght + "_Offset.offsetParentMatrix")

    #region Scale + Twist
    #Creation Nodes No for loop
    DivVol = cmds.shadingNode("multiplyDivide", au=True, name=f"Div_Vol_XZ_ArcLength_InitLength")
    cmds.setAttr(DivVol + ".operation", 2)
    CondVol = cmds.shadingNode("condition", au=True, name=f"cond_Volume")
    cmds.setAttr(CondVol + ".secondTerm", 1)
    DivVolFin = cmds.shadingNode("multiplyDivide", au=True, name=f"Div_Vol_XZ_Final")
    cmds.setAttr(DivVolFin + ".input1X", 1)
    cmds.setAttr(DivVolFin + ".operation", 2)
    CondVolCheck = cmds.shadingNode("condition", au=True, name=f"cond_Volume_Check")
    cmds.setAttr(CondVolCheck + ".secondTerm", 1)
    cmds.setAttr(CondVolCheck + ".operation", 4)
    CondVolSquash = cmds.shadingNode("condition", au=True, name=f"cond_Volume_Squash")
    cmds.setAttr(CondVolSquash + ".secondTerm", 1)
    MultVolFactor = cmds.shadingNode("multDoubleLinear", au=True, name=f"Mult_Factor_Volume")
    MultVolOffset = cmds.shadingNode("multDoubleLinear", au=True, name=f"Mult_Offset_Volume")
    cmds.setAttr(MultVolOffset + ".input2", 0.5)
    ReverseIntensity = cmds.shadingNode("reverse", au=True, name="Rev_IntensityVolume")

    #Connection
    cmds.connectAttr(CurveInfoIso + ".arcLength", DivVol + ".input1X")
    cmds.connectAttr(LocAxisMidSpine + "_Move.translateY", DivVol + ".input2X")

    cmds.connectAttr(CtrlOption + ".VolumeActivation", CondVol + ".firstTerm")
    cmds.connectAttr(DivVol + ".outputX", CondVol + ".colorIfTrueR")

    cmds.connectAttr(CondVol + ".outColorR", DivVolFin + ".input2X")

    cmds.connectAttr(CtrlOption + ".StretchVolume", CondVolCheck + ".colorIfTrueR")
    cmds.connectAttr(CtrlOption + ".SquashVolume", CondVolCheck + ".colorIfFalseR")
    cmds.connectAttr(DivVolFin + ".outputX", CondVolCheck + ".firstTerm")

    cmds.connectAttr(DivVolFin + ".outputX", CondVolSquash + ".colorIfTrueR")
    cmds.connectAttr(CondVolCheck + ".outColorR", CondVolSquash + ".firstTerm")

    cmds.connectAttr(CondVolSquash + ".outColorR", MultVolFactor + ".input1")
    cmds.connectAttr(CtrlOption + ".VolumeFactor", MultVolFactor + ".input2")

    cmds.connectAttr(CtrlOption + ".VolumeOffset", MultVolOffset + ".input1")

    cmds.connectAttr(CtrlOption + ".VolumeIntensity", ReverseIntensity + ".inputX")

    for i in range(JntNbr):
        #Creation des nodes Twist
        MultChest = cmds.shadingNode("multDoubleLinear", au=True, name=f"Mult_Twist_Chest_Point_0{i}")
        cmds.setAttr(MultChest + ".input1", i/(JntNbr-1))
        MultRoot = cmds.shadingNode("multDoubleLinear", au=True, name=f"Mult_Twist_Root_Point_0{i}")
        cmds.setAttr(MultRoot + ".input1", 1-(i/(JntNbr-1)))
        MultMid = cmds.shadingNode("multDoubleLinear", au=True, name=f"Mult_Twist_Mid_Point_0{i}")
        if i<(JntNbr-1)/2 : 
            input1 = 2*(i/(JntNbr-1))
        elif i == (JntNbr-1)/2:
            input1 = 1
        else :
            input1 = 2*(1-(i/(JntNbr-1)))
        cmds.setAttr(MultMid + ".input1", input1)



        AddMid = cmds.shadingNode("addDoubleLinear", au=True, name=f"add_Twist_Mid_Point_0{i}")
        AddChest = cmds.shadingNode("addDoubleLinear", au=True, name=f"add_Twist_Chest_Point_0{i}")

        #Creation des nodes Scale
        AddVol = cmds.shadingNode("addDoubleLinear", au=True, name=f"add_Vol_Offset_Point_0{i}")
        RemapValueScale = cmds.shadingNode("remapValue", au=True, name=f"rV_Scale_XY_Point_0{i}")
        cmds.setAttr(RemapValueScale + ".outputMin", 1)
        cmds.setAttr(RemapValueScale + ".value[0].value_Interp", 3)
        cmds.setAttr(RemapValueScale + ".value[1].value_Interp", 3)
        cmds.setAttr(RemapValueScale + ".value[2].value_Interp", 3)
        cmds.setAttr(RemapValueScale + ".value[3].value_Interp", 3)
        cmds.setAttr(RemapValueScale + ".value[4].value_Interp", 3)

        cmds.setAttr(RemapValueScale + ".value[0].value_Position", 0)
        cmds.setAttr(RemapValueScale + ".value[1].value_Position", 0.25)
        cmds.setAttr(RemapValueScale + ".value[2].value_Position", 0.5)
        cmds.setAttr(RemapValueScale + ".value[3].value_Position", 0.75)
        cmds.setAttr(RemapValueScale + ".value[4].value_Position", 1)

        cmds.setAttr(RemapValueScale + ".value[0].value_FloatValue", 0)
        cmds.setAttr(RemapValueScale + ".value[1].value_FloatValue", 0.5)
        cmds.setAttr(RemapValueScale + ".value[2].value_FloatValue", 1)
        cmds.setAttr(RemapValueScale + ".value[3].value_FloatValue", 0.5)
        cmds.setAttr(RemapValueScale + ".value[4].value_FloatValue", 0)

        #connection Twist
        cmds.connectAttr(CtrlOption + ".TwistChest", MultChest + ".input2")
        cmds.connectAttr(CtrlOption + ".TwistMid", MultMid + ".input2")
        cmds.connectAttr(CtrlOption + ".TwistRoot", MultRoot + ".input2")

        cmds.connectAttr(MultRoot + ".output", AddMid + ".input1")
        cmds.connectAttr(MultMid + ".output", AddMid + ".input2")

        cmds.connectAttr(AddMid + ".output", AddChest + ".input1")
        cmds.connectAttr(MultChest + ".output", AddChest + ".input2")

        cmds.connectAttr(AddChest + ".output", f"TwistScale_RibbonSpine_0{i}.rotateY")

        #Connection Scale
        cmds.connectAttr(MultChest + ".input1", AddVol + ".input1")
        cmds.connectAttr(CtrlOption + ".VolumeOffset", AddVol + ".input2")

        cmds.connectAttr(AddVol + ".output", RemapValueScale + ".inputValue")
        cmds.connectAttr(MultVolFactor + ".output", RemapValueScale + ".outputMax")
        cmds.connectAttr(ReverseIntensity + ".outputX", RemapValueScale + ".inputMin")

        cmds.connectAttr(RemapValueScale + ".outValue", f"TwistScale_RibbonSpine_0{i}.scaleX")
        cmds.connectAttr(RemapValueScale + ".outValue", f"TwistScale_RibbonSpine_0{i}.scaleZ")

ColumnRibbon("01")