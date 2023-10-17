from krita import Krita

def LayerToggleFunction(color_index : int, value : int = -1):
  instance = Krita.instance()
  documement = instance.activeDocument()
  nodes = tuple(n
    for n in documement.rootNode().findChildNodes('', True)
    if n.colorLabel() == color_index
  )

  _is_visible = (True if sum(n.visible() for n in nodes) >= len(nodes) else False)
  _set_visible = not _is_visible
  if value != -1:
    _set_visible = bool(value)

  for node in nodes:
      node.setVisible(_set_visible)

  documement.refreshProjection()
