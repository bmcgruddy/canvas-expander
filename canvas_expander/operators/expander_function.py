from krita import Krita
from PyQt5.QtCore import QRect

def ExpanderFunction(*args,
    selection : bool = False,
    activeLayer : bool = False,
    selectedLayers : bool = False,
    paintLayers : bool = False,
    viewport : bool = False,
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

  if viewport:
    _zoom = c_zoom * w_devicePixelRatioF / (d_resolution/72)
    _c_dx_a = -int(c_dx * w_devicePixelRatioF / _zoom)
    _c_dy_a = -int(c_dy * w_devicePixelRatioF / _zoom)
    _w_width_a = int(w_width * w_devicePixelRatioF / _zoom)
    _w_height_a = int(w_height * w_devicePixelRatioF / _zoom)
    _viewport_bounds = QRect(_c_dx_a, _c_dy_a, _w_width_a, _w_height_a)
    _combined_bounds = _combined_bounds.united(_viewport_bounds)

  if not _combined_bounds:
    return (False, 'Bounding area is zero.')

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
