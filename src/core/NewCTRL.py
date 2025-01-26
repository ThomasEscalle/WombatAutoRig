import maya.cmds as cmds
from wombatAutoRig.src.core import Offset

def NewCTRL(CTRL, Joint, name, nbr=1)->str:

    #Create a group to be the new CTRL
    Toto = cmds.group(n=f"{name}", empty=True)
    cmds.matchTransform(Toto, Joint, pos=True, rot=True)
    Offset.offset(Toto, nbr=nbr)

    #mettre le CTRL dans le bon worldSpace
    cmds.parent(CTRL, f"{name}_Offset")

    #parenter la shape du CTRL dans le new CTRL
    cmds.makeIdentity(CTRL, a=True, t=True, r=True, s=True)
    Shape = cmds.listRelatives(CTRL, s=True)
    cmds.parent(Shape, name, s=True, r=True)

    #Supprimer l'ancien CTRL
    cmds.delete(CTRL)

    return f"{name}_Offset"

def Bend(CTRL, Bend, name)->str:
    #mettre le CTRL dans le meme worldspace que le bend
    cmds.parent(CTRL, Bend +"_Offset")
    cmds.makeIdentity(CTRL, a=True, t=True, r=True, s=True)

    #parent la shape
    Shape = cmds.listRelatives(CTRL, s=True)
    cmds.parent(Shape, Bend, s=True, r=True)

    #rename le Bend

    cmds.rename(Bend, name)

    return name
