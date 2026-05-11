from .base_action_class import BaseAction
from ..operators import ReduceOpacityFunction


class ActionFilterReduceOpacitySelection(BaseAction):
    actionName = "reduce_opacity"
    actionNameFull = (
        "Half Opacity of Selection or Document Bounds (Experimental) (No Undo)"
    )
    operator = ReduceOpacityFunction
    operator_args = ()
    operator_kwargs = {}
    toolTip = "Reduces the opacity of selection or document bounds."
