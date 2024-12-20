import tkinter as tk

TextLabels = {} # Dict to store text labels.
ButtonLabels = {} # Dict to store buttons.
ImageLabels = {} # Dict to store image labels.

# Default button command to satisfy parameter requirements.
# Button functions will eventually get overwritten by new functions. 
def onButtonClick():
    pass

def initializeLabels(window, textColor, backgroundColor):

# Some of these labels may go unused. They will be invisible(ish) by default in the center of
# the screen. Labels can be edited individually using their respective updateLabel() functions.
# Originally each label was created individually but I had a HUGE BRAIN IDEA and converted it
# to while loops to create labels. If more labels are needed, just increase how many loops it does.
# Not only is it easier to make more labels, its also super efficient because its three while
# loops and not 200 lines of code!

    # --------------- Text Labels ---------------

    loopCount = 1

    while loopCount < 10:
        TextID = tk.Label(window, text = "", font = ("Arial", 10), fg = textColor, bg = backgroundColor)
        TextID.place(relx = 0.5, rely = 0.5, anchor = "center")
        TextLabels['Text' + str(loopCount)] = TextID
        loopCount = loopCount + 1
        if loopCount > 10:
            break

    # --------------- Image Labels ---------------

    loopCount = 1

    while loopCount < 5:
        imagepath = tk.PhotoImage(file = "")
        ImageID = tk.Label(window, image = imagepath, borderwidth = 0, bg = backgroundColor)
        ImageID.place(relx = 0.5, rely = 0.5, anchor = "center")
        ImageLabels['Image' + str(loopCount)] = ImageID
        loopCount = loopCount + 1
        if loopCount > 5:
            break

    # --------------- Buttons ---------------

    loopCount = 1

    while loopCount < 15:
        imagepath = tk.PhotoImage(file = "")
        ButtonID = tk.Button(window, image = imagepath, command = onButtonClick, borderwidth = 0, bg = backgroundColor)
        ButtonID.image = imagepath
        ButtonID.place(relx = 0.5, rely = 0.5, anchor = "center")
        ButtonLabels['Button' + str(loopCount)] = ButtonID
        loopCount = loopCount + 1
        if loopCount > 15:
            break

    return TextLabels, ButtonLabels, ImageLabels

def resetLabels():
    for TextID in TextLabels:
        updateTextLabel(TextID, newText = "", 
                        newRelX = 0.5, newRelY = 0.5, newAnchor = "center")
    for ImageID in ImageLabels:
        updateImageLabel(ImageID, newImagePath = "", 
                         newRelX = 0.5, newRelY = 0.5, newAnchor = "center")
    for ButtonID in ButtonLabels:
        updateButtonLabel(ButtonID, newImagePath = "", newCommand = onButtonClick, 
                          newRelX = 0.5, newRelY = 0.5, newAnchor = "center")
    return TextLabels, ButtonLabels, ImageLabels


# Label update functions simply take parameters given to them then adjust the config for the specific object.
# For example, updateTextLabel("Text3", newText = "profanity is my fav coding language", newFont = ("Arial", 32))
# changes Text Box 3 to say "profanity is my fav coding language" with the Arial font at size 32.
# updateImageLabel("Image1", newImagePath = 'path/to/my/image.png') changes Image 1 to whatever the path goes to.

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

    resetLabels()

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
    
# Arranges labels in such a way that sets the file screen
def setFileScreen():

    resetLabels()

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
                      newRelX = 0.297, newRelY = 0.5, newAnchor = "center")
    def deleteFileIconClicked():
        pass
    updateButtonLabel("Button2", newImagePath = "src/images/deleteFileIcon.png", newCommand = deleteFileIconClicked, 
                      newRelX = 0.5, newRelY = 0.5, newAnchor = "center")
    def addDataIconClicked():
        pass
    updateButtonLabel("Button3", newImagePath="src/images/addDataIcon.png", newCommand = addDataIconClicked,
                      newRelX = 0.703, newRelY = 0.5, newAnchor = "center")
    updateButtonLabel("Button4", newImagePath = "src/images/x.png", newCommand = setTitleScreen,
                      newRelX = 0.95, newRelY = 0.05, newAnchor = "center")