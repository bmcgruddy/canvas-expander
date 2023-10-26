from krita import Krita
from krita import QItemSelectionModel, QTreeView

def _is_nodes_visible(nodes):
  return bool(True if sum(n.visible() for n in nodes) >= len(nodes) else False)

def _get_nodes_by_color(documement, color_index : int):
  return tuple(n
    for n in documement.rootNode().findChildNodes('', True)
    if n.colorLabel() == color_index
  )

def LayerToggleFunction(*args, color_index : int = -1, value : int = -1,  **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()
  window = instance.activeWindow()

  
  if color_index == -1:
    _nodes = window.activeView().selectedNodes()
  else:
    _nodes = _get_nodes_by_color(documement, color_index)

  if not _nodes:
    return (False, "No layers in group.")

  _is_visible = _is_nodes_visible(_nodes)
  _set_visible = not _is_visible
  if value != -1:
    _set_visible = bool(value)

  for _node in _nodes:
      _node.setVisible(_set_visible)

  _v = 'visible' if _set_visible else 'hidden'
  _sucess_message = f'{len(_nodes)} layer(s) {_v}.'

  documement.refreshProjection()

  return (True, _sucess_message)

def LayerIsolateFunction(*args, color_index : int = -1, **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()
  window = instance.activeWindow()

  _other_nodes = ()
  if color_index == -1:
    _selected_nodes = window.activeView().selectedNodes()
    _other_nodes = tuple(n for n in documement.rootNode().findChildNodes('', True)
                         if n not in _selected_nodes)
    _other_nodes_visible = _is_nodes_visible(_other_nodes)

  else:
    _selected_nodes = _get_nodes_by_color(documement, color_index)
    for _index in range(1,9):
      if _index != color_index:
        _other_nodes = (*_other_nodes, *_get_nodes_by_color(documement, _index))
    _other_nodes_visible = _is_nodes_visible(_other_nodes)

  if not _selected_nodes:
    return (False, "No layers in group.")

  if not _other_nodes:
    return (False, "No layers to toggle.")

  for _node in _selected_nodes:
    _node.setVisible(True)
  for _node in _other_nodes:
    _node.setVisible( not _other_nodes_visible)

  documement.refreshProjection()

  _v = 'hidden' if _other_nodes_visible else 'visible'
  return (True, f'{len(_other_nodes)} layer(s) {_v}')

def LayerCycleFunction(*args, color_index : int = -1, direction : int = -1, **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()
  window = instance.activeWindow()

  _kisLayerBox = next(d for d in window.dockers() if d.objectName() == 'KisLayerBox')
  _listLayers = _kisLayerBox.findChild(QTreeView, 'listLayers')
  _model = _listLayers.model()
  _sModel = _listLayers.selectionModel()
  _sModelCurrent = _sModel.selectedIndexes()

  if color_index == -1:
    _nodes = window.activeView().selectedNodes()
  else:
    _nodes = _get_nodes_by_color(documement, color_index)

  if not _nodes:
    return (False, "No layers in group.")

  _current_active_index = -1
  _active_layer = documement.activeNode()
  
  for (_loop_index, _loop_node) in enumerate(_nodes):
    if _loop_node.uniqueId() == _active_layer.uniqueId():
      _current_active_index = _loop_index
      break
  
  if _current_active_index == -1:
    for (_loop_index, _loop_node) in enumerate(_nodes):
      if _loop_node.visible():
        _current_active_index = _loop_index
        break
  
  if _current_active_index == -1:
    _current_active_index = 0

  _next_active_index = (_current_active_index + direction) % len(_nodes)
  for (_loop_index, _loop_node) in enumerate(_nodes):
    if _loop_index == _next_active_index:
      documement.setActiveNode(_loop_node)
      _loop_node.setVisible(True)
    else:
      _loop_node.setVisible(False)

  if color_index == -1:
    for _x in _sModelCurrent:
      _sModel.select(_x, QItemSelectionModel.Select)

  documement.refreshProjection()

  return (True, f'Cycling between {len(_nodes)} layer(s).')

def LayerToggleByActiveLayerColorFunction(*args, **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()
  _active_node_color_index = documement.activeNode().colorLabel()
  return LayerToggleFunction(*args, color_index = _active_node_color_index, **kwargs)

def LayerIsolateByActiveLayerColorFunction(*args, **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()
  _active_node_color_index = documement.activeNode().colorLabel()
  return LayerIsolateFunction(*args, color_index = _active_node_color_index, **kwargs)

def LayerCycleByActiveLayerColorFunction(*args, **kwargs):
  instance = Krita.instance()
  documement = instance.activeDocument()
  _active_node_color_index = documement.activeNode().colorLabel()
  return LayerCycleFunction(*args, color_index = _active_node_color_index, **kwargs)