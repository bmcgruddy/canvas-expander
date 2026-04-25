from krita import Krita
from krita import QMdiArea, QAbstractScrollArea


def ScaleToZoomFunction(*args, **kwargs):
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

    if round(c_zoom, 2) == 1.0:
        return (False, "No need to scale zoom level is 100%.")

    _width = int(d_width * c_zoom)
    _height = int(d_height * c_zoom)

    documement.scaleImage(_width, _height, d_resolution, d_resolution, "bicubic")
    window.activeView().canvas().setZoomLevel(1.0)
    scroll.horizontalScrollBar().setValue(s_horizontal)
    scroll.verticalScrollBar().setValue(s_vertical)

    documement.refreshProjection()

    return (True, f"Scaled {c_zoom:.2f}")
