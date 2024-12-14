import tkinter as tk

TextLabels = {}
ButtonLabels = {}
ImageLabels = {}

def initializeLabels(window, textColor, backgroundColor):

    Text1 = tk.Label(window, text = "Stats Tracker", font = ("Arial", 48), fg = textColor, bg = backgroundColor)
    Text1.place(relx = 0.5, rely = 0.06, anchor = "center")
    TextLabels['Text1'] = Text1
    
    def onImageClick():
        return

    imagepath = tk.PhotoImage(file = "src/images/hollinsrobotics.png")
    Button1 = tk.Button(window, image = imagepath, command = onImageClick)
    Button1.image = imagepath
    Button1.place(relx = 0.5, rely = 0.5, anchor = "center")
    ButtonLabels['Button1'] = Button1
    
    return TextLabels, ButtonLabels

def updateButtonLabel(LabelID, newText = None, newImagePath = None, newCommand = None,
                      newRelX = None, newRelY = None, newAnchor = None):
    
    if LabelID in ButtonLabels:
        button = ButtonLabels[LabelID]

    if newText is not None:
        button.config(text = newText, image = '')

    if newImagePath is not None:
        newImage = tk.PhotoImage(file = newImagePath)
        button.config(image = newImage, text = '')
        button.image = newImage
    
    if newCommand is not None:
        button.config(command = newCommand)

    if newRelX is not None or newRelY is not None or newAnchor is not None:
            currentPosition = button.place_info()
            button.place_forget()
            button.place(
                relx = newRelX if newRelX is not None else currentPosition.get('relx', 0.5),
                rely = newRelY if newRelY is not None else currentPosition.get('rely', 0.5),
                anchor = newAnchor if newAnchor is not None else currentPosition.get('anchor', 'center')
            )
    
            
def updateTextLabel(LabelID, newText = None, newFont = None, newTextColor = None,
                    newRelX = None, newRelY = None, newAnchor = None):
    
    if LabelID in TextLabels:
        label = TextLabels[LabelID]

        if newText is not None:
            label.config(text = newText)
        
        if newFont is not None:
            label.config(font = newFont)

        if newTextColor is not None:
            label.config(fg = newTextColor)

        if newRelX is not None or newRelY is not None or newAnchor is not None:

            currentPosition = label.place_info()
            label.place_forget()
            label.place(
                relx = newRelX if newRelX is not None else currentPosition.get('relx', 0.5),
                rely = newRelY if newRelY is not None else currentPosition.get('rely', 0.5),
                anchor = newAnchor if newAnchor is not None else currentPosition.get('anchor', 'center')
            )