

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

- **Crop**; crops the document to fit all affected layers, similar to the trim to selection tool minius the distructive trimming of non visible parts.
- **Scale Image By Zoom Level**; (*destructive*) dynamically re-scale the document based on current zoom making it now 100% zoom.

> **Notes**  
> The most of these operations are non destructive and none of the layer data is changed, it changes the document dimensions that frames them.

### Selection Tools
- **Select Boundary**; used to create a bounding box selection of all affected layers.

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
Tools > Scripts > Canvas Expander: Canvas Operations > Grow to View & Paint Layer(s)
Tools > Scripts > Canvas Expander: Canvas Operations > Crop to Active Layer
Tools > Scripts > Canvas Expander: Canvas Operations > Crop to Selected Layer(s)
Tools > Scripts > Canvas Expander: Canvas Operations > Crop to Paint Layer(s)
Tools > Scripts > Canvas Expander: Canvas Operations > Crop to Viewport
Tools > Scripts > Canvas Expander: Canvas Operations > Crop to Selection
Tools > Scripts > Canvas Expander: Canvas Operations > Scale Image By Zoom Level
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary Of View & Paint Layer(s)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary Of Active Layer
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary Of Selected Layer(s)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary Of Paint Layer(s)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary Of Viewport
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary By Active Layer Color
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary By Layer Color (Blue)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary By Layer Color (Green)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary By Layer Color (Yellow)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary By Layer Color (Orange)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary By Layer Color (Brown)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary By Layer Color (Red)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary By Layer Color (Purple)
Tools > Scripts > Canvas Expander: Selection Operations > Select Boundary By Layer Color (Grey)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle Selected Layer(s)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle By Active Layer Color
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle By Layer Color (Blue)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle By Layer Color (Green)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle By Layer Color (Yellow)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle By Layer Color (Orange)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle By Layer Color (Brown)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle By Layer Color (Red)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle By Layer Color (Purple)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Toggle By Layer Color (Grey)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate Selected Layer(s)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate By Active Layer Color
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate By Layer Color (Blue)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate By Layer Color (Green)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate By Layer Color (Yellow)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate By Layer Color (Orange)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate By Layer Color (Brown)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate By Layer Color (Red)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate By Layer Color (Purple)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Isolate By Layer Color (Grey)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle Selected Layer(s)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle Between Active Layer Color
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle By Layer Color (Blue)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle By Layer Color (Green)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle By Layer Color (Yellow)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle By Layer Color (Orange)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle By Layer Color (Brown)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle By Layer Color (Red)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle By Layer Color (Purple)
Tools > Scripts > Canvas Expander: Layer Visibility Operations > Cycle By Layer Color (Grey)

```

## Installation
Krita's [own guide](https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html)
