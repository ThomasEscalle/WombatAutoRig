
def spineMatrix():
    # Creer une spine matrix ribbon avec des proprietes du systeme hibride
    # Qu'on a vus en seconde année.

    # Creer une surface nurbs
    #   Create -> Nurbs PLane - > Options
    #   Travailler sur le Z ,  Width 1, length 3
    #   U patch 1, V patch 3
    # Renomer Spine_Ribbon_LowDef

    # Rebuild la surface
    # Panneau Modeling -> Surface -> Rebuild
    #    Uniforme
    #    U 1 , V2
    #    U Linear, V Cubic

    # Mettre le pivot de la surface a la base du ribbon
    #    Bonnus_Tool -> Modify Pivot -> ..
    # Mettre la translate a 0 pour que le pivot soit placé sur la grille

    # Mettre un nouveau material sur la surface
    # Lambert,
    # Renomer le shader 'Shader_Spine_Ribbon'
    # Mettre legerement transparent, bleu foncé

    # On vas creer une EP Curve de la taille du ribbon
    # Vue Orthographique
    # Create -> EP Curve Tool
    #   3 Cubique
    # 3 Points, un a la base, un au milieu et un a la fin

    # Node editor
    # Charger la surface nurbs (Spine_Ribbon_LowDef)
    # Isoler la surface shape
    # Creer un node 'RebuildSurface'
    #    Renomer 'rebuildSurface_Ribbon'
    # Prendre le WorldSpace[0] du Spine_Ribbon_LowDef 
    #   - Le connecter a l'inputSurface du rebuildSurface_Ribbon 
    # Attribute editor du rebuildSurface_Ribbon
    #   - Spans U : 1
    #   - Spans V : 2
    #   - U : Cubic
    #   - V : Heptic
    #   - Direction : V

    # Creer un node CurveFromSurfaceIso
    #   Renomer 'curveFromSurfaceIso_Ribbon'
    # Prendre le outputSurface du rebuildSurface_Ribbon
    #   - Le connecter a l'inputSurface du curveFromSurfaceIso_Ribbon
    # Mettre le isoparm value a 0.5
    # Mettre en V
    
    # Mettre la version shape de la EP Curve dans le node editor
    # Prendre le outputCurve du curveFromSurfaceIso_Ribbon
    #   - Le connecter a la "Create" de la EP Curve

    # Renomer la ep curve en 'Crv_Ribbon_Isoparm'

    # Grouper la surface et la curve dans un groupe
    #   - Renomer 'Ribbon_Spine';

    # Creer un groupe GlobalMove_01
    # Creer un groupe ExtraNodes_01
    # Creer un groupe CTRLS_01
    # Creer un groupe Joints_01

    # Mettre l'ensemble dans le Ribbon_Spine et organiser comme d'hbitude


    # On vas creer 3 Locators qui vont nous servir a calculer un certain nombre
    # d'informations

    # Renomer les locators
    #   - Loc_Info_Initial_Lenght
    #   - Loc_Info_Squash_Chest
    #   - Loc_MovableRotate_Pivot_Chest_IK

    # Mettre les deux premiers (Loc_Info_Initial_Lenght et Loc_Info_Squash_Chest)
    # dans un groupe 
    #  - Renomer 'Grp_Locs'
    #  - Mettre le groupe dans le ExtraNodes_01

    # Prendre les deux locators et les placer tout en haut de la surface nurbs
    # (Y = 3)

    # Ne pas freeze, mais mettre des offsets par dessus chaqu'un des locators

    # Prendre le Loc_MovableRotate_Pivot_Chest_IK
    # Le mettre tout en haut de la surface nurbs (Y = 3)
    # Freezer les transformations
    # 
    # Creer une controller Circle
    # Mettre en vert
    # Renomer 'CTRL_IkChest'
    # Mettre en haut de la surface nurbs (Y = 3)
    # Mettre un offset
    # Freeze les transformations de l'offset

    # pRendre le Loc_MovableRotate_Pivot_Chest_IK
    # Le mettre dans le CTRL_IkChest
    # Prendre le locator et le baisser a 1/8 de la curve
    # (Y -= 0.375)

    # Prendre la surface et la grouper dans un groupe 'Grp_Surfaces'
    # Mettre le groupe dans le ExtraNodes_01

    # Prendre la Curve et la grouper dans un groupe 'Grp_Curves'
    # Mettre le groupe dans le ExtraNodes_01


    pass