import shutil
import os.path, time, datetime
from datetime import timedelta
from tkinter import *
from tkinter import filedialog
import tkinter as tk

source = 'C:/Users/sambl/OneDrive/Documents/GitHub/Pyhton_Projects/Modified/'
destination = 'C:/Users/sambl/OneDrive/Documents/GitHub/Pyhton_Projects/Transfer/'

files = os.listdir(source)

for file in files:
    path = os.path.join(source, file)
    if os.path.isfile(path):
        mod_time = time.ctime(os.path.getmtime(path))
        now = datetime.datetime.now()
        print(datetime.datetime.strptime(mod_time, '%c'), datetime.datetime.now())

        hours_to_sub = 24
        new_now = now - timedelta(hours = hours_to_sub)
        if ((datetime.datetime.strptime(mod_time, '%c') >= new_now)):
            shutil.move(source+file, destination)
    


# Function for opening the file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "C:/Users/sambl/OneDrive/Documents/GitHub/Pyhton_Projects/Modified",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

window = Tk()

window.title('File Explorer')
window.geometry("700x300")
window.config(background = "white")


label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")

button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)

button_exit = Button(window,
                     text = "Exit",
                     command = exit)

# Grid method for placing widgets
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1, row = 3)

# Let the window wait for any events
window.mainloop()
