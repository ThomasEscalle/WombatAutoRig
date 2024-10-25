'''
ATTENTION
Probleme si on créer plrs ribbon avec le meme nom

'''

import maya.cmds as cmds
import re
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import Color

def build_Rivet(name, Nurbs):
      
    #--- init

    #objA = Nurbs.split('.')[0]
    Rivet = cmds.spaceLocator(n=name)[0]
    
    #---  Create nodes
    nodes = []
    nodes.append( cmds.createNode('pointOnSurfaceInfo', n= Rivet + '_' + 'POS_Inf_Loc_01') )                # [0]
    nodes.append( cmds.createNode('fourByFourMatrix', n= Rivet + '_' + 'fourByfour') )                      # [1]
    nodes.append( cmds.createNode('decomposeMatrix', n= Rivet + '_' + 'DecMatX_Rivet') )                    # [2]

    #- Set Nodes Connections
  
    cmds.connectAttr( Nurbs[0] + '.worldSpace' ,nodes[0] + '.inputSurface')

    cmds.connectAttr( nodes[0] + '.positionX', nodes[1] + '.in30' )
    cmds.connectAttr( nodes[0] + '.positionY', nodes[1] + '.in31' )
    cmds.connectAttr( nodes[0] + '.positionZ', nodes[1] + '.in32' )

    cmds.connectAttr( nodes[0] + '.normalX', nodes[1] + '.in00' )
    cmds.connectAttr( nodes[0] + '.normalY', nodes[1] + '.in01' )
    cmds.connectAttr( nodes[0] + '.normalZ', nodes[1] + '.in02' )

    cmds.connectAttr( nodes[0] + '.tangentUx', nodes[1] + '.in20' )
    cmds.connectAttr( nodes[0] + '.tangentUy', nodes[1] + '.in21' )
    cmds.connectAttr( nodes[0] + '.tangentUz', nodes[1] + '.in22' )

    cmds.connectAttr( nodes[0] + '.tangentVx', nodes[1] + '.in10' )
    cmds.connectAttr( nodes[0] + '.tangentVy', nodes[1] + '.in11' )
    cmds.connectAttr( nodes[0] + '.tangentVz', nodes[1] + '.in12' )

    cmds.connectAttr( nodes[1] + '.output', nodes[2] + '.inputMatrix' )

    cmds.connectAttr( nodes[2] + '.outputTranslate', Rivet + '.translate' )

    cmds.connectAttr( nodes[2] + '.outputRotate', Rivet + '.rotate' )

    #--- Add Ctrl attributes to Rivet
    cmds.addAttr(Rivet, ln='posU', at='float', min=.0, max=1.0, dv=.5, k=True)
    cmds.addAttr(Rivet, ln='posV', at='float', min=.0, max=1.0, dv=.5, k=True)
    
    cmds.connectAttr( Rivet + '.posU', nodes[0] + '.parameterU', f=True)
    cmds.connectAttr( Rivet + '.posV', nodes[0] + '.parameterV', f=True) 

    #--- Historical intereset
    for node in nodes :
        cmds.setAttr( node + '.ihi', 0)
    
    cmds.setAttr( Rivet + 'Shape.ihi', 0)

    #--- Clean
    for attr in ['t', 'r', 's'] :
        for axis in ['x', 'y', 'z'] :
            cmds.setAttr('%s.%s%s' %(Rivet, attr, axis), k=False)
    for axis in ['X', 'Y', 'Z'] :
        cmds.setAttr('%sShape.localPosition%s' %(Rivet, axis), k=False, cb=False)


def Ribbon(pos1=[2.5,0,0], pos2=[-2.5,0,0], Name="Ribbon_01", Span=5):

    #Hierarchie groupes
    group_Global= cmds.group(name="Grp_"+Name, empty=True)
    group_ExtraNodes = cmds.group(name="Grp_Extra_Nodes_{}".format(Name), empty=True)
    group_GlobalMove = cmds.group(name="Grp_Global_Move_{}".format(Name), empty=True)
    group_CTRLs = cmds.group(name="Grp_CTRLs_Ribbon_{}".format(Name), empty=True)
    group_ExtraNodesToShow = cmds.group(name="Grp_Extra_Nodes_To_Show_{}".format(Name), empty=True)
    group_ExtraNodesToHide = cmds.group(name="Grp_Extra_Nodes_To_Hide_{}".format(Name), empty=True)
    cmds.setAttr("Grp_Extra_Nodes_To_Hide_{}.visibility".format(Name), False)
    group_rivet = cmds.group(name="Grp_Ribbon_Rivet_{}".format(Name), empty=True)
    group_DrvJnt = cmds.group(name="Grp_DrvJnt_Ribbon_{}".format(Name), empty=True)
    CTRL_Global = cmds.curve(p=[(3,0,-2),(-3,0,-2),(-4,0,-1),(-4,0,1),(-3,0,2),(3,0,2),(4,0,1),(4,0,-1),(3,0,-2)], d=1, name="CTRL_Global_{}".format(Name))
    Color.setColor(obj=CTRL_Global, color="yellow")

    cmds.parent(group_ExtraNodes, CTRL_Global, group_Global)
    cmds.parent(group_GlobalMove, CTRL_Global)
    cmds.parent(group_ExtraNodesToShow, group_ExtraNodesToHide, group_ExtraNodes)
    cmds.parent(group_CTRLs, group_GlobalMove)
    cmds.parent(group_DrvJnt, group_ExtraNodesToHide)
    cmds.parent(group_rivet, group_ExtraNodesToShow)

    #creating nurbs
    Ribbon = cmds.nurbsPlane(lr=1/Span, u=Span, ax=[0,1,0], w=8, n=Name)
    cmds.parent(Ribbon, group_GlobalMove)

    #creating rivet
    for i in range(Span):
        build_Rivet(name="rivet_{}_0{}".format(Name,i), Nurbs=Ribbon)
        cmds.setAttr("rivet_{}_0{}Shape.lodVisibility".format(Name,i), False)
    
    #placing rivet
    for i in range(Span):
        cmds.setAttr("rivet_{}_0{}.pos U".format(Name,i), (1-(Span-1)/(Span))/2+(i)/(Span))

    #hierarchisation/groupes
    for i in range(Span):
        cmds.select(["rivet_{}_0{}".format(Name,i)], add=True)
    ls_rivet=cmds.ls(sl=True)
    cmds.parent(ls_rivet, group_rivet)

    #Create Joints
    for i in range(Span):
        cmds.select(["rivet_{}_0{}".format(Name,i)])
        cmds.joint(name= "Bind_{}_0{}".format(Name,i))
        cmds.setAttr("Bind_{}_0{}.jointOrientX".format(Name,i), 90)
        cmds.setAttr("Bind_{}_0{}.jointOrientY".format(Name,i), 90)
        Offset.offset("Bind_{}_0{}".format(Name,i), nbr=2)
        Color.setColor("Bind_{}_0{}".format(Name,i), color="white")
    
    #Setting the BlendShape
    Ribbon_BlShp = cmds.nurbsPlane(lr=1/Span, u=Span, ax=[0,1,0], w=8, name="Blshp_"+Name)
    cmds.blendShape("Blshp_"+Name, Name, envelope=1, n="Blendshape_"+Name)
    cmds.setAttr("Blendshape_{}.Blshp_{}".format(Name, Name), 1)

    #Curve and DrvJnt
    Curve_Ribbon_BlShp = cmds.curve(p=[(-4,0,0),(-2,0,0),(0,0,0),(2,0,0),(4,0,0)], name = "Curve_Ribbon_BlShp_{}".format(Name))
    for i in range(3):
        if i == 0:
            iter = Name+"_End"
            x_DrvJnt = -4
        if i == 1:
            iter = Name+"_Mid"
            x_DrvJnt = 0
        if i == 2:
            iter = Name+"_Start"
            x_DrvJnt = 4
        cmds.select(clear=True)
        cmds.joint(name = "DrvJnt_Ribbon_BlShp_{}".format(iter), rad=2)
        cmds.setAttr("DrvJnt_Ribbon_BlShp_{}.translateX".format(iter), x_DrvJnt)
    
    

    #Hierarchiser elements
    cmds.parent("DrvJnt_Ribbon_BlShp_{}_Start".format(Name), "DrvJnt_Ribbon_BlShp_{}_Mid".format(Name), "DrvJnt_Ribbon_BlShp_{}_End".format(Name), group_DrvJnt)
    cmds.parent(Ribbon_BlShp, Curve_Ribbon_BlShp, group_ExtraNodesToHide)
    Offset.offset(object ="DrvJnt_Ribbon_BlShp_{}_Start".format(Name))
    Offset.offset(object ="DrvJnt_Ribbon_BlShp_{}_Mid".format(Name), nbr=2)
    Offset.offset(object ="DrvJnt_Ribbon_BlShp_{}_End".format(Name))

    #Skin Curve
    cmds.skinCluster("DrvJnt_Ribbon_BlShp_{}_Start".format(Name), "DrvJnt_Ribbon_BlShp_{}_Mid".format(Name), "DrvJnt_Ribbon_BlShp_{}_End".format(Name), Curve_Ribbon_BlShp, bindMethod=1, mi=3, tsb=True, name="Skin_Crv_{}_BlShp".format(Name))

    #twist Deformer
    cmds.nonLinear(Ribbon_BlShp, type="twist", name="Twist_{}_BlShp".format(Name))
    cmds.setAttr("Twist_{}_BlShpHandle.rotateZ".format(Name), 90)
    cmds.connectAttr("DrvJnt_Ribbon_BlShp_{}_Start.rotateX".format(Name), "Twist_{}_BlShp.startAngle".format(Name))
    cmds.connectAttr("DrvJnt_Ribbon_BlShp_{}_End.rotateX".format(Name), "Twist_{}_BlShp.endAngle".format(Name))
    cmds.parent("Twist_{}_BlShpHandle".format(Name), group_ExtraNodesToHide)

    #wire Deformer
    cmds.wire(Ribbon_BlShp, w=Curve_Ribbon_BlShp, dds=[0,50], name="WireDeformer_{}_BlShp".format(Name))

    #Creation des CTRLs
    CTRL_End = cmds.curve(p=[(-3,0,1),(-5,0,1),(-5,0,-1),(-3,0,-1),(-3,0,1)], d=1, name="CTRL_End_"+Name)
    cmds.matchTransform(CTRL_End, "DrvJnt_Ribbon_BlShp_{}_End".format(Name), piv=True)
    Color.setColor(obj=CTRL_End, color="yellow")
    CTRL_Start = cmds.curve(p=[(3,0,1),(5,0,1),(5,0,-1),(3,0,-1),(3,0,1)], d=1, name="CTRL_Start_"+Name)
    cmds.matchTransform(CTRL_Start, "DrvJnt_Ribbon_BlShp_{}_Start".format(Name), piv=True)
    Color.setColor(obj=CTRL_Start, color="yellow")
    CTRL_Mid = cmds.curve(p=[(1,0,1),(-1,0,1),(-1,0,-1),(1,0,-1),(1,0,1)], d=1, name="CTRL_Mid_"+Name)
    Color.setColor(obj=CTRL_Mid, color="yellow")

    cmds.parent(CTRL_Mid, CTRL_End, CTRL_Start, group_CTRLs)
    Offset.offset(CTRL_Mid, nbr=1)

    #Link CTRLs to DrvJnt
    cmds.connectAttr("CTRL_Start_{}.t".format(Name), "DrvJnt_Ribbon_BlShp_{}_Start.t".format(Name))
    cmds.connectAttr("CTRL_Mid_{}.t".format(Name), "DrvJnt_Ribbon_BlShp_{}_Mid.t".format(Name))
    cmds.connectAttr("CTRL_End_{}.t".format(Name), "DrvJnt_Ribbon_BlShp_{}_End.t".format(Name))

    cmds.connectAttr("CTRL_Start_{}.r".format(Name), "DrvJnt_Ribbon_BlShp_{}_Start.r".format(Name))
    cmds.connectAttr("CTRL_Mid_{}.r".format(Name), "DrvJnt_Ribbon_BlShp_{}_Mid.r".format(Name))
    cmds.connectAttr("CTRL_End_{}.r".format(Name), "DrvJnt_Ribbon_BlShp_{}_End.r".format(Name))

    #Contrainte sur Mid
    cmds.parentConstraint(CTRL_Start, CTRL_End, "CTRL_Mid_{}_Offset".format(Name), sr="none")
    cmds.parentConstraint("DrvJnt_Ribbon_BlShp_{}_Start".format(Name), "DrvJnt_Ribbon_BlShp_{}_End".format(Name), "DrvJnt_Ribbon_BlShp_{}_Mid_Move".format(Name), sr="none")



