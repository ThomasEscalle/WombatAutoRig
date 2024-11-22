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


# Remove the Autorig folder
def removeDefaultAutorigFolder(name):
    if cmds.objExists("AutoRig_Data"):
        cmds.delete("AutoRig_Data")


# Make the given list of elements template
def makeTemplate(elements, state = 1):
    for element in elements:
        cmds.setAttr(element + ".template", state)

