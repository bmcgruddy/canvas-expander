# BBD's Krita Script Starter Feb 2018

from krita import Extension
from .expander_function import ExpanderFunction
from .scale_to_zoom_function import ScaleToZoomFunction
from .layer_toggle_function import (LayerToggleFunction, LayerIsolateFunction)
from .action_definitions import BuildActionInstances

class CanvasExpander(Extension):

    def __init__(self, parent):
        # Always initialise the superclass.
        # This is necessary to create the underlying C++ object
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        def _function_constructor(operator, *args, **kwargs):
            def _function(self):
                return operator(*args, **kwargs)
            return _function

        _action_list = BuildActionInstances()

        for _action_def_instance in _action_list:
            setattr(self, _action_def_instance.actionTriggerName, _action_def_instance.construct())

            action = window.createAction(_action_def_instance.actionIdentifier, _action_def_instance.actionMenuEntry, "tools/scripts")
            action.triggered.connect(getattr(self, _action_def_instance.actionTriggerName))

