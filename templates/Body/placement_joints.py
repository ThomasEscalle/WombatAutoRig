from wombatAutoRig.src.core import TemplateBase
from wombatAutoRig.src.core import AutorigHelper
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import Color
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
    #Creating Joints for the legs
    createJoint("PlacementJnt_Root", (0, 97.699, 0), (180,0,90), settings)
    createJoint("PlacementJnt_Hip_L", (7.636, 88.219, 0), (0,-1.767,-90), settings)
    createJoint("PlacementJnt_Knee_L", (7.636, 47.195, 1.265), (0,2.092,-90), settings)
    createJoint("PlacementJnt_Ankle_L", (7.636, 6.223, -0.231), (0,-80,-90), settings)
    createJoint("PlacementJnt_Ball_L", (7.636, 4.696, 8.428), (-90,-90,0), settings)
    createJoint("PlacementJnt_Toe_L", (7.636, 4.696, 16.486), (-90,-90,0), settings)
    
    #Parenting Joints for the legs
    cmds.parent("PlacementJnt_Hip_L", "PlacementJnt_Root")
    cmds.parent("PlacementJnt_Knee_L", "PlacementJnt_Hip_L")
    cmds.parent("PlacementJnt_Ankle_L", "PlacementJnt_Knee_L")
    cmds.parent("PlacementJnt_Ball_L", "PlacementJnt_Ankle_L")
    cmds.parent("PlacementJnt_Toe_L", "PlacementJnt_Ball_L")
    
    return 'PlacementJnt_Root'
        

# Place the placement joints for the body
def placeJoints(settings):
    Joints = placeJointsLegs(settings)
    
    #rangement des joints dans un groupe
    cmds.parent(Joints, "JointsPlacement")
    




#PlacementJnt

