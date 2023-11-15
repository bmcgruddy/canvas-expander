import importlib
_krita_module = importlib.util.find_spec('krita')

if _krita_module:
  from .operators import ExpanderFunction as _operator_expander
  from .operators import SelectorFunction as _operator_selector
  from .operators import SelectorByActiveLayerColorFunction as _operator_active_selector
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
  _operator_selector = None
  _operator_active_selector = None
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
  def categoryIdentifier(self):
    _s = self.categoryName.title()
    _s = _s.replace(' ', '')
    return f'CanvasExpander{_s}'

  @property
  def categoryNameFull(self):
    _s = self.categoryName.title()
    return f'Canvas Expander: {_s}'

  @property
  def actionNameFullSafe(self):
    return self.actionNameFull.replace('&&', '&')

  def construct(self):
    def _function_constructor(operator, *args, **kwargs):
      def _function():
        instance = Krita.instance()
        instance.activeDocument().waitForDone()
        view = instance.activeWindow().activeView()

        (_operator_code, _operator_message) = operator(*args, **kwargs)
        
        _notification_message = f'{self.actionNameFullSafe} : {_operator_message}'
        view.showFloatingMessage(_notification_message, self.iconLoaded, 1000, 1)
        return _operator_code
      return _function
    return _function_constructor(self.operator, *self.operator_args, **self.operator_kwargs)

class BaseCategoryCanvas(BaseAction):
  categoryName = 'Canvas Operations'
  icon = 'krita_tool_transform'

class BaseCategorySelection(BaseAction):
  categoryName = 'Selection Operations'
  icon = 'krita_tool_transform'

class BaseCategoryVisibility(BaseAction):
  categoryName = 'Layer Visibility Operations'
  icon = 'onionOn'

# ExpanderFunction IDS
class ActionExpanderDefault(BaseCategoryCanvas):
  actionName = 'default'
  actionNameFull = 'Grow to View && Paint Layer(s)'
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


# Selector function actions.
class ActionSelectorDefault(BaseCategorySelection):
  actionName = 'selector_default'
  actionNameFull = 'Select Boundary Of View && Paint Layer(s)'
  operator = _operator_selector
  operator_args = ()
  operator_kwargs = { 'paintLayers' : True, 'viewport' : True }
  toolTip = 'Make a selection based on all paint layers and viewport.'

class ActionSelectorActiveLayer(BaseCategorySelection):
  actionName = 'selector_active'
  actionNameFull = 'Select Boundary Of Active Layer'
  operator = _operator_selector
  operator_args = ()
  operator_kwargs = { 'activeLayer' : True }
  toolTip = 'Make a selection based on the current layer.'

class ActionSelectorSelectedLayers(BaseCategorySelection):
  actionName = 'selector_selected_layers'
  actionNameFull = 'Select Boundary Of Selected Layer(s)'
  operator = _operator_selector
  operator_args = ()
  operator_kwargs = { 'selectedLayers' : True }
  toolTip = 'Make a selection based on all selected layer(s).'

class ActionSelectorPaintLayers(BaseCategorySelection):
  actionName = 'selector_paint_layers'
  actionNameFull = 'Select Boundary Of Paint Layer(s)'
  operator = _operator_selector
  operator_args = ()
  operator_kwargs = { 'paintLayers' : True }
  toolTip = 'Make a selection based on all paint layer(s).'

class ActionSelectorViewport(BaseCategorySelection):
  actionName = 'selector_viewport'
  actionNameFull = 'Select Boundary Of Viewport'
  operator = _operator_selector
  operator_args = ()
  operator_kwargs = { 'viewport' : True }
  toolTip = 'Make a selection based of the viewport.'

class ActionSelectorByActiveColor(BaseCategorySelection):
  actionName = 'selector_layer_active_color'
  actionNameFull = 'Select Boundary By Active Layer Color'
  operator = _operator_active_selector
  toolTip = 'Select the combind boundary for all layer(s) that match the active layer\'s color.'

class ActionSelectorByColorBlue(BaseCategorySelection):
  actionName = 'selector_layer_blue'
  actionNameFull = 'Select Boundary By Layer Color (Blue)'
  operator = _operator_selector
  operator_kwargs = { 'color_index' : 1 }
  toolTip = 'Select the combind boundary of all blue colored layer(s).'

class ActionSelectorByColorGreen(BaseCategorySelection):
  actionName = 'selector_layer_green'
  actionNameFull = 'Select Boundary By Layer Color (Green)'
  operator = _operator_selector
  operator_kwargs = { 'color_index' : 2 }
  toolTip = 'Select the combind boundary of all green colored layer(s).'

class ActionSelectorByColorYellow(BaseCategorySelection):
  actionName = 'selector_layer_yellow'
  actionNameFull = 'Select Boundary By Layer Color (Yellow)'
  operator = _operator_selector
  operator_kwargs = { 'color_index' : 3 }
  toolTip = 'Select combind boundary of all yellow colored layer(s).'

class ActionSelectorByColorOrange(BaseCategorySelection):
  actionName = 'selector_layer_orange'
  actionNameFull = 'Select Boundary By Layer Color (Orange)'
  operator = _operator_selector
  operator_kwargs = { 'color_index' : 4 }
  toolTip = 'Select combind boundary of all orange colored layer(s).'

class ActionSelectorByColorBrown(BaseCategorySelection):
  actionName = 'selector_layer_brown'
  actionNameFull = 'Select Boundary By Layer Color (Brown)'
  operator = _operator_selector
  operator_kwargs = { 'color_index' : 5 }
  toolTip = 'Select combind boundary of all brown colored layer(s).'

class ActionSelectorByColorRed(BaseCategorySelection):
  actionName = 'selector_layer_red'
  actionNameFull = 'Select Boundary By Layer Color (Red)'
  operator = _operator_selector
  operator_kwargs = { 'color_index' : 6 }
  toolTip = 'Select combind boundary of all red colored layer(s).'

class ActionSelectorByColorPurple(BaseCategorySelection):
  actionName = 'selector_layer_purple'
  actionNameFull = 'Select Boundary By Layer Color (Purple)'
  operator = _operator_selector
  operator_kwargs = { 'color_index' : 7 }
  toolTip = 'Select combind boundary of all purple colored layer(s).'

class ActionSelectorByColorGrey(BaseCategorySelection):
  actionName = 'selector_layer_grey'
  actionNameFull = 'Select Boundary By Layer Color (Grey)'
  operator = _operator_selector
  operator_kwargs = { 'color_index' : 8 }
  toolTip = 'Select combind boundary of all grey colored layer(s).'


class ActionScaleToZoom(BaseCategoryCanvas):
  actionName = 'scale_to_zoom'
  actionNameFull = 'Scale Image By Zoom Level'
  operator = _operator_scale_to_zoom
  toolTip = 'Scale the image by current zoom level.'

# Toggle actions
class ActionToggleByColorSelected(BaseCategoryVisibility):
  actionName = 'layer_toggle_selected'
  actionNameFull = 'Toggle Selected Layer(s)'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : -1 }
  toolTip = 'Toggle visibility for selected layer(s).'

class ActionToggleByActiveColor(BaseCategoryVisibility):
  actionName = 'layer_toggle_active_color'
  actionNameFull = 'Toggle By Active Layer Color'
  operator = _operator_active_toggle
  toolTip = 'Toggle visibility for all same colored layer(s).'

class ActionToggleByColorBlue(BaseCategoryVisibility):
  actionName = 'layer_toggle_blue'
  actionNameFull = 'Toggle By Layer Color (Blue)'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 1 }
  toolTip = 'Toggle visibility for all blue colored layer(s).'

class ActionToggleByColorGreen(BaseCategoryVisibility):
  actionName = 'layer_toggle_green'
  actionNameFull = 'Toggle By Layer Color (Green)'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 2 }
  toolTip = 'Toggle visibility for all green colored layer(s).'

class ActionToggleByColorYellow(BaseCategoryVisibility):
  actionName = 'layer_toggle_yellow'
  actionNameFull = 'Toggle By Layer Color (Yellow)'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 3 }
  toolTip = 'Toggle visibility for all yellow colored layer(s).'

class ActionToggleByColorOrange(BaseCategoryVisibility):
  actionName = 'layer_toggle_orange'
  actionNameFull = 'Toggle By Layer Color (Orange)'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 4 }
  toolTip = 'Toggle visibility for all orange colored layer(s).'

class ActionToggleByColorBrown(BaseCategoryVisibility):
  actionName = 'layer_toggle_brown'
  actionNameFull = 'Toggle By Layer Color (Brown)'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 5 }
  toolTip = 'Toggle visibility for all brown colored layer(s).'

class ActionToggleByColorRed(BaseCategoryVisibility):
  actionName = 'layer_toggle_red'
  actionNameFull = 'Toggle By Layer Color (Red)'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 6 }
  toolTip = 'Toggle visibility for all red colored layer(s).'

class ActionToggleByColorPurple(BaseCategoryVisibility):
  actionName = 'layer_toggle_purple'
  actionNameFull = 'Toggle By Layer Color (Purple)'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 7 }
  toolTip = 'Toggle visibility for all purple colored layer(s).'

class ActionToggleByColorGrey(BaseCategoryVisibility):
  actionName = 'layer_toggle_grey'
  actionNameFull = 'Toggle By Layer Color (Grey)'
  operator = _operator_visibility_toggle
  operator_kwargs = { 'color_index' : 8 }
  toolTip = 'Toggle visibility for all grey colored layer(s).'

class ActionIsolateBySelected(BaseCategoryVisibility):
  actionName = 'layer_isolate_selected'
  actionNameFull = 'Isolate Selected Layer(s)'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : -1 }
  toolTip = 'Toggle isolate selected layer(s).'

class ActionIsolateByActiveColor(BaseCategoryVisibility):
  actionName = 'layer_isolate_active_color'
  actionNameFull = 'Isolate By Active Layer Color'
  operator = _operator_active_isolate
  toolTip = 'Toggle isolate for all similarly colored layer(s).'

class ActionIsolateByColorBlue(BaseCategoryVisibility):
  actionName = 'layer_isolate_blue'
  actionNameFull = 'Isolate By Layer Color (Blue)'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 1 }
  toolTip = 'Toggle isolate all blue colored layer(s).'

class ActionIsolateByColorGreen(BaseCategoryVisibility):
  actionName = 'layer_isolate_green'
  actionNameFull = 'Isolate By Layer Color (Green)'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 2 }
  toolTip = 'Toggle isolate all green colored layer(s).'

class ActionIsolateByColorYellow(BaseCategoryVisibility):
  actionName = 'layer_isolate_yellow'
  actionNameFull = 'Isolate By Layer Color (Yellow)'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 3 }
  toolTip = 'Toggle isolate all yellow colored layer(s).'

class ActionIsolateByColorOrange(BaseCategoryVisibility):
  actionName = 'layer_isolate_orange'
  actionNameFull = 'Isolate By Layer Color (Orange)'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 4 }
  toolTip = 'Toggle isolate all orange colored layer(s).'

class ActionIsolateByColorBrown(BaseCategoryVisibility):
  actionName = 'layer_isolate_brown'
  actionNameFull = 'Isolate By Layer Color (Brown)'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 5 }
  toolTip = 'Toggle isolate all brown colored layer(s).'

class ActionIsolateByColorRed(BaseCategoryVisibility):
  actionName = 'layer_isolate_red'
  actionNameFull = 'Isolate By Layer Color (Red)'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 6 }
  toolTip = 'Toggle isolate all red colored layer(s).'

class ActionIsolateByColorPurple(BaseCategoryVisibility):
  actionName = 'layer_isolate_purple'
  actionNameFull = 'Isolate By Layer Color (Purple)'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 7 }
  toolTip = 'Toggle isolate all purple colored layer(s).'

class ActionIsolateByColorGrey(BaseCategoryVisibility):
  actionName = 'layer_isolate_grey'
  actionNameFull = 'Isolate By Layer Color (Grey)'
  operator = _operator_layer_toggle
  operator_kwargs = { 'color_index' : 8 }
  toolTip = 'Toggle isolate all grey colored layer(s).'

class ActionCycleBySelected(BaseCategoryVisibility):
  actionName = 'layer_cycle_selected'
  actionNameFull = 'Cycle Selected Layer(s)'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : -1 }
  toolTip = 'Cycle between selected layer(s).'

class ActionCycleByActiveColor(BaseCategoryVisibility):
  actionName = 'layer_cycle_active_color'
  actionNameFull = 'Cycle Between Active Layer Color'
  operator = _operator_active_cycle
  toolTip = 'Cycle between all similarly colored layer(s).'

class ActionCycleByColorBlue(BaseCategoryVisibility):
  actionName = 'layer_cycle_blue'
  actionNameFull = 'Cycle By Layer Color (Blue)'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 1 }
  toolTip = 'Cycle between all blue colored layer(s).'

class ActionCycleByColorGreen(BaseCategoryVisibility):
  actionName = 'layer_cycle_green'
  actionNameFull = 'Cycle By Layer Color (Green)'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 2 }
  toolTip = 'Cycle between all green colored layer(s).'

class ActionCycleByColorYellow(BaseCategoryVisibility):
  actionName = 'layer_cycle_yellow'
  actionNameFull = 'Cycle By Layer Color (Yellow)'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 3 }
  toolTip = 'Cycle between all yellow colored layer(s).'

class ActionCycleByColorOrange(BaseCategoryVisibility):
  actionName = 'layer_cycle_orange'
  actionNameFull = 'Cycle By Layer Color (Orange)'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 4 }
  toolTip = 'Cycle between all orange colored layer(s).'

class ActionCycleByColorBrown(BaseCategoryVisibility):
  actionName = 'layer_cycle_brown'
  actionNameFull = 'Cycle By Layer Color (Brown)'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 5 }
  toolTip = 'Cycle between all brown colored layer(s).'

class ActionCycleByColorRed(BaseCategoryVisibility):
  actionName = 'layer_cycle_red'
  actionNameFull = 'Cycle By Layer Color (Red)'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 6 }
  toolTip = 'Cycle between all red colored layer(s).'

class ActionCycleByColorPurple(BaseCategoryVisibility):
  actionName = 'layer_cycle_purple'
  actionNameFull = 'Cycle By Layer Color (Purple)'
  operator = _operator_layer_cycle
  operator_kwargs = { 'color_index' : 7 }
  toolTip = 'Cycle between all purple colored layer(s).'

class ActionCycleByColorGrey(BaseCategoryVisibility):
  actionName = 'layer_cycle_grey'
  actionNameFull = 'Cycle By Layer Color (Grey)'
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
