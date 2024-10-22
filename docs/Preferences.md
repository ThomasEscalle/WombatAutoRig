# Preferences

```python
from wombatAutoRig.src.core.Preferences import Preferences
```
Source: [Preferences.py](../src/core/Colors.py)


## Description
The Preferences class is used to store user preferences in a JSON file. 
It has methods to load, save, get, and set preferences.

The file is saved in the root of the script directory :
``C:\Users\USERNAME\Documents\maya\VERSION\scripts\wombatAutoRig\preferences.json``

## Usage
    
```python
from wombatAutoRig.src.core.Preferences import Preferences

# Create a preference object, the file is automatically loaded
prefs = Preferences.Preferences()

# Set a preference, the file is automatically saved
prefs.set("key", 125)
prefs.set("key_2", {"name": "John", "age": 30} )

# Get a preference
value_0 = prefs.get("key")
value_1 = prefs.get("key_2", "default_value")
```	


## Detailed Description

### Preferences() : None
Parameters:
- None

Returns:
- None

----------------------------------------------------------------------------------------------------------------------------

### set(key, value) : None

Set a value associated with a key.

Parameters:
- **key**: key to set the value
- **value**: value to set

Returns:
- None

----------------------------------------------------------------------------------------------------------------------------

### get(key, default=None) : value

Get the value associated with a key.

Parameters:
- **key**: key to get the value
- **default**: default value if the key does not exist, default is None

Returns:
- The value associated with the key, or the default value if the key does not exist

----------------------------------------------------------------------------------------------------------------------------

### load() : None

Save the preferences to the file. This function is called automatically when the object is created.
Parameters:
- None

Returns:
- None


----------------------------------------------------------------------------------------------------------------------------

### save() : None

Load the preferences from the file. This function is called automatically a preference is set.

Parameters:
- None

Returns:
- None