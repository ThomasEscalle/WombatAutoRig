import maya.cmds as cmds

'''
matchSize (return None): This tool allows you to easily put a mesh on the center of the world based on its shape. It can also take an another mesh as a source and it will match its position and its size 

@source ==> str   : specify the source you want your object to match. If you don't want your object to match a source just give None
@target ==> str   : specify your mesh to move
@justifyY ==> str : you have 3 options : "min" -> put the mesh on the surface / "center" put the middle of the mesh on the surface / "max" put the mesh below the surface
@scaleAxis ==> str: you have 4 options : "Best Fit" -> nothing will get out of the bounding box / "X" or "Y" or "Z" -> Does a uniform scale to match the scale of the bounding box relative to this axis


'''


def matchSize(source=None, target=None, justifyX="center", justifyY="min", justifyZ="center", scaleAxis="Y"):
    if target:
        cmds.makeIdentity(target, t=True, r=True, s=True, a=True)
        #get target BBox
        TargetBbox = cmds.exactWorldBoundingBox(target, ii=True)
        TargetWidth = TargetBbox[3]-TargetBbox[0]
        TargetHeight = TargetBbox[4]-TargetBbox[1]
        TargetDepth = TargetBbox[5]-TargetBbox[2]
    else:
        print("Please select a target")
        return

    #region put the target lowest point on the ground
    
    #set the pivot point of the target on the lowest point of the object
    cmds.xform(target, cp=True)
    
    cmds.xform(target, piv=[0,-TargetHeight/2,0], a=True, ws=True)

    cmds.makeIdentity(target, t=True, r=True, s=True, a=True)

    #Justify
    if justifyX == "min":
        justX = 0
    if justifyX == "center":
        justX = TargetWidth/2
    if justifyX == "max":
        justX = TargetWidth
    cmds.setAttr(target + ".translateX", -TargetBbox[0]-justX)
    if justifyY == "min":
        justY = 0
    if justifyY == "center":
        justY = TargetHeight/2
    if justifyY == "max":
        justY = TargetHeight
    cmds.setAttr(target + ".translateY", -TargetBbox[1]-justY)
    if justifyZ == "min":
        justZ = 0
    if justifyZ == "center":
        justZ = TargetDepth/2
    if justifyZ == "max":
        justZ = TargetDepth
    cmds.setAttr(target + ".translateZ", -TargetBbox[2]-justZ)

    cmds.makeIdentity(target, t=True, r=True, s=True, a=True)

    cmds.xform(target, rp=[0,0,0], a=True, ws=True)
    cmds.xform(target, piv=[0,0,0], a=True, ws=True)

    #get source BBox if it exists
    if source:
        sourceBis = cmds.duplicate(source, rc=True)
        if type(sourceBis) == str:
            cmds.makeIdentity(sourceBis, t=True, r=True, s=True, a=True)
            SourceBbox = cmds.exactWorldBoundingBox(sourceBis, ii=True)
        elif type(sourceBis) == list:
            for i in range(len(sourceBis)):
                if len(sourceBis)>1:
                    cmds.delete(sourceBis[-1])
                    sourceBis.pop()
            cmds.makeIdentity(sourceBis, t=True, r=True, s=True, a=True)
            SourceBbox = cmds.xform(sourceBis, q=True, ws=True, bb=True)
        SourceWidth = SourceBbox[3]-SourceBbox[0]
        SourceHeight = SourceBbox[4]-SourceBbox[1]
        SourceDepth = SourceBbox[5]-SourceBbox[2]

        #get the scale factor to match target and source
        if scaleAxis == "X":
            ScaleFactor = SourceWidth/TargetWidth
        if scaleAxis == "Y":
            ScaleFactor = SourceHeight/TargetHeight
        if scaleAxis == "Z":
            ScaleFactor = SourceDepth/TargetDepth
        if scaleAxis == "Best Fit":
            ScaleFactor = min(SourceWidth/TargetWidth, SourceHeight/TargetHeight, SourceDepth/TargetDepth)

        #multiply the target by the scale factor
        cmds.scale(ScaleFactor, ScaleFactor, ScaleFactor, target, r=True)

        if justifyX == "min":
            sourceX = SourceWidth
        if justifyX == "center":
            sourceX = SourceWidth/2
        if justifyX == "max":
            sourceX = 0

        if justifyY == "min":
            sourceY = SourceHeight
        if justifyY == "center":
            sourceY = SourceHeight/2
        if justifyY == "max":
            sourceY = 0
        cmds.setAttr(target + ".translateY", -TargetBbox[1]-justY)
        if justifyZ == "min":
            sourceZ = SourceDepth
        if justifyZ == "center":
            sourceZ = SourceDepth/2
        if justifyZ == "max":
            sourceZ = 0
        cmds.setAttr(target + ".t", SourceBbox[0]+sourceX, 0, SourceBbox[2]+sourceZ) #SourceBbox[1]+sourceY

        #cmds.makeIdentity(target, t=True, r=True, s=True, a=True)

        cmds.delete(sourceBis)

    