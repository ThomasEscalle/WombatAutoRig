#### Script to apply colors to maya objects
import maya.cmds as cmds
from wombatAutoRig.src.core.Preferences import Preferences


# Get the hexadecimal value of a color
# @param color: color name, string
def getHexColor(color):
   if color == "white" : 
      return "#FFFFFF"
   if color == "pink" : 
      return "#F9BFCB"
   if color == "crimson" : 
      return "#DD1E3F"
   if color == "red" : 
      return "#ED1E24"
   if color == "maroon" : 
      return "#7E1416"
   if color == "brown" : 
      return "#A62A2A"
   if color == "misty" : 
      return "#FCE3DF"
   if color == "salmon" : 
      return "#F57F73"
   if color == "coral" : 
      return "#F47D52"
   if color == "orange-red" : 
      return "#F14924"
   if color == "chocolate" : 
      return "#D36A28"
   if color == "dark-gray" : 
      return "#AAAAAA"
   if color == "orange" : 
      return "#FFA419"
   if color == "gold" : 
      return "#E4BD20"
   if color == "ivory" : 
      return "#FAF9E5"
   if color == "yellow" : 
      return "#F7EC14"
   if color == "olive" : 
      return "#6B692C"
   if color == "yellow-green" : 
      return "#9AC93B"
   if color == "lawn-green" : 
      return "#91C73E"
   if color == "lime" : 
      return "#69BD44"
   if color == "green" : 
      return "#10813F"
   if color == "spring-green" : 
      return "#71C16A"
   if color == "gray" : 
      return "#696969"
   if color == "aqua-marine" : 
      return "#99D4C0"
   if color == "turquoise" : 
      return "#63C6C1"
   if color == "azure" : 
      return "#DEF2F3"
   if color == "aqua" : 
      return "#6FCCDD"
   if color == "teal" : 
      return "#008181"
   if color == "lavender" : 
      return "#D9D7EC"
   if color == "blue" : 
      return "#3853A4"
   if color == "navy" : 
      return "#272974"
   if color == "blue-violet" : 
      return "#7651A1"
   if color == "black" : 
      return "#000000"
   if color == "indigo" : 
      return "#4E2A7C"
   if color == "dark-violet" : 
      return "#80469B"
   if color == "plum" : 
      return "#D4A2C8"
   if color == "magenta" : 
      return "#B9539F"
   if color == "purple" : 
      return "#7D277E"
   if color == "red-violet" : 
      return "#C71784"
   if color == "tan" : 
      return "#D1B48C"
   if color == "slate-gray" : 
      return "#6F7F8F"
   if color == "dark-slate-gray" : 
      return "#2F4F4E"
   if color == "light-gray" : 
      return "#D3D3D3"
   
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