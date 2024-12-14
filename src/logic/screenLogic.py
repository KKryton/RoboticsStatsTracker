import tkinter as tk

def initializeLabels(window, textColor, backgroundColor):
    Labels = {}

    Label1 = tk.Label(window, text="Stats Tracker", font=("Arial", 48), fg=textColor, bg=backgroundColor)
    Label1.place(relx=0.5, rely=0.06, anchor="center")
    Labels['Label1'] = Label1
    
    def onImageClick():
        return

    imagepath = tk.PhotoImage(file="src/images/hollinsrobotics.png")
    ButtonLabel1 = tk.Button(window, image=imagepath, command=onImageClick)
    ButtonLabel1.image = imagepath
    ButtonLabel1.place(relx=0.5, rely=0.5, anchor="center")
    Labels['ButtonLabel1'] = ButtonLabel1
    
    return Labels

def updateTextLabel(Labels, LabelID, newText = None, newFont = None, newFontSize = None, 
                    newTextColor = None, newRelX = None, newRelY = None, newAnchor = None):
    
    if LabelID in Labels:
        label = Labels[LabelID]

        if newText is not None:
            label.config(text=newText)
        
        if newFont is not None:
            label.config(font=newFont)
        
        if newFontSize is not None:
            label.config(size=newFontSize)

        if newTextColor is not None:
            label.config(fg=newTextColor)

        if newRelX is not None or newRelY is not None or newAnchor is not None:

            current_position = label.place_info()
            label.place_forget()
            label.place(
                relx=newRelX if newRelX is not None else current_position.get('relx', 0.5),
                rely=newRelY if newRelY is not None else current_position.get('rely', 0.5),
                anchor=newAnchor if newAnchor is not None else current_position.get('anchor', 'center')
            )