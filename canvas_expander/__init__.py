from krita import Krita
from .canvas_expander import CanvasExpander
from ._generate_action_file import GenerateActionFile


GenerateActionFile()


# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = CanvasExpander(parent=app)
app.addExtension(extension)
