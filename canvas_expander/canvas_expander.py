# BBD's Krita Script Starter Feb 2018

from krita import Extension
from .expander_function import ExpanderFunction
from .scale_to_zoom_function import ScaleToZoomFunction
from .layer_toggle_function import (LayerToggleFunction, LayerIsolateFunction)
from . import action_definitions

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

        _action_list = tuple(getattr(action_definitions, n)
                             for n in dir(action_definitions) if n.startswith('Action'))

        for _action_def in _action_list:
            _action_id = f'pykrita_canvas_expander_{_action_def.extenstionID}'
            _action_triggered_name = f'action_triggered_{_action_def.extenstionID}'
            setattr(self, _action_triggered_name, _function_constructor(
                _action_def.operator, *_action_def.operator_args, **_action_def.operator_kwargs))

            action = window.createAction(_action_id, _action_def.menuEntry, "tools/scripts")
            action.triggered.connect(getattr(self, _action_triggered_name))

