from maya import cmds



# Create a folder hierarchy for the rig looking like this:
# <name>
#    <name>_Geo
#    GlobalMove_01
#       Joints_01
#       IKs_01
#       CTRLs_01
#    RelaySystem_01
#    Extra_Nodes_01
#       Extra_Nodes_To_Show_01
#       Extra_Nodes_To_Hide_01
def createDefaultFolder(name):
    # Remove the group if it already exists
    if cmds.objExists(name):
        cmds.delete(name)

    cmds.group(name=name, empty=True)
    cmds.group(name=name + "_Geo", empty=True, parent=name)
    cmds.group(name="GlobalMove_01", empty=True, parent=name)
    cmds.group(name="Joints_01", empty=True, parent="GlobalMove_01")
    cmds.group(name="IKs_01", empty=True, parent="GlobalMove_01")
    cmds.group(name="CTRLs_01", empty=True, parent="GlobalMove_01")
    cmds.group(name="RelaySystem_01", empty=True, parent=name)
    cmds.group(name="Extra_Nodes_01", empty=True, parent=name)
    cmds.group(name="Extra_Nodes_To_Show_01", empty=True, parent="Extra_Nodes_01")
    cmds.group(name="Extra_Nodes_To_Hide_01", empty=True, parent="Extra_Nodes_01")


# Create a folder hierarchy for the autorig looking like this:
# AutoRig_Data
#    JointsPlacement
#    ControllersPlacement
#        IK_Controllers
#        FK_Controllers
def createDefaultAutorigFolder(name):
    # Remove the group if it already exists
    if cmds.objExists("AutoRig_Data"):
        cmds.delete("AutoRig_Data")

    cmds.group(name="AutoRig_Data", empty=True)
    cmds.group(name="JointsPlacement", empty=True, parent="AutoRig_Data")
    cmds.group(name="ControllersPlacement", empty=True, parent="AutoRig_Data")
    cmds.group(name="IK_Controllers", empty=True, parent="ControllersPlacement")
    cmds.group(name="FK_Controllers", empty=True, parent="ControllersPlacement")
    cmds.group(name="Other_Controllers", empty=True, parent="ControllersPlacement")
    cmds.group(name="Global_Controllers", empty=True, parent="ControllersPlacement")

    # Hide the controllers by default
    cmds.hide("AutoRig_Data|ControllersPlacement")
    # Hide the Fk controllers by default
    cmds.hide("AutoRig_Data|ControllersPlacement|FK_Controllers")
    cmds.hide("AutoRig_Data|ControllersPlacement|Other_Controllers")


# Remove the Autorig folder
def removeDefaultAutorigFolder(name):
    if cmds.objExists("AutoRig_Data"):
        cmds.delete("AutoRig_Data")



# Take all the joints in the scene and disable the local rotation axis
def disableLocalRotationAxis():
    joints = cmds.ls(type="joint")
    for jnt in cmds.ls(type="joint"):
        # Check if the LRA is visible
        if cmds.getAttr(jnt + ".displayLocalAxis"):
            cmds.setAttr(jnt + ".displayLocalAxis", 0)


# Make the given list of elements template
def makeTemplate(elements, state = 1):
    for element in elements:
        cmds.setAttr(element + ".template", state)

def hideJointsPlacement(state = 1):
    cmds.setAttr("AutoRig_Data|JointsPlacement.visibility", not state)

def hideControllersPlacement(state = 1):
    cmds.setAttr("AutoRig_Data|ControllersPlacement.visibility", not state)

# Save the settings object into a string attribute on a group named "AutoRig_Data"
def saveSettings(settings) : 
    # Remove the attribute if it already exists
    if cmds.attributeQuery("settings", node="AutoRig_Data", exists=True):
        cmds.deleteAttr("AutoRig_Data.settings")

    # Save the settings object into an attribute as json on the "AutoRig_Data" node (group)
    cmds.addAttr("AutoRig_Data", longName="settings", dataType="string")
    cmds.setAttr("AutoRig_Data.settings", str(settings), type="string")

# Load the settings object from the "AutoRig_Data" node (group)
def loadSettings():
    # Load the settings object from the "AutoRig_Data" node (group)
    if cmds.attributeQuery("settings", node="AutoRig_Data", exists=True):
        settings = cmds.getAttr("AutoRig_Data.settings")
        return eval(settings)
    else:
        return None


def resizeJnts(bbox, size):
    referenceSizeY = 170
    sizeY = bbox[4] - bbox[1]
    
    sizeList = list(size)

    sizeList[0] = sizeList[0] * (sizeY / referenceSizeY)
    sizeList[1] = sizeList[1] * (sizeY / referenceSizeY)
    sizeList[2] = sizeList[2] * (sizeY / referenceSizeY)

    return tuple(sizeList)

def resizeCtrl(bbox, size):
    referenceSizeY = 166
    sizeY = bbox[4] - bbox[1]

    sizeList = list(size)

    sizeList[0] = sizeList[0] * (sizeY / referenceSizeY)
    sizeList[1] = sizeList[1] * (sizeY / referenceSizeY)
    sizeList[2] = sizeList[2] * (sizeY / referenceSizeY)

    return tuple(sizeList)

# Add a suffix to all the children of the given node
def addSuffixRecursive(node, suffix):
    children = cmds.listRelatives(node, children=True, fullPath=True)
    print(children)
    if children:
        for child in children:
            addSuffixRecursive(child, suffix)
    cmds.rename(node, node.split("|")[-1] + suffix)

# Remove a suffix from all the children of the given node
def removeSuffixRecursive(node, suffix):
    children = cmds.listRelatives(node, children=True, fullPath=True)
    if children:
        for child in children:
            removeSuffixRecursive(child, suffix)
    cmds.rename(node, node.split("|")[-1].replace(suffix, ""))