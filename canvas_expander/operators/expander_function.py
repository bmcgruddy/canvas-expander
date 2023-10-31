from krita import Krita, Selection
from PyQt5.QtCore import QRect

from .layer_toggle_function import _get_nodes_by_color

def _get_boundry(*args,
    selection : bool = False,
    activeLayer : bool = False,
    selectedLayers : bool = False,
    paintLayers : bool = False,
    viewport : bool = False,
    color_index : int = -1,
    **kwargs
    ):

  instance = Krita.instance()
  documement = instance.activeDocument()
  window = instance.activeWindow()

  n_active_layer = documement.activeNode()
  c_zoom = window.activeView().canvas().zoomLevel()
  c_dx = window.activeView().flakeToCanvasTransform().dx()
  c_dy = window.activeView().flakeToCanvasTransform().dy()
  w_width = window.qwindow().centralWidget().width()
  w_height = window.qwindow().centralWidget().height()
  d_resolution = documement.resolution()
  w_devicePixelRatioF = window.qwindow().devicePixelRatioF()

  # Combine all bounding box infomation.
  _combined_bounds = QRect()

  if activeLayer:
    _combined_bounds = _combined_bounds.united(n_active_layer.bounds())

  if selectedLayers:
    for node in window.activeView().selectedNodes():
      _combined_bounds = _combined_bounds.united(node.bounds())

  if selection:
    _selection = documement.selection()
    if _selection:
      _selection_qrect = QRect(
        _selection.x(),
        _selection.y(),
        _selection.width(),
        _selection.height()
      )
      _combined_bounds = _combined_bounds.united(_selection_qrect)

  if paintLayers:
    for node in documement.rootNode().findChildNodes('', True, True, 'paintlayer'):
      _combined_bounds = _combined_bounds.united(node.bounds())

  if color_index != -1:
    for node in _get_nodes_by_color(documement, color_index):
      if node.visible():
        _combined_bounds = _combined_bounds.united(node.bounds())
      
  if viewport:
    _zoom = c_zoom * w_devicePixelRatioF / (d_resolution/72)
    _c_dx_a = -int(c_dx * w_devicePixelRatioF / _zoom)
    _c_dy_a = -int(c_dy * w_devicePixelRatioF / _zoom)
    _w_width_a = int(w_width * w_devicePixelRatioF / _zoom)
    _w_height_a = int(w_height * w_devicePixelRatioF / _zoom)
    _viewport_bounds = QRect(_c_dx_a, _c_dy_a, _w_width_a, _w_height_a)
    _combined_bounds = _combined_bounds.united(_viewport_bounds)

  if not _combined_bounds:
    return (False, None, 'Bounding area is zero.')

  return (True, _combined_bounds, '')


def ExpanderFunction(*args, **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()

  (_func_return, _combined_bounds, _func_message) = _get_boundry(*args, **kwargs)
  if not _func_return:
    return (_func_return, _func_message)

  if all((
    documement.xOffset() == _combined_bounds.x(),
    documement.yOffset() == _combined_bounds.y(),
    documement.width() == _combined_bounds.width(),
    documement.height() == _combined_bounds.height(),
    )):
    return (False, 'Nothing to change.')

  # Apply combined bounding box to document.
  documement.resizeImage(
    _combined_bounds.x(),
    _combined_bounds.y(),
    _combined_bounds.width(),
    _combined_bounds.height()
  )

  documement.refreshProjection()
  return (True, 'Canvas expanded.')

def SelectorFunction(*args, **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()

  (_func_return, _combined_bounds, _func_message) = _get_boundry(*args, **kwargs)
  if not _func_return:
    return (_func_return, _func_message)

  _selection = Selection()
  _selection.select(_combined_bounds.x(), _combined_bounds.y(), _combined_bounds.width(), _combined_bounds.height(), 255)
  documement.setSelection(_selection)
  return (True, 'Selected.')

def SelectorByActiveLayerColorFunction(*args, **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()
  _active_node_color_index = documement.activeNode().colorLabel()
  return SelectorFunction(*args, color_index = _active_node_color_index, **kwargs)
