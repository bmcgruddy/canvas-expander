from .base_action_class import BaseAction
from ..operators import LayerToggleFunction
from ..operators import LayerToggleByActiveLayerColorFunction


class ActionToggleByColorSelected(BaseAction):
    actionName = "layer_toggle_selected"
    actionNameFull = "Toggle Selected Layer(s)"
    operator = LayerToggleFunction
    operator_kwargs = {"color_index": -1}
    toolTip = "Toggle visibility for selected layer(s)."


class ActionToggleByActiveColor(BaseAction):
    actionName = "layer_toggle_active_color"
    actionNameFull = "Toggle By Active Layer Color"
    operator = LayerToggleByActiveLayerColorFunction
    toolTip = "Toggle visibility for all same colored layer(s)."


class ActionToggleByColorBlue(BaseAction):
    actionName = "layer_toggle_blue"
    actionNameFull = "Toggle By Layer Color (Blue)"
    operator = LayerToggleFunction
    operator_kwargs = {"color_index": 1}
    toolTip = "Toggle visibility for all blue colored layer(s)."


class ActionToggleByColorGreen(BaseAction):
    actionName = "layer_toggle_green"
    actionNameFull = "Toggle By Layer Color (Green)"
    operator = LayerToggleFunction
    operator_kwargs = {"color_index": 2}
    toolTip = "Toggle visibility for all green colored layer(s)."


class ActionToggleByColorYellow(BaseAction):
    actionName = "layer_toggle_yellow"
    actionNameFull = "Toggle By Layer Color (Yellow)"
    operator = LayerToggleFunction
    operator_kwargs = {"color_index": 3}
    toolTip = "Toggle visibility for all yellow colored layer(s)."


class ActionToggleByColorOrange(BaseAction):
    actionName = "layer_toggle_orange"
    actionNameFull = "Toggle By Layer Color (Orange)"
    operator = LayerToggleFunction
    operator_kwargs = {"color_index": 4}
    toolTip = "Toggle visibility for all orange colored layer(s)."


class ActionToggleByColorBrown(BaseAction):
    actionName = "layer_toggle_brown"
    actionNameFull = "Toggle By Layer Color (Brown)"
    operator = LayerToggleFunction
    operator_kwargs = {"color_index": 5}
    toolTip = "Toggle visibility for all brown colored layer(s)."


class ActionToggleByColorRed(BaseAction):
    actionName = "layer_toggle_red"
    actionNameFull = "Toggle By Layer Color (Red)"
    operator = LayerToggleFunction
    operator_kwargs = {"color_index": 6}
    toolTip = "Toggle visibility for all red colored layer(s)."


class ActionToggleByColorPurple(BaseAction):
    actionName = "layer_toggle_purple"
    actionNameFull = "Toggle By Layer Color (Purple)"
    operator = LayerToggleFunction
    operator_kwargs = {"color_index": 7}
    toolTip = "Toggle visibility for all purple colored layer(s)."


class ActionToggleByColorGrey(BaseAction):
    actionName = "layer_toggle_grey"
    actionNameFull = "Toggle By Layer Color (Grey)"
    operator = LayerToggleFunction
    operator_kwargs = {"color_index": 8}
    toolTip = "Toggle visibility for all grey colored layer(s)."
