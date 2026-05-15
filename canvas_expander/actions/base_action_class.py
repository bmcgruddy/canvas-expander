from krita import Krita, QIcon

import os

icon_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.abspath(os.path.join(icon_path, "..", "icons"))


class BaseAction:
    categoryName = "Tool"
    actionName = None
    actionNameFull = None
    operator = None
    operator_args = ()
    operator_kwargs = {}
    actionIcon: QIcon = QIcon()
    icon = None
    activationFlags = "1"

    def __init__(self, *args, **kwargs):
        self.actionIdentifier = f"pykrita_canvas_expander_{self.actionName}"
        self.actionTriggerName = f"action_triggered_{self.actionName}"

        if self.icon:
            print(f"{icon_path}/{self.icon}.svg")
            self.actionIcon = QIcon(f"{icon_path}/{self.icon}.svg")
        else:
            self.actionIcon = QIcon()

        super().__init__(*args, **kwargs)

    @property
    def actionNameFullSafe(self):
        return self.actionNameFull.replace("&&", "&")

    def construct(self):
        def _function_constructor(operator, *args, **kwargs):
            def _function():
                instance = Krita.instance()
                instance.activeDocument().waitForDone()
                view = instance.activeWindow().activeView()

                (_operator_code, _operator_message) = operator(*args, **kwargs)

                _notification_message = (
                    f"{self.actionNameFullSafe} : {_operator_message}"
                )
                view.showFloatingMessage(
                    _notification_message, self.actionIcon, 2000, 1
                )
                return _operator_code

            return _function

        return _function_constructor(
            self.operator, *self.operator_args, **self.operator_kwargs
        )
