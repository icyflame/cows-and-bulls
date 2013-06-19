from Tkinter import *

import tkFont

import tkMessageBox

alert = tkMessageBox.showinfo

SHOW_TOPBAR = True

def getGuess():

    flag = True

    while flag:

        flag = False

        root = Toplevel()

        root.title('Enter your guess')

        font2 = tkFont.Font(family='Helvetica',size=20)

        f = Frame(root)

        f.grid()

        f.grid_propagate(1)  ##size can change

        Label(f,text='Enter your guess:').grid(row=1,column=0)

        a = Entry(f,width=3)

        a.focus()

        a.grid(row=1,column=1)
        
        c = Button(f,text='Confirm',command=root.quit)

        c.grid(row=2,column=0)

        root.mainloop()

        guess = a.get()

        if not (len(guess) == 3):

            alert('INSTRUCTIONS','YOU DID NOT ENTER A THREE DIGIT NUMBER')

            root.destroy()

            flag = True

            continue

        try:

            int(guess)

        except:

            alert('INSTRUCTIONS','A NUMBER SHOULD HAVE DIGITS ONLY')

            root.destroy()

            flag = True

            continue
                

    root.destroy()    

    return (guess)

##Script level testing code.
##
##root = Tk()
##
##print getGuess()
##
##mainloop()
