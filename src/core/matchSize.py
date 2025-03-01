import maya.cmds as cmds

def matchSize(source, target, justifyY):
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
    #cmds.xform(target, rp=[0,0,0], a=True, ws=True)
    cmds.xform(target, piv=[0,-TargetHeight/2,0], a=True, ws=True)

    cmds.makeIdentity(target, t=True, r=True, s=True, a=True)

    cmds.setAttr(target + ".translateX", -TargetBbox[0]-TargetWidth/2)
    if justifyY == "min":
        justifyY = 0
    if justifyY == "center":
        justifyY = TargetHeight/2
    if justifyY == "max":
        justifyY = TargetHeight
    cmds.setAttr(target + ".translateY", -TargetBbox[1]-justifyY)
    cmds.setAttr(target + ".translateZ", -TargetBbox[2]-TargetDepth/2)

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
        ScaleFactor = SourceHeight/TargetHeight

        #multiply the target by the scale factor
        cmds.scale(ScaleFactor, ScaleFactor, ScaleFactor, target, r=True)
        cmds.setAttr(target + ".t", SourceBbox[0]+SourceWidth/2, SourceBbox[1], SourceBbox[2]+SourceDepth/2)

        #cmds.makeIdentity(target, t=True, r=True, s=True, a=True)

        cmds.delete(sourceBis)

    