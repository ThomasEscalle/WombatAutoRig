import maya.cmds as cmds
import maya.mel as mel
import os
from wombatAutoRig.src.core import FileHelper

from PySide2.QtGui import QImage



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


    # Create a 96x96 icon for the controller and save it to a file
    iconPath = controllerPath + ".png"
    # Create a empty 96x96 icon for the controller
    icon = QImage(96, 96, QImage.Format_ARGB32) 
    # Save the icon to a file
    icon.save(iconPath, "PNG")



    print("Controller saved: " + controllerPath)




# Load a controller from a file and create it in the scene
# @param controllerName: The name of the controller to load
# @param name: The name of the controller to create
# @return: The created controller
def createController(controllerName , name = ""):
    # Check if the controller exists
    controllerPath = controllerName

    if not os.path.exists(controllerPath):
        controllerPath = FileHelper.getControllersPath() + "/" + controllerName + ".ctrl.txt"
        
        if not os.path.exists(controllerPath):
            print("Controller not found: " + controllerName)
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
    # Get the maximum of the width, height and depth
    maximum = max(width, height, depth)

    # Get the parent of the old controller
    parent = cmds.listRelatives(selection, parent=True)

    # Get the color of the shape of the old controller
    shapes = cmds.listRelatives(selection, shapes=True)
    color = cmds.getAttr(shapes[0] + ".overrideColorRGB")

    # Get the rotation of the old controller
    rotation = cmds.xform(selection, query=True, rotation=True)

    # Delete the old controller
    selectionName = selection.split("|")[-1]
    cmds.delete(selection)
    
    # Create the new controller
    newController = createController(controllerName, name=selectionName)

    if newController is None:
        print("Error creating controller")
        return

    # Get the BBox of the created controller
    createdBBox = cmds.xform(newController, query=True, boundingBox=True)
    # Get the width, height and depth of the created controller
    createdWidth = createdBBox[3] - createdBBox[0]
    createdHeight = createdBBox[4] - createdBBox[1]
    createdDepth = createdBBox[5] - createdBBox[2]
    createdMaximum = max(createdWidth, createdHeight, createdDepth)



    
    # Scale the new controller to match the size of the old one
    scaleValue = maximum / createdMaximum
    cmds.scale(scaleValue, scaleValue, scaleValue, newController)
    

    # Get the position of the old controller from the center of the bounding box
    position = bbox[0] + width / 2, bbox[1] + height / 2, bbox[2] + depth / 2
    # Move the new controller to the position of the old one
    cmds.move(position[0], position[1], position[2], newController)

    color = list(color)
    color = list(color[0])

    # Set the color of the shape of the new controller
    shapes = cmds.listRelatives(newController, shapes=True)
    for shape in shapes:
        cmds.setAttr(shape + ".overrideEnabled", 1)
        cmds.setAttr(shape + ".overrideRGBColors", 1)
        cmds.setAttr(shape + ".overrideColorRGB", color[0], color[1], color[2])
    



    # Rotate the new controller to match the rotation of the old one
    cmds.rotate(rotation[0], rotation[1], rotation[2], newController)

    # Parent the new controller to the old parent
    if parent is not None:
        cmds.parent(newController, parent)




    # Select the new controller
    cmds.select(newController)


    pass