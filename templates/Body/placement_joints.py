from wombatAutoRig.src.core import TemplateBase
from wombatAutoRig.src.core import AutorigHelper
from wombatAutoRig.src.core import Offset
from maya import cmds



# fonction that clear the selection and create a joint at the given position and orientation
def createJoint(name, position, orientation, settings):
    cmds.select(clear=True)
    joint = cmds.joint(name=name, p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = position))
    cmds.joint(joint, e=True, o=orientation, ch=True, zso=True)
    cmds.setAttr(joint+ ".displayLocalAxis", 1)
    return joint


def placeJointsLegs(settings):
    createJoint("PlacementJnt_Root", (0, 100, 0), (0,0,90), settings)
    createJoint("PlacementJnt_Hip_L", (8, 92.424, 0), (0,-1.767,-90), settings)
    createJoint("PlacementJnt_Knee_L", (8, 49.445, 1.326), (0,2.208,-90), settings)
    createJoint("PlacementJnt_Ankle_L", (8, 6.476, -0.331), (0,2.208,-90), settings)

# Place the placement joints for the body
def placeJoints(settings):
    placeJointsLegs(settings)




#PlacementJnt


