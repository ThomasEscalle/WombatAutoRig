# Offset

```python
from wombatAutoRig.src.core import Offset
```
Source: [Colors.py](https://github.com/ThomasEscalle/WombatAutoRig/blob/main/src/core/Offset.py)


## Description

This module provides a function to create an offset group for an object or a list of objects. The offset group is a group that is created and parented to the object. The object is then parented to the offset group. This allows the object to be moved without affecting its children.

## Usage

```python
from wombatAutoRig.src.core import Offset

### Create an offset group for the object
Offset.offset("locator")

### Create an offset, move , and hook
Offset.offset("locator", nbr = 3)
```

## Detailed Description

### offset(obj, nbr=1) : None
Create an offset group for the object. The offset group is a group that is created and parented to the object. The object is then parented to the offset group. This allows the object to be moved without affecting its children.

Parameters:
- **obj**: list of objects to create an offset group for, or a single object
- **nbr**: number of offset groups to create. The offset groups are parented to each other. Default is 1.

Returns:
- Nothing