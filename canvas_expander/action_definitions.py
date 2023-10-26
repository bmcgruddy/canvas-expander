import importlib
_krita_module = importlib.util.find_spec('krita')

if _krita_module:
  from .operators import ExpanderFunction as _operator_expander
  from .operators import ScaleToZoomFunction as _operator_scale_to_zoom
  from .operators import LayerToggleFunction as _operator_visibility_toggle
  from .operators import LayerIsolateFunction as _operator_layer_toggle
  from .operators import LayerCycleFunction as _operator_layer_cycle
  from .operators import LayerCycleByActiveLayerColorFunction as _operator_active_cycle
  from .operators import LayerIsolateByActiveLayerColorFunction as _operator_active_isolate
  from .operators import LayerToggleByActiveLayerColorFunction as _operator_active_toggle
  from krita import *
else:
  _operator_expander = None
  _operator_scale_to_zoom = None
  _operator_visibility_toggle = None
  _operator_layer_toggle = None
  _operator_layer_cycle = None
  _operator_active_cycle = None
  _operator_active_isolate = None
  _operator_active_toggle = None

class BaseAction:
  categoryName = 'Tool'
  actionName = None
  actionNameFull = None
  operator = None
  operator_args = ()
  operator_kwargs = {}
  iconLoaded = None

  def __init__(self, *args, **kwargs):
    self.actionIdentifier = f'pykrita_canvas_expander_{self.actionName}'
    self.actionTriggerName = f'action_triggered_{self.actionName}'

    if _krita_module and self.icon:
      self.iconLoaded = QIcon(self.icon)
    elif _krita_module:
      self.iconLoaded = QIcon()

    super().__init__(*args, **kwargs)

  @property
  def actionNameFullSafe(self):
    return self.actionNameFull.replace('&&', '&')

  def construct(self):
    def _function_constructor(operator, *args, **kwargs):
      def _function():
        view = Krita().instance().activeWindow().activeView()
        

        (_operator_code, _operator_message) = operator(*args, **kwargs)
        _notification_message = f'{self.actionNameFullSafe} : {_operator_message}'
        view.showFloatingMessage(_notification_message, self.iconLoaded, 1000, 1)
        return _operator_code
      return _function
    return _function_constructor(self.operator, *self.operator_args, **self.operator_kwargs)

class BaseCategoryCanvas(BaseAction):
  categoryName = 'Canvas operations'
  icon = 'krita_tool_transform'

class BaseCategoryVisibility(BaseAction):
  categoryName = 'Layer visibility operations'
  icon = 'onionOn'

# ExpanderFunction IDS
class ActionExpanderDefault(BaseCategoryCanvas):
  actionName = 'default'
  actionNameFull = 'Grow to View && Paint Layers'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'paintLayers' : True, 'viewport' : True }
  toolTip = 'Resize the canvas to fit all paint layers and viewport (psudo infinite canvas).'

class ActionExpanderActiveLayer(BaseCategoryCanvas):
  actionName = 'active'
  actionNameFull = 'Crop to Active Layer'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'activeLayer' : True }
  toolTip = 'Resize the canvas to fit the current layer.'

class ActionExpanderSelectedLayers(BaseCategoryCanvas):
  actionName = 'selected_layers'
  actionNameFull = 'Crop to Selected Layer(s)'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'selectedLayers' : True }
  toolTip = 'Resize the canvas to fit all selected layer(s).'

class ActionExpanderPaintLayers(BaseCategoryCanvas):
  actionName = 'paint_layers'
  actionNameFull = 'Crop to Paint Layer(s)'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'paintLayers' : True }
  toolTip = 'Resize the canvas to fit all paint layer(s).'

class ActionExpanderViewport(BaseCategoryCanvas):
  actionName = 'viewport'
  actionNameFull = 'Crop to Viewport'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'viewport' : True }
  toolTip = 'Resize the canvas to match the viewport (fast crop).'

class ActionExpanderSelection(BaseCategoryCanvas):
  actionName = 'selection'
  actionNameFull = 'Crop to Selection'
  operator = _operator_expander
  operator_args = ()
  operator_kwargs = { 'selection' : True }
  toolTip = 'Resize the canvas to fit the current selection.'

class ActionScaleToZoom(BaseCategoryCanvas):
  actionName = 'scale_to_zoom'
  actionNameFull = 'Scale Image By Zoom Level'
  operator = _operator_scale_to_zoom
  toolTip = 'Scale the image by current zoom level.'

class ActionToggleByColorSelected(BaseCategoryVisibility):
  actionName = 'layer_toggle_selected'
  actionNameFull = 'Toggle Selected Layers'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : -1 }
  toolTip = 'Toggle visibility for selected layer(s).'

class ActionToggleByActiveColor(BaseCategoryVisibility):
  actionName = 'layer_toggle_active_color'
  actionNameFull = 'Toggle By Active Color'
  operator = _operator_active_toggle
  toolTip = 'Toggle visibility for all same colored layer(s).'

class ActionToggleByColorBlue(BaseCategoryVisibility):
  actionName = 'layer_toggle_blue'
  actionNameFull = 'Toggle Blue Layers'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 1 }
  toolTip = 'Toggle visibility for all blue colored layer(s).'

class ActionToggleByColorGreen(BaseCategoryVisibility):
  actionName = 'layer_toggle_green'
  actionNameFull = 'Toggle Green Layers'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 2 }
  toolTip = 'Toggle visibility for all green colored layer(s).'

class ActionToggleByColorYellow(BaseCategoryVisibility):
  actionName = 'layer_toggle_yellow'
  actionNameFull = 'Toggle Yellow Layers'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 3 }
  toolTip = 'Toggle visibility for all yellow colored layer(s).'

class ActionToggleByColorOrange(BaseCategoryVisibility):
  actionName = 'layer_toggle_orange'
  actionNameFull = 'Toggle Orange Layers'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 4 }
  toolTip = 'Toggle visibility for all orange colored layer(s).'

class ActionToggleByColorBrown(BaseCategoryVisibility):
  actionName = 'layer_toggle_brown'
  actionNameFull = 'Toggle Brown Layers'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 5 }
  toolTip = 'Toggle visibility for all brown colored layer(s).'

class ActionToggleByColorRed(BaseCategoryVisibility):
  actionName = 'layer_toggle_red'
  actionNameFull = 'Toggle Red Layers'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 6 }
  toolTip = 'Toggle visibility for all red colored layer(s).'

class ActionToggleByColorPurple(BaseCategoryVisibility):
  actionName = 'layer_toggle_purple'
  actionNameFull = 'Toggle Purple Layers'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 7 }
  toolTip = 'Toggle visibility for all purple colored layer(s).'

class ActionToggleByColorGrey(BaseCategoryVisibility):
  actionName = 'layer_toggle_grey'
  actionNameFull = 'Toggle Grey Layers'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 8 }
  toolTip = 'Toggle visibility for all grey colored layer(s).'

class ActionIsolateBySelected(BaseCategoryVisibility):
  actionName = 'layer_isolate_selected'
  actionNameFull = 'Isolate Selected Layers'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : -1 }
  toolTip = 'Toggle isolate selected layer(s).'

class ActionIsolateByActiveColor(BaseCategoryVisibility):
  actionName = 'layer_isolate_active_color'
  actionNameFull = 'Isolate By Active Color'
  operator = _operator_active_isolate
  toolTip = 'Toggle isolate for all similarly colored layer(s).'

class ActionIsolateByColorBlue(BaseCategoryVisibility):
  actionName = 'layer_isolate_blue'
  actionNameFull = 'Isolate Blue Layers'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 1 }
  toolTip = 'Toggle isolate all blue colored layer(s).'

class ActionIsolateByColorGreen(BaseCategoryVisibility):
  actionName = 'layer_isolate_green'
  actionNameFull = 'Isolate Green Layers'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 2 }
  toolTip = 'Toggle isolate all green colored layer(s).'

class ActionIsolateByColorYellow(BaseCategoryVisibility):
  actionName = 'layer_isolate_yellow'
  actionNameFull = 'Isolate Yellow Layers'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 3 }
  toolTip = 'Toggle isolate all yellow colored layer(s).'

class ActionIsolateByColorOrange(BaseCategoryVisibility):
  actionName = 'layer_isolate_orange'
  actionNameFull = 'Isolate Orange Layers'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 4 }
  toolTip = 'Toggle isolate all orange colored layer(s).'

class ActionIsolateByColorBrown(BaseCategoryVisibility):
  actionName = 'layer_isolate_brown'
  actionNameFull = 'Isolate Brown Layers'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 5 }
  toolTip = 'Toggle isolate all brown colored layer(s).'

class ActionIsolateByColorRed(BaseCategoryVisibility):
  actionName = 'layer_isolate_red'
  actionNameFull = 'Isolate Red Layers'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 6 }
  toolTip = 'Toggle isolate all red colored layer(s).'

class ActionIsolateByColorPurple(BaseCategoryVisibility):
  actionName = 'layer_isolate_purple'
  actionNameFull = 'Isolate Purple Layers'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 7 }
  toolTip = 'Toggle isolate all purple colored layer(s).'

class ActionIsolateByColorGrey(BaseCategoryVisibility):
  actionName = 'layer_isolate_grey'
  actionNameFull = 'Isolate Grey Layers'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 8 }
  toolTip = 'Toggle isolate all grey colored layer(s).'

class ActionCycleBySelected(BaseCategoryVisibility):
  actionName = 'layer_cycle_selected'
  actionNameFull = 'Cycle Selected Layers'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : -1 }
  toolTip = 'Cycle between selected layer(s).'

class ActionCycleByActiveColor(BaseCategoryVisibility):
  actionName = 'layer_cycle_active_color'
  actionNameFull = 'Cycle Between Active Color'
  operator = _operator_active_cycle
  toolTip = 'Cycle between all similarly colored layer(s).'

class ActionCycleByColorBlue(BaseCategoryVisibility):
  actionName = 'layer_cycle_blue'
  actionNameFull = 'Cycle Blue Layers'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 1 }
  toolTip = 'Cycle between all blue colored layer(s).'

class ActionCycleByColorGreen(BaseCategoryVisibility):
  actionName = 'layer_cycle_green'
  actionNameFull = 'Cycle Green Layers'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 2 }
  toolTip = 'Cycle between all green colored layer(s).'

class ActionCycleByColorYellow(BaseCategoryVisibility):
  actionName = 'layer_cycle_yellow'
  actionNameFull = 'Cycle Yellow Layers'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 3 }
  toolTip = 'Cycle between all yellow colored layer(s).'

class ActionCycleByColorOrange(BaseCategoryVisibility):
  actionName = 'layer_cycle_orange'
  actionNameFull = 'Cycle Orange Layers'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 4 }
  toolTip = 'Cycle between all orange colored layer(s).'

class ActionCycleByColorBrown(BaseCategoryVisibility):
  actionName = 'layer_cycle_brown'
  actionNameFull = 'Cycle Brown Layers'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 5 }
  toolTip = 'Cycle between all brown colored layer(s).'

class ActionCycleByColorRed(BaseCategoryVisibility):
  actionName = 'layer_cycle_red'
  actionNameFull = 'Cycle Red Layers'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 6 }
  toolTip = 'Cycle between all red colored layer(s).'

class ActionCycleByColorPurple(BaseCategoryVisibility):
  actionName = 'layer_cycle_purple'
  actionNameFull = 'Cycle Purple Layers'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 7 }
  toolTip = 'Cycle between all purple colored layer(s).'

class ActionCycleByColorGrey(BaseCategoryVisibility):
  actionName = 'layer_cycle_grey'
  actionNameFull = 'Cycle Grey Layers'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 8 }
  toolTip = 'Cycle between all grey colored layer(s).'

def BuildActionInstances():
  _action_list = ()
  for _attr in globals().keys():
    if _attr.startswith('Action'):
      _c = globals().get(_attr)
      _action_list = (*_action_list, _c())
  return _action_list

def BuildSortedActions():
  _sorted_actions = {}
  for _action in BuildActionInstances():
    _sorted_actions = {**_sorted_actions, _action.categoryName : [*_sorted_actions.get(_action.categoryName, []), _action]}
  return _sorted_actions
