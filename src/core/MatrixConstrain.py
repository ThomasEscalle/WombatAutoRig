# ------ Matrix Parent with Offset ------ #

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math

from wombatAutoRig.src.core import Bookmark

## import maya.cmds as cmds
## nodeName = cmds.scriptNode( st=2, afterScript='cmds.sphere()' , n='MATRIX', stp='python')




def MatrixConstrain(Master, Slave, Offset=True, tX=True, tY=True, tZ=True, rX=True, rY=True, rZ=True, sX=True, sY=True, sZ=True, BookmarkName=None, BookRowOffset=0, BookColumnOffset=0):
    
    if len(Master)<1 :
        return "NOTHING IS SELECTED!!!!!!!!!!!!!!!!!"

    if len(Master) < 2 :

        # Creation des differents Nodes Matrix

        MultMatX  = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_'+Slave)
        DecMatX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_'+Master[0])
        ComPivMatX = cmds.shadingNode('composeMatrix', asUtility=True, n='ComPivMatX_'+Master[0])
        MultPivMatX  = cmds.shadingNode('multMatrix',asUtility=True, n='MultPivMatX_'+Slave)

        cmds.connectAttr(Master[0]+'.rotatePivot',ComPivMatX+'.inputTranslate')
        cmds.connectAttr(ComPivMatX+'.outputMatrix',MultPivMatX+'.matrixIn[0]')
        cmds.connectAttr(Master[0]+'.worldMatrix[0]',MultPivMatX+'.matrixIn[1]')
        cmds.connectAttr(MultPivMatX+'.matrixSum',MultMatX+'.matrixIn[1]')
        cmds.connectAttr(Slave+'.parentInverseMatrix[0]',MultMatX+'.matrixIn[2]')
        cmds.connectAttr(MultMatX+'.matrixSum',DecMatX+'.inputMatrix')

        if Offset == True:
            MultMatX_Offset = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_Offset_'+Slave)
            DecMatX_Offset = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_Offset_'+Slave)
            InversePivMatX = cmds.shadingNode('inverseMatrix', asUtility=True, n='InversePiv_MatX_Offset_'+Master[0])

            # Creation et recuperation de l'Offset

            cmds.connectAttr(MultPivMatX+'.matrixSum',InversePivMatX+'.inputMatrix')
            cmds.connectAttr(Slave+'.worldMatrix[0]',MultMatX_Offset+'.matrixIn[0]')
            cmds.connectAttr(InversePivMatX+'.outputMatrix',MultMatX_Offset+'.matrixIn[1]')
            cmds.connectAttr(MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
            cmds.disconnectAttr (MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
            cmds.delete(MultMatX_Offset)

            # Connexion de l'Offset, du Slave et du Master dans le Multiply Matrix puis dans le Decompose Matrix

            cmds.connectAttr(DecMatX_Offset+'.inputMatrix',MultMatX+'.matrixIn[0]')
        

        if cmds.objectType(Slave) == "joint" :
            ComposeMatX = cmds.shadingNode("composeMatrix", asUtility=True, n='ComposeMatX_'+Slave)
            cmds.connectAttr(Slave + ".jointOrient", ComposeMatX + ".inputRotate")
            MultMatX_Jnt_Parent = cmds.shadingNode("multMatrix", asUtility=True, n='MultMatX_Jnt_Parent_'+Slave)
            cmds.connectAttr(ComposeMatX + ".outputMatrix", MultMatX_Jnt_Parent + ".matrixIn[0]")
            cmds.connectAttr(Slave + ".parentMatrix[0]", MultMatX_Jnt_Parent + ".matrixIn[1]")
            InverseMatX = cmds.shadingNode("inverseMatrix", asUtility=True, n='InverseMatX'+Slave)
            cmds.connectAttr(MultMatX_Jnt_Parent + ".matrixSum", InverseMatX + ".inputMatrix")
            MultMatX_Jnt = cmds.shadingNode("multMatrix", asUtility=True, n='MultMatX_Jnt_'+Slave)
            cmds.connectAttr(Master[0] + ".worldMatrix[0]", MultMatX_Jnt + ".matrixIn[0]")
            cmds.connectAttr(InverseMatX + ".outputMatrix", MultMatX_Jnt + ".matrixIn[1]")
            DecMatX_Jnt = cmds.shadingNode("decomposeMatrix", asUtility=True, n='DecMatX_Jnt_'+Slave)
            cmds.connectAttr(MultMatX_Jnt + ".matrixSum", DecMatX_Jnt + ".inputMatrix")

            #cmds.disconnectAttr(Slave + ".parentInverseMatrix[0]", MultMatX+'.matrixIn[2]')
            #cmds.connectAttr(InverseMatX + ".outputMatrix", MultMatX+'.matrixIn[2]')




        # Connexion des outputs des Attribts du Decompose Matrix dans les input du Slave
        if tX == True:
            cmds.connectAttr(DecMatX+'.outputTranslateX',Slave+'.translateX')
        if tY == True:
            cmds.connectAttr(DecMatX+'.outputTranslateY',Slave+'.translateY')
        if tZ == True:
            cmds.connectAttr(DecMatX+'.outputTranslateZ',Slave+'.translateZ')
        if rX == True:
            MatX = DecMatX
            if cmds.objectType(Slave) == "joint" :
                MatX = DecMatX_Jnt
            cmds.connectAttr(MatX+'.outputRotateX',Slave+'.rotateX')
        if rY == True:
            MatX = DecMatX
            if cmds.objectType(Slave) == "joint" :
                MatX = DecMatX_Jnt
            cmds.connectAttr(MatX+'.outputRotateY',Slave+'.rotateY')
        if rZ == True:
            MatX = DecMatX
            if cmds.objectType(Slave) == "joint" :
                MatX = DecMatX_Jnt
            cmds.connectAttr(MatX+'.outputRotateZ',Slave+'.rotateZ')
        if sX == True:
            cmds.connectAttr(DecMatX+'.outputScaleX',Slave+'.scaleX')
        if sY == True:
            cmds.connectAttr(DecMatX+'.outputScaleY',Slave+'.scaleY')
        if sZ == True:
            cmds.connectAttr(DecMatX+'.outputScaleZ',Slave+'.scaleZ')

        locator = cmds.spaceLocator(name='IS_CONSTRAIN_BY_{}'.format(Master))[0]

        afterScript = 'import maya.cmds as cmds\n'

        afterScript += 'cmds.delete("{}")\n'.format(MultMatX, DecMatX)
        afterScript += 'cmds.delete("{}")\n'.format(MultPivMatX)
        afterScript += 'cmds.delete("{}")\n'.format(ComPivMatX)
        
        if Offset == True:
            afterScript += 'cmds.delete("{}")\n'.format(DecMatX_Offset)
        if cmds.objectType(Slave) == 'joint' :
            afterScript += 'cmds.delete("{}")\n'.format(ComposeMatX)
            afterScript += 'cmds.delete("{}")\n'.format(MultMatX_Jnt_Parent)
            afterScript += 'cmds.delete("{}")\n'.format(MultMatX_Jnt)
            afterScript += 'cmds.delete("{}")\n'.format(DecMatX_Jnt)
        Script = cmds.scriptNode(stp ='python', st = 1, afterScript = afterScript, name='MATRIX_CONSTRAIN_BY_{}'.format(Master))
        cmds.connectAttr(Script + '.nodeState', locator + '.visibility')
        cmds.parent(locator, Slave)

        #Bookmark parenthese
        if BookmarkName == None:
            if cmds.objectType(Slave) == 'joint' :
                return [DecMatX,DecMatX_Jnt]
            else :
                return DecMatX
        else :
            Bookmark.createBookmark(BookmarkName)

            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=Master[0], column = 0 +BookColumnOffset ,row = 0+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=ComPivMatX, column = 1 +BookColumnOffset ,row = 0+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=MultPivMatX, column = 2 +BookColumnOffset ,row = 0+BookRowOffset ,state=0)
            if cmds.objectType(Slave) == 'joint' :
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=ComposeMatX, column = 0 +BookColumnOffset ,row = -0.2+BookRowOffset ,state=0)
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=MultMatX_Jnt_Parent, column = 1 +BookColumnOffset ,row = -0.2+BookRowOffset ,state=0)
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=InverseMatX, column = 2 +BookColumnOffset ,row = -0.2+BookRowOffset ,state=0)

            if Offset == True:
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=DecMatX_Offset, column = 2 +BookColumnOffset ,row = 0.2+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=MultMatX, column = 3 +BookColumnOffset ,row = 0+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=DecMatX, column = 4 +BookColumnOffset ,row = 0+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=Slave, column = 5 +BookColumnOffset ,row = 0+BookRowOffset ,state=0)
            
            if cmds.objectType(Slave) == 'joint' :
                return [DecMatX,DecMatX_Jnt]
            else :
                return DecMatX
    else : 
        MultMatX  = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_'+Slave)
        DecMatXFin = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_'+Slave)
        for i in range (len(Master)):
            DecMatX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_{}'.format(i)+Slave)
            ComPivMatX = cmds.shadingNode('composeMatrix', asUtility=True, n='ComPivMatX_{}'.format(i)+Slave)
            MultPivMatX = cmds.shadingNode('multMatrix', asUtility=True, n='MultPivMatX_{}'.format(i)+Slave)
        PmaTranslate = cmds.shadingNode('plusMinusAverage', asUtility=True, n='PmaTranslate_'+Slave)
        cmds.setAttr(PmaTranslate+'.operation', 3)
        PmaRotate = cmds.shadingNode('plusMinusAverage', asUtility=True, n='PmaRotate_'+Slave)
        cmds.setAttr(PmaRotate+'.operation', 3)
        PmaScale = cmds.shadingNode('plusMinusAverage', asUtility=True, n='PmaScale_'+Slave)
        cmds.setAttr(PmaScale+'.operation', 3)
        ComMatX = cmds.shadingNode('composeMatrix', asUtility=True, n='ComMatX_'+Slave)

        #Connect Master and DecomposeMatX
        for i in range (len(Master)):
            cmds.connectAttr(Master[i]+'.worldMatrix[0]','MultPivMatX_{}{}.matrixIn[0]'.format(i, Slave))
            cmds.connectAttr(Master[i]+'.rotatePivot','ComPivMatX_{}{}.inputTranslate'.format(i, Slave))
            cmds.connectAttr('ComPivMatX_{}'.format(i)+Slave+'.outputMatrix','MultPivMatX_{}'.format(i)+Slave+'.matrixIn[1]')
            cmds.connectAttr('MultPivMatX_{}'.format(i)+Slave+'.matrixSum','DecMatX_{}'.format(i)+Slave+'.inputMatrix')

        #Connect decomposeMatX to plusMinusAverage
        for i in range (len(Master)):
            cmds.connectAttr('DecMatX_{}'.format(i)+Slave+'.outputTranslate',PmaTranslate+'.input3D[{}]'.format(i))
            cmds.connectAttr('DecMatX_{}'.format(i)+Slave+'.outputRotate',PmaRotate+'.input3D[{}]'.format(i))
            cmds.connectAttr('DecMatX_{}'.format(i)+Slave+'.outputScale',PmaScale+'.input3D[{}]'.format(i))
        
        #Connect plusMinusAverage to composeMatrix
        cmds.connectAttr(PmaTranslate+'.output3D',ComMatX+'.inputTranslate')
        cmds.connectAttr(PmaRotate+'.output3D',ComMatX+'.inputRotate')
        cmds.connectAttr(PmaScale+'.output3D',ComMatX+'.inputScale')

        if Offset == True:
            MultMatX_Offset = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_Offset_'+Slave)
            DecMatX_Offset = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_Offset_'+Slave)
            InvMatX_Offset = cmds.shadingNode('inverseMatrix', asUtility=True, n='InvMatX_Offset_'+Slave)

            # Creation et recuperation de l'Offset

            cmds.connectAttr(ComMatX+'.outputMatrix', InvMatX_Offset+'.inputMatrix')
            cmds.connectAttr(Slave+'.worldMatrix[0]',MultMatX_Offset+'.matrixIn[0]')
            cmds.connectAttr(InvMatX_Offset+'.outputMatrix',MultMatX_Offset+'.matrixIn[1]')
            cmds.connectAttr(MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
            cmds.disconnectAttr (MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
            cmds.delete(MultMatX_Offset)

            # Connexion de l'Offset, du Slave et du Master dans le Multiply Matrix puis dans le Decompose Matrix

            cmds.connectAttr(DecMatX_Offset+'.inputMatrix',MultMatX+'.matrixIn[0]')
        cmds.connectAttr(ComMatX+'.outputMatrix',MultMatX+'.matrixIn[1]')
        cmds.connectAttr(Slave+'.parentInverseMatrix[0]',MultMatX+'.matrixIn[2]')
        cmds.connectAttr(MultMatX+'.matrixSum',DecMatXFin+'.inputMatrix')

        if cmds.objectType(Slave) == "joint" :
            ComposeMatX = cmds.shadingNode("composeMatrix", asUtility=True, n='ComposeMatX_'+Slave)
            cmds.connectAttr(Slave + ".jointOrient", ComposeMatX + ".inputRotate")
            MultMatX_Jnt_Parent = cmds.shadingNode("multMatrix", asUtility=True, n='MultMatX_Jnt_'+Slave)
            cmds.connectAttr(ComposeMatX + ".outputMatrix", MultMatX_Jnt_Parent + ".matrixIn[0]")
            cmds.connectAttr(Slave + ".parentMatrix[0]", MultMatX_Jnt_Parent + ".matrixIn[1]")
            InverseMatX = cmds.shadingNode("inverseMatrix", asUtility=True, n='InverseMatX'+Slave)
            cmds.connectAttr(MultMatX_Jnt_Parent + ".matrixSum", InverseMatX + ".inputMatrix")

            cmds.disconnectAttr(Slave + ".parentInverseMatrix[0]", MultMatX+'.matrixIn[2]')
            cmds.connectAttr(InverseMatX + ".outputMatrix", MultMatX+'.matrixIn[2]')
        
        # Connexion des outputs des Attribts du Decompose Matrix dans les input du Slave
        
        if tX == True:
            cmds.connectAttr(DecMatXFin+'.outputTranslateX',Slave+'.translateX')
        if tY == True:
            cmds.connectAttr(DecMatXFin+'.outputTranslateY',Slave+'.translateY')
        if tZ == True:
            cmds.connectAttr(DecMatXFin+'.outputTranslateZ',Slave+'.translateZ')
        if rX == True:
            cmds.connectAttr(DecMatXFin+'.outputRotateX',Slave+'.rotateX')
        if rY == True:
            cmds.connectAttr(DecMatXFin+'.outputRotateY',Slave+'.rotateY')
        if rZ == True:
            cmds.connectAttr(DecMatXFin+'.outputRotateZ',Slave+'.rotateZ')
        if sX == True:
            cmds.connectAttr(DecMatXFin+'.outputScaleX',Slave+'.scaleX')
        if sY == True:
            cmds.connectAttr(DecMatXFin+'.outputScaleY',Slave+'.scaleY')
        if sZ == True:
            cmds.connectAttr(DecMatXFin+'.outputScaleZ',Slave+'.scaleZ')

        locator = cmds.spaceLocator(name='IS_CONSTRAIN_BY_{}'.format(Master))[0]

        afterScript = 'import maya.cmds as cmds\n'

        afterScript += 'cmds.delete("{}")\n'.format(MultMatX)
        afterScript += 'cmds.delete("{}")\n'.format(PmaScale)
        afterScript += 'cmds.delete("{}")\n'.format(PmaRotate)
        afterScript += 'cmds.delete("{}")\n'.format(PmaTranslate)
        for i in range(len(Master)):
            afterScript += 'cmds.delete("{}")\n'.format(f'DecMatX_{i}'+Slave)
            afterScript += 'cmds.delete("{}")\n'.format(f'ComPivMatX_{i}'+Slave)
            afterScript += 'cmds.delete("{}")\n'.format(f'MultPivMatX_{i}'+Slave)

        if Offset == True:
            afterScript += 'cmds.delete("{}")\n'.format(DecMatX_Offset)
        if cmds.objectType(Slave) == 'joint' :
            afterScript += 'cmds.delete("{}")\n'.format(ComposeMatX)
            afterScript += 'cmds.delete("{}")\n'.format(MultMatX_Jnt_Parent)
        Script = cmds.scriptNode(stp ='python', st = 1, afterScript = afterScript, name='MATRIX_CONSTRAIN_BY_{}'.format(Master))
        cmds.connectAttr(Script + '.nodeState', locator + '.visibility')
        cmds.parent(locator, Slave)

        if BookmarkName == None:
            return DecMatXFin
        else :
            Bookmark.createBookmark(BookmarkName)

            for i in range(len(Master)):
                h = 0.15*i/2
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=Master[i], column = 0 +BookColumnOffset ,row = 0.15*i-h+BookRowOffset ,state=0)
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=f'ComPivMatX_{i}'+Slave, column = 1 +BookColumnOffset ,row =  0.15*i-h+BookRowOffset ,state=0)
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=f'MultPivMatX_{i}'+Slave, column = 2 +BookColumnOffset ,row =  0.15*i-h+BookRowOffset ,state=0)
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=f'DecMatX_{i}'+Slave, column = 3 +BookColumnOffset ,row =  0.15*i-h+BookRowOffset ,state=0)
            
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=PmaTranslate, column = 4 +BookColumnOffset ,row =  0.15+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=PmaRotate, column = 4 +BookColumnOffset ,row =  0+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=PmaScale, column = 4 +BookColumnOffset ,row =  -0.15+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=ComMatX, column = 5 +BookColumnOffset ,row =  0+BookRowOffset ,state=0)
            if cmds.objectType(Slave) == 'joint' :
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=ComposeMatX, column = 3 +BookColumnOffset ,row = -0.25+BookRowOffset ,state=0)
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=MultMatX_Jnt_Parent, column = 4 +BookColumnOffset ,row = -0.25+BookRowOffset ,state=0)
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=InverseMatX, column = 5 +BookColumnOffset ,row = -0.25+BookRowOffset ,state=0)
            if Offset == True:
                Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=DecMatX_Offset, column = 5 +BookColumnOffset ,row = 0.2+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=MultMatX, column = 6 +BookColumnOffset ,row = 0+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=DecMatXFin, column = 7 +BookColumnOffset ,row = 0+BookRowOffset ,state=0)
            Bookmark.addNodeToBookmark(bookmark_node=BookmarkName, node_name=Slave, column = 8 +BookColumnOffset ,row = 0+BookRowOffset ,state=0)

        return DecMatXFin




if __name__ == '__main__':
    selection = cmds.ls(selection = True)
    n = len(selection)
    if len(selection) < 3 :
        Master = selection[0]
        Slave = selection[1]
    else :
        Master = []
        for i in range(n):
            if i != n-1:
                Master.append(selection[i])
            else :
                Slave = selection[i]
    MatrixConstrain(Master, Slave, Offset = False)