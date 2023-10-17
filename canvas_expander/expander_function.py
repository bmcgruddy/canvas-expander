from krita import Krita
from PyQt5.QtCore import QRect

def _allChildNodes(root) :
  nodes = ()
  for childNode in root.childNodes():
    if childNode.type() == 'paintlayer':
      nodes = (*nodes, childNode)
    nodes = (*nodes,*_allChildNodes(childNode))
  return nodes

def ExpanderFunction(selectedLayer=False, paintLayers=True, viewport=True):
  instance = Krita.instance()
  documement = instance.activeDocument()
  window = instance.activeWindow()

  n_selected_layer = documement.activeNode()
  c_zoom = window.activeView().canvas().zoomLevel()
  c_dx = window.activeView().flakeToCanvasTransform().dx()
  c_dy = window.activeView().flakeToCanvasTransform().dy()
  w_width = window.qwindow().centralWidget().width()
  w_height = window.qwindow().centralWidget().height()
  d_resolution = documement.resolution()
  w_devicePixelRatioF = window.qwindow().devicePixelRatioF()

  # Combine all paintlayer bounding box infomation.
  _combined_bounds = QRect()
  if selectedLayer:
    _combined_bounds = _combined_bounds.united(n_selected_layer.bounds())

  if paintLayers:
    for node in _allChildNodes(documement.rootNode()):
      _combined_bounds = _combined_bounds.united(node.bounds())

  if viewport:
    _zoom = c_zoom * w_devicePixelRatioF / (d_resolution/72)
    _c_dx_a = -int(c_dx * w_devicePixelRatioF / _zoom)
    _c_dy_a = -int(c_dy * w_devicePixelRatioF / _zoom)
    _w_width_a = int(w_width * w_devicePixelRatioF / _zoom)
    _w_height_a = int(w_height * w_devicePixelRatioF / _zoom)
    _viewport_bounds = QRect(_c_dx_a, _c_dy_a, _w_width_a, _w_height_a)
    _combined_bounds = _combined_bounds.united(_viewport_bounds)

  # Apply combined bounding box to document.
  documement.resizeImage(
    _combined_bounds.x(),
    _combined_bounds.y(),
    _combined_bounds.width(),
    _combined_bounds.height()
  )
