# Colors
```python
import wombatAutoRig.src.core.Colors as Colors
```
Source: [Colors.py](https://github.com/ThomasEscalle/WombatAutoRig/blob/main/src/core/Color.py)

## Description

This module provides a function to set the color of an object or a list of objects. The color can be set by name or by hexadecimal value. The list of available colors is provided below.

## Usage

```python
import wombatAutoRig.src.core.Colors as Colors

### Set the color of the object to red
Colors.setColor("locator", "red")

### Apply to the locator the default color for the DrvJnt saved in the preferences
Colors.setDefaultColor("locator", "DrvJnt")
```



## Detailed Description

### setColor(obj, color) : None
Set the color of the object to the specified color. The color can be set by name or by hexadecimal value.

Parameters:
- **obj**: list of objects to color, or a single object
- **color**: color to set to the object, name or hexadecimal (e.g. "red" or "#FF0000")

Returns: 
- Nothing


### setDefaultColor(obj, type) : None
Set the color of the object to the default color for the specified type. 
The color can be set by name or by hexadecimal value.
The color is saved in the preferences.json file.

Parameters:
- **obj**: list of objects to color, or a single object.
- **type**: type of object to color, the way it is saved in the preferences.json file.

Returns:
- Nothing



## Color list :

| Name             | Identifier       | Hex       |
|------------------|------------------|-----------|
| ![#FFFFFF](https://placehold.co/15x15/FFFFFF/FFFFFF.png) White        | white            | `#FFFFFF` |
| ![#FFC0CB](https://placehold.co/15x15/FFC0CB/FFC0CB.png) Pink         | pink             | `#FFC0CB` |
| ![#DC143C](https://placehold.co/15x15/DC143C/DC143C.png) Crimson      | crimson          | `#DC143C` |
| ![#FF0000](https://placehold.co/15x15/FF0000/FF0000.png) Red          | red              | `#FF0000` |
| ![#800000](https://placehold.co/15x15/800000/800000.png) Maroon       | maroon           | `#800000` |
| ![#A52A2A](https://placehold.co/15x15/A52A2A/A52A2A.png) Brown        | brown            | `#A52A2A` |
| ![#FFE4E1](https://placehold.co/15x15/FFE4E1/FFE4E1.png) Misty        | misty            | `#FFE4E1` |
| ![#FA8072](https://placehold.co/15x15/FA8072/FA8072.png) Salmon       | salmon           | `#FA8072` |
| ![#FF7F50](https://placehold.co/15x15/FF7F50/FF7F50.png) Coral        | coral            | `#FF7F50` |
| ![#FF4500](https://placehold.co/15x15/FF4500/FF4500.png) Orange Red   | orange-red       | `#FF4500` |
| ![#D2691E](https://placehold.co/15x15/D2691E/D2691E.png) Chocolate    | chocolate        | `#D2691E` |
| ![#A9A9A9](https://placehold.co/15x15/A9A9A9/A9A9A9.png) Dark Gray    | dark-gray        | `#A9A9A9` |
| ![#FFA500](https://placehold.co/15x15/FFA500/FFA500.png) Orange       | orange           | `#FFA500` |
| ![#FFD700](https://placehold.co/15x15/FFD700/FFD700.png) Gold         | gold             | `#FFD700` |
| ![#FFFFF0](https://placehold.co/15x15/FFFFF0/FFFFF0.png) Ivory        | ivory            | `#FFFFF0` |
| ![#FFFF00](https://placehold.co/15x15/FFFF00/FFFF00.png) Yellow       | yellow           | `#FFFF00` |
| ![#808000](https://placehold.co/15x15/808000/808000.png) Olive        | olive            | `#808000` |
| ![#9ACD32](https://placehold.co/15x15/9ACD32/9ACD32.png) Yellow Green | yellow-green     | `#9ACD32` |
| ![#7CFC00](https://placehold.co/15x15/7CFC00/7CFC00.png) Lawn Green   | lawn-green       | `#7CFC00` |
| ![#00FF00](https://placehold.co/15x15/00FF00/00FF00.png) Lime         | lime             | `#00FF00` |
| ![#008000](https://placehold.co/15x15/008000/008000.png) Green        | green            | `#008000` |
| ![#00FF7F](https://placehold.co/15x15/00FF7F/00FF7F.png) Spring Green | spring-green     | `#00FF7F` |
| ![#808080](https://placehold.co/15x15/808080/808080.png) Gray         | gray             | `#808080` |
| ![#7FFFD4](https://placehold.co/15x15/7FFFD4/7FFFD4.png) Aqua Marine  | aqua-marine      | `#7FFFD4` |
| ![#40E0D0](https://placehold.co/15x15/40E0D0/40E0D0.png) Turquoise    | turquoise        | `#40E0D0` |
| ![#007FFF](https://placehold.co/15x15/007FFF/007FFF.png) Azure        | azure            | `#007FFF` |
| ![#00FFFF](https://placehold.co/15x15/00FFFF/00FFFF.png) Aqua         | aqua             | `#00FFFF` |
| ![#008080](https://placehold.co/15x15/008080/008080.png) Teal         | teal             | `#008080` |
| ![#E6E6FA](https://placehold.co/15x15/E6E6FA/E6E6FA.png) Lavender     | lavender         | `#E6E6FA` |
| ![#0000FF](https://placehold.co/15x15/0000FF/0000FF.png) Blue         | blue             | `#0000FF` |
| ![#000080](https://placehold.co/15x15/000080/000080.png) Navy         | navy             | `#000080` |
| ![#8A2BE2](https://placehold.co/15x15/8A2BE2/8A2BE2.png) Blue Violet  | blue-violet      | `#8A2BE2` |
| ![#000000](https://placehold.co/15x15/000000/000000.png) Black        | black            | `#000000` |
| ![#4B0082](https://placehold.co/15x15/4B0082/4B0082.png) Indigo       | indigo           | `#4B0082` |
| ![#9400D3](https://placehold.co/15x15/9400D3/9400D3.png) Dark Violet  | dark-violet      | `#9400D3` |
| ![#DDA0DD](https://placehold.co/15x15/DDA0DD/DDA0DD.png) Plum         | plum             | `#DDA0DD` |
| ![#FF00FF](https://placehold.co/15x15/FF00FF/FF00FF.png) Magenta      | magenta          | `#FF00FF` |
| ![#800080](https://placehold.co/15x15/800080/800080.png) Purple       | purple           | `#800080` |
| ![#C71585](https://placehold.co/15x15/C71585/C71585.png) Red Violet   | red-violet       | `#C71585` |
| ![#D2B48C](https://placehold.co/15x15/D2B48C/D2B48C.png) Tan          | tan              | `#D2B48C` |
| ![#708090](https://placehold.co/15x15/708090/708090.png) Slate Gray   | slate-gray       | `#708090` |
| ![#2F4F4F](https://placehold.co/15x15/2F4F4F/2F4F4F.png) Dark Slate Gray | dark-slate-gray | `#2F4F4F` |
| ![#D3D3D3](https://placehold.co/15x15/D3D3D3/D3D3D3.png) Light Gray   | light-gray       | `#D3D3D3` |
