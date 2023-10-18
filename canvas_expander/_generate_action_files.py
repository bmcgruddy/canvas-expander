# nix-shell -p python311 -p python311Packages.jinja2
# python -m canvas_expander._generate_action_files

import os
from jinja2 import Template
from .action_definitions import BuildActionInstances

ACTION_TEMPLATE="""<?xml version="1.0" encoding="UTF-8"?>
<ActionCollection version="2" name="Scripts">
    <Actions category="Scripts">
        <text>Canvas Expander</text>

        <Action name="{{ action.actionIdentifier }}">
        <icon></icon>
        <text>Canvas Expander</text>
        <whatsThis></whatsThis>
        <toolTip></toolTip>
        <iconText></iconText>
        <activationFlags>10000</activationFlags>
        <activationConditions>1</activationConditions>
        <shortcut></shortcut>
        <isCheckable>false</isCheckable>
        <statusTip></statusTip>
        </Action>
    </Actions>
</ActionCollection>
"""


for _action in BuildActionInstances():
  _template = Template(ACTION_TEMPLATE)
  _render = _template.render(action=_action)
  _file_path = f'./canvas_expander/actions/{_action.actionIdentifier}.action'
  with open(_file_path, 'w') as _f:
    _f.write(_render)
