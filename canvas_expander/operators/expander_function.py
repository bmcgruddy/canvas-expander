from krita import (
    Krita,
    Selection,
    QRect,
    Window,
)

from .layer_toggle_function import _get_nodes_by_color


# Used to get the transformed dimentions of the "visiable" area of the canvas,
# scaled and tranformed based on zoom and scroll.
def _get_viewport_bounds(window: Window) -> QRect:
    # Get centralWidget dimentions (QRect)
    _viewport_bounds = window.qwindow().centralWidget().rect()

    # Translate inverted flakeToCanvasTransform.
    _c_transform = window.activeView().flakeToCanvasTransform()
    _c_tranform_inverted, _ = _c_transform.inverted()
    _viewport_bounds = _c_tranform_inverted.mapRect(_viewport_bounds)

    # Translate flakeToImageTransform.
    _c_transform = window.activeView().flakeToImageTransform()
    _viewport_bounds = _c_transform.mapRect(_viewport_bounds)

    return _viewport_bounds


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

    _viewport_bounds = _get_viewport_bounds(window)
    if viewport:
        _combined_bounds = _combined_bounds.united(_viewport_bounds)

    if _combined_bounds and padding:
        _i_padding = int(
            max(_viewport_bounds.width(), _viewport_bounds.height()) * 0.25
        )
        _combined_bounds.adjust(-_i_padding, -_i_padding, _i_padding, _i_padding)

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
