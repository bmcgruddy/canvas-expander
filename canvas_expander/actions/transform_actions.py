from .base_action_class import BaseAction
from ..operators import ReduceOpacityFunction


class ActionFilterReduceOpacitySelection(BaseAction):
    actionName = "reduce_opacity_selected_layers"
    actionNameFull = "Half Opacity Of Selected Area (selected layers)"
    operator = ReduceOpacityFunction
    operator_args = ()
    operator_kwargs = {"selectedLayersOnly": True}
    toolTip = "Reduces the opacity of selection."


class ActionFilterReduceOpacitySelectionAllPaintLayers(BaseAction):
    actionName = "reduce_opacity_all_paint_layers"
    actionNameFull = "Half Opacity Of Selected Area (all paint layers)"
    operator = ReduceOpacityFunction
    operator_args = ()
    operator_kwargs = {"selectedLayersOnly": False}
    toolTip = "Reduces the opacity of selection."
