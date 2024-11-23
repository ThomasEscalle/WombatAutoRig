from wombatAutoRig.src.core import TemplateBase
from wombatAutoRig.src.core import AutorigHelper
from wombatAutoRig.src.core import Offset
from maya import cmds



# Place the placement joints for the body
def placeJoints(settings):
    
    # Root
    cmds.select(clear=True)
    root = cmds.joint(name="Placement_root", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (0, 50, 0)))
    # Hip_Left
    cmds.select(clear=True)
    hip_left = cmds.joint(name="Placement_hip_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5, 46, 0)))
    # Knee_Left
    cmds.select(clear=True)
    knee_left = cmds.joint(name="Placement_knee_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5, 26, 0)))
    # Ankle_Left
    cmds.select(clear=True)
    ankle_left = cmds.joint(name="Placement_ankle_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5,  6, 0)))
    # Foot_Left
    cmds.select(clear=True)
    foot_left = cmds.joint(name="Placement_foot_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5,  2, 4)))
    # Foot_left_end
    cmds.select(clear=True)
    foot_left_end = cmds.joint(name="Placement_foot_left_end", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  5,  2, 7)))
    # Hip_Right
    cmds.select(clear=True)
    hip_right = cmds.joint(name="Placement_hip_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -5, 46, 0)))
    # Knee_Right
    cmds.select(clear=True)
    knee_right = cmds.joint(name="Placement_knee_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -5, 26, 0)))
    # Ankle_Right
    cmds.select(clear=True)
    ankle_right = cmds.joint(name="Placement_ankle_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -5,  6, 0)))
    # Foot_Right
    cmds.select(clear=True)
    foot_right = cmds.joint(name="Placement_foot_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  -5,  2, 4)))
    # Foot_right_end
    cmds.select(clear=True)
    foot_right_end = cmds.joint(name="Placement_foot_right_end", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  -5,  2, 7)))
    # Spine end
    cmds.select(clear=True)
    spine_end = cmds.joint(name="Placement_spine_end", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (0, 70, 0)))
    # Neck
    cmds.select(clear=True)
    neck = cmds.joint(name="Placement_neck", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (0, 78, -2)))
    # Clavicle_Left
    cmds.select(clear=True)
    clavicle_left = cmds.joint(name="Placement_clavicle_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  1, 70, 2)))
    # Shoulder_Left
    cmds.select(clear=True)
    shoulder_left = cmds.joint(name="Placement_shoulder_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  7, 70, -2)))
    # Elbow_Left
    cmds.select(clear=True)
    elbow_left = cmds.joint(name="Placement_elbow_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  16, 60, -4)))
    # Wrist_Left
    cmds.select(clear=True)
    wrist_left = cmds.joint(name="Placement_wrist_left", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = (  25, 52, -2)))
    # Clavicle_Right
    cmds.select(clear=True)
    clavicle_right = cmds.joint(name="Placement_clavicle_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -1, 70, 2)))
    # Shoulder_Right
    cmds.select(clear=True)
    shoulder_right = cmds.joint(name="Placement_shoulder_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -7, 70, -2)))
    # Elbow_Right
    cmds.select(clear=True)
    elbow_right = cmds.joint(name="Placement_elbow_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -16, 60, -4)))
    # Wrist_Right
    cmds.select(clear=True)
    wrist_right = cmds.joint(name="Placement_wrist_right", p=AutorigHelper.resizeJnts(bbox = settings["bbox"] , size = ( -25, 52, -2)))
    # Parent the joints together
    cmds.parent(hip_left, root)
    cmds.parent(hip_right, root)
    cmds.parent(knee_left, hip_left)
    cmds.parent(knee_right, hip_right)
    cmds.parent(ankle_left, knee_left)
    cmds.parent(ankle_right, knee_right)
    cmds.parent(foot_left, ankle_left)
    cmds.parent(foot_right, ankle_right)
    cmds.parent(foot_left_end, foot_left)
    cmds.parent(foot_right_end, foot_right)
    cmds.parent(spine_end, root)
    cmds.parent(neck, spine_end)
    cmds.parent(clavicle_left, spine_end)
    cmds.parent(shoulder_left, clavicle_left)
    cmds.parent(elbow_left, shoulder_left)
    cmds.parent(wrist_left, elbow_left)
    cmds.parent(clavicle_right, spine_end)
    cmds.parent(shoulder_right, clavicle_right)
    cmds.parent(elbow_right, shoulder_right)
    cmds.parent(wrist_right, elbow_right)
    # Place the root inside of the "AutoRig_Data|JointsPlacement"
    cmds.parent(root, "AutoRig_Data|JointsPlacement")
    Offset.offset(root)


def placeJointsLegs(settings):
    pass
