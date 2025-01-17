# Maya script to create a cartoon eye rig
import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMaya


from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Offset


# Up EyeLid vertices
# select -r Face.vtx[165] ;
# select -tgl Face.vtx[169] ;
# select -tgl Face.vtx[178] ;
# select -tgl Face.vtx[183] ;
# select -tgl Face.vtx[193] ;
# select -tgl Face.vtx[198] ;
# select -tgl Face.vtx[207] ;
# select -tgl Face.vtx[211] ;
# select -tgl Face.vtx[216] ;
# select -tgl Face.vtx[223] ;
# select -tgl Face.vtx[228] ;

# Down EyeLid vertices
# select -r Face.vtx[266] ;
# select -r Face.vtx[265] ;
# select -tgl Face.vtx[262] ;
# select -tgl Face.vtx[259] ;
# select -tgl Face.vtx[257] ;
# select -tgl Face.vtx[254] ;
# select -tgl Face.vtx[251] ;
# select -tgl Face.vtx[247] ;
# select -tgl Face.vtx[243] ;
# select -tgl Face.vtx[237] ;
# select -tgl Face.vtx[229] ;

# Eye Geo
# select -r Eye_0 ;

# Face Geo
# select -r Face ;


def test():
    # Select the eye geometry
    eyeGeo = "Eye_0"
    faceGeo = "Face"

    # Select the up lid vertices
    upLidVertices = ["Face.vtx[165]", "Face.vtx[169]", "Face.vtx[178]", "Face.vtx[183]", "Face.vtx[193]", "Face.vtx[198]", "Face.vtx[207]", "Face.vtx[211]", "Face.vtx[216]", "Face.vtx[223]", "Face.vtx[228]"]

    # Select the down lid vertices
    downLidVertices = ["Face.vtx[266]", "Face.vtx[265]", "Face.vtx[262]", "Face.vtx[259]", "Face.vtx[257]", "Face.vtx[254]", "Face.vtx[251]", "Face.vtx[247]", "Face.vtx[243]", "Face.vtx[237]", "Face.vtx[229]"]

    cartoonEye(eyeGeo, faceGeo , upLidVertices, downLidVertices , "L")
    



# Create joints on vertices
def createJointsOnVertices( centerLocator , vertices , side = "L" , topBottom = "up" ):

    returnvalue = []
    index = 0
    for v in vertices :
        index += 1

        cmds.select(cl = 1 )
        jnt = cmds.joint()
        jnt = cmds.rename(jnt , "Bind_EyeLid_{0}_{1}_{2}_end".format(topBottom , index , side) )
        Color.setColor(jnt, "white")
        pos = cmds.xform(v , q =1 , ws = 1 , t =1 )
        cmds.xform(jnt , ws =1 , t = pos )
        posC = cmds.xform(centerLocator , q =1 , ws = 1 , t =1 )
        cmds.select(cl =1 )
        jntC = cmds.joint()
        jntC = cmds.rename(jntC , "Bind_EyeLid_{0}_{1}_{2}".format(topBottom , index , side) )
        Color.setColor(jntC, "white")
        cmds.xform(jntC , ws =1 , t = posC )
        cmds.parent(jnt , jntC)
        cmds.joint(jntC , e =1 , oj = "xyz" , secondaryAxisOrient= "yup" , ch = 1 , zso =1 )
        returnvalue.append(jntC)
    
    return returnvalue




# Get U parameter on a curve
def getUParam( pnt = [], crv = None):

    point = OpenMaya.MPoint(pnt[0],pnt[1],pnt[2])
    curveFn = OpenMaya.MFnNurbsCurve(getDagPath(crv))
    paramUtill=OpenMaya.MScriptUtil()
    paramPtr=paramUtill.asDoublePtr()
    isOnCurve = curveFn.isPointOnCurve(point)
    if isOnCurve == True:
        
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    else :
        point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    
    param = paramUtill.getDouble(paramPtr)  
    return param

# Get dag path
def getDagPath( objectName):
    
    if isinstance(objectName, list)==True:
        oNodeList=[]
        for o in objectName:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(o)
            oNode = OpenMaya.MDagPath()
            selectionList.getDagPath(0, oNode)
            oNodeList.append(oNode)
        return oNodeList
    else:
        selectionList = OpenMaya.MSelectionList()
        selectionList.add(objectName)
        oNode = OpenMaya.MDagPath()
        selectionList.getDagPath(0, oNode)
        return oNode
    




# Make up aim on joints
def makeUpAimOnJoints(joints, side = "L"):

    createdLocators = []

    index = 0

    for s in joints :
        index += 1
        loc = cmds.spaceLocator()[0]
        cmds.setAttr(loc+'.localScaleX', 0.01)
        cmds.setAttr(loc+'.localScaleY', 0.01)
        cmds.setAttr(loc+'.localScaleZ', 0.01)

        loc_name = s.replace("Bind_" , "loc_")
        loc = cmds.rename(loc , loc_name )
        
        Color.setColor(loc, "blue")
        pos = cmds.xform(s , q =1 , ws =1 , t =1)
        cmds.xform(loc , ws =1 , t =pos )
        par = cmds.listRelatives(s , p =1 ) [0]
        cmds.aimConstraint(loc , par , mo =1 , weight =1 , aimVector = (1,0,0) , upVector = (0,1,0) ,worldUpType = "object" , worldUpObject = "Loc_EyeUpVec_{0}".format(side))

        createdLocators.append(loc)

    return createdLocators


def locOnCurveConst(crvShape, locs):
    sel = locs 
    crv = crvShape
    for s in sel :
        pos = cmds.xform(s ,q = 1 , ws = 1 ,t = 1)
        u = getUParam(pos , crv)
        
        # Remplacer les suffixes (Loc_ par Pci_) (Point On Curve Infos)
        name = s.replace("Loc_" , "Pci_")
        print (name)
        
        # Creer le node "pointOnCurveInfo"
        pci = cmds.createNode("pointOnCurveInfo" , n = name)
        cmds.connectAttr(crv + '.worldSpace' , pci + '.inputCurve')
        cmds.setAttr(pci + '.parameter' , u )
        
        # Connecter les Output du Node Point on Curve Info de chaque CV sur les Locators correspondants.
        cmds.connectAttr( pci + '.position' , s + '.t')


def joint_on_curve(curve: str, num: int, name: str = "jnt"):
    """ """

    curve_shape = cmds.listRelatives(curve, shapes=True)[0]
    joint_list = []

    for i in range(num):

        poci = cmds.createNode("pointOnCurveInfo", name=f"poci_{name}_{i+1:02}")
        cmds.connectAttr(f"{curve_shape}.worldSpace[0]", f"{poci}.inputCurve")
        cmds.setAttr(f"{poci}.turnOnPercentage", 1)
        parameter = (1 / (num - 1)) * i
        cmds.setAttr(f"{poci}.parameter", parameter)
        translates = cmds.getAttr(f"{poci}.result.position")[0]
        cmds.delete(poci)

        joint = cmds.joint(name=f"{name}_{i+1:02}")
        joint_list.append(joint)
        cmds.setAttr(f"{joint}.translate", *translates, type="double3")

    return joint_list


# Create a cartoon eye rig
# region main
def cartoonEye(eyeGeo,faceGeo, upLidVertices, downLidVertices, side = "L"):

    print("Cartoon Eye Rig for the geometry: " + eyeGeo)




    # Create a locator at the center of the eye
    eyeCenterLocator = cmds.spaceLocator(name="Center_Eye_{0}".format(side))[0]
    cmds.select(eyeGeo)
    cmds.matchTransform(eyeCenterLocator, eyeGeo)
    Color.setColor(eyeCenterLocator, "pink")


    # Create joints on the up lid vertices
    upLidJoints = createJointsOnVertices(eyeCenterLocator, upLidVertices, side, "up")
    upLidJointsGrp = cmds.group(empty=True, name="grp_Jnts_EyeLid_{0}_{1}_Grp".format("up", side))
    cmds.parent(upLidJoints, upLidJointsGrp)

    # Create joints on the down lid vertices
    downLidJoints = createJointsOnVertices(eyeCenterLocator, downLidVertices, side, "down")
    downLidJointsGrp = cmds.group(empty=True, name="grp_Jnts_EyeLid_{0}_{1}_Grp".format("down", side))
    cmds.parent(downLidJoints, downLidJointsGrp)



    # Duplicate the eyeCenterLocator
    eyeCenterLocatorDup = cmds.duplicate(eyeCenterLocator, name="Loc_EyeUpVec_{}".format(side))[0]

    # Place the eyeCenterLocatorDup on top of the eye, for that get the bounding box of the eye, and move
    # the controller half of the bounding box up in Y
    bbox = cmds.exactWorldBoundingBox(eyeGeo)
    bBoxYSize = bbox[4] - bbox[1]
    cmds.move(0, bBoxYSize/2, 0, eyeCenterLocatorDup, relative=True)
    Color.setColor(eyeCenterLocatorDup, "green")


    # Get all the bind joints that end with '_end'
    endJointNames = []
    for j in upLidJoints:
        # Get the child of the joint
        child = cmds.listRelatives(j, children=True)[0]
        if child.endswith("_end"):
            endJointNames.append(child)

    for j in downLidJoints:
        # Get the child of the joint
        child = cmds.listRelatives(j, children=True)[0]
        if child.endswith("_end"):
            endJointNames.append(child)

    # Make up aim on the joints
    aimLocators = makeUpAimOnJoints(endJointNames, side)
    # Group the created aim locators into a "Grp_Loc_Aim_EyeLid_{side}"
    aimLocatorsGrp = cmds.group(aimLocators, name="Grp_Loc_Aim_EyeLid_{0}".format(side))


    # Create a curve that goes through the up lid joints
    crvPoints = []
    for j in upLidVertices:
        pos = cmds.xform(j, q=True, ws=True, t=True)
        pos = [round(p, 3) for p in pos]
        crvPoints.append((pos[0], pos[1], pos[2]))
    curve_top = cmds.curve( d=3,p=crvPoints)
    curve_top = cmds.rename(curve_top, "Crv_EyeLid_{0}_Top_hDef".format(side))
    # Delete the history of the curve , and center the pivot
    cmds.delete(curve_top, ch=True)
    cmds.xform(curve_top, cp=True)
    Color.setColor(curve_top, "blue")

    # Select the curve's shape node
    curve_top_shape = cmds.listRelatives(curve_top, shapes=True)[0]
    print("Curve Shape: " + curve_top_shape)
    
    # Get the locators who's name contains 'up'
    locs_top = []
    for loc in aimLocators:
        if "up" in loc:
            locs_top.append(loc)
    locOnCurveConst(curve_top_shape, locs_top)


    # Create a curve that goes through the down lid joints
    crvPoints = []
    for j in downLidVertices:
        pos = cmds.xform(j, q=True, ws=True, t=True)
        pos = [round(p, 3) for p in pos]
        crvPoints.append((pos[0], pos[1], pos[2]))
    curve_bottom = cmds.curve( d=3,p=crvPoints)
    curve_bottom = cmds.rename(curve_bottom, "Crv_EyeLid_{0}_Bottom_hDef".format(side))
    # Delete the history of the curve , and center the pivot
    cmds.delete(curve_bottom, ch=True)
    cmds.xform(curve_bottom, cp=True)
    Color.setColor(curve_bottom, "blue")

    # Select the curve's shape node
    curve_bottom_shape = cmds.listRelatives(curve_bottom, shapes=True)[0]
    print("Curve Shape: " + curve_bottom_shape)

    # Get the locators who's name contains 'down'
    locs_bottom = []
    for loc in aimLocators:
        if "down" in loc:
            locs_bottom.append(loc)
    locOnCurveConst(curve_bottom_shape, locs_bottom)


    # Create a 'lDef' curve (low definition curve) which is similar to the 'hDef' curve, but rebuilt
    # with 2 spans, cubic degree, uniform
    cmds.select(curve_top)
    curve_top_lDef = cmds.duplicate(curve_top, name="Crv_EyeLid_{0}_Top_lowDef".format(side))[0]
    mel.eval("rebuildCurve -ch 1 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s 2 -d 3 -tol 0.01")
    cmds.delete(curve_top_lDef, ch=True)
    cmds.xform(curve_top_lDef, cp=True)

    cmds.select(curve_bottom)
    curve_bottom_lDef = cmds.duplicate(curve_bottom, name="Crv_EyeLid_{0}_Bottom_lowDef".format(side))[0]
    mel.eval("rebuildCurve -ch 1 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s 2 -d 3 -tol 0.01")
    cmds.xform(curve_bottom_lDef, cp=True)
    cmds.delete(curve_bottom_lDef, ch=True)

    
    # Create a wire deformer from the low definition curve to the high definition curve
    # With a dropoff distance of 20
    cmds.select(curve_top_lDef)
    cmds.select(curve_top, add=True)
    wire_top = cmds.wire(curve_top, w=curve_top_lDef, dropoffDistance=[0, 20])

    cmds.select(curve_bottom_lDef)
    cmds.select(curve_bottom, add=True)
    wire_bottom = cmds.wire(curve_bottom, w=curve_bottom_lDef, dropoffDistance=[0, 20])


    # Group the curves and the wires into a group
    grp_curves = cmds.group([curve_top, curve_bottom, curve_top_lDef, curve_bottom_lDef,curve_top_lDef + "BaseWire", curve_bottom_lDef + "BaseWire"], name="Grp_Crv_EyeLid_{0}".format(side))
    
    # Group the two locators into a group (Center_Eye_L and Loc_EyeUpVec_L)
    grp_locators = cmds.group([eyeCenterLocator, eyeCenterLocatorDup], name="Grp_Loc_Eye_{0}".format(side))

    # Group the joints groups into a group
    grp_joints = cmds.group([upLidJointsGrp, downLidJointsGrp], name="Grp_Jnts_EyeLid_{0}".format(side))



    # Create 5 joints on the top curve
    top_Drvjoints = joint_on_curve(curve_top_lDef, 5, name="DrvJnt_Eyelid_01_up_{0}".format(side))
    Color.setColor(top_Drvjoints, "yellow")
    grp_top_joints = cmds.group(top_Drvjoints, name="Grp_DrvJnt_Eyelid_01_up_{0}".format(side))

    # Create 5 joints on the bottom curve
    bottom_Drvjoints = joint_on_curve(curve_bottom_lDef, 5, name="DrvJnt_Eyelid_01_down_{0}".format(side))
    Color.setColor(bottom_Drvjoints, "yellow")
    grp_bottom_joints = cmds.group(bottom_Drvjoints, name="Grp_DrvJnt_Eyelid_01_down_{0}".format(side))

    # Bind skin the top_Drvjoints to the top low definition curve
    # Linear, maximum influences to 5
    cmds.select(top_Drvjoints)
    cmds.select(curve_top_lDef, add=True)
    cmds.skinCluster(tsb=True, mi=5, bm=0)
    Offset.offset(top_Drvjoints, nbr = 3)

    cmds.select(bottom_Drvjoints)
    cmds.select(curve_bottom_lDef, add=True)
    cmds.skinCluster(tsb=True, mi=5)
    Offset.offset(bottom_Drvjoints, nbr = 3)

    # Create a group for the drivers
    grp_drivers = cmds.group([grp_top_joints, grp_bottom_joints], name="Grp_DrvJnt_Eyelid_{0}".format(side))

    # Create a group for the whole rig
    grp_rig = cmds.group([grp_curves, grp_locators, grp_joints, grp_drivers, "Grp_Loc_Aim_EyeLid_{0}". format(side)], name="Grp_CartoonEye_{0}".format(side))

    # Hide the loc and the curves group
    cmds.hide(grp_locators)
    cmds.hide(grp_curves)
    cmds.hide("Grp_Loc_Aim_EyeLid_{0}". format(side))