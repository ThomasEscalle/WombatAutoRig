import maya.cmds as cmds
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import Bookmark

#JntStill : joint correspondant a la reference du non mouvement (ex:Hip, clavicle, wristNonRoll ...)
# JntMove : joint correspondant a la reference du mouvement (ex:Leg, Arm, wrist...)
# Creer un reseau de node matriciel qui extrait les rotation d'une articualtion proprement.


def NonRollMatrix(JntStill, JntMove, OffsetBookmark=0):
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

    row = OffsetBookmark

    Bookmark.createBookmark("NonRoll")

    Bookmark.addNodeToBookmark(bookmark_node = "NonRoll", node_name = Loc_Still, row =0.1 + row, column = 0, state=0)
    Bookmark.addNodeToBookmark(bookmark_node = "NonRoll", node_name = Loc_Move, row =-0.1 + row, column = 0, state=0)
    Bookmark.addNodeToBookmark(bookmark_node = "NonRoll", node_name = MultMatX, row =0 + row, column = 1, state=0)
    Bookmark.addNodeToBookmark(bookmark_node = "NonRoll", node_name = DecMatX, row =0 + row, column = 2, state=0)
    Bookmark.addNodeToBookmark(bookmark_node = "NonRoll", node_name = QuatToE, row =0 + row, column = 3, state=0)

    return QuatToE

