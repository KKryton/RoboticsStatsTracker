import tkinter as tk # Tkinter GUI library native to Python.
import platform # Data retriever for the sole purpose of allowing the icon to be set properly on non-windows systems.
import ctypes # Library to manipulate C data types so the taskbar icon changes accordingly.
import os # OS library for file path error workarounds.

from src.logic.screenLogic import initializeLabels, updateTextLabel # Import logic from other files

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Makes sure the file directory is correct so assets can be retrieved.

SYSTEMWINDOW = tk.Tk() # Instantiate a new window.
SYSTEMWINDOW.title("Robotics Stats Tracker") # Window title.
SYSTEMWINDOW.geometry("1280x720") # Window resolution.

if platform.system() == "Windows":
    path = os.path.abspath("src/images/hollinsrobotics.ico")
    SYSTEMWINDOW.iconbitmap(path)
    app_id = "stats.tracker.hollins.robotics" # Needed for Windows to identify it as an application so it sets the icon.
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
else: # This if-else block sets the icon to the logo of Hollins Robotics. Windows uses .ico files; Mac and (some) Linux distributions use .png files.
    icon_image = tk.PhotoImage(file="src/images/hollinsrobotics.png")
    SYSTEMWINDOW.wm_iconphoto(True, icon_image)

SYSTEMWINDOW.resizable(False, False) # Disables window resizing. If changed, resizing may cause text to squish 

BackgroundColors = ["#1c1c1c"] # List to store background colors.
TextColors = ["#FFFFFF"] # List to store text colors.

SYSTEMWINDOW.configure(bg=BackgroundColors[0]) # Sets background color.

Labels = initializeLabels(SYSTEMWINDOW, TextColors[0], BackgroundColors[0])

SYSTEMWINDOW.mainloop() # Loop so the program doesn't expire.