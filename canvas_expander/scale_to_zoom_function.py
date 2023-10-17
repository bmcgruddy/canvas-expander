from krita import Krita
from krita import QMdiArea, QAbstractScrollArea

def ScaleToZoomFunction():
  instance = Krita.instance()
  documement = instance.activeDocument()
  window = instance.activeWindow()
  scroll = (
    window.qwindow()
    .findChild(QMdiArea)
    .currentSubWindow()
    .findChild(QAbstractScrollArea)
    )

  s_horizontal = scroll.horizontalScrollBar().value()
  s_vertical = scroll.verticalScrollBar().value()

  c_zoom = window.activeView().canvas().zoomLevel()
  d_resolution = documement.resolution()
  d_width = documement.width()
  d_height = documement.height()
  w_devicePixelRatioF = window.qwindow().devicePixelRatioF()


  _zoom = c_zoom * w_devicePixelRatioF / (d_resolution/72)

  if round(_zoom, 2) == 1.0:
    return False

  _width = int(d_width * _zoom)
  _height = int(d_height * _zoom)

  documement.scaleImage(_width, _height, d_resolution, d_resolution, 'bicubic')
  window.activeView().canvas().setZoomLevel(1.0)
  scroll.horizontalScrollBar().setValue(s_horizontal)
  scroll.verticalScrollBar().setValue(s_vertical)
  documement.refreshProjection()
  return True
