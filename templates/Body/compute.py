import maya.cmds as cmds
from wombatAutoRig.templates.Body import computeThomas
from wombatAutoRig.src.core import Color
from wombatAutoRig.src.core import Offset
from wombatAutoRig.src.core import PoleVector
from wombatAutoRig.src.core import MatrixConstrain



def compute(settings):
    computeThomas.compute(settings)

    #region Leg L

    #Creating the joints 
    cmds.duplicate("PlacementJnt_Root", n="Bind_Root", po = True)
    cmds.duplicate("PlacementJnt_Hip_L", n="Bind_Hip_L", po = True)
    
    cmds.duplicate("PlacementJnt_Hip_L", n="DrvJnt_Leg_L", po=True)
    Color.setColor("DrvJnt_Leg_L", "yellow")
    cmds.duplicate("PlacementJnt_Knee_L", n="DrvJnt_Knee_L", po=True)
    Color.setColor("DrvJnt_Knee_L", "yellow")
    cmds.duplicate("PlacementJnt_Ankle_L", n="DrvJnt_Ankle_L", po=True)
    Color.setColor("DrvJnt_Ankle_L", "yellow")
    
    cmds.duplicate("PlacementJnt_Hip_L", n="FK_Leg_L", po=True)
    Color.setColor("FK_Leg_L", "blue")
    cmds.duplicate("PlacementJnt_Knee_L", n="FK_Knee_L", po=True)
    Color.setColor("FK_Knee_L", "blue")
    cmds.duplicate("PlacementJnt_Ankle_L", n="FK_Ankle_L", po=True)
    Color.setColor("FK_Ankle_L", "blue")
    
    cmds.duplicate("PlacementJnt_Knee_L", n="Preserve_Knee_L", po=True)
    
    #Unparenting the joints
    
    cmds.parent("Bind_Root", world=True)
    cmds.parent("Bind_Hip_L", world=True)
    cmds.parent("DrvJnt_Leg_L", world=True)
    cmds.parent("DrvJnt_Knee_L", world=True)
    cmds.parent("DrvJnt_Ankle_L", world=True)
    cmds.parent("FK_Leg_L", world=True)
    cmds.parent("FK_Knee_L", world=True)
    cmds.parent("FK_Ankle_L", world=True)
    cmds.parent("Preserve_Knee_L", world=True)
    
    #Reparenting the joints
    
    cmds.parent("Bind_Hip_L", "Bind_Root")
    cmds.parent("DrvJnt_Knee_L", "DrvJnt_Leg_L")
    cmds.parent("DrvJnt_Ankle_L", "DrvJnt_Knee_L")
    cmds.parent("FK_Knee_L", "FK_Leg_L")
    cmds.parent("FK_Ankle_L", "FK_Knee_L")
    
    #Offset for the joints
    
    Offset.offset("Bind_Root", nbr=3)
    Offset.offset("DrvJnt_Leg_L", nbr=3)
    Offset.offset("FK_Leg_L", nbr=3)
    Offset.offset("Preserve_Knee_L", nbr=3)
    
    #Rangement des joints dans un groupe
    
    cmds.parent("Bind_Root_Offset", "{}|GlobalMove_01|Joints_01".format(settings["name"]))
    cmds.parent("DrvJnt_Leg_L_Offset", "{}|GlobalMove_01|Joints_01".format(settings["name"]))
    cmds.parent("FK_Leg_L_Offset", "{}|GlobalMove_01|Joints_01".format(settings["name"]))
    cmds.parent("Preserve_Knee_L_Offset", "{}|GlobalMove_01|Joints_01".format(settings["name"]))
    
    #Creating the IK handle
    cmds.ikHandle(n="IK_Leg_L", sj="DrvJnt_Leg_L", ee="DrvJnt_Ankle_L", sol="ikRPsolver")
    cmds.parent("IK_Leg_L", "{}|GlobalMove_01|IKs_01".format(settings["name"]))
    Locator = cmds.spaceLocator(n="PoleVector_L")
    Color.setColor("PoleVector_L", "green")
    PoleVector.PoleVector(joint_1="DrvJnt_Leg_L", joint_2="DrvJnt_Knee_L", joint_3="DrvJnt_Ankle_L", CTRL="PoleVector_L")
    Offset.offset("PoleVector_L", nbr=1)
    cmds.poleVectorConstraint(Locator, "IK_Leg_L")
    cmds.parent("PoleVector_L_Offset", "{}|GlobalMove_01|CTRLs_01".format(settings["name"]))
    
    #Attach Joints chain To Hip
    Bind_Hip_L = ["Bind_Hip_L"]
    DrvJnt_Knee_L = ["DrvJnt_Knee_L"]
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, "DrvJnt_Leg_L_Hook", Offset=False, sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, "FK_Leg_L_Hook", Offset=False, sX=False, sY=False, sZ=False)
    MatrixConstrain.MatrixConstrain(DrvJnt_Knee_L, "Preserve_Knee_L_Hook", Offset=False, sX=False, sY=False, sZ=False, rX=False, rY=False, rZ=False)
    
    #Creating a switch for the IK FK
    cmds.circle(n="Switch_Leg_L", nr=(0, 0, 1))
    cmds.addAttr("Switch_Leg_L", ln="IK_FK", at="enum", en="IK:FK", k=True)
    cmds.setAttr("Switch_Leg_L.t", "Bind_Hip_L.t"+(8,0,0))
    Color.setColor("Switch_Leg_L", "yellow")
    Offset.offset("Switch_Leg_L", nbr=2)
    MatrixConstrain.MatrixConstrain(Bind_Hip_L, "Switch_Leg_L_Move", Offset=True, sX=False, sY=False, sZ=False)
    
    
    #endregion Leg L 
    
    
    
    