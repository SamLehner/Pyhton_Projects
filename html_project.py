# Importing our modules we will need

import webbrowser
from tkinter import *

# Creating the HTML file if it doesnt exist
f = open('StayTuned.html', 'w')

# Created a function to create the html with a variable for the text in the body
def writeHtml(msg):
    return f"""<!DOCTYPE html>
    <html>
        <body>
            <h1> {msg} </h1>
        </body>
    </html>
    """
f.write(writeHtml("Stay tuned for our amazing summer sale!"))
# Opens in a new tab
webbrowser.open_new("file:///C:/Users/sambl/OneDrive/Documents/GitHub/Pyhton_Projects/StayTuned.html")
f.close()

# Function for commiting the text value the user puts in 
def SubmitChange():
    f = open('StayTuned.html', 'w')
    f.write(writeHtml(txt.get()))
    webbrowser.open("file:///C:/Users/sambl/OneDrive/Documents/GitHub/Pyhton_Projects/StayTuned.html", new=0)
    f.close()


# GUI CODE
window = Tk()

window.title("Web Page Maker")
window.geometry('350x200')

txt = Entry(window, width=20)
txt.grid(row=4, columnspan=2)

# Button to submit the text change
btn1 = Button(window, text="Submit", command=SubmitChange)
btn1.grid(row=5,column=5)

lbl = Label(window, text="Please enter the text you would like in your webpage!")
lbl.grid(column=0, row=0)


        

window.mainloop()
