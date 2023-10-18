# BBD's Krita Script Starter Feb 2018

from krita import Extension
from .action_definitions import BuildActionInstances

class CanvasExpander(Extension):

  def __init__(self, parent):
    # Always initialise the superclass.
    # This is necessary to create the underlying C++ object
    super().__init__(parent)

  def setup(self):
    pass

  def createActions(self, window):
    _action_list = BuildActionInstances()

    for _action_def_instance in _action_list:
      setattr(self, _action_def_instance.actionTriggerName, _action_def_instance.construct())

      action = window.createAction(_action_def_instance.actionIdentifier, _action_def_instance.actionMenuEntry, "tools/scripts")
      action.triggered.connect(getattr(self, _action_def_instance.actionTriggerName))

