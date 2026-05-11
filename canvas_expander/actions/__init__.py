from .main_actions import (
    ActionExpanderActiveLayer,
    ActionExpanderDefault,
    ActionExpanderNoPadding,
    ActionExpanderPaintLayers,
    ActionExpanderSelectedLayers,
    ActionExpanderSelection,
    ActionExpanderViewport,
    ActionScaleToZoom,
)
from .transform_actions import ActionFilterReduceOpacitySelection
from .selection_actions import (
    ActionSelectorDefault,
    ActionSelectorPaintLayers,
    ActionSelectorSelectedLayers,
    ActionSelectorViewport,
    ActionSelectorActiveLayer,
    ActionSelectorByActiveColor,
    ActionSelectorByColorBlue,
    ActionSelectorByColorBrown,
    ActionSelectorByColorGreen,
    ActionSelectorByColorGrey,
    ActionSelectorByColorOrange,
    ActionSelectorByColorPurple,
    ActionSelectorByColorRed,
    ActionSelectorByColorYellow,
)
from .visibility_cycle_actions import (
    ActionCycleBySelected,
    ActionCycleByActiveColor,
    ActionCycleByColorBlue,
    ActionCycleByColorBrown,
    ActionCycleByColorGreen,
    ActionCycleByColorGrey,
    ActionCycleByColorOrange,
    ActionCycleByColorPurple,
    ActionCycleByColorRed,
    ActionCycleByColorYellow,
)
from .visibility_isolate_actions import (
    ActionIsolateBySelected,
    ActionIsolateByActiveColor,
    ActionIsolateByColorBlue,
    ActionIsolateByColorBrown,
    ActionIsolateByColorGreen,
    ActionIsolateByColorGrey,
    ActionIsolateByColorOrange,
    ActionIsolateByColorPurple,
    ActionIsolateByColorRed,
    ActionIsolateByColorYellow,
)


from .visibility_toggle_actions import (
    ActionToggleByColorSelected,
    ActionToggleByActiveColor,
    ActionToggleByColorBlue,
    ActionToggleByColorBrown,
    ActionToggleByColorGreen,
    ActionToggleByColorGrey,
    ActionToggleByColorOrange,
    ActionToggleByColorPurple,
    ActionToggleByColorRed,
    ActionToggleByColorYellow,
)

ActionMainList = (
    ActionExpanderActiveLayer,
    ActionExpanderDefault,
    ActionExpanderNoPadding,
    ActionExpanderPaintLayers,
    ActionExpanderSelectedLayers,
    ActionExpanderSelection,
    ActionExpanderViewport,
    ActionScaleToZoom,
)

ActionSelectorList = (
    ActionSelectorDefault,
    ActionSelectorPaintLayers,
    ActionSelectorSelectedLayers,
    ActionSelectorViewport,
    ActionSelectorActiveLayer,
    ActionSelectorByActiveColor,
    ActionSelectorByColorBlue,
    ActionSelectorByColorBrown,
    ActionSelectorByColorGreen,
    ActionSelectorByColorGrey,
    ActionSelectorByColorOrange,
    ActionSelectorByColorPurple,
    ActionSelectorByColorRed,
    ActionSelectorByColorYellow,
)
ActionCycleList = (
    ActionCycleBySelected,
    ActionCycleByActiveColor,
    ActionCycleByColorBlue,
    ActionCycleByColorBrown,
    ActionCycleByColorGreen,
    ActionCycleByColorGrey,
    ActionCycleByColorOrange,
    ActionCycleByColorPurple,
    ActionCycleByColorRed,
    ActionCycleByColorYellow,
)

ActionIsolateList = (
    ActionIsolateBySelected,
    ActionIsolateByActiveColor,
    ActionIsolateByColorBlue,
    ActionIsolateByColorBrown,
    ActionIsolateByColorGreen,
    ActionIsolateByColorGrey,
    ActionIsolateByColorOrange,
    ActionIsolateByColorPurple,
    ActionIsolateByColorRed,
    ActionIsolateByColorYellow,
)
ActionToggleList = (
    ActionToggleByColorSelected,
    ActionToggleByActiveColor,
    ActionToggleByColorBlue,
    ActionToggleByColorBrown,
    ActionToggleByColorGreen,
    ActionToggleByColorGrey,
    ActionToggleByColorOrange,
    ActionToggleByColorPurple,
    ActionToggleByColorRed,
    ActionToggleByColorYellow,
)
ActionTransformList = (ActionFilterReduceOpacitySelection,)
