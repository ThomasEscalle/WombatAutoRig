# ------ Matrix Parent with Offset ------ #

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math



## import maya.cmds as cmds
## nodeName = cmds.scriptNode( st=2, afterScript='cmds.sphere()' , n='MATRIX', stp='python')




def MatrixConstrain(Master, Slave, Offset=True, tX=True, tY=True, tZ=True, rX=True, rY=True, rZ=True, sX=True, sY=True, sZ=True):

    if Master == None :
        selection = cmds.ls(selection = True)
        n = len(selection)
        Master = []
        for i in range(n):
            if i != n-1:
                Master.append(toto[i])
            else :
                Slave = toto[i]
    
    if type(Master) != list :
        Master = [Master]

    if len(Master)<1 :
        print("NOTHING IS SELECTED!!!!!!!!!!!!!!!!!")

    if len(Master) < 2 :

        # Creation des differents Nodes Matrix

        MultMatX  = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_'+Slave)
        DecMatX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_'+Slave)
        if Offset == True:
            MultMatX_Offset = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_Offset_'+Slave)
            DecMatX_Offset = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_Offset_'+Slave)

            # Creation et recuperation de l'Offset

            cmds.connectAttr(Slave+'.worldMatrix[0]',MultMatX_Offset+'.matrixIn[0]')
            cmds.connectAttr(Master+'.worldInverseMatrix[0]',MultMatX_Offset+'.matrixIn[1]')
            cmds.connectAttr(MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
            cmds.disconnectAttr (MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
            cmds.delete(MultMatX_Offset)

            # Connexion de l'Offset, du Slave et du Master dans le Multiply Matrix puis dans le Decompose Matrix

            cmds.connectAttr(DecMatX_Offset+'.inputMatrix',MultMatX+'.matrixIn[0]')
        cmds.connectAttr(Master+'.worldMatrix[0]',MultMatX+'.matrixIn[1]')
        cmds.connectAttr(Slave+'.parentInverseMatrix[0]',MultMatX+'.matrixIn[2]')
        cmds.connectAttr(MultMatX+'.matrixSum',DecMatX+'.inputMatrix')

        # Connexion des outputs des Attribts du Decompose Matrix dans les input du Slave

        if tX == True:
            cmds.connectAttr(DecMatX+'.outputTranslateX',Slave+'.translateX')
        if tY == True:
            cmds.connectAttr(DecMatX+'.outputTranslateY',Slave+'.translateY')
        if tZ == True:
            cmds.connectAttr(DecMatX+'.outputTranslateZ',Slave+'.translateZ')
        if rX == True:
            cmds.connectAttr(DecMatX+'.outputRotateX',Slave+'.rotateX')
        if rY == True:
            cmds.connectAttr(DecMatX+'.outputRotateY',Slave+'.rotateY')
        if rZ == True:
            cmds.connectAttr(DecMatX+'.outputRotateZ',Slave+'.rotateZ')
        if sX == True:
            cmds.connectAttr(DecMatX+'.outputScaleX',Slave+'.scaleX')
        if sY == True:
            cmds.connectAttr(DecMatX+'.outputScaleY',Slave+'.scaleY')
        if sZ == True:
            cmds.connectAttr(DecMatX+'.outputScaleZ',Slave+'.scaleZ')

        locator = cmds.spaceLocator(name='IS_CONSTRAIN_BY_{}'.format(Master))[0]

        afterScript = 'import maya.cmds as cmds\n'

        afterScript += 'cmds.delete("{}")\n'.format(MultMatX, DecMatX)
        if Offset == True:
            afterScript += 'cmds.delete("{}")\n'.format(DecMatX_Offset)
        Script = cmds.scriptNode(stp ='python', st = 1, afterScript = afterScript, name='MATRIX_CONSTRAIN_BY_{}'.format(Master))
        cmds.connectAttr(Script + '.nodeState', locator + '.visibility')
        cmds.parent(locator, Slave)
    else : 

        j = 1/len(Master)
        AddMatX = cmds.shadingNode('addMatrix', asUtility=True, n='AddMatrix_'+Slave)
        MultMatX  = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_'+Slave)
        DecMatX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_'+Slave)
        InitMatX = cmds.shadingNode('addMatrix', asUtility=True, n='InitMatX_'+Slave)
        cmds.setAttr(InitMatX+'.matrixIn[0]', (j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j), type = 'matrix')
        MultMasterMatX = cmds.shadingNode('addMatrix', asUtility=True, n='MultMasterMatX'+Slave)

        k =n-1

        for i in range(k) :
            cmds.connectAttr(Master[i]+'.worldMatrix[0]', AddMatX+'.matrixIn[{}]'.format(i))
        
        cmds.connectAttr(InitMatX+'.matrixSum', MultMasterMatX+'.matrixIn[0]')
        cmds.connectAttr(AddMatX+'.matrixSum', MultMasterMatX+'.matrixIn[1]')

        if Offset == True:
            MultMatX_Offset = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_Offset_'+Slave)
            DecMatX_Offset = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_Offset_'+Slave)
            InvMatX_Offset = cmds.shadingNode('inverseMatrix', asUtility=True, n='InvMatX_Offset_'+Slave)

            # Creation et recuperation de l'Offset

            cmds.connectAttr(MultMasterMatX+'.matrixSum', InvMatX_Offset+'.inputMatrix')
            cmds.connectAttr(Slave+'.worldMatrix[0]',MultMatX_Offset+'.matrixIn[0]')
            cmds.connectAttr(InvMatX_Offset+'.outputMatrix',MultMatX_Offset+'.matrixIn[1]')
            cmds.connectAttr(MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
            cmds.disconnectAttr (MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
            cmds.delete(MultMatX_Offset)

            # Connexion de l'Offset, du Slave et du Master dans le Multiply Matrix puis dans le Decompose Matrix

            cmds.connectAttr(DecMatX_Offset+'.inputMatrix',MultMatX+'.matrixIn[0]')
        cmds.connectAttr(MultMasterMatX+'.matrixSum',MultMatX+'.matrixIn[1]')
        cmds.connectAttr(Slave+'.parentInverseMatrix[0]',MultMatX+'.matrixIn[2]')
        cmds.connectAttr(MultMatX+'.matrixSum',DecMatX+'.inputMatrix')

        # Connexion des outputs des Attribts du Decompose Matrix dans les input du Slave

        if tX == True:
            cmds.connectAttr(DecMatX+'.outputTranslateX',Slave+'.translateX')
        if tY == True:
            cmds.connectAttr(DecMatX+'.outputTranslateY',Slave+'.translateY')
        if tZ == True:
            cmds.connectAttr(DecMatX+'.outputTranslateZ',Slave+'.translateZ')
        if rX == True:
            cmds.connectAttr(DecMatX+'.outputRotateX',Slave+'.rotateX')
        if rY == True:
            cmds.connectAttr(DecMatX+'.outputRotateY',Slave+'.rotateY')
        if rZ == True:
            cmds.connectAttr(DecMatX+'.outputRotateZ',Slave+'.rotateZ')
        if sX == True:
            cmds.connectAttr(DecMatX+'.outputScaleX',Slave+'.scaleX')
        if sY == True:
            cmds.connectAttr(DecMatX+'.outputScaleY',Slave+'.scaleY')
        if sZ == True:
            cmds.connectAttr(DecMatX+'.outputScaleZ',Slave+'.scaleZ')

        locator = cmds.spaceLocator(name='IS_CONSTRAIN_BY_{}'.format(Master))[0]

        afterScript = 'import maya.cmds as cmds\n'

        afterScript += 'cmds.delete("{}")\n'.format(MultMatX)
        afterScript += 'cmds.delete("{}")\n'.format(MultMasterMatX)
        afterScript += 'cmds.delete("{}")\n'.format(AddMatX)
        afterScript += 'cmds.delete("{}")\n'.format(InitMatX)
        if Offset == True:
            afterScript += 'cmds.delete("{}")\n'.format(DecMatX_Offset)
        Script = cmds.scriptNode(stp ='python', st = 1, afterScript = afterScript, name='MATRIX_CONSTRAIN_BY_{}'.format(Master))
        cmds.connectAttr(Script + '.nodeState', locator + '.visibility')
        cmds.parent(locator, Slave)


if __name__ == '__main__':
    toto = cmds.ls(selection=True)
    Master = []
    n = len(toto)
    for i in range(n):
        if i != n-1:
            Master.append(toto[i])
        else :
            Slave = toto[i]
    MatrixConstrain(Master, Slave, Offset = False)