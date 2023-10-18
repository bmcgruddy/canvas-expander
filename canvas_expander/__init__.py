import importlib
_krita_module = importlib.util.find_spec('krita')

if _krita_module:
  from .canvas_expander import CanvasExpander

  # And add the extension to Krita's list of extensions:
  app = Krita.instance()
  # Instantiate your class:
  extension = CanvasExpander(parent = app)
  app.addExtension(extension)
