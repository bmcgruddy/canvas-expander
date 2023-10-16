from krita import Krita


def ScaleToZoomFunction():
  instance = Krita.instance()
  documement = instance.activeDocument()
  window = instance.activeWindow()

  c_zoom = window.activeView().canvas().zoomLevel()
  d_resolution = documement.resolution()
  d_width = documement.width()
  d_height = documement.height()
  w_devicePixelRatioF = window.qwindow().devicePixelRatioF()

  _zoom = c_zoom * w_devicePixelRatioF / (d_resolution/72)
  _width = int(d_width * _zoom)
  _height = int(d_height * _zoom)

  documement.scaleImage(_width, _height, d_resolution, d_resolution, 'bicubic')
  window.activeView().canvas().setZoomLevel(1.0)
  documement.refreshProjection()
