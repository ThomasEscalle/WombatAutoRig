from wombatAutoRig.src.core import TemplateBase
from wombatAutoRig.src.core import AutorigHelper
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import JointPlacement
from maya import cmds



# fonction that clear the selection and create a joint at the given position and orientation
def createJoint(name, position, orientation, settings):
    cmds.select(clear=True)
    joint = cmds.joint(name=name, p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = position))
    cmds.joint(joint, e=True, o=orientation, ch=True, zso=True)
    cmds.setAttr(joint+ ".displayLocalAxis", 1)
    Color.setColor(joint, "white")
    return joint


def placeJointsLegs(settings):
    # Creating the root joint
    createJoint("PlacementJnt_Root", (0, 97.699, 0), (180,0,90), settings)

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

def placeJointsArm(settings):
    createJoint("PlacementJnt_Arm_L", (15.215, 134.727, -3.639), (180,10.360,-45.005), settings)
    createJoint("PlacementJnt_Elbow_L", (32.256, 117.684, -8.045), (180,-8.329,-43.347), settings)
    createJoint("PlacementJnt_Wrist_L", (49.884, 101.044, -4.496), (180,-8.329,-43.347), settings)

        

# Place the placement joints for the body
def placeJoints(settings):
    Joints = placeJointsLegs(settings)
    
    #rangement des joints dans un groupe
    cmds.parent(Joints, "JointsPlacement")
    




#PlacementJnt

