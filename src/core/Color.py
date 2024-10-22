#### Script to apply colors to maya objects
import maya.cmds as cmds
from wombatAutoRig.src.core.Preferences import Preferences


# Get the hexadecimal value of a color
# @param color: color name, string
def getHexColor(color):
    if color == "white": 
       return "#FFFFFF"
    if color == "pink": 
       return "#FFC0CB"
    if color == "crimson": 
       return "#DC143C"
    if color == "red": 
       return "#FF0000"
    if color == "maroon": 
       return "#800000"
    if color == "brown": 
       return "#A52A2A"
    if color == "misty": 
       return "#FFE4E1"
    if color == "salmon": 
       return "#FA8072"
    if color == "coral": 
       return "#FF7F50"
    if color == "orange-red": 
       return "#FF4500"
    if color == "chocolate": 
       return "#D2691E"
    if color == "dark-gray": 
       return "#A9A9A9"
    if color == "orange": 
       return "#FFA500"
    if color == "gold": 
       return "#FFD700"
    if color == "ivory": 
       return "#FFFFF0"
    if color == "yellow": 
       return "#FFFF00"
    if color == "olive": 
       return "#808000"
    if color == "yellow-green": 
       return "#9ACD32"
    if color == "lawn-green": 
       return "#7CFC00"
    if color == "lime": 
       return "#00FF00"
    if color == "green": 
       return "#008000"
    if color == "spring-green": 
       return "#00FF7F"
    if color == "gray": 
       return "#808080"
    if color == "aqua-marine": 
       return "#7FFFD4"
    if color == "turquoise": 
       return "#40E0D0"
    if color == "azure": 
       return "#007FFF"
    if color == "aqua": 
       return "#00FFFF"
    if color == "teal": 
       return "#008080"
    if color == "lavender": 
       return "#E6E6FA"
    if color == "blue": 
       return "#0000FF"
    if color == "navy": 
       return "#000080"
    if color == "blue-violet": 
       return "#8A2BE2"
    if color == "black": 
       return "#000000"
    if color == "indigo": 
       return "#4B0082"
    if color == "dark-violet": 
       return "#9400D3"
    if color == "plum": 
       return "#DDA0DD"
    if color == "magenta": 
       return "#FF00FF"
    if color == "purple": 
       return "#800080"
    if color == "red-violet": 
       return "#C71585"
    if color == "tan": 
       return "#D2B48C"
    if color == "slate-gray": 
       return "#708090"
    if color == "dark-slate-gray": 
       return "#2F4F4F"
    if color == "light-gray": 
       return "#D3D3D3"
    return ""

# Set the color of an object
# @param obj: list of objects to color, or a single object
# @param color: color to apply to the object , string (hexadecimal or color name)
#
# Possible colors are listed here : https://github.com/ThomasEscalle/WombatAutoRig/blob/main/docs/Colors.md
def setColor(obj, color ):

    # If the color is empty, we return
    if color == "":
        print("Invalid color : " + color)
        return

    # If the color doesnt start with #, we get the hexadecimal value
    if color[0] != "#":
        color = getHexColor(color)

    # If the color is not valid (size != 7), we return
    if len(color) != 7:
        print("Invalid color : " + color)
        return
    
    # If the object is a list, we iterate over it
    # and call the function recursively
    if type(obj) == list:
        for o in obj:
            setColor(o, color)
        return
    
    # Get the color as RGB
    r = int(color[1:3], 16) / 255
    g = int(color[3:5], 16) / 255
    b = int(color[5:7], 16) / 255

    # Round the values
    r = round(r, 3)
    g = round(g, 3)
    b = round(b, 3)

    # Convert the color to display space
    colorV = [r , g , b]
    colorVdp = cmds.colorManagementConvert(toDisplaySpace=[colorV[0], colorV[1], colorV[2]])


    # Set the color in the viewport
    cmds.setAttr(obj + ".overrideEnabled", 1)
    cmds.setAttr(obj + ".overrideRGBColors", 1)
    cmds.setAttr(obj + ".overrideColorRGB", colorV[0], colorV[1], colorV[2])

    # Color in the outliner
    cmds.setAttr(obj + ".useOutlinerColor", 1)
    cmds.setAttr(obj + ".outlinerColor", colorVdp[0], colorVdp[1], colorVdp[2])


    # Get the shapes of the object
    shapes = cmds.listRelatives(obj, shapes=True)

    # If the object has shapes, we color them
    if shapes is not None:
        for shape in shapes:
            cmds.setAttr(shape + ".overrideEnabled", 1)
            cmds.setAttr(shape + ".overrideRGBColors", 1)
            cmds.setAttr(shape + ".overrideColorRGB", colorV[0], colorV[1], colorV[2])



# Set the default color of an object by it's type
# @param obj: object to color, or a list of objects
# @param type: type of the object, string
def setDefaultColor(obj, type):
   prefs = Preferences()
   defaultColors = prefs.get("defaultColors", {})
   
   if type in defaultColors:
      setColor(obj, defaultColors[type])




def test():
   selected = cmds.ls(selection=True)
   setDefaultColor(selected, "DrvJnt")

test()