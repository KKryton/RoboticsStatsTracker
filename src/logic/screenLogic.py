import tkinter as tk

TextLabels = {} # Dict to store text labels.
ButtonLabels = {} # Dict to store buttons.
ImageLabels = {} # Dict to store image labels.
Screens = {"TitleScreen"} # Dict to store ScreenIDs.
CurrentScreen = None

# Empty button click function to be overwritten. 
def onButtonClick():
    return

def initializeLabels(window, textColor, backgroundColor):

# Some of these labels may go unused. They will be invisible(ish) by default in the center of
# the screen. Labels can be edited individually using their respective updateLabel() functions.


    # --------------- Text Labels ---------------

    Text1 = tk.Label(window, text = "", font = ("Arial", 10), fg = textColor, bg = backgroundColor)
    Text1.place(relx = 0.5, rely = 0.5, anchor = "center")
    TextLabels['Text1'] = Text1

    Text2 = tk.Label(window, text = "", font = ("Arial", 10), fg = textColor, bg = backgroundColor)
    Text2.place(relx = 0.5, rely = 0.5, anchor = "center")
    TextLabels['Text2'] = Text2

    Text3 = tk.Label(window, text = "", font = ("Arial", 10), fg = textColor, bg = backgroundColor)
    Text3.place(relx = 0.5, rely = 0.5, anchor = "center")
    TextLabels['Text3'] = Text3
    # All of these text labels appear invisible but can be repurposed.
    Text4 = tk.Label(window, text = "", font = ("Arial", 10), fg = textColor, bg = backgroundColor)
    Text4.place(relx = 0.5, rely = 0.5, anchor = "center")
    TextLabels['Text4'] = Text4

    Text5 = tk.Label(window, text = "", font = ("Arial", 10), fg = textColor, bg = backgroundColor)
    Text5.place(relx = 0.5, rely = 0.5, anchor = "center")
    TextLabels['Text5'] = Text5

    Text6 = tk.Label(window, text = "", font = ("Arial", 10), fg = textColor, bg = backgroundColor)
    Text6.place(relx = 0.5, rely = 0.5, anchor = "center")
    TextLabels['Text6'] = Text6


    # --------------- Image Labels ---------------

    imagepath = tk.PhotoImage(file = "")
    Image1 = tk.Label(window, image = imagepath, borderwidth = 0, bg = backgroundColor)
    Image1.place(relx = 0.5, rely = 0.5, anchor = "center")
    ImageLabels['Image1'] = Image1

    imagepath = tk.PhotoImage(file = "")
    Image2 = tk.Label(window, image = imagepath, borderwidth = 0, bg = backgroundColor)
    Image2.place(relx = 0.5, rely = 0.5, anchor = "center")
    ImageLabels['Image2'] = Image2

    imagepath = tk.PhotoImage(file = "")
    Image3 = tk.Label(window, image = imagepath, borderwidth = 0, bg = backgroundColor)
    Image3.place(relx = 0.5, rely = 0.5, anchor = "center")
    ImageLabels['Image3'] = Image3

    imagepath = tk.PhotoImage(file = "")
    Image4 = tk.Label(window, image = imagepath, borderwidth = 0, bg = backgroundColor)
    Image4.place(relx = 0.5, rely = 0.5, anchor = "center")
    ImageLabels['Image4'] = Image4


    # --------------- Buttons ---------------

    def onButtonClick():
        return # Overwritten function on a per-button basis.
    imagepath = tk.PhotoImage(file = "")
    Button1 = tk.Button(window, image = imagepath, command = onButtonClick, borderwidth = 0, bg = backgroundColor)
    Button1.image = imagepath
    Button1.place(relx = 0.5, rely = 0.5, anchor = "center")
    ButtonLabels['Button1'] = Button1

    def onButtonClick():
        return
    imagepath = tk.PhotoImage(file = "")
    Button2 = tk.Button(window, image = imagepath, command = onButtonClick, borderwidth = 0, bg = backgroundColor)
    Button2.image = imagepath
    Button2.place(relx = 0.5, rely = 0.5, anchor = "center")
    ButtonLabels['Button2'] = Button2

    def onButtonClick():
        return
    imagepath = tk.PhotoImage(file = "")
    Button3 = tk.Button(window, image = imagepath, command = onButtonClick, borderwidth = 0, bg = backgroundColor)
    Button3.image = imagepath
    Button3.place(relx = 0.5, rely = 0.5, anchor = "center")
    ButtonLabels['Button3'] = Button3

    def onButtonClick():
        return
    imagepath = tk.PhotoImage(file = "")
    Button4 = tk.Button(window, image = imagepath, command = onButtonClick, borderwidth = 0, bg = backgroundColor)
    Button4.image = imagepath
    Button4.place(relx = 0.5, rely = 0.5, anchor = "center")
    ButtonLabels['Button4'] = Button4
    
    return TextLabels, ButtonLabels, ImageLabels


def updateImageLabel(LabelID, newImagePath = None, newRelX = None, newRelY = None, newAnchor = None):
    
    if LabelID in ImageLabels:
        labelImage = ImageLabels[LabelID]

    if newImagePath is not None:
        newImage = tk.PhotoImage(file = newImagePath)
        labelImage.config(image = newImage)
        labelImage.image = newImage
    
    if newRelX is not None or newRelY is not None or newAnchor is not None:
            currentPosition = labelImage.place_info()
            labelImage.place_forget()
            labelImage.place(
                relx = newRelX if newRelX is not None else currentPosition.get('relx', 0.5),
                rely = newRelY if newRelY is not None else currentPosition.get('rely', 0.5),
                anchor = newAnchor if newAnchor is not None else currentPosition.get('anchor', 'center')
            )
        

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

# Arranges labels in such a way that sets the title screen
def setTitleScreen():

    updateTextLabel("Text1", newText = "Match Stats Tracker", newFont = ("Arial", 52), 
                    newRelX = 0.5, newRelY = 0.08, newAnchor = "center")
    updateTextLabel("Text2", newText = "Data", newFont = ("Arial", 32), 
                    newRelX = 0.297, newRelY = 0.25, newAnchor = "center")
    updateTextLabel("Text3", newText = "Stats", newFont = ("Arial", 32), 
                    newRelX = 0.703, newRelY = 0.25, newAnchor = "center")
    def dataIconClicked():
        setFileScreen()
    updateButtonLabel("Button1", newImagePath = "src/images/dataIcon.png", newCommand = dataIconClicked, 
                      newRelX = 0.2, newRelY = 0.3, newAnchor = "nw")
    def statIconClicked():
        pass
    updateButtonLabel("Button2", newImagePath = "src/images/statsIcon.png", newCommand = statIconClicked, 
                      newRelX = 0.8, newRelY = 0.3, newAnchor = "ne")
    

def setFileScreen():

    updateTextLabel("Text1", newText = "File Manager", newFont = ("Arial", 52), 
                    newRelX = 0.5, newRelY = 0.08, newAnchor = "center")
    updateTextLabel("Text2", newText = "New File", newFont = ("Arial", 32),
                    newRelX = 0.297, newRelY = 0.25, newAnchor = "center")
    updateTextLabel("Text3", newText = "Delete File", newFont = ("Arial", 32), 
                    newRelX = 0.5, newRelY = 0.25, newAnchor = "center")
    updateTextLabel("Text4", newText = "Add Data", newFont = ("Arial", 32), 
                    newRelX = 0.703, newRelY = 0.25, newAnchor = "center")
    def addFileIconClicked():
        pass
    updateButtonLabel("Button1", newImagePath = "src/images/addFileIcon.png", newCommand = addFileIconClicked, 
                      newRelX = 0.2, newRelY = 0.3, newAnchor = "nw")
    def deleteFileIconClicked():
        pass
    updateButtonLabel("Button2", newImagePath = "src/ images/deleteFileIcon.png", newCommand = deleteFileIconClicked, 
                      newRelX = 0.8, newRelY = 0.3, newAnchor = "ne")
    def addDataIconClicked():
        pass
    updateButtonLabel("Button3", newImagePath="src/images/addDataIcon.png")