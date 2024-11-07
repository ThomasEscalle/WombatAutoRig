from wombatAutoRig.src.core import JointPlacement
from wombatAutoRig.src.core import Offset

def connectLine(object0, object1, name="line", width = 4 ):
    # Create a curve with two points
    curve = cmds.curve(d=1, p=[(0, 0, 0), (0, 0, 0)], k=[0, 1], name=name)

    #Get world transform of the object
    decomposeMatrix0 = cmds.createNode('decomposeMatrix', n='decomposeMatrix0')
    decomposeMatrix1 = cmds.createNode('decomposeMatrix', n='decomposeMatrix1')

    cmds.connectAttr(object0+'.worldMatrix', decomposeMatrix0+'.inputMatrix')
    cmds.connectAttr(object1+'.worldMatrix', decomposeMatrix1+'.inputMatrix')

    # Connect the object's position to the curve's points
    cmds.connectAttr(decomposeMatrix0 + ".outputTranslate", curve + ".controlPoints[0]")
    cmds.connectAttr(decomposeMatrix1 + ".outputTranslate", curve + ".controlPoints[1]")

    # Set the line width of the shape
    cmds.setAttr(curve + ".lineWidth", width)

    # Set the object to template so it is not selectable
    cmds.setAttr(curve + ".template", 1)

    return curve


groupJointPlacement = cmds.group(name='JointPlacement', empty=True)
groupLineJointPlacement = cmds.group(name='LineJointPlacement', empty=True)

#AIMCONSTRAINT MODE

##CREATING THE BOUBOUL
#Ankle_L = JointPlacement.createController(pos=(4.125,9.609,-0.318),name='Ankle_L')
#Ball_L = JointPlacement.createController(pos=(4.366,2.707,4.391),name='Ball_L')
#Toe_L = JointPlacement.createController(pos=(4.411,1.428,8.568),name='Toe_L')
#Knee_L = JointPlacement.createController(pos=(4.299,28.693,0.09),name='Knee_L')
#Leg_L = JointPlacement.createController(pos=(4.46,46.985,0), name='Leg_L')
#Root = JointPlacement.createController(pos=(0,52,0), localRotation = [0,0,90], name='Root')

###LINE
#Line0 = connectLine(Leg_L, Knee_L)
#Line1 = connectLine(Knee_L, Ankle_L)
#Line2 = connectLine(Ankle_L, Ball_L)
#Line3 = connectLine(Ball_L, Toe_L)
#Line4 = connectLine(Root, Leg_L)
#
##RANGEMENT
#cmds.parent('Ankle_L','Ball_L','Toe_L','Knee_L', Leg_L, Root, groupJointPlacement)
#cmds.parent( Line0, Line1, Line2, Line3, Line4, groupLineJointPlacement)
#Offset.offset(Toe_L, nbr=1)
#Offset.offset(Ball_L, nbr=1)
#Offset.offset(Ankle_L, nbr=1)
#Offset.offset(Knee_L, nbr=1)
#Offset.offset(Leg_L, nbr=1)
#Offset.offset(Root, nbr=1)


##AIMCONSTRAINT
#cmds.aimConstraint(Ball_L,Ankle_L, wu=(1,0,0))
#cmds.aimConstraint(Ankle_L,Knee_L, wu=(1,0,0))
#cmds.aimConstraint(Toe_L,Ball_L, wu=(1,0,0))
#cmds.aimConstraint(Knee_L,Leg_L, wu=(1,0,0))
#cmds.connectAttr(Ball_L+'.r', Toe_L+'.r')



#FK MODE

##CREATING THE BOUBOUL
Root = JointPlacement.createController(pos=(0,52,0), localRotation = [0,180,-90], name='Root')
Leg_L = JointPlacement.createController(pos=(0,0,0), name='Leg_L')
Knee_L = JointPlacement.createController(pos=(0,0,0), name='Knee_L')
Ankle_L = JointPlacement.createController(pos=(0,0,0), name='Ankle_L')
Ball_L = JointPlacement.createController(pos=(0,0,0), name='Ball_L')
Toe_L = JointPlacement.createController(pos=(0,0,0), name='Toe_L')

#FK SYSTEME
cmds.parent(Toe_L, Ball_L)
cmds.parent(Ball_L, Ankle_L)
cmds.parent(Ankle_L, Knee_L)
cmds.parent(Knee_L, Leg_L)
cmds.parent(Leg_L, Root)

#SETATTRIBUTE
cmds.setAttr(Leg_L+'.t', -5.015,-4.46,0)
cmds.setAttr(Leg_L+'.r', 0.002,-0.282,179.496)
cmds.setAttr(Knee_L+'.t', 18.293,0,0)
cmds.setAttr(Knee_L+'.r', 0,1.507,0)
cmds.setAttr(Ankle_L+'.t', 19.089,0,0)
cmds.setAttr(Ankle_L+'.r', 0,-35.512,0)
cmds.setAttr(Ball_L+'.t', 8.359,0,0)
cmds.setAttr(Ball_L+'.r', 0,-38.669,0)
cmds.setAttr(Toe_L+'.t', 4.369,0,0)


##LINE
Line0 = connectLine(Leg_L, Knee_L)
Line1 = connectLine(Knee_L, Ankle_L)
Line2 = connectLine(Ankle_L, Ball_L)
Line3 = connectLine(Ball_L, Toe_L)
Line4 = connectLine(Root, Leg_L)

#RANGEMENT
cmds.parent( Line0, Line1, Line2, Line3, Line4, groupLineJointPlacement)
Offset.offset(Toe_L, nbr=1)
Offset.offset(Ball_L, nbr=1)
Offset.offset(Ankle_L, nbr=1)
Offset.offset(Knee_L, nbr=1)
Offset.offset(Leg_L, nbr=1)
Offset.offset(Root, nbr=1)


cmds.parent(Root, groupJointPlacement)