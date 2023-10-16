from .canvas_expander import CanvasExpander

# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = CanvasExpander(parent = app)
app.addExtension(extension)
