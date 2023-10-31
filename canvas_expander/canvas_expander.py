# BBD's Krita Script Starter Feb 2018

import importlib
_krita_module = importlib.util.find_spec('krita')

if _krita_module:
  from krita import *
  from .action_definitions import BuildSortedActions

  class CanvasExpander(Extension):

    def __init__(self, parent):
      # Always initialise the superclass.
      # This is necessary to create the underlying C++ object
      super().__init__(parent)

    def setup(self):
      pass

    def createActions(self, window):
      _sorted_actions = BuildSortedActions()

      # action = window.createAction("CanvasExpander", "Canvas Expander", "tools/scripts")
      # menu = QtWidgets.QMenu("CanvasExpander", window.qwindow())
      # action.setMenu(menu)

      for (_, actionObjects) in _sorted_actions.items():
        _category_identifier = actionObjects[0].categoryIdentifier
        _category_name_full = actionObjects[0].categoryNameFull
        
        action = window.createAction(_category_identifier, _category_name_full, "tools/scripts/CanvasExpander")
        menu = QtWidgets.QMenu(_category_identifier, window.qwindow())
        action.setMenu(menu)

        for _action_def_instance in actionObjects:
          setattr(self, _action_def_instance.actionTriggerName, _action_def_instance.construct())

          action = window.createAction(_action_def_instance.actionIdentifier, _action_def_instance.actionNameFull, f"tools/scripts/{_category_identifier}")
          action.triggered.connect(getattr(self, _action_def_instance.actionTriggerName))

