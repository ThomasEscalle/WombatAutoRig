# Maya script to create custom controllers for an auto-rigging system.
from maya import cmds

def createMaterialsIfNotExists():
    # Check if the project contains a lambert node named 'thLambert_Yellow'
    if not cmds.objExists('thLambert_Yellow'):
        # Create a new lambert shader named 'thLambert_Yellow'
        cmds.shadingNode('lambert', asShader=True, name='thLambert_Yellow')
        # Set the color of the shader to yellow
        cmds.setAttr('thLambert_Yellow.incandescence', 1, 1, 0, type='double3')
        cmds.setAttr('thLambert_Yellow.color', 0, 0, 0, type='double3')

    # Check if the project contains a lambert node named 'thLambert_Red'
    if not cmds.objExists('thLambert_Red'):
        # Create a new lambert shader named 'thLambert_Red'
        cmds.shadingNode('lambert', asShader=True, name='thLambert_Red')
        # Set the color of the shader to red
        cmds.setAttr('thLambert_Red.incandescence', 1, 0, 0, type='double3')
        cmds.setAttr('thLambert_Red.color', 0, 0, 0, type='double3')

    # Check if the project contains a lambert node named 'thLambert_Blue'
    if not cmds.objExists('thLambert_Blue'):
        # Create a new lambert shader named 'thLambert_Blue'
        cmds.shadingNode('lambert', asShader=True, name='thLambert_Blue')
        # Set the color of the shader to blue
        cmds.setAttr('thLambert_Blue.incandescence', 0, 0, 1, type='double3')
        cmds.setAttr('thLambert_Blue.color', 0, 0, 0, type='double3')

    # Check if the project contains a lambert node named 'thLambert_Green'
    if not cmds.objExists('thLambert_Green'):
        # Create a new lambert shader named 'thLambert_Green'
        cmds.shadingNode('lambert', asShader=True, name='thLambert_Green')
        # Set the color of the shader to green
        cmds.setAttr('thLambert_Green.incandescence', 0, 1, 0, type='double3')
        cmds.setAttr('thLambert_Green.color', 0, 0, 0, type='double3')

    # Check if the project contains a lambert node named 'thLambert_Cyan'
    if not cmds.objExists('thLambert_Cyan'):
        # Create a new lambert shader named 'thLambert_Cyan'
        cmds.shadingNode('lambert', asShader=True, name='thLambert_Cyan')
        # Set the color of the shader to cyan
        cmds.setAttr('thLambert_Cyan.incandescence', 0, 1, 1, type='double3')
        cmds.setAttr('thLambert_Cyan.color', 0, 0, 0, type='double3')




def createControllerSphere(pos, scale = 1 ,name = "controller"):
    print("Creating controller at position: {0}".format(pos))

    # Create a sphere of radius 1 at position 0,0,0 with 12 subdivisions
    sphere = cmds.polySphere(radius=1, name=name, subdivisionsX=12, subdivisionsY=12)

    createMaterialsIfNotExists()

    # Assign the yellow material to the sphere
    cmds.select(sphere)
    cmds.hyperShade(assign='thLambert_Cyan')

    # Move the controller to the specified position
    cmds.move(pos[0], pos[1], pos[2])
    cmds.scale(scale, scale, scale)

    return name

def createController(pos, scale = 1 ,name = "controller", localRotation = [0, 0, 0]):
    print("Creating controller at position: {0}".format(pos))

    # Create a sphere of radius 1 at position 0,0,0 with 12 subdivisions
    sphere = cmds.polySphere(radius=1, name="controller", subdivisionsX=12, subdivisionsY=12)

    # Create a polyCone with radius 0.5, height 2, and subdivisions 12
    cone_Y = cmds.polyCone(radius=0.5, height=2, name="controller_cone_Y", subdivisionsX=12)
    cmds.move(0, 1.5, 0)

    # Create a polyCone with radius 0.5, height 2, and subdivisions 12
    cone_X = cmds.polyCone(radius=0.5, height=2, name="controller_cone_X", subdivisionsX=12)
    cmds.rotate(180, 0, 90)
    cmds.move(1.5, 0, 0)

    # Create a polyCone with radius 0.5, height 2, and subdivisions 12
    cone_Z = cmds.polyCone(radius=0.5, height=2, name="controller_cone_Z", subdivisionsX=12)
    cmds.rotate(90, 0, 0)
    cmds.move(0, 0, 1.5)

    createMaterialsIfNotExists()

    # Assign the yellow material to the sphere
    cmds.select(sphere)
    cmds.hyperShade(assign='thLambert_Yellow')

    # Assign the red material to the cone_X
    cmds.select(cone_X)
    cmds.hyperShade(assign='thLambert_Red')

    # Assign the green material to the cone_Y
    cmds.select(cone_Y)
    cmds.hyperShade(assign='thLambert_Green')

    # Assign the blue material to the cone_Z
    cmds.select(cone_Z)
    cmds.hyperShade(assign='thLambert_Blue')

    # Merge all the objects into a single object
    cmds.select(sphere, cone_X, cone_Y, cone_Z)
    cmds.polyUnite(name="controller")
    # Delete the historique
    cmds.delete(ch=True)

    # Move the controller to the specified position
    cmds.move(pos[0], pos[1], pos[2])
    cmds.scale(scale, scale, scale)
    cmds.rotate(localRotation[0], localRotation[1], localRotation[2])

    # Rename the controller
    cmds.rename(name)

    return name
    

def connectLine(object0, object1, name="line", width = 4 ):
    # Create a curve with two points
    curve = cmds.curve(d=1, p=[(0, 0, 0), (0, 0, 0)], k=[0, 1], name=name)

    # Connect the object's position to the curve's points
    cmds.connectAttr(object0 + ".translate", curve + ".controlPoints[0]")
    cmds.connectAttr(object1 + ".translate", curve + ".controlPoints[1]")

    # Set the line width of the shape
    cmds.setAttr(curve + ".lineWidth", width)

    # Set the object to template so it is not selectable
    cmds.setAttr(curve + ".template", 1)

    return curve


groupWIP = cmds.group(name='WIP', empty=True)

createController(pos=(4.125,9.609,-0.318),name='Ankle_L')
createController(pos=(-4.125,9.609,-0.318),name='Ankle_R')
createController(pos=(4.366,2.707,4.391),name='Ball_L')
createController(pos=(-4.366,2.707,4.391),name='Ball_R')
createController(pos=(4.411,1.428,8.568),name='Toe_L')
createController(pos=(-4.411,1.428,8.568),name='Toe_R')
createController(pos=(4.299,28.693,0.09),name='Knee_L')
createController(pos=(-4.299,28.693,0.09),name='Knee_R')

cmds.parent('Ankle_L','Ankle_R','Ball_L','Ball_R','Toe_L','Toe_R','Knee_L','Knee_R', groupWIP)