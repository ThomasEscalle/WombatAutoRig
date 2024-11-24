### Maya script to create a twist extractor system for rig setup
import maya.cmds as cmds
from wombatAutoRig.src.core import MatrixConstrain

def create_twist_extractor(name):
    ### Create a Joint in the midle of the world
    cmds.select(clear=True)
    cmds.joint(name= 'Twist_' + name + '_00', position=(0, 0, 0))
    cmds.joint(name= 'Twist_' + name + '_end', position=(1, 0, 0))

    cmds.select(clear=True)
    cmds.joint(name= 'TwistEx_' + name + '_00', position=(0, 0, 0))
    cmds.joint(name= 'TwistEx_' + name + '_end', position=(1, 0, 0))

    ### Create a locator in the midle of the world
    cmds.spaceLocator(name='Loc_Twist_' + name)

    ### Parent the locator to the Twist_<name>_end joint
    cmds.parent('Loc_Twist_' + name, 'Twist_' + name + '_end')
    ### Clear the transformations of the locator
    cmds.setAttr('Loc_Twist_' + name + '.translate', 0, 0, 0)


    ### Add a rotate plane ik handle between the TwistEx_<name>_00 and TwistEx_<name>_end joints
    cmds.ikHandle(name='ik_Twist_' + name, startJoint='TwistEx_' + name + '_00', endEffector='TwistEx_' + name + '_end', solver='ikRPsolver')

    ### Parent the ik handle to the Twist_<name>_end joint
    cmds.parent('ik_Twist_' + name, 'Twist_' + name + '_end')
    cmds.setAttr('ik_Twist_' + name + '.poleVectorX', 0)
    cmds.setAttr('ik_Twist_' + name + '.poleVectorY', 0)
    cmds.setAttr('ik_Twist_' + name + '.poleVectorZ', 0)

    ### Add an orient constraint between the Twist_<name>_00 joint, the TwistEx_<name>_00 joint and the locator
    cmds.select(clear=True)
    cmds.select('Twist_' + name + '_00', 'TwistEx_' + name + '_00', 'ik_Twist_' + name, 'Loc_Twist_' + name)
    MatrixConstrain.MatrixConstrain(('Twist_' + name + '_00', 'TwistEx_' + name + '_00'), 'Loc_Twist_' + name, Offset=False, tX=False, tY=False, tZ=False, sX=False, sY=False, sZ=False,)

    ### Add a \"TwistEx\" attribute to the Twist_<name>_00 joint
    cmds.addAttr('Twist_' + name + '_00', longName='TwistEx', attributeType='float', keyable=True)


    ### Create a multiplyDivide node
    cmds.shadingNode('multiplyDivide', asUtility=True, name='Twist_' + name + '_mult')

    ### Connect the xRotation of the Locator to the input1X of the multiplyDivide node
    cmds.connectAttr('Loc_Twist_' + name + '.rotateX', 'Twist_' + name + '_mult.input1X')
    ### Set the input2X of the multiplyDivide node to -2
    cmds.setAttr('Twist_' + name + '_mult.input2X', -2)

    ### Connect the outputX of the multiplyDivide node to the TwistEx attribute of the Twist_<name>_00 joint
    cmds.connectAttr('Twist_' + name + '_mult.outputX', 'Twist_' + name + '_00.TwistEx')

    ### Group the Twist_<name>_00 joint and the TwistEx_<name>_00 joint into \"Twist_<name>_grp\"
    cmds.group('Twist_' + name + '_00', 'TwistEx_' + name + '_00', name='Twist_' + name + '_grp')
    ### Hide the Twist_<name>_grp
    cmds.setAttr('Twist_' + name + '_grp.visibility', 0)


