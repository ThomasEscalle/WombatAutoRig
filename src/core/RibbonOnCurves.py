import maya.cmds as cmds
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import Color


def build_Rivet(name, Nurbs):
      
    #--- init

    #objA = Nurbs.split('.')[0]
    Rivet = cmds.spaceLocator(n=name)[0]
    
    #---  Create nodes
    nodes = []
    nodes.append( cmds.createNode('pointOnSurfaceInfo', n= Rivet + '_' + 'POS_Inf_Loc') )                # [0]
    cmds.setAttr(Rivet + '_POS_Inf_Loc.turnOnPercentage', 1)
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


'''
Fonction qui permet de créer un ribbon facial a partir de 2 curves.
@Joints : int Nombres de joints voulu sur le ribbon
@DrvJnt : int Nombre de joints voulu controllant le ribbon
@Rev : boolean Permet de reverse le ribbon a sa creation s'il s'est créer dans le mauvais sens
@Name : str Nom du système
@ws : boolean Indique si vous souhaitez que les Bind joints soient orienté par rapport au monde ou au rivet (True==> monde, False==> rivet, default=False)
@wsDrvjnt : boolean Indique si vous souhaitez que les DrvJnt joints soient orienté par rapport au monde ou au rivet (True==> monde, False==> rivet, default=True)
'''
def RibbonOnCurve(Joints=5, DrvJnt=3, Rev=False, Name="Ribbon_Face", ws=False, wsDrvJnt=True):
    #Creation Loft
    Curves = cmds.ls(selection=True)
    Loft = cmds.loft(Curves, rsn=Rev, rebuild=Joints, name=Name, u=True, autoReverse=True)

    #Hierarchie
    group_Global = cmds.group(name = Name, empty=True)
    group_Curves = cmds.group(name='Grp_Crvs_'+Name, empty=True)
    group_DrvJnt = cmds.group(name="Grp_DrvJnt_"+Name, empty=True)
    group_rivet = cmds.group(name='Grp_Riv_'+Name, empty=True)

    cmds.parent(Curves, Loft[0], group_Curves)
    cmds.parent(group_Curves, group_DrvJnt, group_rivet, group_Global)

    #Creation rivets

    if Rev == True :
        uvSpace = "U"
        for i in range(Joints):
            build_Rivet(name="Riv_{}_{}".format(Name,i), Nurbs=Loft)
            cmds.setAttr("Riv_{}_{}.pos {}".format(Name,i,uvSpace), (1-(Joints-1)/(Joints))/2+(i)/(Joints))
            cmds.setAttr("Riv_{}_{}Shape.lodVisibility".format(Name,i), False)
    else :
        uvSpace = "V"
        for i in range(Joints):
            build_Rivet(name="Riv_{}_{}".format(Name,i), Nurbs=Loft)
            cmds.setAttr("Riv_{}_{}.pos {}".format(Name,i,uvSpace), (1-(Joints-1)/(Joints))/2+(i)/(Joints))
            cmds.setAttr("Riv_{}_{}Shape.lodVisibility".format(Name,i), False)
    for i in range(Joints):
        cmds.select(["Riv_{}_{}".format(Name,i)], add=True)
    ls_rivet=cmds.ls(sl=True)
    cmds.parent(ls_rivet, group_rivet)
    
    #Creation Joints
    if ws == True:
        for i in range(Joints):
            cmds.joint(name='Bind_{}_{}'.format(Name,i))
            cmds.parent('Bind_{}_{}'.format(Name,i), "Riv_{}_{}".format(Name,i))
            cmds.setAttr('Bind_{}_{}.t'.format(Name,i), 0,0,0)
            Color.setColor('Bind_{}_{}'.format(Name,i), color="white")
    else :
        for i in range(Joints):
            cmds.select("Riv_{}_{}".format(Name,i))
            cmds.joint(name='Bind_{}_{}'.format(Name,i))
            Color.setColor('Bind_{}_{}'.format(Name,i), color="white")
    
    #Creation curve intermediaire pour placer DrvJnt
    cmds.select(clear=True)
    if Rev == True:
        uvSpace = "U"
        for i in range(DrvJnt):
            build_Rivet(name="RivDrvJnt_{}_{}".format(Name,i), Nurbs=Loft)
            cmds.setAttr("RivDrvJnt_{}_{}.pos {}".format(Name,i,uvSpace), (1-(i/(DrvJnt-1))))
    else :
        uvSpace = "V"
        for i in range(DrvJnt):
            build_Rivet(name="RivDrvJnt_{}_{}".format(Name,i), Nurbs=Loft)
            cmds.setAttr("RivDrvJnt_{}_{}.pos {}".format(Name,i,uvSpace), (1-(i/(DrvJnt-1))))
    
    if wsDrvJnt == True:
        for i in range(DrvJnt):
            cmds.joint(name='DrvJnt_{}_{}'.format(Name,i), rad = 2)
            cmds.parent('DrvJnt_{}_{}'.format(Name,i), "RivDrvJnt_{}_{}".format(Name,i))
            cmds.setAttr('DrvJnt_{}_{}.t'.format(Name,i), 0,0,0)
            cmds.parent('DrvJnt_{}_{}'.format(Name,i), group_DrvJnt)
            cmds.delete("RivDrvJnt_{}_{}".format(Name,i))
            Offset.offset('DrvJnt_{}_{}'.format(Name,i))
            Color.setColor('DrvJnt_{}_{}'.format(Name,i), color="yellow")
    else :
        for i in range(DrvJnt):
            cmds.select("RivDrvJnt_{}_{}".format(Name,i))
            cmds.joint(name='DrvJnt_{}_{}'.format(Name,i), rad = 2)
            cmds.parent('DrvJnt_{}_{}'.format(Name,i), group_DrvJnt)
            cmds.delete("RivDrvJnt_{}_{}".format(Name,i))
            Offset.offset('DrvJnt_{}_{}'.format(Name,i))
            Color.setColor('DrvJnt_{}_{}'.format(Name,i), color="yellow")

    #Skinner le ribbon
    for i in range(DrvJnt):
        cmds.select('DrvJnt_{}_{}'.format(Name,i),add=True)
    DrvJnt_ls = cmds.ls(selection=True)
    cmds.skinCluster(DrvJnt_ls, Loft, bindMethod=1, mi=3, tsb=True, name="Skin_Crv_{}_BlShp".format(Name))


    


