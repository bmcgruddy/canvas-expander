from krita import Krita

def ReduceOpacityFunction(*args, **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()
  window = instance.activeWindow()

  _x = 0
  _y = 0
  _w = documement.width()
  _h = documement.height()
  selection = documement.selection()
  if selection:
    _x = selection.x()
    _y = selection.y()
    _w = selection.width()
    _h = selection.height()

  _levelFilter = instance.filter('levels')
  _levelFilterConfig = _levelFilter.configuration()
  _levelFilterConfig.setProperty('mode', 'channels')
  _levelFilterConfig.setProperty('number_of_channels', 8)
  _levelFilterConfig.setProperty('channel_0', '0;1;1;0;1')
  _levelFilterConfig.setProperty('channel_1', '0;1;1;0;1')
  _levelFilterConfig.setProperty('channel_2', '0;1;1;0;1')
  _levelFilterConfig.setProperty('channel_3', '0;1;1;0;1')
  _levelFilterConfig.setProperty('channel_4', '0;1;1;0;0.5')
  _levelFilterConfig.setProperty('channel_5', '0;1;1;0;1')
  _levelFilterConfig.setProperty('channel_6', '0;1;1;0;1')
  _levelFilterConfig.setProperty('channel_7', '0;1;1;0;1')
  _levelFilter.setConfiguration(_levelFilterConfig)

  for node in window.activeView().selectedNodes():
    _levelFilter.apply(node, _x, _y, _w, _h)

  documement.refreshProjection()

  return (True, "Complete")
