from krita import Krita


def ReduceOpacityFunction(
    *args,
    selectedLayersOnly: bool = False,
    **kwargs,
):
    instance = Krita.instance()
    documement = instance.activeDocument()
    window = instance.activeWindow()
    originalActiveNode = documement.activeNode()

    selection = documement.selection()
    if not selection:
        return (False, "No selection")

    nodes = []
    if selectedLayersOnly:
        for node in window.activeView().selectedNodes():
            if node.type() == "paintlayer":
                if not node.locked():
                    nodes.append(node)
    else:
        for node in documement.rootNode().findChildNodes("", True, True, "paintlayer"):
            if not node.locked():
                nodes.append(node)

    if not nodes:
        return (False, "No unlocked paint layers")

    for node in nodes:
        documement.setActiveNode(node)
        documement.setSelection(selection)
        instance.action("edit_cut").trigger()
        documement.waitForDone()
        instance.action("edit_paste").trigger()
        documement.waitForDone()
        documement.activeNode().setOpacity(128)
        instance.action("merge_layer").trigger()
        documement.waitForDone()

    documement.setSelection(selection)
    documement.setActiveNode(originalActiveNode)
    documement.refreshProjection()

    return (True, "Complete")
