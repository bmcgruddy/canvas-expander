

# Canvas Expander
A [krita](https://krita.org/) extension that supplies helpful canvas related operations to help speed up workflow.

> **Notes**
> This extension begin its development with the 5.2.0 release of krita, cannot guarantee backwards compatibility at this time.

## Features

### Canvas resizing Tools

- **Grow to View & Paint Layers**; psudo infinte canvas. Grow the document to contain both paint layers and view.
Simply run this action after panning to area you wish to start drawing but have ran out of canvas space.
> **Note**  
> You will need to either set an opaque background color for the document, or create a **fill layer** with a desired background color.
Otherwise you see tranparent areas where the document has expanded.

- **Crop to Active Layer**; its "Trim To Current Layer" minus the destructive **trimming**.
- **Crop to Selected Layer(s)**; like above but crops to all layers checked.
- **Crop to Paint Layer(s)**; as above instead crops to all paint layers.
- **Crop to Viewport**; as above instead crops to the active viewport (what you can see).
- **Crop to Selection**; as above instead crops to the current selection.
- **Scale Image By Zoom Level**; (*destructive*) dynamically re-scale the document based on current zoom making it now 100% zoom.

> **Notes**  
> The most of these operations are non destructive and none of the layer data is changed, it changes the document dimensions that frames them.

### Layer Tools
- **Toggle Visibility**; quickly toggle all the affected layer(s) visibility.
- **Isolate**; toggle visibility for everything other than the affected layer(s).
- **Cycle between**; switch between affected layer(s) having only one visible at a time.

> **Notes**  
> Most to all layer operations have a by **selected**, **color**, **active color** variant.  
> Currently color based operations ignore layers with no color set to them.  
> To uniformly change state often the average of affected layers of visibility is used. This is to help make it more reliable but does not eliminate edge ceases where it get it wrong... in other words press it again it should get right the second time.  

## Usage & Shortcuts
To get the most of this extension its advised to set shortcuts for the tools most used for muscle memory.
But here are the menu paths to gain access to provided tools.

### Menu entries
```
Tools > Scripts > Canvas Expander > Grow to View & Paint Layers
Tools > Scripts > Canvas Expander > Crop to Active Layer
Tools > Scripts > Canvas Expander > Crop to Selected Layer(s)
Tools > Scripts > Canvas Expander > Crop to Paint Layer(s)
Tools > Scripts > Canvas Expander > Crop to Viewport
Tools > Scripts > Canvas Expander > Crop to Selection
Tools > Scripts > Canvas Expander > Scale Image By Zoom Level
Tools > Scripts > Canvas Expander > Toggle Selected Layers
Tools > Scripts > Canvas Expander > Toggle By Active Color
Tools > Scripts > Canvas Expander > Toggle Blue Layers
Tools > Scripts > Canvas Expander > Toggle Green Layers
Tools > Scripts > Canvas Expander > Toggle Yellow Layers
Tools > Scripts > Canvas Expander > Toggle Orange Layers
Tools > Scripts > Canvas Expander > Toggle Brown Layers
Tools > Scripts > Canvas Expander > Toggle Red Layers
Tools > Scripts > Canvas Expander > Toggle Purple Layers
Tools > Scripts > Canvas Expander > Toggle Grey Layers
Tools > Scripts > Canvas Expander > Isolate Selected Layers
Tools > Scripts > Canvas Expander > Isolate By Active Color
Tools > Scripts > Canvas Expander > Isolate Blue Layers
Tools > Scripts > Canvas Expander > Isolate Green Layers
Tools > Scripts > Canvas Expander > Isolate Yellow Layers
Tools > Scripts > Canvas Expander > Isolate Orange Layers
Tools > Scripts > Canvas Expander > Isolate Brown Layers
Tools > Scripts > Canvas Expander > Isolate Red Layers
Tools > Scripts > Canvas Expander > Isolate Purple Layers
Tools > Scripts > Canvas Expander > Isolate Grey Layers
Tools > Scripts > Canvas Expander > Cycle Selected Layers
Tools > Scripts > Canvas Expander > Cycle Between Active Color
Tools > Scripts > Canvas Expander > Cycle Blue Layers
Tools > Scripts > Canvas Expander > Cycle Green Layers
Tools > Scripts > Canvas Expander > Cycle Yellow Layers
Tools > Scripts > Canvas Expander > Cycle Orange Layers
Tools > Scripts > Canvas Expander > Cycle Brown Layers
Tools > Scripts > Canvas Expander > Cycle Red Layers
Tools > Scripts > Canvas Expander > Cycle Purple Layers
Tools > Scripts > Canvas Expander > Cycle Grey Layers
```

## Installation
Krita's [own guide](https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html)
