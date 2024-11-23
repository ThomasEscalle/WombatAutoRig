import maya.cmds as cmds
import maya.mel as mel
import os
from wombatAutoRig.src.core import FileHelper




### Save the selected curve to a file as a controller 
# @param controllerName: The name of the controller to save
def saveController(controllerName):

    selection = cmds.ls(selection=True)
    commands = []

    for curve in selection:
        cv_array = cmds.getAttr(curve + ".cv[*]")
        degree = cmds.getAttr(curve + ".degree")
        form = cmds.getAttr(curve + ".form")

        command = "curve -d " + str(degree)

        for i in range(len(cv_array)):
            command += " -p " + " ".join(map(str, cv_array[i]))

        if form == 2:  # periodic
            knots = cmds.getAttr(curve + ".knots[0:" + str(degree) + "]")
            command += " -k " + " ".join(map(str, knots))

        commands.append(command)
    
    if len(commands) == 0:
        print("No curves selected")
        return
    
    # Save the controller to a file
    controllerPath = FileHelper.getControllersPath() + "/" + controllerName + ".ctrl.txt"
    with open(controllerPath, "w") as file:
        for command in commands:
            file.write(command + "\n")

    print("Controller saved: " + controllerPath)




# Load a controller from a file and create it in the scene
# @param controllerName: The name of the controller to load
# @param name: The name of the controller to create
# @return: The created controller
def createController(controllerName , name = ""):
    # Check if the controller exists
    controllerPath = FileHelper.getControllersPath() + "/" + controllerName + ".ctrl.txt"

    if not os.path.exists(controllerPath):
        print("Controller not found: " + controllerPath)
        return
    
    commands = []
    # Load the controller from the file
    with open(controllerPath, "r") as file:
        commands = file.readlines()

    for command in commands:
        # Evaluate the mel command
        mel.eval(command)

        # Rename the controller
        if name != "":
            cmds.rename(name)


    sel = cmds.ls(selection=True)
    return sel[0] if len(sel) > 0 else None


# Replace the selected controller with a new one, at the same location
# @param controllerName: The name of the controller to replace
def replaceController(controllerName):

    print("Replace controller: " + controllerName)
    # Get the selected controller
    selection = cmds.ls(selection=True)

    if len(selection) == 0:
        print("No controller selected")
        return

    selection = selection[0]

    # Get the bounding box of the controller
    bbox = cmds.xform(selection, query=True, boundingBox=True)
    # Get the width, height and depth of the controller
    width = bbox[3] - bbox[0]
    height = bbox[4] - bbox[1]
    depth = bbox[5] - bbox[2]

    maximum = max(width, height, depth)

    parent = cmds.listRelatives(selection, parent=True)

    # Delete the old controller
    cmds.delete(selection)

    # Create the new controller
    newController = createController(controllerName, name=selection)

    if newController is None:
        print("Error creating controller")
        return
    
    # Scale the new controller to match the size of the old one
    cmds.scale(maximum / 2, maximum / 2, maximum / 2, newController)

    # Get the position of the old controller from the center of the bounding box
    position = bbox[0] + width / 2, bbox[1] + height / 2, bbox[2] + depth / 2
    # Move the new controller to the position of the old one
    cmds.move(position[0], position[1], position[2], newController)

    # Get the rotation of the old controller
    rotation = cmds.xform(selection, query=True, rotation=True)
    # Rotate the new controller to match the rotation of the old one
    cmds.rotate(rotation[0], rotation[1], rotation[2], newController)

    # Parent the new controller to the old parent
    if parent is not None:
        cmds.parent(newController, parent)

    # Select the new controller
    cmds.select(newController)


    pass