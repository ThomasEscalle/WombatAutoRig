# Colors
```python
from wombatAutoRig.src.core import Colors
```
Source: [Colors.py](https://github.com/ThomasEscalle/WombatAutoRig/blob/main/src/core/Color.py)

See also: [Preferences](https://github.com/ThomasEscalle/WombatAutoRig/blob/main/docs/Preferences.md)

## Description

This module provides a function to set the color of an object or a list of objects. The color can be set by name or by hexadecimal value. The list of available colors is provided below.

## Usage

```python
from wombatAutoRig.src.core import Colors

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
| ![#F9BFCB](https://placehold.co/15x15/F9BFCB/F9BFCB.png) Pink         | pink             | `#F9BFCB` |
| ![#DD1E3F](https://placehold.co/15x15/DD1E3F/DD1E3F.png) Crimson      | crimson          | `#DD1E3F` |
| ![#ED1E24](https://placehold.co/15x15/ED1E24/ED1E24.png) Red          | red              | `#ED1E24` |
| ![#7E1416](https://placehold.co/15x15/7E1416/7E1416.png) Maroon       | maroon           | `#7E1416` |
| ![#A62A2A](https://placehold.co/15x15/A62A2A/A62A2A.png) Brown        | brown            | `#A62A2A` |
| ![#FCE3DF](https://placehold.co/15x15/FCE3DF/FCE3DF.png) Misty        | misty            | `#FCE3DF` |
| ![#F57F73](https://placehold.co/15x15/F57F73/F57F73.png) Salmon       | salmon           | `#F57F73` |
| ![#F47D52](https://placehold.co/15x15/F47D52/F47D52.png) Coral        | coral            | `#F47D52` |
| ![#F14924](https://placehold.co/15x15/F14924/F14924.png) Orange Red   | orange-red       | `#F14924` |
| ![#D36A28](https://placehold.co/15x15/D36A28/D36A28.png) Chocolate    | chocolate        | `#D36A28` |
| ![#AAAAAA](https://placehold.co/15x15/A9A9A9/AAAAAA.png) Dark Gray    | dark-gray        | `#AAAAAA` |
| ![#FFA419](https://placehold.co/15x15/FFA419/FFA419.png) Orange       | orange           | `#FFA419` |
| ![#E4BD20](https://placehold.co/15x15/E4BD20/E4BD20.png) Gold         | gold             | `#E4BD20` |
| ![#FAF9E5](https://placehold.co/15x15/FAF9E5/FAF9E5.png) Ivory        | ivory            | `#FAF9E5` |
| ![#F7EC14](https://placehold.co/15x15/F7EC14/F7EC14.png) Yellow       | yellow           | `#F7EC14` |
| ![#6B692C](https://placehold.co/15x15/808000/6B692C.png) Olive        | olive            | `#6B692C` |
| ![#9AC93B](https://placehold.co/15x15/9AC93B/9AC93B.png) Yellow Green | yellow-green     | `#9AC93B` |
| ![#91C73E](https://placehold.co/15x15/91C73E/91C73E.png) Lawn Green   | lawn-green       | `#91C73E` |
| ![#69BD44](https://placehold.co/15x15/69BD44/69BD44.png) Lime         | lime             | `#69BD44` |
| ![#10813F](https://placehold.co/15x15/10813F/10813F.png) Green        | green            | `#10813F` |
| ![#71C16A](https://placehold.co/15x15/71C16A/71C16A.png) Spring Green | spring-green     | `#71C16A` |
| ![#696969](https://placehold.co/15x15/696969/696969.png) Gray         | gray             | `#696969` |
| ![#99D4C0](https://placehold.co/15x15/99D4C0/99D4C0.png) Aqua Marine  | aqua-marine      | `#99D4C0` |
| ![#63C6C1](https://placehold.co/15x15/63C6C1/63C6C1.png) Turquoise    | turquoise        | `#63C6C1` |
| ![#DEF2F3](https://placehold.co/15x15/DEF2F3/DEF2F3.png) Azure        | azure            | `#DEF2F3` |
| ![#6FCCDD](https://placehold.co/15x15/6FCCDD/6FCCDD.png) Aqua         | aqua             | `#6FCCDD` |
| ![#008181](https://placehold.co/15x15/008181/008181.png) Teal         | teal             | `#008181` |
| ![#D9D7EC](https://placehold.co/15x15/D9D7EC/D9D7EC.png) Lavender     | lavender         | `#D9D7EC` |
| ![#3853A4](https://placehold.co/15x15/3853A4/3853A4.png) Blue         | blue             | `#3853A4` |
| ![#272974](https://placehold.co/15x15/272974/272974.png) Navy         | navy             | `#272974` |
| ![#7651A1](https://placehold.co/15x15/7651A1/7651A1.png) Blue Violet  | blue-violet      | `#7651A1` |
| ![#000000](https://placehold.co/15x15/000000/000000.png) Black        | black            | `#000000` |
| ![#4E2A7C](https://placehold.co/15x15/4E2A7C/4E2A7C.png) Indigo       | indigo           | `#4E2A7C` |
| ![#80469B](https://placehold.co/15x15/80469B/80469B.png) Dark Violet  | dark-violet      | `#80469B` |
| ![#D4A2C8](https://placehold.co/15x15/D4A2C8/D4A2C8.png) Plum         | plum             | `#D4A2C8` |
| ![#B9539F](https://placehold.co/15x15/B9539F/B9539F.png) Magenta      | magenta          | `#B9539F` |
| ![#7D277E](https://placehold.co/15x15/7D277E/7D277E.png) Purple       | purple           | `#7D277E` |
| ![#C71784](https://placehold.co/15x15/C71784/C71784.png) Red Violet   | red-violet       | `#C71784` |
| ![#D1B48C](https://placehold.co/15x15/D1B48C/D1B48C.png) Tan          | tan              | `#D1B48C` |
| ![#6F7F8F](https://placehold.co/15x15/6F7F8F/6F7F8F.png) Slate Gray   | slate-gray       | `#6F7F8F` |
| ![#2F4F4E](https://placehold.co/15x15/2F4F4E/2F4F4E.png) Dark Slate Gray | dark-slate-gray | `#2F4F4E` |
| ![#D3D3D3](https://placehold.co/15x15/D3D3D3/D3D3D3.png) Light Gray   | light-gray       | `#D3D3D3` |
