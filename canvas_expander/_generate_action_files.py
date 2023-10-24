# nix-shell -p python311 -p python311Packages.jinja2
# python -m canvas_expander._generate_action_files

import os
from jinja2 import Template
from .action_definitions import BuildSortedActions

ACTION_TEMPLATE="""<?xml version="1.0" encoding="UTF-8"?>
<ActionCollection version="2" name="Scripts">
  {% for categoryName, actions in sorted_actions.items() %}
    <Actions category="Scripts">
        <text>Canvas Expander: {{ categoryName }}</text>
        {% for action in actions %}
        <Action name="{{ action.actionIdentifier }}">
        <toolTip>{{ action.toolTip }}</toolTip>
        <statusTip>{{ action.toolTip }}</statusTip>
        <activationFlags>1</activationFlags>
        </Action>
        {% endfor %}
    </Actions>
  {% endfor %}
</ActionCollection>
"""

_sorted_actions = BuildSortedActions()

_template = Template(ACTION_TEMPLATE)
_render = _template.render(sorted_actions=_sorted_actions)
_file_path = f'./canvas_expander/canvas_expander.action'

print(_render)
with open(_file_path, 'w') as _f:
  _f.write(_render)

for (categoryName, actionObjects) in _sorted_actions.items():
  for _action_def_instance in actionObjects:
    print(f'Tools > Scripts > Canvas Expander > {_action_def_instance.actionNameFull.replace("&&", "&")}')