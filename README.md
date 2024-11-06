# Wombat AutoRig

## Description
Wombat AutoRig is a tool for automatically rigging 3D models in maya.

## Installation
1. Download the repository as a zip file, or clone it using git to your local machine.
2. Navigate to your maya scripts directory. On windows, this is usually located at `C:\Users\USERNAME\Documents\maya\VERSION\scripts`.
3. Place the "WombatAutoRig-main" folder into the maya script folder
4. Rename the "WombatAutoRig-main" folder to "wombatAutoRig"
5. Open maya and run the following python code in the script editor to run the tool:
```python
from wombatAutoRig import wombatAutoRig
wombatAutoRig.run()
```





## Documentation

- [Color](https://github.com/ThomasEscalle/WombatAutoRig/blob/main/docs/Colors.md)
- [Offset](https://github.com/ThomasEscalle/WombatAutoRig/blob/main/docs/Offset.md)
- [Preferences](https://github.com/ThomasEscalle/WombatAutoRig/blob/main/docs/Preferences.md)
- [Ribbon](https://github.com/ThomasEscalle/WombatAutoRig/blob/main/docs/Ribbon.md)




AutoRig_Data
    JointsPlacement
    ControllersPlacement
        IK_Controllers
        FK_Controllers