# BBD's Krita Script Starter Feb 2018

from krita import Extension
from .expander_function import ExpanderFunction
from .scale_to_zoom_function import ScaleToZoomFunction


EXTENSION_ID_FULL = 'pykrita_canvas_expander_full'
MENU_ENTRY_FULL = 'Canvas Expander (Default)'

EXTENSION_ID_CURRENT = 'pykrita_canvas_expander_current'
MENU_ENTRY_CURRENT = 'Canvas Expander (Current Layer)'

EXTENSION_ID_ALL_LAYERS = 'pykrita_canvas_expander_layers'
MENU_ENTRY_ALL_LAYERS = 'Canvas Expander (Paint Layers)'

EXTENSION_ID_VIEWPORT = 'pykrita_canvas_expander_crop_to_view'
MENU_ENTRY_VIEWPORT  = 'Canvas Expander (Viewport)'

EXTENSION_ID_SELECTION = 'pykrita_canvas_expander_selection'
MENU_ENTRY_SELECTION = 'Canvas Expander (Selection)'

EXTENSION_ID_SCALE_TO_ZOOM = 'pykrita_canvas_expander_scale_to_zoom'
MENU_ENTRY_SCALE_TO_ZOOM = 'Canvas Expander (Scale To Zoom)'

class CanvasExpander(Extension):

    def __init__(self, parent):
        # Always initialise the superclass.
        # This is necessary to create the underlying C++ object
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(EXTENSION_ID_FULL, MENU_ENTRY_FULL, "tools/scripts")
        action.triggered.connect(self.action_triggered_full)

        action = window.createAction(EXTENSION_ID_CURRENT, MENU_ENTRY_CURRENT, "tools/scripts")
        action.triggered.connect(self.action_triggered_current)

        action = window.createAction(EXTENSION_ID_ALL_LAYERS, MENU_ENTRY_ALL_LAYERS, "tools/scripts")
        action.triggered.connect(self.action_triggered_layers)

        action = window.createAction(EXTENSION_ID_VIEWPORT, MENU_ENTRY_VIEWPORT, "tools/scripts")
        action.triggered.connect(self.action_triggered_viewport)

        action = window.createAction(EXTENSION_ID_SELECTION, MENU_ENTRY_SELECTION, "tools/scripts")
        action.triggered.connect(self.action_triggered_selection)

        action = window.createAction(EXTENSION_ID_SCALE_TO_ZOOM, MENU_ENTRY_SCALE_TO_ZOOM, "tools/scripts")
        action.triggered.connect(self.action_triggered_scale_to_zoom)

    def action_triggered_full(self):
        ExpanderFunction(selection=False, selectedLayer=False, paintLayers=True, viewport=True)

    def action_triggered_current(self):
        ExpanderFunction(selection=False, selectedLayer=True, paintLayers=False, viewport=False)

    def action_triggered_layers(self):
        ExpanderFunction(selection=False, selectedLayer=False, paintLayers=True, viewport=False)

    def action_triggered_viewport(self):
        ExpanderFunction(selection=False, selectedLayer=False, paintLayers=False, viewport=True)

    def action_triggered_selection(self):
        ExpanderFunction(selection=True, selectedLayer=False, paintLayers=False, viewport=False)

    def action_triggered_scale_to_zoom(self):
        ScaleToZoomFunction()
