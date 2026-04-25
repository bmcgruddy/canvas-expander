from krita import (
    Krita,
    Selection,
    QRect,
    QRectF,
    QTransform,
)

from .layer_toggle_function import _get_nodes_by_color


def _get_boundry(
    *args,
    selection: bool = False,
    activeLayer: bool = False,
    selectedLayers: bool = False,
    paintLayers: bool = False,
    viewport: bool = False,
    padding: bool = False,
    color_index: int = -1,
    **kwargs,
):
    instance = Krita.instance()
    documement = instance.activeDocument()
    window = instance.activeWindow()

    # Combine all bounding box infomation.
    _combined_bounds = QRect()

    if activeLayer:
        _n_active_layer = documement.activeNode()
        _combined_bounds = _combined_bounds.united(_n_active_layer.bounds())

    if selectedLayers:
        for node in window.activeView().selectedNodes():
            _combined_bounds = _combined_bounds.united(node.bounds())

    if selection:
        _selection = documement.selection()
        if _selection:
            _selection_qrect = QRect(
                _selection.x(), _selection.y(), _selection.width(), _selection.height()
            )
            _combined_bounds = _combined_bounds.united(_selection_qrect)

    if paintLayers:
        for node in documement.rootNode().findChildNodes("", True, True, "paintlayer"):
            _combined_bounds = _combined_bounds.united(node.bounds())

    if color_index != -1:
        for node in _get_nodes_by_color(documement, color_index):
            if node.visible():
                _combined_bounds = _combined_bounds.united(node.bounds())

    # Create viewport bounds
    _w_width = window.qwindow().centralWidget().width()
    _w_height = window.qwindow().centralWidget().height()

    if viewport:
        _window_rect = QRectF(0.0, 0.0, float(_w_width), float(_w_height))

        # Translate viewport bounds with inverted canvas transform.
        _c_transform = window.activeView().flakeToCanvasTransform()
        _c_tranform_inverted, _ = _c_transform.inverted()
        _viewport_bounds = _c_tranform_inverted.mapRect(_window_rect)

        # Translate bounds by the zoom ratio.
        _c_zoom = window.activeView().canvas().zoomLevel()
        (_t_ratio, _) = QTransform().scale(_c_zoom, _c_zoom).inverted()
        _viewport_bounds = _t_ratio.mapRect(_viewport_bounds)

        # Convert from QRectF to QRect
        _viewport_bounds = _viewport_bounds.toRect()

        _combined_bounds = _combined_bounds.united(_viewport_bounds)

    if _combined_bounds and padding:
        _v = max(_w_width, _w_height) * 0.4
        _paddin_rect = QRectF(
            (_combined_bounds.x() - _v),
            (_combined_bounds.y() - _v),
            (_combined_bounds.width() + (_v * 2)),
            (_combined_bounds.height() + (_v * 2)),
        ).toRect()
        _combined_bounds = _combined_bounds.united(_paddin_rect)

    if not _combined_bounds:
        return (False, None, "Bounding area is zero.")

    return (True, _combined_bounds, "")


def ExpanderFunction(*args, **kwargs):
    instance = Krita.instance()
    documement = instance.activeDocument()

    (_func_return, _combined_bounds, _func_message) = _get_boundry(*args, **kwargs)
    if not _func_return:
        return (_func_return, _func_message)

    if all(
        (
            documement.xOffset() == _combined_bounds.x(),
            documement.yOffset() == _combined_bounds.y(),
            documement.width() == _combined_bounds.width(),
            documement.height() == _combined_bounds.height(),
        )
    ):
        return (False, "Nothing to change.")

    # Apply combined bounding box to document.
    documement.resizeImage(
        _combined_bounds.x(),
        _combined_bounds.y(),
        _combined_bounds.width(),
        _combined_bounds.height(),
    )

    documement.refreshProjection()
    return (True, "Canvas expanded.")


def SelectorFunction(*args, **kwargs):
    instance = Krita.instance()
    documement = instance.activeDocument()

    (_func_return, _combined_bounds, _func_message) = _get_boundry(*args, **kwargs)
    if not _func_return:
        return (_func_return, _func_message)

    _selection = Selection()
    _selection.select(
        _combined_bounds.x(),
        _combined_bounds.y(),
        _combined_bounds.width(),
        _combined_bounds.height(),
        255,
    )
    documement.setSelection(_selection)
    return (True, "Selected.")


def SelectorByActiveLayerColorFunction(*args, **kwargs):
    instance = Krita.instance()
    documement = instance.activeDocument()
    _active_node_color_index = documement.activeNode().colorLabel()
    return SelectorFunction(*args, color_index=_active_node_color_index, **kwargs)
