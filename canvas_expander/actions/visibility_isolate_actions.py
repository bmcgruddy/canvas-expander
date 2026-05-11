from .base_action_class import BaseAction
from ..operators import LayerIsolateFunction
from ..operators import LayerIsolateByActiveLayerColorFunction


class ActionIsolateBySelected(BaseAction):
    actionName = "layer_isolate_selected"
    actionNameFull = "Isolate Selected Layer(s)"
    operator = LayerIsolateFunction
    operator_kwargs = {"color_index": -1}
    toolTip = "Toggle isolate selected layer(s)."


class ActionIsolateByActiveColor(BaseAction):
    actionName = "layer_isolate_active_color"
    actionNameFull = "Isolate By Active Layer Color"
    operator = LayerIsolateByActiveLayerColorFunction
    toolTip = "Toggle isolate for all similarly colored layer(s)."


class ActionIsolateByColorBlue(BaseAction):
    actionName = "layer_isolate_blue"
    actionNameFull = "Isolate By Layer Color (Blue)"
    operator = LayerIsolateFunction
    operator_kwargs = {"color_index": 1}
    toolTip = "Toggle isolate all blue colored layer(s)."


class ActionIsolateByColorGreen(BaseAction):
    actionName = "layer_isolate_green"
    actionNameFull = "Isolate By Layer Color (Green)"
    operator = LayerIsolateFunction
    operator_kwargs = {"color_index": 2}
    toolTip = "Toggle isolate all green colored layer(s)."


class ActionIsolateByColorYellow(BaseAction):
    actionName = "layer_isolate_yellow"
    actionNameFull = "Isolate By Layer Color (Yellow)"
    operator = LayerIsolateFunction
    operator_kwargs = {"color_index": 3}
    toolTip = "Toggle isolate all yellow colored layer(s)."


class ActionIsolateByColorOrange(BaseAction):
    actionName = "layer_isolate_orange"
    actionNameFull = "Isolate By Layer Color (Orange)"
    operator = LayerIsolateFunction
    operator_kwargs = {"color_index": 4}
    toolTip = "Toggle isolate all orange colored layer(s)."


class ActionIsolateByColorBrown(BaseAction):
    actionName = "layer_isolate_brown"
    actionNameFull = "Isolate By Layer Color (Brown)"
    operator = LayerIsolateFunction
    operator_kwargs = {"color_index": 5}
    toolTip = "Toggle isolate all brown colored layer(s)."


class ActionIsolateByColorRed(BaseAction):
    actionName = "layer_isolate_red"
    actionNameFull = "Isolate By Layer Color (Red)"
    operator = LayerIsolateFunction
    operator_kwargs = {"color_index": 6}
    toolTip = "Toggle isolate all red colored layer(s)."


class ActionIsolateByColorPurple(BaseAction):
    actionName = "layer_isolate_purple"
    actionNameFull = "Isolate By Layer Color (Purple)"
    operator = LayerIsolateFunction
    operator_kwargs = {"color_index": 7}
    toolTip = "Toggle isolate all purple colored layer(s)."


class ActionIsolateByColorGrey(BaseAction):
    actionName = "layer_isolate_grey"
    actionNameFull = "Isolate By Layer Color (Grey)"
    operator = LayerIsolateFunction
    operator_kwargs = {"color_index": 8}
    toolTip = "Toggle isolate all grey colored layer(s)."
