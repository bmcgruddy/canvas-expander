from krita import Krita

def _is_nodes_visible(nodes):
  return bool(True if sum(n.visible() for n in nodes) >= len(nodes) else False)

def _get_nodes_by_color(documement, color_index : int):
  return tuple(n
    for n in documement.rootNode().findChildNodes('', True)
    if n.colorLabel() == color_index
  )

def LayerToggleFunction(color_index : int, value : int = -1, refreshProjection=True):
  instance = Krita.instance()
  documement = instance.activeDocument()
  nodes = _get_nodes_by_color(documement, color_index)

  _is_visible = _is_nodes_visible(nodes)
  _set_visible = not _is_visible
  if value != -1:
    _set_visible = bool(value)

  for node in nodes:
      node.setVisible(_set_visible)

  documement.refreshProjection()

def LayerIsolateFunction(color_index : int):
  instance = Krita.instance()
  documement = instance.activeDocument()

  _nodes = ()
  for _index in range(1,9):
    if _index != color_index:
      _nodes = (*_nodes, *_get_nodes_by_color(documement, _index))
  _other_nodes_visible = _is_nodes_visible(_nodes)

  for _index in range(1,9):
    if _index == color_index:
      LayerToggleFunction(color_index, 1, refreshProjection=False)
    else:
      if _other_nodes_visible:
        LayerToggleFunction(_index, 0, refreshProjection=False)
      else:
        LayerToggleFunction(_index, 1, refreshProjection=False)


  documement.refreshProjection()
