from .main_actions import (
    ActionScaleToZoom,
    ActionExpanderDefault,
    ActionExpanderNoPadding,
    ActionExpanderActiveLayer,
    ActionExpanderPaintLayers,
    ActionExpanderSelectedLayers,
    ActionExpanderSelection,
    ActionExpanderViewport,
)
from .transform_actions import ActionFilterReduceOpacitySelection
from .selection_actions import (
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
    ActionSelectorDefault,
    ActionSelectorPaintLayers,
    ActionSelectorSelectedLayers,
    ActionSelectorViewport,
)
from .visibility_cycle_actions import (
    ActionCycleByActiveColor,
    ActionCycleByColorBlue,
    ActionCycleByColorBrown,
    ActionCycleByColorGreen,
    ActionCycleByColorGrey,
    ActionCycleByColorOrange,
    ActionCycleByColorPurple,
    ActionCycleByColorRed,
    ActionCycleByColorYellow,
    ActionCycleBySelected,
)
from .visibility_isolate_actions import (
    ActionIsolateByActiveColor,
    ActionIsolateByColorBlue,
    ActionIsolateByColorBrown,
    ActionIsolateByColorGreen,
    ActionIsolateByColorGrey,
    ActionIsolateByColorOrange,
    ActionIsolateByColorPurple,
    ActionIsolateByColorRed,
    ActionIsolateByColorYellow,
    ActionIsolateBySelected,
)


from .visibility_toggle_actions import (
    ActionToggleByActiveColor,
    ActionToggleByColorBlue,
    ActionToggleByColorBrown,
    ActionToggleByColorGrey,
    ActionToggleByColorRed,
    ActionToggleByColorGreen,
    ActionToggleByColorOrange,
    ActionToggleByColorPurple,
    ActionToggleByColorYellow,
    ActionToggleByColorSelected,
)

ActionMainList = (
    ActionScaleToZoom,
    ActionExpanderDefault,
    ActionExpanderNoPadding,
    ActionExpanderActiveLayer,
    ActionExpanderPaintLayers,
    ActionExpanderSelectedLayers,
    ActionExpanderSelection,
    ActionExpanderViewport,
)

ActionSelectorList = (
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
    ActionSelectorDefault,
    ActionSelectorPaintLayers,
    ActionSelectorSelectedLayers,
    ActionSelectorViewport,
)
ActionCycleList = (
    ActionCycleByActiveColor,
    ActionCycleByColorBlue,
    ActionCycleByColorBrown,
    ActionCycleByColorGreen,
    ActionCycleByColorGrey,
    ActionCycleByColorOrange,
    ActionCycleByColorPurple,
    ActionCycleByColorRed,
    ActionCycleByColorYellow,
    ActionCycleBySelected,
)

ActionIsolateList = (
    ActionIsolateByActiveColor,
    ActionIsolateByColorBlue,
    ActionIsolateByColorBrown,
    ActionIsolateByColorGreen,
    ActionIsolateByColorGrey,
    ActionIsolateByColorOrange,
    ActionIsolateByColorPurple,
    ActionIsolateByColorRed,
    ActionIsolateByColorYellow,
    ActionIsolateBySelected,
)
ActionToggleList = (
    ActionToggleByActiveColor,
    ActionToggleByColorBlue,
    ActionToggleByColorBrown,
    ActionToggleByColorGrey,
    ActionToggleByColorRed,
    ActionToggleByColorGreen,
    ActionToggleByColorOrange,
    ActionToggleByColorPurple,
    ActionToggleByColorYellow,
    ActionToggleByColorSelected,
)
ActionTransformList = (ActionFilterReduceOpacitySelection,)
