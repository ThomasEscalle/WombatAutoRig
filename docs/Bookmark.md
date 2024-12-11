# Bookmark

```python
from wombatAutoRig.src.core import Bookmark
```
Source: [Bookmark.py](https://github.com/ThomasEscalle/WombatAutoRig/blob/main/src/core/Bookmark.py)

## Description 

This module allow the creation of maya bookmarks in the node editor. It is used to save the layout of the node editor and restore it later.

## Usage


```python
from wombatAutoRig.src.core import Bookmark

### Example Usage ###
Bookmark.createBookmark("MyBookmark")

# Add a node to the bookmark
Bookmark.addNodeToBookmark("MyBookmark", "pCube1")

# Add another node to the bookmark at a specific position
Bookmark.addNodeToBookmark("MyBookmark", "pCube2", xPos=300, yPos=-300)

# Add another node to the bookmark in a specific column
Bookmark.addNodeToBookmark("MyBookmark", "pCube3", column=1)

# Add another node to the bookmark in a specific row and column
Bookmark.addNodeToBookmark("MyBookmark", "pCube4", row=1, column=1)

```