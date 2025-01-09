import maya.cmds as cmds
from wombatAutoRig.src.core import Offset

#JntStill : joint correspondant a la reference du non mouvement (ex:Hip, clavicle, wristNonRoll ...)
# JntMove : joint correspondant a la reference du mouvement (ex:Leg, Arm, wrist...)
# Creer un reseau de node matriciel qui extrait les rotation d'une articualtion proprement.


def NonRollMatrix(JntStill, JntMove):
    #Create Locators
    Loc_Still = cmds.spaceLocator(name='Loc_nonRoll_Still_{}'.format(JntStill))[0]
    Loc_Move = cmds.spaceLocator(name='Loc_nonRoll_Move_{}'.format(JntMove))[0]

    cmds.parent(Loc_Still, JntStill)
    cmds.parent(Loc_Move, JntMove)

    cmds.setAttr(Loc_Move + ".translateX", 0)
    cmds.setAttr(Loc_Move + ".translateY", 0)
    cmds.setAttr(Loc_Move + ".translateZ", 0)
    cmds.setAttr(Loc_Move + ".rotateX", 0)
    cmds.setAttr(Loc_Move + ".rotateY", 0)
    cmds.setAttr(Loc_Move + ".rotateZ", 0)    
    cmds.setAttr(Loc_Move + ".scaleX", 1)
    cmds.setAttr(Loc_Move + ".scaleY", 1)
    cmds.setAttr(Loc_Move + ".scaleZ", 1)

    cmds.matchTransform(Loc_Still, Loc_Move, pos=True, rot=True, scl=True)

    Offset.offset(Loc_Still, nbr=1)


    #Nodale 
    MultMatX = cmds.shadingNode("multMatrix", asUtility=True, n="MultMatX_NonRoll_{}".format(JntMove))
    DecMatX = cmds.shadingNode("decomposeMatrix", asUtility=True, n="DecMatX_NonRoll_{}".format(JntMove))
    QuatToE = cmds.shadingNode("quatToEuler", asUtility=True, n="QuatToE_NonRoll_{}".format(JntMove))

    cmds.connectAttr(Loc_Move+".worldMatrix[0]", MultMatX+".matrixIn[0]")
    cmds.connectAttr(Loc_Still+".worldInverseMatrix[0]", MultMatX+".matrixIn[1]")

    cmds.connectAttr(MultMatX + ".matrixSum", DecMatX + ".inputMatrix")

    cmds.connectAttr(DecMatX + ".outputQuat", QuatToE + ".inputQuat")

    return QuatToE

