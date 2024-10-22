#### Script to apply colors to maya objects
import maya.cmds as cmds


# Set the color of an object
# @param obj: list of objects to color, or a single object
# @param color: color to apply to the object , string (hexadecimal or color name)
def setColor(obj, color):
