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
    pass


createController("test_2222")