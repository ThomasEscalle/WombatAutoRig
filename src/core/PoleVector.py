import maya.cmds as cmds
import maya.api.OpenMaya as om
import math

if __name__ == '__main__':
        joints = cmds.ls(selection = True)
        joint_1 = joints[0]
        joint_2 = joints[1]
        joint_3 = joints[2]
        CTRL = joints[3]

def PoleVector(joint_1, joint_2, joint_3, CTRL):
    a = om.MVector(cmds.xform(joint_1, q=True, rp=True, ws=True))
    b = om.MVector(cmds.xform(joint_2, q=True, rp=True, ws=True))
    c = om.MVector(cmds.xform(joint_3, q=True, rp=True, ws=True))
    
    start_to_end = c-a
    mid_to_end = c-b
    start_to_mid = b-a
    
    len_start_to_mid= om.MVector.length(start_to_mid)
    len_mid_to_end= om.MVector.length(mid_to_end)
    len_start_to_end= om.MVector.length(start_to_end)
    angle_BAC = om.MVector.angle(start_to_end,start_to_mid)
        
    mid_point = math.cos(angle_BAC) * len_start_to_mid * (start_to_end/len_start_to_end)
    
    mid = mid_point + a
    
    projection = b - mid
    len_projection = om.MVector.length(projection)
    mult = ((len_start_to_mid+len_mid_to_end)/2)/len_projection
    projection *= mult
    projection += b


    cmds.setAttr('{}.translateX'.format(CTRL), projection.x)
    cmds.setAttr('{}.translateY'.format(CTRL), projection.y)
    cmds.setAttr('{}.translateZ'.format(CTRL), projection.z)


if __name__ == '__main__':
        PoleVector(joint_1, joint_2, joint_3, CTRL)



    
