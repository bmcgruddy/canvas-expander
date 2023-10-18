

# Canvas Expander
A [krita](https://krita.org/) extension that supplies helpful canvas related operations to help speed up workflow.

> Note:
> This extension begin its development with the 5.2.0 release of krita, cannot guarantee backwards compatibility at this time.

## Features

### Canvas resizing Tools

- **Default**; like a pseudo infinite canvas!
- **Active Layer**; its "Trim To Current Layer" minus the destructive "trimming".
- **Selected Layer(s)**; like above but all layers checked.
- **Paint Layers**; as above instead it fits to all paint layers.
- **Viewport**; to be used as a non destructive cropping tool.
- **Selection**; to be used as a non destructive cropping tool.
- **Scale To Zoom**; (*destructive*) dynamically re-scale the document based on current zoom making it now 100% zoom.

> Note:
> The most of these operations are non destructive and none of the layer data is changed, it changes the document dimensions that frames them.

### Layer Tools
- **Toggle Selected Layer(s) Visibility**, quickly toggle all the selected layers visibility.
- **Isolate Selected Layer(s)**, like isolate layer but all layers selected.
- **Toggle Layer Visibility By Color**; almost limitless with possibles! turn sketch, filter, background layers on or off at the press of a button.
- **Isolate Layer(s) By Color**; Quickly show or hide layers that are not said color.

> Note:
> Currently color based operations ignore layers with no color set to them.
> To uniformly change state often the average of affected layers of visibility is used. This is to help make it more reliable but does not eliminate edge ceases where it get it wrong... in other words press it again it should get right the second time.


## Usage & Shortcuts
To get the most of this extension its advised to set shortcuts for the tools most used for muscle memory.
But here are the menu paths to gain access to provided tools.

### Menu entries
```
Tools > Scripts > Canvas Expander (Default)
Tools > Scripts > Canvas Expander (Active Layer)
Tools > Scripts > Canvas Expander (Selected Layers)
Tools > Scripts > Canvas Expander (Paint Layers)
Tools > Scripts > Canvas Expander (Viewport)
Tools > Scripts > Canvas Expander (Selection)
Tools > Scripts > Canvas Expander (Scale To Zoom)
Tools > Scripts > Canvas Expander (Toggle Selected Layers)
Tools > Scripts > Canvas Expander (Toggle Blue Layers)
Tools > Scripts > Canvas Expander (Toggle Green Layers)
Tools > Scripts > Canvas Expander (Toggle Yellow Layers)
Tools > Scripts > Canvas Expander (Toggle Orange Layers)
Tools > Scripts > Canvas Expander (Toggle Brown Layers)
Tools > Scripts > Canvas Expander (Toggle Red Layers)
Tools > Scripts > Canvas Expander (Toggle Purple Layers)
Tools > Scripts > Canvas Expander (Toggle Grey Layers)
Tools > Scripts > Canvas Expander (Isolate Selected Layers)
Tools > Scripts > Canvas Expander (Isolate Blue Layers)
Tools > Scripts > Canvas Expander (Isolate Green Layers)
Tools > Scripts > Canvas Expander (Isolate Yellow Layers)
Tools > Scripts > Canvas Expander (Isolate Orange Layers)
Tools > Scripts > Canvas Expander (Isolate Brown Layers)
Tools > Scripts > Canvas Expander (Isolate Red Layers)
Tools > Scripts > Canvas Expander (Isolate Purple Layers)
Tools > Scripts > Canvas Expander (Isolate Grey Layers)
```

## Installation
Krita's [own guide](https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html)
