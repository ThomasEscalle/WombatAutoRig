import maya.cmds as cmds
from wombatAutoRig.src.core import Color


# Create an offset group under the selected object
# @param object: string, name of the object to offset, it can also be a list of objects
# @param nbr: int, number of groups to create (offset, move, hook)
def offset(object, nbr=1):

    # check if object is a list
    if type(object) == list:
        for obj in object:
            offset(obj, nbr)
        return


    

    # get selected object's parent and store name
    selParent = cmds.listRelatives(object, parent=True)

    # create OFFSET and MOVE groups under temp names
    offsetGroup = cmds.group(em=True, name= object+'_Offset')
    if nbr >1:
        moveGroup = cmds.group(em=True, name=object+'_Move')
    if nbr >2:
        hookGroup = cmds.group(em=True, name=object+'_Hook')


    # set group color 
    if nbr >1:
        cmds.setAttr(moveGroup + '.useOutlinerColor', 1)
        cmds.setAttr(moveGroup + '.outlinerColorR', 0.7)
        cmds.setAttr(moveGroup + '.outlinerColorG', 0.6)
        cmds.setAttr(moveGroup + '.outlinerColorB', 1)

    if nbr >2:
        cmds.setAttr(hookGroup + '.useOutlinerColor', 1)
        cmds.setAttr(hookGroup + '.outlinerColorR', 1)
        cmds.setAttr(hookGroup + '.outlinerColorG', 0.62)
        cmds.setAttr(hookGroup + '.outlinerColorB', 0.09)

    # Match group transforms to selected object and
    #   create parent hierarchy
    cmds.matchTransform(offsetGroup, object)
    if nbr >1:
        cmds.matchTransform(moveGroup, object)
    if nbr >2:
        cmds.matchTransform(hookGroup, object)
    
    cmds.parent(object, offsetGroup)
    if nbr >1:
        cmds.parent(moveGroup, offsetGroup)
        cmds.parent(object, moveGroup)
    if nbr >2:
        cmds.parent(moveGroup, hookGroup)
        cmds.parent(hookGroup, offsetGroup)
    if selParent is None:
        print('none')
    else:
        cmds.parent(offsetGroup, selParent)


    # set group color
    Color.setDefaultColor(offsetGroup, "Offset")
    if nbr >1:
        Color.setDefaultColor(moveGroup, "Move")
    if nbr >2:
        Color.setDefaultColor(hookGroup, "Hook")

