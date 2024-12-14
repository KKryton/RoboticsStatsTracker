import tkinter as tk # Tkinter GUI library native to Python.
import platform # Data retriever for the sole purpose of allowing the icon to be set properly on non-windows systems.

SYSTEMWINDOW = tk.Tk() # Instantiate a new window.
SYSTEMWINDOW.title("Robotics Stats Tracker") # Window title.
SYSTEMWINDOW.geometry("1280x720") # Window resolution.

if platform.system() == "Windows":
    SYSTEMWINDOW.iconbitmap("src/images/hollinsrobotics.ico")
else: # This if-else block sets the icon to the logo of Hollins Robotics. Windows uses .ico files, mac and linux use .png files.
    icon_image = tk.PhotoImage(file="src/images/hollinsrobotics.png")
    SYSTEMWINDOW.wm_iconphoto(True, icon_image)

SYSTEMWINDOW.resizable(False, False) # Disables window resizing. If changed, resizing may cause text to squish 

BackgroundColors = ["#1c1c1c"] # List to store background colors.
TextColors = ["#FFFFFF"] # List to store text colors.
SYSTEMWINDOW.configure(bg=BackgroundColors[0]) # Sets background color/

text_label = tk.Label(SYSTEMWINDOW, text="Data Tracker", font=("Arial", 48), fg=TextColors[0], bg=BackgroundColors[0])
text_label.place(relx=0.5, rely=0.06, anchor="center")


SYSTEMWINDOW.mainloop() # Loop so the program doesn't expire.