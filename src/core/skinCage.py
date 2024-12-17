import maya.cmds as cmds
import maya.api.OpenMaya as om

def create_skin_cage(joints, body_mesh):
    """Creates proxy cubes around joints and skins them to individual joints."""
    # List to store created cages
    cages = []

    for joint in joints:
        # Create a cube for the joint
        cube = cmds.polyCube(name=f"cage_{joint}", w=1, h=1, d=1)[0]

        # Match cube's position to the joint
        cmds.matchTransform(cube, joint, pos=True, rot=True)

        # Adjust the cube's size and shape dynamically
        modify_cube_shape(cube, joint, body_mesh)

        #Scale up cubes so the skin works better
        cmds.setAttr(cube + ".scaleY", 1.1*(cube + ".scaleY"))
        cmds.setAttr(cube + ".scaleZ", 1.1*(cube + ".scaleZ"))

        # Skin the cube to the joint
        cmds.skinCluster(joint, cube, toSelectedBones=True, maximumInfluences=1)

        cages.append(cube)

    return cages

def modify_cube_shape(cube, joint, body_mesh):
    """Adjusts the shape of the cube to conform to the body mesh."""
    # Get the joint's world position
    joint_pos = cmds.xform(joint, q=True, ws=True, t=True)
    joint_vec = om.MVector(joint_pos)
    if "Leg" or "Foot" or "Knee" or "Ball" or "Toe" or "Ankle" or "Hip" in joint:
        bbox_CTRL = cmds.xform("CTRL_FK_Knee_L", query=True, boundingBox=True)
        radius = (bbox_CTRL[4] - bbox_CTRL[1])/2
    elif "Arm" or "Elbow" or "Wrist" or "Clavicle" or "Hand" in joint:
        bbox_CTRL = cmds.xform("CTRL_FK_Elbow_L", query=True, boundingBox=True)
        radius = (bbox_CTRL[4] - bbox_CTRL[1])/2
    elif "Spine" or "Root" in joint:
        bbox_CTRL = cmds.xform("CTRL_FK_Spine_L", query=True, boundingBox=True)
        radius = (bbox_CTRL[4] - bbox_CTRL[1])/2
    elif "Thumb" or "Index" or "Middle" or "Ring" or "Pimky" in joint:
        bbox_CTRL = cmds.xform("CTRL_FK_Index_L", query=True, boundingBox=True)
        radius = (bbox_CTRL[4] - bbox_CTRL[1])/2


    # Scale cube to fit a localized bounding box of the body mesh
    bbox = get_local_bounding_box(joint_vec, body_mesh, radius=radius)

    # Adjust cube scale
    cmds.setAttr(f"{cube}.scaleX", bbox['size'][0])
    cmds.setAttr(f"{cube}.scaleY", bbox['size'][1])
    cmds.setAttr(f"{cube}.scaleZ", bbox['size'][2])

    # Move the cube's vertices to conform better to the body shape
    vertices = cmds.ls(f"{cube}.vtx[*]", fl=True)
    for vtx in vertices:
        vtx_pos = cmds.pointPosition(vtx, w=True)
        vtx_vec = om.MVector(vtx_pos)

        # Find the closest point on the body mesh
        closest_point = get_closest_point_on_mesh(body_mesh, vtx_vec)

        # Blend vertex position towards the body mesh
        new_pos = (closest_point * 0.8) + (vtx_vec * 0.2)
        cmds.xform(vtx, ws=True, t=[new_pos.x, new_pos.y, new_pos.z])

def get_local_bounding_box(center_vec, mesh, radius):
    """Returns the bounding box size around a specific region of the mesh."""
    # Get all vertices of the mesh
    vertices = cmds.ls(f"{mesh}.vtx[*]", fl=True)
    points = [om.MVector(cmds.pointPosition(vtx, w=True)) for vtx in vertices]

    # Filter vertices within the given radius
    local_points = [p for p in points if (p - center_vec).length() <= radius]

    # Determine the bounding box for these points
    if local_points:
        min_x = min(p.x for p in local_points)
        max_x = max(p.x for p in local_points)
        min_y = min(p.y for p in local_points)
        max_y = max(p.y for p in local_points)
        min_z = min(p.z for p in local_points)
        max_z = max(p.z for p in local_points)

        size = [(max_x - min_x), (max_y - min_y), (max_z - min_z)]
        return {'size': size, 'center': [(min_x + max_x) / 2, (min_y + max_y) / 2, (min_z + max_z) / 2]}
    else:
        return {'size': [1, 1, 1], 'center': [center_vec.x, center_vec.y, center_vec.z]}  # Default size

def get_closest_point_on_mesh(mesh, point_vec):
    """Finds the closest point on the mesh to a given point."""
    selection = om.MSelectionList()
    selection.add(mesh)
    dag_path = selection.getDagPath(0)
    mfn_mesh = om.MFnMesh(dag_path)

    point = om.MPoint(point_vec)
    closest_point, _ = mfn_mesh.getClosestPoint(point, om.MSpace.kWorld)
    return om.MVector(closest_point)

def transfer_skin_weights(joints, source_meshes, target_mesh):
    """Transfers skin weights from the proxy geometry to the target mesh."""
    # Create a skin cluster on the target mesh
    skin_cluster = cmds.skinCluster(joints, target_mesh, maximumInfluences=4, toSelectedBones=True)[0]

    # Transfer weights
    for source in source_meshes:
        cmds.copySkinWeights(ss=source, destinationSkin=skin_cluster, noMirror=True, surfaceAssociation='closestPoint')
    print("Skin weights transferred!")



joints = cmds.ls(selection=True)  
body_mesh = "group_Harley_0000_Harley_Queen_Geo_Harley_0000_Harley_Queen_Geo"  
#Create skin cage
cage_meshes = create_skin_cage(joints, body_mesh)

#Transfer skin weights to the body mesh
transfer_skin_weights(joints, cage_meshes, body_mesh)

#suppr cubes
cmds.delete(cage_meshes)