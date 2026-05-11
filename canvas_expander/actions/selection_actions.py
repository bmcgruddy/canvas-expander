from .base_action_class import BaseAction
from ..operators import SelectorFunction
from ..operators import SelectorByActiveLayerColorFunction


# Selector function actions.
class ActionSelectorDefault(BaseAction):
    actionName = "selector_default"
    actionNameFull = "Select Boundary Of View && Paint Layer(s)"
    operator = SelectorFunction
    operator_args = ()
    operator_kwargs = {"paintLayers": True, "viewport": True}
    toolTip = "Make a selection based on all paint layers and viewport."


class ActionSelectorActiveLayer(BaseAction):
    actionName = "selector_active"
    actionNameFull = "Select Boundary Of Active Layer"
    operator = SelectorFunction
    operator_args = ()
    operator_kwargs = {"activeLayer": True}
    toolTip = "Make a selection based on the current layer."


class ActionSelectorSelectedLayers(BaseAction):
    actionName = "selector_selected_layers"
    actionNameFull = "Select Boundary Of Selected Layer(s)"
    operator = SelectorFunction
    operator_args = ()
    operator_kwargs = {"selectedLayers": True}
    toolTip = "Make a selection based on all selected layer(s)."


class ActionSelectorPaintLayers(BaseAction):
    actionName = "selector_paint_layers"
    actionNameFull = "Select Boundary Of Paint Layer(s)"
    operator = SelectorFunction
    operator_args = ()
    operator_kwargs = {"paintLayers": True}
    toolTip = "Make a selection based on all paint layer(s)."


class ActionSelectorViewport(BaseAction):
    actionName = "selector_viewport"
    actionNameFull = "Select Boundary Of Viewport"
    operator = SelectorFunction
    operator_args = ()
    operator_kwargs = {"viewport": True}
    toolTip = "Make a selection based of the viewport."


class ActionSelectorByActiveColor(BaseAction):
    actionName = "selector_layer_active_color"
    actionNameFull = "Select Boundary By Active Layer Color"
    operator = SelectorByActiveLayerColorFunction
    toolTip = "Select the combind boundary for all layer(s) that match the active layer's color."


class ActionSelectorByColorBlue(BaseAction):
    actionName = "selector_layer_blue"
    actionNameFull = "Select Boundary By Layer Color (Blue)"
    operator = SelectorFunction
    operator_kwargs = {"color_index": 1}
    toolTip = "Select the combind boundary of all blue colored layer(s)."


class ActionSelectorByColorGreen(BaseAction):
    actionName = "selector_layer_green"
    actionNameFull = "Select Boundary By Layer Color (Green)"
    operator = SelectorFunction
    operator_kwargs = {"color_index": 2}
    toolTip = "Select the combind boundary of all green colored layer(s)."


class ActionSelectorByColorYellow(BaseAction):
    actionName = "selector_layer_yellow"
    actionNameFull = "Select Boundary By Layer Color (Yellow)"
    operator = SelectorFunction
    operator_kwargs = {"color_index": 3}
    toolTip = "Select combind boundary of all yellow colored layer(s)."


class ActionSelectorByColorOrange(BaseAction):
    actionName = "selector_layer_orange"
    actionNameFull = "Select Boundary By Layer Color (Orange)"
    operator = SelectorFunction
    operator_kwargs = {"color_index": 4}
    toolTip = "Select combind boundary of all orange colored layer(s)."


class ActionSelectorByColorBrown(BaseAction):
    actionName = "selector_layer_brown"
    actionNameFull = "Select Boundary By Layer Color (Brown)"
    operator = SelectorFunction
    operator_kwargs = {"color_index": 5}
    toolTip = "Select combind boundary of all brown colored layer(s)."


class ActionSelectorByColorRed(BaseAction):
    actionName = "selector_layer_red"
    actionNameFull = "Select Boundary By Layer Color (Red)"
    operator = SelectorFunction
    operator_kwargs = {"color_index": 6}
    toolTip = "Select combind boundary of all red colored layer(s)."


class ActionSelectorByColorPurple(BaseAction):
    actionName = "selector_layer_purple"
    actionNameFull = "Select Boundary By Layer Color (Purple)"
    operator = SelectorFunction
    operator_kwargs = {"color_index": 7}
    toolTip = "Select combind boundary of all purple colored layer(s)."


class ActionSelectorByColorGrey(BaseAction):
    actionName = "selector_layer_grey"
    actionNameFull = "Select Boundary By Layer Color (Grey)"
    operator = SelectorFunction
    operator_kwargs = {"color_index": 8}
    toolTip = "Select combind boundary of all grey colored layer(s)."
