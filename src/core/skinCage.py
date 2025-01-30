import maya.cmds as cmds
import maya.api.OpenMaya as om
import math

def Cube(Joint1, Joint2, CTRL):
    #creer un cube
    cube = cmds.polyCube(name=f"cage_{Joint1}", w=1, h=1, d=1)[0]

    #le parenter dans le joint master
    cmds.parent(cube, Joint1)

    #le mettre à 0 partout sauf au translateX pour qu'il soit entre les 2 joints
    translateX = cmds.getAttr(Joint2 + ".translateX")/2
    cmds.setAttr(cube + ".t", translateX,0,0)
    cmds.setAttr(cube + ".r", 0,0,0)

    #Scale Y et Z par rapport a la bbox du CTRL et X par rapport a la distance entre les joints
    bbox_CTRL = cmds.xform(CTRL, query=True, boundingBox=True)
    radius = max((bbox_CTRL[4] - bbox_CTRL[1])/2, (bbox_CTRL[3] - bbox_CTRL[0])/2, (bbox_CTRL[5] - bbox_CTRL[2])/2)/2
    cmds.setAttr(cube + ".s", translateX*2, radius, radius)

    Joints = cmds.sets( "Bind_JNTs", q=True )
    SkinJoints = []

    if "Leg" in Joint1:
        for Joint in Joints:
            if "Leg" in Joint:
                SkinJoints.append(Joint)

    elif "Foot" in Joint1:
        for Joint in Joints:
            if "Foot" in Joint:
                SkinJoints.append(Joint)

    elif "Knee" in Joint1:
        for Joint in Joints:
            if "Knee" in Joint:
                SkinJoints.append(Joint)
    
    elif "Ball" in Joint1:
        for Joint in Joints:
            if "Ball" in Joint:
                SkinJoints.append(Joint)
    
    elif "Hip" in Joint1:
        for Joint in Joints:
            if "Hip" in Joint:
                SkinJoints.append(Joint)
            
    elif "Arm" in Joint1:
        for Joint in Joints:
            if "Arm" in Joint:
                SkinJoints.append(Joint)

    elif "Elbow" in Joint1:
        for Joint in Joints:
            if "Elbow" in Joint:
                SkinJoints.append(Joint)

    elif "Hand" in Joint1:
        for Joint in Joints:
            if "Hand" in Joint:
                SkinJoints.append(Joint)

    elif "Clavicle" in Joint1:
        for Joint in Joints:
            if "Clavicle" in Joint:
                SkinJoints.append(Joint)

    elif "Thumb" in Joint1:
        for Joint in Joints:
            if "Thumb" in Joint:
                SkinJoints.append(Joint)

    elif "Index" in Joint1:
        for Joint in Joints:
            if "Index" in Joint:
                SkinJoints.append(Joint)
    
    elif "Middle" in Joint1:
        for Joint in Joints:
            if "Middle" in Joint:
                SkinJoints.append(Joint)
    
    elif "Ring" in Joint1:
        for Joint in Joints:
            if "Ring" in Joint:
                SkinJoints.append(Joint)

    elif "Pinky" in Joint1:
        for Joint in Joints:
            if "Pinky" in Joint:
                SkinJoints.append(Joint)
    
    #skin the cube by the SkinJoints

    cmds.skinCluster(SkinJoints, cube, toSelectedBones=True, maximumInfluences=5)
    
    return cube

def CubeSpine(Joint1, CTRL, settings):
    cube = cmds.polyCube(name=f"cage_{Joint1}", w=1, h=1, d=1)[0]

    #Récuperer la hauteur du root, celle du chest et le nombre de jnt spine pour en déduire le scaleY, le scale X et Z étant donné par la BBox max du CTRL
    #Pour le translate il suffira de match all transform

    PosRoot = cmds.xform("Bind_Root", q=True, ws=True, t=True)
    PosChest = cmds.xform("Bind_Chest", q=True, ws=True, t=True)
    JntNbr = int(settings["nbrJointsSpine"])

    DistanceRootChest = math.sqrt((PosRoot[0]-PosChest[0])*(PosRoot[0]-PosChest[0])+(PosRoot[1]-PosChest[1])*(PosRoot[1]-PosChest[1])+(PosRoot[2]-PosChest[2])*(PosRoot[2]-PosChest[2]))

    ScaleY = DistanceRootChest / ((JntNbr-1))

    bbox_CTRL = cmds.xform(CTRL, query=True, boundingBox=True)
    ScaleXZ = max((bbox_CTRL[4] - bbox_CTRL[1])/2, (bbox_CTRL[3] - bbox_CTRL[0])/2, (bbox_CTRL[5] - bbox_CTRL[2])/2)/2

    cmds.setAttr(cube + ".s", ScaleXZ, ScaleY, ScaleXZ)

    cmds.matchTransform(cube, Joint1, pos=True)

    cmds.skinCluster(Joint1, cube, toSelectedBones=True, maximumInfluences=5)

    return cube

def SkinCage(settings):
    skinCage = []

    skinCage.append(Cube("DrvJnt_Arm_L", "DrvJnt_Elbow_L", "CTRL_FK_Elbow_L"))
    skinCage.append(Cube("DrvJnt_Arm_R", "DrvJnt_Elbow_R", "CTRL_FK_Elbow_R"))

    skinCage.append(Cube("DrvJnt_Elbow_L", "DrvJnt_Wrist_L", "CTRL_FK_Elbow_L"))
    skinCage.append(Cube("DrvJnt_Elbow_R", "DrvJnt_Wrist_R", "CTRL_FK_Elbow_R"))


    skinCage.append(Cube("DrvJnt_Leg_L", "DrvJnt_Knee_L", "CTRL_FK_Knee_L"))
    skinCage.append(Cube("DrvJnt_Leg_R", "DrvJnt_Knee_R", "CTRL_FK_Knee_R"))

    skinCage.append(Cube("Bind_Hip", "Bind_Hip_L", "CTRL_FK_Knee_L"))
    #skinCage.append(Cube("Bind_Hip", "Bind_Hip_R", "CTRL_FK_Knee_R"))

    skinCage.append(Cube("DrvJnt_Knee_L", "DrvJnt_Ankle_L", "CTRL_FK_Knee_L"))
    skinCage.append(Cube("DrvJnt_Knee_R", "DrvJnt_Ankle_R", "CTRL_FK_Knee_R"))

    skinCage.append(Cube("Bind_Foot_L", "Bind_Ball_L", "CTRL_FK_Knee_L"))
    skinCage.append(Cube("Bind_Foot_R", "Bind_Ball_R", "CTRL_FK_Knee_R"))

    skinCage.append(Cube("Bind_Ball_L", "Bind_Toe_L", "CTRL_FK_Knee_L"))
    skinCage.append(Cube("Bind_Ball_R", "Bind_Toe_R", "CTRL_FK_Knee_R"))


    skinCage.append(Cube("Bind_Thumb_Metacarpus_L", "Bind_Thumb_01_L", "CTRL_Finger_Index_01_L"))
    skinCage.append(Cube("Bind_Thumb_01_L", "Bind_Thumb_02_L", "CTRL_Finger_Index_01_L"))
    skinCage.append(Cube("Bind_Thumb_02_L", "Bind_Thumb_end_L", "CTRL_Finger_Index_01_L"))

    skinCage.append(Cube("Bind_Index_Metacarpus_L", "Bind_Index_01_L", "CTRL_Finger_Index_01_L"))
    skinCage.append(Cube("Bind_Index_01_L", "Bind_Index_02_L", "CTRL_Finger_Index_01_L"))
    skinCage.append(Cube("Bind_Index_02_L", "Bind_Index_03_L", "CTRL_Finger_Index_01_L"))
    skinCage.append(Cube("Bind_Index_03_L", "Bind_Index_end_L", "CTRL_Finger_Index_01_L"))

    skinCage.append(Cube("Bind_Middle_Metacarpus_L", "Bind_Middle_01_L", "CTRL_Finger_Middle_01_L"))
    skinCage.append(Cube("Bind_Middle_01_L", "Bind_Middle_02_L", "CTRL_Finger_Middle_01_L"))
    skinCage.append(Cube("Bind_Middle_02_L", "Bind_Middle_03_L", "CTRL_Finger_Middle_01_L"))
    skinCage.append(Cube("Bind_Middle_03_L", "Bind_Middle_end_L", "CTRL_Finger_Middle_01_L"))

    skinCage.append(Cube("Bind_Ring_Metacarpus_L", "Bind_Ring_01_L", "CTRL_Finger_Ring_01_L"))
    skinCage.append(Cube("Bind_Ring_01_L", "Bind_Ring_02_L", "CTRL_Finger_Ring_01_L"))
    skinCage.append(Cube("Bind_Ring_02_L", "Bind_Ring_03_L", "CTRL_Finger_Ring_01_L"))
    skinCage.append(Cube("Bind_Ring_03_L", "Bind_Ring_end_L", "CTRL_Finger_Ring_01_L"))

    skinCage.append(Cube("Bind_Pinky_Metacarpus_L", "Bind_Pinky_01_L", "CTRL_Finger_Pinky_01_L"))
    skinCage.append(Cube("Bind_Pinky_01_L", "Bind_Pinky_02_L", "CTRL_Finger_Pinky_01_L"))
    skinCage.append(Cube("Bind_Pinky_02_L", "Bind_Pinky_03_L", "CTRL_Finger_Pinky_01_L"))
    skinCage.append(Cube("Bind_Pinky_03_L", "Bind_Pinky_end_L", "CTRL_Finger_Pinky_01_L"))


    skinCage.append(Cube("Bind_Thumb_Metacarpus_R", "Bind_Thumb_01_R", "CTRL_Finger_Index_01_R"))
    skinCage.append(Cube("Bind_Thumb_01_R", "Bind_Thumb_02_R", "CTRL_Finger_Index_01_R"))
    skinCage.append(Cube("Bind_Thumb_02_R", "Bind_Thumb_end_R", "CTRL_Finger_Index_01_R"))

    skinCage.append(Cube("Bind_Index_Metacarpus_R", "Bind_Index_01_R", "CTRL_Finger_Index_01_R"))
    skinCage.append(Cube("Bind_Index_01_R", "Bind_Index_02_R", "CTRL_Finger_Index_01_R"))
    skinCage.append(Cube("Bind_Index_02_R", "Bind_Index_03_R", "CTRL_Finger_Index_01_R"))
    skinCage.append(Cube("Bind_Index_03_R", "Bind_Index_end_R", "CTRL_Finger_Index_01_R"))

    skinCage.append(Cube("Bind_Middle_Metacarpus_R", "Bind_Middle_01_R", "CTRL_Finger_Middle_01_R"))
    skinCage.append(Cube("Bind_Middle_01_R", "Bind_Middle_02_R", "CTRL_Finger_Middle_01_R"))
    skinCage.append(Cube("Bind_Middle_02_R", "Bind_Middle_03_R", "CTRL_Finger_Middle_01_R"))
    skinCage.append(Cube("Bind_Middle_03_R", "Bind_Middle_end_R", "CTRL_Finger_Middle_01_R"))

    skinCage.append(Cube("Bind_Ring_Metacarpus_R", "Bind_Ring_01_R", "CTRL_Finger_Ring_01_R"))
    skinCage.append(Cube("Bind_Ring_01_R", "Bind_Ring_02_R", "CTRL_Finger_Ring_01_R"))
    skinCage.append(Cube("Bind_Ring_02_R", "Bind_Ring_03_R", "CTRL_Finger_Ring_01_R"))
    skinCage.append(Cube("Bind_Ring_03_R", "Bind_Ring_end_R", "CTRL_Finger_Ring_01_R"))

    skinCage.append(Cube("Bind_Pinky_Metacarpus_R", "Bind_Pinky_01_R", "CTRL_Finger_Pinky_01_R"))
    skinCage.append(Cube("Bind_Pinky_01_R", "Bind_Pinky_02_R", "CTRL_Finger_Pinky_01_R"))
    skinCage.append(Cube("Bind_Pinky_02_R", "Bind_Pinky_03_R", "CTRL_Finger_Pinky_01_R"))
    skinCage.append(Cube("Bind_Pinky_03_R", "Bind_Pinky_end_R", "CTRL_Finger_Pinky_01_R"))


    skinCage.append(Cube("Bind_Clavicle_L", "Bind_Clavicle_end_L", "CTRL_Clavicle_L"))
    skinCage.append(Cube("Bind_Clavicle_R", "Bind_Clavicle_end_R", "CTRL_Clavicle_R"))


    for i in range(int(settings["nbrJointsSpine"])-2):
        skinCage.append(CubeSpine(f"Bind_RibbonSpine_0{i+1}", "CTRL_RibbonSpine_01", settings=settings))

    skinCage.append(CubeSpine(f"Bind_Root", "CTRL_Root", settings=settings))
    skinCage.append(CubeSpine(f"Bind_Chest", "CTRL_FK_Chest", settings=settings))

    return skinCage
    
def transfer_skin_weights(joints, source_meshes, target_mesh):
    """Transfers skin weights from the proxy geometry to the target mesh."""
    # Create a skin cluster on the target mesh
    skin_cluster = cmds.skinCluster(joints, target_mesh, maximumInfluences=5, toSelectedBones=True)[0]

    # Transfer weights
    for source in source_meshes:
        sourceSkin = None
        for node in source.connections():
            if node.nodeType() == 'skinCluster':
                sourceSkin = node
                break
        cmds.copySkinWeights(destinationSkin=skin_cluster, ss=sourceSkin, noMirror=True, surfaceAssociation='closestPoint')
    print("Skin weights transferred!")



#joints = cmds.ls(selection=True)  
#body_mesh = "group_Harley_0000_Harley_Queen_Geo_Harley_0000_Harley_Queen_Geo"  
##Create skin cage
#cage_meshes = SkinCage(settings=settings)
#
##Transfer skin weights to the body mesh
#transfer_skin_weights(joints, cage_meshes, body_mesh)
#
##suppr cubes
#cmds.delete(cage_meshes)