from .expander_function import ExpanderFunction as _operator_expander
from .scale_to_zoom_function import ScaleToZoomFunction as _operator_scale_to_zoom
from .layer_toggle_function import LayerToggleFunction as _operator_color_toggle
from .layer_toggle_function import LayerIsolateFunction as _operator_color_isolate

class BaseAction:
  extenstionID = None
  menuEntry = None
  operator = None
  operator_args = ()
  operator_kwargs = {}

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

# ExpanderFunction IDS
class ActionExpanderDefault(BaseAction):
  extenstionID = 'default'
  menuEntry = 'Canvas Expander (Default)'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'paintLayers' : True, 'viewport' : True }

class ActionExpanderActiveLayer(BaseAction):
  extenstionID = 'active'
  menuEntry = 'Canvas Expander (Active Layer)'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'activeLayer' : True }

class ActionExpanderSelectedLayers(BaseAction):
  extenstionID = 'selected_layers'
  menuEntry = 'Canvas Expander (Selected Layers)'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'selectedLayers' : True }

class ActionExpanderPaintLayers(BaseAction):
  extenstionID = 'paint_layers'
  menuEntry = 'Canvas Expander (Paint Layers)'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'paintLayers' : True }

class ActionExpanderViewportLayers(BaseAction):
  extenstionID = 'viewport'
  menuEntry = 'Canvas Expander (Viewport Layers)'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'viewport' : True }

class ActionExpanderSelection(BaseAction):
  extenstionID = 'selection'
  menuEntry = 'Canvas Expander (Selection)'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'selection' : True }

class ActionScaleToZoom(BaseAction):
  extenstionID = 'scale_to_zoom'
  menuEntry = 'Canvas Expander (Scale To Zoom)'
  operator = _operator_scale_to_zoom
  operator_args = ()
  operator_kwargs = {}

class ActionToggleByColorBlue(BaseAction):
  extenstionID = 'layer_toggle_blue'
  menuEntry = 'Canvas Expander (Toggle Blue Layers)'
  operator = _operator_color_toggle
  operator_args = ( 1, )
  operator_kwargs = {}

class ActionToggleByColorGreen(BaseAction):
  extenstionID = 'layer_toggle_green'
  menuEntry = 'Canvas Expander (Toggle Green Layers)'
  operator = _operator_color_toggle
  operator_args = ( 2, )
  operator_kwargs = {}

class ActionToggleByColorYellow(BaseAction):
  extenstionID = 'layer_toggle_yellow'
  menuEntry = 'Canvas Expander (Toggle Yellow Layers)'
  operator = _operator_color_toggle
  operator_args = (3,)
  operator_kwargs = {}

class ActionToggleByColorOrange(BaseAction):
  extenstionID = 'layer_toggle_orange'
  menuEntry = 'Canvas Expander (Toggle Orange Layers)'
  operator = _operator_color_toggle
  operator_args = (4,)
  operator_kwargs = {}

class ActionToggleByColorBrown(BaseAction):
  extenstionID = 'layer_toggle_brown'
  menuEntry = 'Canvas Expander (Toggle Brown Layers)'
  operator = _operator_color_toggle
  operator_args = (5,)
  operator_kwargs = {}

class ActionToggleByColorRed(BaseAction):
  extenstionID = 'layer_toggle_red'
  menuEntry = 'Canvas Expander (Toggle Red Layers)'
  operator = _operator_color_toggle
  operator_args = (6,)
  operator_kwargs = {}

class ActionToggleByColorPurple(BaseAction):
  extenstionID = 'layer_toggle_purple'
  menuEntry = 'Canvas Expander (Toggle Purple Layers)'
  operator = _operator_color_toggle
  operator_args = (7,)
  operator_kwargs = {}

class ActionToggleByColorGrey(BaseAction):
  extenstionID = 'layer_toggle_grey'
  menuEntry = 'Canvas Expander (Toggle Grey Layers)'
  operator = _operator_color_toggle
  operator_args = (8,)
  operator_kwargs = {}

class ActionIsolateByColorBlue(BaseAction):
  extenstionID = 'layer_isolate_blue'
  menuEntry = 'Canvas Expander (Isolate Blue Layers)'
  operator = _operator_color_isolate
  operator_args = (1,)
  operator_kwargs = {}

class ActionIsolateByColorGreen(BaseAction):
  extenstionID = 'layer_isolate_green'
  menuEntry = 'Canvas Expander (Isolate Green Layers)'
  operator = _operator_color_isolate
  operator_args = (2,)
  operator_kwargs = {}

class ActionIsolateByColorYellow(BaseAction):
  extenstionID = 'layer_isolate_yellow'
  menuEntry = 'Canvas Expander (Isolate Yellow Layers)'
  operator = _operator_color_isolate
  operator_args = (3,)
  operator_kwargs = {}

class ActionIsolateByColorOrange(BaseAction):
  extenstionID = 'layer_isolate_orange'
  menuEntry = 'Canvas Expander (Isolate Orange Layers)'
  operator = _operator_color_isolate
  operator_args = (4,)
  operator_kwargs = {}

class ActionIsolateByColorBrown(BaseAction):
  extenstionID = 'layer_isolate_brown'
  menuEntry = 'Canvas Expander (Isolate Brown Layers)'
  operator = _operator_color_isolate
  operator_args = (5,)
  operator_kwargs = {}

class ActionIsolateByColorRed(BaseAction):
  extenstionID = 'layer_isolate_red'
  menuEntry = 'Canvas Expander (Isolate Red Layers)'
  operator = _operator_color_isolate
  operator_args = (6,)
  operator_kwargs = {}

class ActionIsolateByColorPurple(BaseAction):
  extenstionID = 'layer_isolate_purple'
  menuEntry = 'Canvas Expander (Isolate Purple Layers)'
  operator = _operator_color_isolate
  operator_args = (7,)
  operator_kwargs = {}

class ActionIsolateByColorGrey(BaseAction):
  extenstionID = 'layer_isolate_grey'
  menuEntry = 'Canvas Expander (Isolate Grey Layers)'
  operator = _operator_color_isolate
  operator_args = (8,)
  operator_kwargs = {}
