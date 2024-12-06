import importlib


# Recharger le module wombatAutoRig
from wombatAutoRig import wombatAutoRig
importlib.reload(wombatAutoRig)

# Recharger le module wombatAutoRig.ui.MainWindow
from wombatAutoRig.src.ui import MainWindow
importlib.reload(MainWindow)

# Recharge le module wombatautoRig.src.ui.forms.ui_MainWindow
from wombatAutoRig.src.ui.forms import ui_MainWindow
importlib.reload(ui_MainWindow)

# Recharge le module wombatAutoRig.src.ui.PageTemplateSelection
from wombatAutoRig.src.ui import PageTemplateSelection
importlib.reload(PageTemplateSelection)

# Recharge le module wombatAutoRig.src.ui.forms.ui_PageTemplateSelection
from wombatAutoRig.src.ui.forms import ui_PageTemplateSelection
importlib.reload(ui_PageTemplateSelection)

# Recharge le module wombatAutoRig.src.ui.IconLoader
from wombatAutoRig.src.ui import IconLoader
importlib.reload(IconLoader)

# Recharge le module wombatAutoRig.src.ui.PageGlobalSettings
from wombatAutoRig.src.ui import PageGlobalSettings
importlib.reload(PageGlobalSettings)

# Recharge le module wombatAutoRig.src.ui.forms.ui_PageGlobalSettings
from wombatAutoRig.src.ui.forms import ui_PageGlobalSettings
importlib.reload(ui_PageGlobalSettings)

# Recharge le module wombatAutoRig.src.ui.PageGeometrySelection
from wombatAutoRig.src.ui import PageGeometrySelection
importlib.reload(PageGeometrySelection)

# Recharge le module wombatAutoRig.src.ui.forms.ui_PageGeometrySelection
from wombatAutoRig.src.ui.forms import ui_PageGeometrySelection
importlib.reload(ui_PageGeometrySelection)

# Recharge le module wombatAutoRig.src.ui.PageJointPlacement
from wombatAutoRig.src.ui import PageJointPlacement
importlib.reload(PageJointPlacement)

# Recharge le module wombatAutoRig.src.ui.forms.ui_PageJointPlacement
from wombatAutoRig.src.ui.forms import ui_PageJointPlacement
importlib.reload(ui_PageJointPlacement)

# Recharge le module wombatAutoRig.src.ui.PageControllerPlacement
from wombatAutoRig.src.ui import PageControllerPlacement
importlib.reload(PageControllerPlacement)

# Recharge le module wombatAutoRig.src.ui.forms.ui_PageControllerPlacement
from wombatAutoRig.src.ui.forms import ui_PageControllerPlacement
importlib.reload(ui_PageControllerPlacement)

# Recharge le module wombatAutoRig.src.ui.PageValidation
from wombatAutoRig.src.ui import PageValidation
importlib.reload(PageValidation)

# Recharge le module wombatAutoRig.src.ui.forms.ui_PageValidation
from wombatAutoRig.src.ui.forms import ui_PageValidation
importlib.reload(ui_PageValidation)

# Recharge le module wombatAutoRig.src.ui.PageBase
from wombatAutoRig.src.ui import PageBase
importlib.reload(PageBase)

# Recharge le module wombatAutoRig.src.core.TemplateManager
from wombatAutoRig.src.core import TemplateManager
importlib.reload(TemplateManager)

# Recharge le module wombatAutoRig.src.core.FileHelper
from wombatAutoRig.src.core import FileHelper
importlib.reload(FileHelper)

# Recharge le module wombatAutoRig.src.core.TemplateBase
from wombatAutoRig.src.core import TemplateBase
importlib.reload(TemplateBase)

# Recharge le module wombatAutoRig.src.ui.DlgNewTemplate
from wombatAutoRig.src.ui import DlgNewTemplate
importlib.reload(DlgNewTemplate)

# Recharge le module wombatAutoRig.src.ui.forms.ui_DlgNewTemplate
from wombatAutoRig.src.ui.forms import ui_DlgNewTemplate
importlib.reload(ui_DlgNewTemplate)

# Recharge le module wombatAutoRig.src.ui.DlgColor
from wombatAutoRig.src.ui import DlgColor
importlib.reload(DlgColor)

# Recharge le module wombatAutoRig.src.ui.forms.ui_DlgColor
from wombatAutoRig.src.ui.forms import ui_DlgColor
importlib.reload(ui_DlgColor)

from wombatAutoRig.src.ui.forms import ui_DlgRibbonOnCurves
importlib.reload(ui_DlgRibbonOnCurves)

from wombatAutoRig.src.ui import DlgRibbonOnCurves
importlib.reload(DlgRibbonOnCurves)

from wombatAutoRig.src.ui import DlgAddToShelf
importlib.reload(DlgAddToShelf)

from wombatAutoRig.src.ui.forms import ui_DlgAddToShelf
importlib.reload(ui_DlgAddToShelf)

from wombatAutoRig.src.ui.forms import ui_DlgRibbon
importlib.reload(ui_DlgRibbon)

from wombatAutoRig.src.ui import DlgRibbon
importlib.reload(DlgRibbon)

from wombatAutoRig.src.ui.forms import ui_DlgMatrixConstraint
importlib.reload(ui_DlgMatrixConstraint)

from wombatAutoRig.src.ui import DlgMatrixConstraint
importlib.reload(DlgMatrixConstraint)

from wombatAutoRig.src.ui.forms import ui_DlgControllers
importlib.reload(ui_DlgControllers)

from wombatAutoRig.src.ui import DlgControllers
importlib.reload(DlgControllers)


from wombatAutoRig.src.core import Controllers
importlib.reload(Controllers)


from wombatAutoRig.src.core import MatrixConstrain
importlib.reload(MatrixConstrain)

from wombatAutoRig.src.core import AutorigHelper
importlib.reload(AutorigHelper)

from wombatAutoRig.templates.Body import placement_joints
importlib.reload(placement_joints)

from wombatAutoRig.templates.Body import placement_controllers
importlib.reload(placement_controllers)

from wombatAutoRig.templates.Body import compute
importlib.reload(compute)

from wombatAutoRig.src.core import Ribbon
importlib.reload(Ribbon)

from wombatAutoRig.src.core import TwistExtractor
importlib.reload(TwistExtractor)

from wombatAutoRig.src.core import NonRollMatrix
importlib.reload(NonRollMatrix)

from wombatAutoRig.templates.Body import computeThomas
importlib.reload(computeThomas)


#wombatAutoRig.run()  # Appeler la fonction run() après rechargement

dialog = DlgControllers.DlgControllers()
dialog.run()  # Appeler la fonction run() après rechargement