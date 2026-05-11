from .base_action_class import BaseAction
from ..operators import LayerCycleFunction
from ..operators import LayerCycleByActiveLayerColorFunction


class ActionCycleBySelected(BaseAction):
    actionName = "layer_cycle_selected"
    actionNameFull = "Cycle Selected Layer(s)"
    operator = LayerCycleFunction
    operator_kwargs = {"color_index": -1}
    toolTip = "Cycle between selected layer(s)."


class ActionCycleByActiveColor(BaseAction):
    actionName = "layer_cycle_active_color"
    actionNameFull = "Cycle Between Active Layer Color"
    operator = LayerCycleByActiveLayerColorFunction
    toolTip = "Cycle between all similarly colored layer(s)."


class ActionCycleByColorBlue(BaseAction):
    actionName = "layer_cycle_blue"
    actionNameFull = "Cycle By Layer Color (Blue)"
    operator = LayerCycleFunction
    operator_kwargs = {"color_index": 1}
    toolTip = "Cycle between all blue colored layer(s)."


class ActionCycleByColorGreen(BaseAction):
    actionName = "layer_cycle_green"
    actionNameFull = "Cycle By Layer Color (Green)"
    operator = LayerCycleFunction
    operator_kwargs = {"color_index": 2}
    toolTip = "Cycle between all green colored layer(s)."


class ActionCycleByColorYellow(BaseAction):
    actionName = "layer_cycle_yellow"
    actionNameFull = "Cycle By Layer Color (Yellow)"
    operator = LayerCycleFunction
    operator_kwargs = {"color_index": 3}
    toolTip = "Cycle between all yellow colored layer(s)."


class ActionCycleByColorOrange(BaseAction):
    actionName = "layer_cycle_orange"
    actionNameFull = "Cycle By Layer Color (Orange)"
    operator = LayerCycleFunction
    operator_kwargs = {"color_index": 4}
    toolTip = "Cycle between all orange colored layer(s)."


class ActionCycleByColorBrown(BaseAction):
    actionName = "layer_cycle_brown"
    actionNameFull = "Cycle By Layer Color (Brown)"
    operator = LayerCycleFunction
    operator_kwargs = {"color_index": 5}
    toolTip = "Cycle between all brown colored layer(s)."


class ActionCycleByColorRed(BaseAction):
    actionName = "layer_cycle_red"
    actionNameFull = "Cycle By Layer Color (Red)"
    operator = LayerCycleFunction
    operator_kwargs = {"color_index": 6}
    toolTip = "Cycle between all red colored layer(s)."


class ActionCycleByColorPurple(BaseAction):
    actionName = "layer_cycle_purple"
    actionNameFull = "Cycle By Layer Color (Purple)"
    operator = LayerCycleFunction
    operator_kwargs = {"color_index": 7}
    toolTip = "Cycle between all purple colored layer(s)."


class ActionCycleByColorGrey(BaseAction):
    actionName = "layer_cycle_grey"
    actionNameFull = "Cycle By Layer Color (Grey)"
    operator = LayerCycleFunction
    operator_kwargs = {"color_index": 8}
    toolTip = "Cycle between all grey colored layer(s)."
