from . import actions


MenuLayout = (
    (
        "Canvas Operations",
        (
            "Expand Operators",
            actions.ActionScaleToZoom,
            actions.ActionExpanderDefault,
            actions.ActionExpanderNoPadding,
            "Crop Operations",
            actions.ActionExpanderActiveLayer,
            actions.ActionExpanderSelectedLayers,
            actions.ActionExpanderPaintLayers,
            actions.ActionExpanderViewport,
            actions.ActionExpanderSelection,
        ),
    ),
    (
        "Selection Operations",
        (
            "Select Operators",
            actions.ActionSelectorViewport,
            actions.ActionSelectorActiveLayer,
            actions.ActionSelectorDefault,
            actions.ActionSelectorPaintLayers,
            actions.ActionSelectorSelectedLayers,
            "Select By Color",
            actions.ActionSelectorByActiveColor,
            actions.ActionSelectorByColorBlue,
            actions.ActionSelectorByColorBrown,
            actions.ActionSelectorByColorGreen,
            actions.ActionSelectorByColorGrey,
            actions.ActionSelectorByColorOrange,
            actions.ActionSelectorByColorPurple,
            actions.ActionSelectorByColorRed,
            actions.ActionSelectorByColorYellow,
        ),
    ),
    ("Transform Operations", (*actions.ActionTransformList,)),
    (
        "Layer Visibility Operations",
        (
            "Cycle Layers",
            *actions.ActionCycleList,
            "Toggle Layers",
            *actions.ActionToggleList,
            "Isolate Layers",
            *actions.ActionIsolateList,
        ),
    ),
)
