import webbrowser
from tkinter import *

f = open('StayTuned.html', 'w')

f.write("""<!DOCTYPE html>
<html>
    <body>
        <h1> Stay tuned for our amazing summer sale! </h1>
    </body>
</html>
""")

webbrowser.open_new("file:///C:/Users/sambl/OneDrive/Documents/GitHub/Pyhton_Projects/StayTuned.html")
f.close()



window = Tk()

window.title("Web Page Maker")
window.geometry('350x200')

btn1 = Button(window, text="Submit", command=SubmitChange)
btn1.grid(row=5,column=5)

lbl = Label(window, text="Please enter the text you would like in your webpage!")
lbl.grid(column=0, row=0)

txt = Entry(window, width=20)
txt.grid(row=4, columnspan=2)


def SubmitCHange():
    


    




window.mainloop()
