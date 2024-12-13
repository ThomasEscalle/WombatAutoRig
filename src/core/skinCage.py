import maya.cmds as cmds

def skinCage(Joints, settings=settings):
    cube = cmds.polyCube()
    for joint in Joints : 
        cage=cmds.duplicate(cube, n=f"cube_{joint}")
        cmds.matchTransform(cage, joint, pos=True)


Joints = cmds.ls(selection=True)

skinCage(Joints)