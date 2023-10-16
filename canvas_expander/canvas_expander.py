# BBD's Krita Script Starter Feb 2018

from krita import Extension
from .operation_function import ExpanderFunction

EXTENSION_ID = 'pykrita_canvas_expander'
MENU_ENTRY = 'Canvas Expander'

class CanvasExpander(Extension):

    def __init__(self, parent):
        # Always initialise the superclass.
        # This is necessary to create the underlying C++ object
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(EXTENSION_ID, MENU_ENTRY, "tools/scripts")
        # parameter 1 = the name that Krita uses to identify the action
        # parameter 2 = the text to be added to the menu entry for this script
        # parameter 3 = location of menu entry
        action.triggered.connect(self.action_triggered)

    def action_triggered(self):
        ExpanderFunction()
