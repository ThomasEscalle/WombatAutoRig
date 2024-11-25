import maya.cmds as cmds
from wombatAutoRig.src.core import Offset

def NonRollMatrix(JntStill, JntMove):
    #Create Locators
    Loc_Still = cmds.spaceLocator(name='Loc_nonRoll_Still_{}'.format(JntStill))[0]
    Loc_Move = cmds.spaceLocator(name='Loc_nonRoll_Move_{}'.format(JntMove))[0]

    cmds.parent(Loc_Still, JntStill)
    cmds.parent(Loc_Move, JntMove)

    cmds.setAttr(Loc_Still + ".translateX", 0)
    cmds.setAttr(Loc_Still + ".translateY", 0)
    cmds.setAttr(Loc_Still + ".translateZ", 0)
    cmds.setAttr(Loc_Still + ".rotateX", 0)
    cmds.setAttr(Loc_Still + ".rotateY", 0)
    cmds.setAttr(Loc_Still + ".rotateZ", 0)    
    cmds.setAttr(Loc_Still + ".scaleX", 1)
    cmds.setAttr(Loc_Still + ".scaleY", 1)
    cmds.setAttr(Loc_Still + ".scaleZ", 1)

    cmds.matchTransform(Loc_Move, Loc_Still, pos=True, rot=True, scl=True)

    Offset.offset(Loc_Move, nbr=1)


    #Nodale 
    MultMatX = cmds.shadingNode("multMatrix", asUtility=True, n="MultMatX_NonRoll_{}".format(JntMove))
    DecMatX = cmds.shadingNode("decomposeMatrix", asUtility=True, n="DecMatX_NonRoll_{}".format(JntMove))
    QuatToE = cmds.shadingNode("quatToEuler", asUtility=True, n="QuatToE_NonRoll_{}".format(JntMove))

    cmds.connectAttr(Loc_Move+".worldInverseMatrix[0]", MultMatX+".matrixIn[0]")
    cmds.connectAttr(Loc_Still+".worldMatrix[0]", MultMatX+".matrixIn[1]")

    cmds.connectAttr(MultMatX + ".matrixSum", DecMatX + ".inputMatrix")

    cmds.connectAttr(DecMatX + ".outputQuat", QuatToE + ".inputQuat")

