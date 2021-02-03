import webbrowser
from tkinter import *

f = open('StayTuned.html', 'w')


def writeHtml(msg):
    return f"""<!DOCTYPE html>
    <html>
        <body>
            <h1> {msg} </h1>
        </body>
    </html>
    """
f.write(writeHtml("Stay tuned for our amazing summer sale!"))

webbrowser.open_new("file:///C:/Users/sambl/OneDrive/Documents/GitHub/Pyhton_Projects/StayTuned.html")
f.close()


def SubmitChange():
    f = open('StayTuned.html', 'w')
    f.write(writeHtml(txt.get()))
    webbrowser.open("file:///C:/Users/sambl/OneDrive/Documents/GitHub/Pyhton_Projects/StayTuned.html", new=0)
    f.close()

window = Tk()

window.title("Web Page Maker")
window.geometry('350x200')

txt = Entry(window, width=20)
txt.grid(row=4, columnspan=2)


btn1 = Button(window, text="Submit", command=SubmitChange)
btn1.grid(row=5,column=5)

lbl = Label(window, text="Please enter the text you would like in your webpage!")
lbl.grid(column=0, row=0)


        

window.mainloop()
