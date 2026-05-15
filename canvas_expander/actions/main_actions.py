from .base_action_class import BaseAction
from ..operators import ExpanderFunction
from ..operators import ScaleToZoomFunction


class ActionScaleToZoom(BaseAction):
    actionName = "scale_to_zoom"
    actionNameFull = "Scale Image By Zoom Level"
    operator = ScaleToZoomFunction
    toolTip = "Scale the image by current zoom level."
    icon = "canvas-expander-scale-to-zoom"


class ActionExpanderDefault(BaseAction):
    actionName = "default"
    actionNameFull = "Grow to View && Paint Layer(s)"
    operator = ExpanderFunction
    operator_args = ()
    operator_kwargs = {"paintLayers": True, "viewport": True, "padding": True}
    toolTip = "Resize the canvas to fit all paint layers and viewport (psudo infinite canvas)."
    icon = "canvas-expander-expand"


class ActionExpanderNoPadding(BaseAction):
    actionName = "expander"
    actionNameFull = "Grow to View && Paint Layer(s) (no padding)"
    operator = ExpanderFunction
    operator_args = ()
    operator_kwargs = {"paintLayers": True, "viewport": True}
    toolTip = "Resize the canvas to fit all paint layers and viewport (psudo infinite canvas) (no padding)."
    icon = "canvas-expander-expand-no-padding"


class ActionExpanderActiveLayer(BaseAction):
    actionName = "active"
    actionNameFull = "Crop to Active Layer"
    operator = ExpanderFunction
    operator_args = ()
    operator_kwargs = {"activeLayer": True}
    toolTip = "Resize the canvas to fit the current layer."


class ActionExpanderSelectedLayers(BaseAction):
    actionName = "selected_layers"
    actionNameFull = "Crop to Selected Layer(s)"
    operator = ExpanderFunction
    operator_args = ()
    operator_kwargs = {"selectedLayers": True}
    toolTip = "Resize the canvas to fit all selected layer(s)."


class ActionExpanderPaintLayers(BaseAction):
    actionName = "paint_layers"
    actionNameFull = "Crop to Paint Layer(s)"
    operator = ExpanderFunction
    operator_args = ()
    operator_kwargs = {"paintLayers": True}
    toolTip = "Resize the canvas to fit all paint layer(s)."


class ActionExpanderViewport(BaseAction):
    actionName = "viewport"
    actionNameFull = "Crop to Viewport"
    operator = ExpanderFunction
    operator_args = ()
    operator_kwargs = {"viewport": True}
    toolTip = "Resize the canvas to match the viewport (fast crop)."


class ActionExpanderSelection(BaseAction):
    actionName = "selection"
    actionNameFull = "Crop to Selection"
    operator = ExpanderFunction
    operator_args = ()
    operator_kwargs = {"selection": True}
    toolTip = "Resize the canvas to fit the current selection."
