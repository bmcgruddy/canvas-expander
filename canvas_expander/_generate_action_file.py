import os
import xml.etree.ElementTree as ET

from .menu_layout import MenuLayout


# We need an action file for shortcut definitions
def GenerateActionFile():
    path_dir = os.path.dirname(os.path.abspath(__file__))
    action_file = os.path.join(path_dir, "canvas_expander.action")
    if not os.path.exists(action_file):
        ActionCollection = ET.Element(
            "ActionCollection", version="2", name="Canvas Expander"
        )

        for SubMenu, ActionDefinitions in MenuLayout:
            Actions = ET.Element("Actions", category=SubMenu)
            ET.SubElement(Actions, "text").text = SubMenu

            for _action_def in ActionDefinitions:
                if type(_action_def) in [None, str]:
                    continue

                action = _action_def()

                Action = ET.Element("Action", name=action.actionIdentifier)
                ET.SubElement(Action, "toolTip").text = action.toolTip
                ET.SubElement(Action, "statusTip").text = action.toolTip
                ET.SubElement(Action, "activationFlags").text = action.activationFlags

                Actions.append(Action)
            ActionCollection.append(Actions)

        tree = ET.ElementTree(ActionCollection)
        ET.indent(tree, space="\t", level=0)
        tree.write(action_file, xml_declaration=True, encoding="utf-8")
