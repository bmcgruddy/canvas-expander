from krita import Krita

def _is_nodes_visible(nodes):
  return bool(True if sum(n.visible() for n in nodes) >= len(nodes) else False)

def _get_nodes_by_color(documement, color_index : int):
  return tuple(n
    for n in documement.rootNode().findChildNodes('', True)
    if n.colorLabel() == color_index
  )

def LayerToggleFunction(color_index : int = -1, value : int = -1, refreshProjection=True):
  instance = Krita.instance()
  documement = instance.activeDocument()
  window = instance.activeWindow()

  if color_index == -1:
    _nodes = window.activeView().selectedNodes()
  else:
    _nodes = _get_nodes_by_color(documement, color_index)

  if not _nodes:
    return False

  _is_visible = _is_nodes_visible(_nodes)
  _set_visible = not _is_visible
  if value != -1:
    _set_visible = bool(value)

  for _node in _nodes:
      _node.setVisible(_set_visible)

  if refreshProjection:
    documement.refreshProjection()

def LayerIsolateFunction(color_index : int = -1):
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

  for _node in _selected_nodes:
    _node.setVisible(True)
  for _node in _other_nodes:
    _node.setVisible( not _other_nodes_visible)

  documement.refreshProjection()
