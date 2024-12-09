from wombatAutoRig.src.core import TemplateBase
from wombatAutoRig.src.core import AutorigHelper
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import JointPlacement
from maya import cmds



# fonction that clear the selection and create a joint at the given position and orientation
def createJoint(name, position, orientation, settings, ro="xyz"):
    cmds.select(clear=True)
    joint = cmds.joint(name=name, p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = position), roo=ro)
    cmds.joint(joint, e=True, o=orientation, ch=True, zso=True)
    cmds.setAttr(joint+ ".displayLocalAxis", 1)
    Color.setColor(joint, "white")
    return joint


def placeJointsLegs(settings):
    # Creating the root joint
    createJoint("PlacementJnt_Root", (0, 97.699, 0), (0,0,0), settings, ro="xzy")

    # Creating Joints for the legs left
    createJoint("PlacementJnt_Hip_L", (7.636, 88.219, 0), (0,-1.767,-90), settings)
    createJoint("PlacementJnt_Knee_L", (7.636, 47.195, 1.265), (0,2.092,-90), settings)
    createJoint("PlacementJnt_Ankle_L", (7.636, 6.223, -0.231), (0,-80,-90), settings)
    createJoint("PlacementJnt_Ball_L", (7.636, 4.696, 8.428), (-90,-90,0), settings)
    createJoint("PlacementJnt_Toe_L", (7.636, 4.696, 16.486), (-90,-90,0), settings)

    # Creating Joints for the legs right
    createJoint("PlacementJnt_Hip_R", (-7.636, 88.219, 0), (0,-1.767,-90), settings)
    createJoint("PlacementJnt_Knee_R", (-7.636, 47.195, 1.265), (0,2.092,-90), settings)
    createJoint("PlacementJnt_Ankle_R", (-7.636, 6.223, -0.231), (0,-80,-90), settings)
    createJoint("PlacementJnt_Ball_R", (-7.636, 4.696, 8.428), (-90,-90,0), settings)
    createJoint("PlacementJnt_Toe_R", (-7.636, 4.696, 16.486), (-90,-90,0), settings)

    
    #Parenting Joints for the legs
    cmds.parent("PlacementJnt_Hip_L", "PlacementJnt_Root")
    cmds.parent("PlacementJnt_Knee_L", "PlacementJnt_Hip_L")
    cmds.parent("PlacementJnt_Ankle_L", "PlacementJnt_Knee_L")
    cmds.parent("PlacementJnt_Ball_L", "PlacementJnt_Ankle_L")
    cmds.parent("PlacementJnt_Toe_L", "PlacementJnt_Ball_L")

    cmds.parent("PlacementJnt_Hip_R", "PlacementJnt_Root")
    cmds.parent("PlacementJnt_Knee_R", "PlacementJnt_Hip_R")
    cmds.parent("PlacementJnt_Ankle_R", "PlacementJnt_Knee_R")
    cmds.parent("PlacementJnt_Ball_R", "PlacementJnt_Ankle_R")
    cmds.parent("PlacementJnt_Toe_R", "PlacementJnt_Ball_R")

    
    # Create the placement controllers for the foot (front, left, right, back)
    sphereRadius = 0.3
    JointPlacement.createControllerSphere(AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (7.636, 0, 16.905)), sphereRadius, "PlacementCtrl_Foot_Front_L" )
    JointPlacement.createControllerSphere(AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (2.969, 0, 8.428 )), sphereRadius, "PlacementCtrl_Foot_Int_L")
    JointPlacement.createControllerSphere(AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (13.606, 0, 8.428)), sphereRadius, "PlacementCtrl_Foot_Ext_L")
    JointPlacement.createControllerSphere(AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (7.636, 0, -5.765)), sphereRadius, "PlacementCtrl_Foot_Back_L")
    
    cmds.parent("PlacementCtrl_Foot_Front_L", "JointsPlacement")
    cmds.parent("PlacementCtrl_Foot_Int_L", "JointsPlacement")
    cmds.parent("PlacementCtrl_Foot_Ext_L", "JointsPlacement")
    cmds.parent("PlacementCtrl_Foot_Back_L", "JointsPlacement")


    # Create the placement controllers for the foot (front, left, right, back)
    JointPlacement.createControllerSphere(AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (-7.636, 0, 16.905)), sphereRadius, "PlacementCtrl_Foot_Front_R" )
    JointPlacement.createControllerSphere(AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (-2.969, 0, 8.428 )), sphereRadius, "PlacementCtrl_Foot_Int_R")
    JointPlacement.createControllerSphere(AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (-13.606, 0, 8.428)), sphereRadius, "PlacementCtrl_Foot_Ext_R")
    JointPlacement.createControllerSphere(AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (-7.636, 0, -5.765)), sphereRadius, "PlacementCtrl_Foot_Back_R")

    cmds.parent("PlacementCtrl_Foot_Front_R", "JointsPlacement")
    cmds.parent("PlacementCtrl_Foot_Int_R", "JointsPlacement")
    cmds.parent("PlacementCtrl_Foot_Ext_R", "JointsPlacement")
    cmds.parent("PlacementCtrl_Foot_Back_R", "JointsPlacement")


    return 'PlacementJnt_Root'

def placeJointsArm(side="L", settings={}):
    if side == 'R':
        sign = -1
        offset = 180
    else :
        sign = 1
        offset = 0
    arm = createJoint(f"PlacementJnt_Arm_{side}", (sign * 15.215, 134.727, -3.639), (180 - offset,sign * 10.360,sign * -45.005), settings)
    elbow = createJoint(f"PlacementJnt_Elbow_{side}", (sign * 31.212, 118.728, -7.775), (180 - offset,sign * -8.329,sign * -43.347), settings)
    wrist = createJoint(f"PlacementJnt_Wrist_{side}", (sign * 47.761, 103.106, -4.443), (180 - offset,sign * -8.329,sign * -43.347), settings)

    metacarpus_thumb = createJoint(f"PlacementJnt_Thumb_Metacarpus_{side}", (sign * 49.265, 101.532, -1.675), (9.185 - offset,sign * -31.656,sign * -78.280), settings)
    metacarpus_index = createJoint(f"PlacementJnt_Index_Metacarpus_{side}", (sign * 50.027, 101.707, -2.196), (-86.749- offset,sign * -10.830,sign * -51.210), settings)
    metacarpus_middle = createJoint(f"PlacementJnt_Middle_Metacarpus_{side}", (sign * 50.58, 101.536, -3.816), (-95.005- offset,sign * -6.043,sign * -50.973), settings)
    metacarpus_ring = createJoint(f"PlacementJnt_Ring_Metacarpus_{side}", (sign * 50.248, 101.303, -5.276), (-118.259- offset,sign * -0.152,sign * -55.370), settings)
    metacarpus_pimky = createJoint(f"PlacementJnt_Pimky_Metacarpus_{side}", (sign * 49.461, 101.317, -6.536), (-119.440- offset,sign * 3.341,sign * -59.948), settings)

    one_thumb = createJoint(f"PlacementJnt_Thumb_01_{side}", (sign * 50.159, 97.224, 1.038), (8.775- offset,sign * -27.050,sign * -77.445), settings)
    one_index = createJoint(f"PlacementJnt_Index_01_{side}", (sign * 54.325, 96.506, -0.900), (-84.247- offset,sign * -9.745,sign * -65.150), settings)
    one_middle = createJoint(f"PlacementJnt_Middle_01_{side}", (sign * 54.690, 95.880, -3.044), (-93.276- offset,sign * -7.128,sign * -65.968), settings)
    one_ring =createJoint(f"PlacementJnt_Ring_01_{side}", (sign * 54.015, 95.619, -5.188), (-117.553- offset,sign * -6.542,sign * -67.405), settings)
    one_pimky = createJoint(f"PlacementJnt_Pimky_01_{side}", (sign * 52.981, 95.327, -6.968), (-117.673- offset,sign * -10.984,sign * -85.811), settings)

    two_thumb = createJoint(f"PlacementJnt_Thumb_02_{side}", (sign * 50.633, 95.125, 2.087), (8.388- offset,sign * -21.347,sign * -76.502), settings)
    two_index = createJoint(f"PlacementJnt_Index_02_{side}", (sign * 56.100, 92.644, -0.171), (-82.858- offset,sign * -8.783,sign * -73.762), settings)
    two_middle = createJoint(f"PlacementJnt_Middle_02_{side}", (sign * 56.398, 92.047, -2.519), (-92.174- offset,sign * -7.535,sign * -74.582), settings)
    two_ring =createJoint(f"PlacementJnt_Ring_02_{side}", (sign * 55.553, 92.029, -4.762), (-116.414- offset,sign * -10.428,sign * -75.110), settings)
    two_pimky = createJoint(f"PlacementJnt_Pimky_02_{side}", (sign * 53.449, 92.635, -6.585), (-118.305- offset,sign * -9.087,sign * -82.188), settings)

    end_thumb = createJoint(f"PlacementJnt_Thumb_end_{side}", (sign * 51.134, 93.039, 2.925), (8.388- offset,sign * -21.347,sign * -76.502), settings)
    three_index = createJoint(f"PlacementJnt_Index_03_{side}", (sign * 56.691, 90.787, 0.136), (-82.190- offset,sign * -8.195,sign * -78.284), settings)
    three_middle = createJoint(f"PlacementJnt_Middle_03_{side}", (sign * 57.082, 89.567, -2.179), (-91.079- offset,sign * -7.767,sign * -82.798), settings)
    three_ring = createJoint(f"PlacementJnt_Ring_03_{side}", (sign * 56.127, 89.990, -4.388), (-114.047- offset,sign * -15.307,sign * -85.696), settings)
    three_pimky = createJoint(f"PlacementJnt_Pimky_03_{side}", (sign * 53.711, 91.075, -6.358), (-117.764- offset,sign * -10.735,sign * -85.330), settings)
    
    end_index = createJoint(f"PlacementJnt_Index_end_{side}", (sign * 57.097, 88.828, 0.424), (-82.190- offset,sign * -8.195,sign * -78.284), settings)
    end_middle = createJoint(f"PlacementJnt_Middle_end_{side}", (sign * 57.401, 87.045, -1.832), (-91.079- offset,sign * -7.767,sign * -82.798), settings)
    end_ring = createJoint(f"PlacementJnt_Ring_end_{side}", (sign * 56.271, 89.990, -3.863), (-114.047- offset,sign * -15.307,sign * -85.696), settings)
    end_pimky = createJoint(f"PlacementJnt_Pimky_end_{side}", (sign * 53.845, 89.431, -6.045), (-117.764- offset,sign * -10.735,sign * -85.330), settings)

    clavicle = createJoint(f"PlacementJnt_Clavicle_{side}", (sign * 2.214, 133.598, 0.001), (4.028- offset,sign * 20.182,sign *11.537), settings)
    clavicle_end = createJoint(f"PlacementJnt_Clavicle_end_{side}", (sign * 15.682, 136.347, -5.051), (4.028- offset,sign * 20.182,sign *11.537), settings)


    #parenting
    cmds.parent(end_index, three_index)
    cmds.parent(end_middle, three_middle)
    cmds.parent(end_ring, three_ring)
    cmds.parent(end_pimky, three_pimky)

    cmds.parent(end_thumb, two_thumb)
    cmds.parent(three_index, two_index)
    cmds.parent(three_middle, two_middle)
    cmds.parent(three_ring, two_ring)
    cmds.parent(three_pimky, two_pimky)

    cmds.parent(two_thumb, one_thumb)
    cmds.parent(two_index, one_index)
    cmds.parent(two_middle, one_middle)
    cmds.parent(two_ring, one_ring)
    cmds.parent(two_pimky, one_pimky)

    cmds.parent(one_thumb, metacarpus_thumb)
    cmds.parent(one_index, metacarpus_index)
    cmds.parent(one_middle, metacarpus_middle)
    cmds.parent(one_ring, metacarpus_ring)
    cmds.parent(one_pimky, metacarpus_pimky)

    cmds.parent(metacarpus_thumb, wrist)
    cmds.parent(metacarpus_index, wrist)
    cmds.parent(metacarpus_middle, wrist)
    cmds.parent(metacarpus_ring, wrist)
    cmds.parent(metacarpus_pimky, wrist)

    cmds.parent(wrist, elbow)
    cmds.parent(elbow, arm)

    cmds.parent(clavicle_end, clavicle)

    cmds.parent(arm, "JointsPlacement")
    cmds.parent(clavicle, "JointsPlacement")



# Place the placement joints for the body
def placeJoints(settings):
    Joints = placeJointsLegs(settings)
    
    placeJointsArm(side="L", settings = settings)
    placeJointsArm(side="R", settings = settings)

    #rangement des joints dans un groupe
    cmds.parent(Joints, "JointsPlacement")
    




#PlacementJnt

