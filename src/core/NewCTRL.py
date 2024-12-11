import maya.cmds as cmds
from wombatAutoRig.src.core import Offset

def NewCTRL(CTRL, Joint, name)->str:

    #Create a group to be the new CTRL
    cmds.group(n=f"{name}", empty=True)
    cmds.matchTransform(name, Joint, pos=True, rot=True)
    Offset.offset(f"{name}", nbr=1)

    #mettre le CTRL dans le bon worldSpace
    cmds.parent(CTRL, f"{name}_Offset")

    #parenter la shape du CTRL dans le new CTRL
    cmds.makeIdentity(CTRL, a=True, t=True, r=True, s=True)
    Shape = cmds.listRelatives(CTRL, s=True)
    cmds.parent(Shape, name, s=True, r=True)

    #Supprimer l'ancien CTRL
    cmds.delete(CTRL)

    return f"{name}_Offset"