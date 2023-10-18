import importlib
_krita_module = importlib.util.find_spec('krita')

if _krita_module:
  from .expander_function import ExpanderFunction as _operator_expander
  from .scale_to_zoom_function import ScaleToZoomFunction as _operator_scale_to_zoom
  from .layer_toggle_function import LayerToggleFunction as _operator_visibility_toggle
  from .layer_toggle_function import LayerIsolateFunction as _operator_layer_toggle
else:
  _operator_expander = None
  _operator_scale_to_zoom = None
  _operator_visibility_toggle = None
  _operator_layer_toggle = None

class BaseAction:
  actionName = None
  actionNameFull = None
  operator = None
  operator_args = ()
  operator_kwargs = {}

  def __init__(self, *args, **kwargs):
    self.actionIdentifier = f'pykrita_canvas_expander_{self.actionName}'
    self.actionMenuEntry = f'Canvas Expander ({self.actionNameFull})'
    self.actionTriggerName = f'action_triggered_{self.actionName}'
    super().__init__(*args, **kwargs)

  def construct(self):
    def _function_constructor(operator, *args, **kwargs):
        def _function(self):
            return operator(*args, **kwargs)
        return _function
    return _function_constructor(self.operator, *self.operator_args, **self.operator_kwargs)

# ExpanderFunction IDS
class ActionExpanderDefault(BaseAction):
  actionName = 'default'
  actionNameFull = 'Default'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'paintLayers' : True, 'viewport' : True }

class ActionExpanderActiveLayer(BaseAction):
  actionName = 'active'
  actionNameFull = 'Active Layer'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'activeLayer' : True }

class ActionExpanderSelectedLayers(BaseAction):
  actionName = 'selected_layers'
  actionNameFull = 'Selected Layers'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'selectedLayers' : True }

class ActionExpanderPaintLayers(BaseAction):
  actionName = 'paint_layers'
  actionNameFull = 'Paint Layers'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'paintLayers' : True }

class ActionExpanderViewportLayers(BaseAction):
  actionName = 'viewport'
  actionNameFull = 'Viewport Layers'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'viewport' : True }

class ActionExpanderSelection(BaseAction):
  actionName = 'selection'
  actionNameFull = 'Selection'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'selection' : True }

class ActionScaleToZoom(BaseAction):
  actionName = 'scale_to_zoom'
  actionNameFull = 'Scale To Zoom'
  operator = _operator_scale_to_zoom
  operator_args = ()
  operator_kwargs = {}

class ActionToggleByColorSelected(BaseAction):
  actionName = 'layer_toggle_selected'
  actionNameFull = 'Toggle Selected Layers'
  operator = _operator_visibility_toggle
  operator_args = ( -1, )
  operator_kwargs = {}

class ActionToggleByColorBlue(BaseAction):
  actionName = 'layer_toggle_blue'
  actionNameFull = 'Toggle Blue Layers'
  operator = _operator_visibility_toggle
  operator_args = ( 1, )
  operator_kwargs = {}

class ActionToggleByColorGreen(BaseAction):
  actionName = 'layer_toggle_green'
  actionNameFull = 'Toggle Green Layers'
  operator = _operator_visibility_toggle
  operator_args = ( 2, )
  operator_kwargs = {}

class ActionToggleByColorYellow(BaseAction):
  actionName = 'layer_toggle_yellow'
  actionNameFull = 'Toggle Yellow Layers'
  operator = _operator_visibility_toggle
  operator_args = (3,)
  operator_kwargs = {}

class ActionToggleByColorOrange(BaseAction):
  actionName = 'layer_toggle_orange'
  actionNameFull = 'Toggle Orange Layers'
  operator = _operator_visibility_toggle
  operator_args = (4,)
  operator_kwargs = {}

class ActionToggleByColorBrown(BaseAction):
  actionName = 'layer_toggle_brown'
  actionNameFull = 'Toggle Brown Layers'
  operator = _operator_visibility_toggle
  operator_args = (5,)
  operator_kwargs = {}

class ActionToggleByColorRed(BaseAction):
  actionName = 'layer_toggle_red'
  actionNameFull = 'Toggle Red Layers'
  operator = _operator_visibility_toggle
  operator_args = (6,)
  operator_kwargs = {}

class ActionToggleByColorPurple(BaseAction):
  actionName = 'layer_toggle_purple'
  actionNameFull = 'Toggle Purple Layers'
  operator = _operator_visibility_toggle
  operator_args = (7,)
  operator_kwargs = {}

class ActionToggleByColorGrey(BaseAction):
  actionName = 'layer_toggle_grey'
  actionNameFull = 'Toggle Grey Layers'
  operator = _operator_visibility_toggle
  operator_args = (8,)
  operator_kwargs = {}

class ActionIsolateBySelected(BaseAction):
  actionName = 'layer_isolate_selected'
  actionNameFull = 'Isolate Selected Layers'
  operator = _operator_layer_toggle
  operator_args = (-1,)
  operator_kwargs = {}

class ActionIsolateByColorBlue(BaseAction):
  actionName = 'layer_isolate_blue'
  actionNameFull = 'Isolate Blue Layers'
  operator = _operator_layer_toggle
  operator_args = (1,)
  operator_kwargs = {}

class ActionIsolateByColorGreen(BaseAction):
  actionName = 'layer_isolate_green'
  actionNameFull = 'Isolate Green Layers'
  operator = _operator_layer_toggle
  operator_args = (2,)
  operator_kwargs = {}

class ActionIsolateByColorYellow(BaseAction):
  actionName = 'layer_isolate_yellow'
  actionNameFull = 'Isolate Yellow Layers'
  operator = _operator_layer_toggle
  operator_args = (3,)
  operator_kwargs = {}

class ActionIsolateByColorOrange(BaseAction):
  actionName = 'layer_isolate_orange'
  actionNameFull = 'Isolate Orange Layers'
  operator = _operator_layer_toggle
  operator_args = (4,)
  operator_kwargs = {}

class ActionIsolateByColorBrown(BaseAction):
  actionName = 'layer_isolate_brown'
  actionNameFull = 'Isolate Brown Layers'
  operator = _operator_layer_toggle
  operator_args = (5,)
  operator_kwargs = {}

class ActionIsolateByColorRed(BaseAction):
  actionName = 'layer_isolate_red'
  actionNameFull = 'Isolate Red Layers'
  operator = _operator_layer_toggle
  operator_args = (6,)
  operator_kwargs = {}

class ActionIsolateByColorPurple(BaseAction):
  actionName = 'layer_isolate_purple'
  actionNameFull = 'Isolate Purple Layers'
  operator = _operator_layer_toggle
  operator_args = (7,)
  operator_kwargs = {}

class ActionIsolateByColorGrey(BaseAction):
  actionName = 'layer_isolate_grey'
  actionNameFull = 'Isolate Grey Layers'
  operator = _operator_layer_toggle
  operator_args = (8,)
  operator_kwargs = {}

def BuildActionInstances():
  _action_list = ()
  for _attr in globals().keys():
    if _attr.startswith('Action'):
      _c = globals().get(_attr)
      _action_list = (*_action_list, _c())
  return _action_list
