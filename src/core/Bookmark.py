import maya.cmds as cmds

"""
Maya Bookmark Utility

### Example Usage ###
createBookmark("MyBookmark")

# Add a node to the bookmark
addNodeToBookmark("MyBookmark", "pCube1")

# Add another node to the bookmark at a specific position
addNodeToBookmark("MyBookmark", "pCube2", xPos=300, yPos=-300)

# Add another node to the bookmark in a specific column
addNodeToBookmark("MyBookmark", "pCube3", column=1)

# Add another node to the bookmark in a specific row and column
addNodeToBookmark("MyBookmark", "pCube4", row=1, column=1)

"""


def createBookmark(bookmark_name="Untitled_1"):
    """
    Creates a bookmark in the Maya Node Editor with the specified name.
    This function sets up a bookmark and stores its tab information.
    @param bookmark_name: The name of the bookmark to create.
    """

    # Check if a bookmark with the same name already exists
    if cmds.objExists(bookmark_name):
        cmds.warning("Bookmark with name '{}' already exists.".format(bookmark_name))
        return

    # Create a bookmark node
    bookmark_node = cmds.createNode("nodeGraphEditorBookmarkInfo", name=bookmark_name)
    cmds.setAttr(bookmark_node + ".nm", bookmark_name, type="string")

    # Set the size of the bookmark
    size = 600
    cmds.setAttr(bookmark_node + ".vl", -size, -size, type="double2")
    cmds.setAttr(bookmark_node + ".vh", size, size, type="double2")

    return bookmark_node


def addNodeToBookmark(bookmark_node, node_name , column = 0 , row = None , xPos = None , yPos = None):
    """
    Adds a node to the specified bookmark in the Maya Node Editor.

    @param bookmark_node: The name of the bookmark to add the node to.
    @param node_name: The name of the node to add to the bookmark.
    @param column: The column index of the node in the bookmark. Default is 0.
    @param row: The row index of the node in the bookmark. Default is None. If None, the node will be placed below the last node in the bookmark.
    @param xPos: The x position of the node in the bookmark. Default is None. If None, the node will be placed at the default x position.
    @param yPos: The y position of the node in the bookmark. Default is None. If None, the node will be placed at the default y position.
    """

    # Get the number of elements connected to the bookmark node (bookmark_node.ni)
    num_elements = cmds.getAttr(bookmark_node + ".ni", size=True)

    # connectAttr "nurbsCircleShape1.msg" "nodeView1.ni[0].dn";
    cmds.connectAttr(node_name + ".message", bookmark_node + ".ni[{}].dn".format(num_elements), force=True)

    xSpacing = 300
    ySpacing = -550

    x = xSpacing * column
    if row is None:
        y = ySpacing * num_elements
    else:
        y = ySpacing * row

    if xPos != None:
        x = xPos
    if yPos != None:
        y = yPos
    
    # Set the position of the node in the bookmark
    cmds.setAttr(bookmark_node + ".ni[{}].x".format(num_elements), x)
    cmds.setAttr(bookmark_node + ".ni[{}].y".format(num_elements), y)

    # Set the visual state of the node (0: Small, 1: Medium, 2: Full)
    cmds.setAttr(bookmark_node + ".ni[{}].nvs".format(num_elements), 2)





