from . import actions


MenuLayout = (
    ("Canvas Operations", (*actions.ActionMainList,)),
    ("Selection Operations", (*actions.ActionSelectorList,)),
    ("Transform Operations", (*actions.ActionTransformList,)),
    (
        "Layer Visibility Operations",
        (
            *actions.ActionCycleList,
            *actions.ActionToggleList,
            *actions.ActionIsolateList,
        ),
    ),
)
