from krita import Extension, QtWidgets, QIcon
from .menu_layout import MenuLayout

import os

file_path = os.path.realpath(__file__)
module_path = os.path.dirname(file_path)


class CanvasExpander(Extension):
    def __init__(self, parent):
        # Always initialise the superclass.
        # This is necessary to create the underlying C++ object
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        for SubMenu, ActionDefinitions in MenuLayout:
            # create SubMenu
            _category_identifier = f"CanvasExpander{SubMenu}".replace(" ", "")
            _category_name_full = f"Canvas Expander: {SubMenu}"
            action = window.createAction(
                _category_identifier,
                _category_name_full,
                "tools/scripts",
            )
            menu = QtWidgets.QMenu(_category_identifier, window.qwindow())
            action.setMenu(menu)

            # Create Actions
            for ActionDefinition in ActionDefinitions:
                if type(ActionDefinition) is str:
                    menu.addSection(ActionDefinition)
                    continue
                elif ActionDefinition is None:
                    menu.addSeparator()
                    continue

                definition = ActionDefinition()
                action = window.createAction(
                    definition.actionIdentifier,
                    definition.actionNameFull,
                    f"tools/scripts/{_category_identifier}",
                )
                if definition.icon:
                    action.setIcon(definition.actionIcon)

                action.triggered.connect(definition.construct())

                menu.addAction(action)
