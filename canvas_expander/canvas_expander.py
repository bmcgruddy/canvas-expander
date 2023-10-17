# BBD's Krita Script Starter Feb 2018

from krita import Extension
from .expander_function import ExpanderFunction
from .scale_to_zoom_function import ScaleToZoomFunction
from .layer_toggle_function import (LayerToggleFunction, LayerIsolateFunction)
from .extenstion_ids import *

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

        action = window.createAction(EXTENSION_ID_ACTIVE_LAYER, MENU_ENTRY_ACTIVE_LAYER, "tools/scripts")
        action.triggered.connect(self.action_triggered_active_layer)

        action = window.createAction(EXTENSION_ID_SELECTED_LAYERS, MENU_ENTRY_SELECTED_LAYERS, "tools/scripts")
        action.triggered.connect(self.action_triggered_selected_layers)

        action = window.createAction(EXTENSION_ID_ALL_LAYERS, MENU_ENTRY_ALL_LAYERS, "tools/scripts")
        action.triggered.connect(self.action_triggered_layers)

        action = window.createAction(EXTENSION_ID_VIEWPORT, MENU_ENTRY_VIEWPORT, "tools/scripts")
        action.triggered.connect(self.action_triggered_viewport)

        action = window.createAction(EXTENSION_ID_SELECTION, MENU_ENTRY_SELECTION, "tools/scripts")
        action.triggered.connect(self.action_triggered_selection)

        action = window.createAction(EXTENSION_ID_SCALE_TO_ZOOM, MENU_ENTRY_SCALE_TO_ZOOM, "tools/scripts")
        action.triggered.connect(self.action_triggered_scale_to_zoom)

        action = window.createAction(EXTENSION_ID_LAYER_TOGGLE_BLUE, MENU_ENTRY_LAYER_TOGGLE_BLUE, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_toggle_blue)

        action = window.createAction(EXTENSION_ID_LAYER_TOGGLE_GREEN, MENU_ENTRY_LAYER_TOGGLE_GREEN, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_toggle_green)

        action = window.createAction(EXTENSION_ID_LAYER_TOGGLE_YELLOW, MENU_ENTRY_LAYER_TOGGLE_YELLOW, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_toggle_yellow)

        action = window.createAction(EXTENSION_ID_LAYER_TOGGLE_ORANGE, MENU_ENTRY_LAYER_TOGGLE_ORANGE, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_toggle_orange)

        action = window.createAction(EXTENSION_ID_LAYER_TOGGLE_BROWN, MENU_ENTRY_LAYER_TOGGLE_BROWN, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_toggle_brown)

        action = window.createAction(EXTENSION_ID_LAYER_TOGGLE_RED, MENU_ENTRY_LAYER_TOGGLE_RED, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_toggle_red)

        action = window.createAction(EXTENSION_ID_LAYER_TOGGLE_PURPLE, MENU_ENTRY_LAYER_TOGGLE_PURPLE, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_toggle_purple)

        action = window.createAction(EXTENSION_ID_LAYER_TOGGLE_GREY, MENU_ENTRY_LAYER_TOGGLE_GREY, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_toggle_grey)

        action = window.createAction(EXTENSION_ID_LAYER_ISOLATE_BLUE, MENU_ENTRY_LAYER_ISOLATE_BLUE, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_isolate_blue)

        action = window.createAction(EXTENSION_ID_LAYER_ISOLATE_GREEN, MENU_ENTRY_LAYER_ISOLATE_GREEN, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_isolate_green)

        action = window.createAction(EXTENSION_ID_LAYER_ISOLATE_YELLOW, MENU_ENTRY_LAYER_ISOLATE_YELLOW, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_isolate_yellow)

        action = window.createAction(EXTENSION_ID_LAYER_ISOLATE_ORANGE, MENU_ENTRY_LAYER_ISOLATE_ORANGE, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_isolate_orange)

        action = window.createAction(EXTENSION_ID_LAYER_ISOLATE_BROWN, MENU_ENTRY_LAYER_ISOLATE_BROWN, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_isolate_brown)

        action = window.createAction(EXTENSION_ID_LAYER_ISOLATE_RED, MENU_ENTRY_LAYER_ISOLATE_RED, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_isolate_red)

        action = window.createAction(EXTENSION_ID_LAYER_ISOLATE_PURPLE, MENU_ENTRY_LAYER_ISOLATE_PURPLE, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_isolate_purple)

        action = window.createAction(EXTENSION_ID_LAYER_ISOLATE_GREY, MENU_ENTRY_LAYER_ISOLATE_GREY, "tools/scripts")
        action.triggered.connect(self.action_triggered_layer_isolate_grey)

    def action_triggered_full(self):
        ExpanderFunction(paintLayers=True, viewport=True)

    def action_triggered_active_layer(self):
        ExpanderFunction(activeLayer=True)

    def action_triggered_selected_layers(self):
        ExpanderFunction(selectedLayers=True)

    def action_triggered_layers(self):
        ExpanderFunction(paintLayers=True)

    def action_triggered_viewport(self):
        ExpanderFunction(viewport=True)

    def action_triggered_selection(self):
        ExpanderFunction(selection=True)

    def action_triggered_scale_to_zoom(self):
        ScaleToZoomFunction()

    def action_triggered_layer_toggle_blue(self):
        LayerToggleFunction(1)

    def action_triggered_layer_toggle_green(self):
        LayerToggleFunction(2)

    def action_triggered_layer_toggle_yellow(self):
        LayerToggleFunction(3)

    def action_triggered_layer_toggle_orange(self):
        LayerToggleFunction(4)

    def action_triggered_layer_toggle_brown(self):
        LayerToggleFunction(5)

    def action_triggered_layer_toggle_red(self):
        LayerToggleFunction(6)

    def action_triggered_layer_toggle_purple(self):
        LayerToggleFunction(7)

    def action_triggered_layer_toggle_grey(self):
        LayerToggleFunction(8)

    def action_triggered_layer_isolate_blue(self):
        LayerIsolateFunction(1)

    def action_triggered_layer_isolate_green(self):
        LayerIsolateFunction(2)

    def action_triggered_layer_isolate_yellow(self):
        LayerIsolateFunction(3)

    def action_triggered_layer_isolate_orange(self):
        LayerIsolateFunction(4)

    def action_triggered_layer_isolate_brown(self):
        LayerIsolateFunction(5)

    def action_triggered_layer_isolate_red(self):
        LayerIsolateFunction(6)

    def action_triggered_layer_isolate_purple(self):
        LayerIsolateFunction(7)

    def action_triggered_layer_isolate_grey(self):
        LayerIsolateFunction(8)
