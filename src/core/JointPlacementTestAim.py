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
