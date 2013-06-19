from Tkinter import *

import tkMessageBox

alert = tkMessageBox.showinfo

import tkFont

SHOW_TOPBAR = True

class CowsAndBulls:

    def __init__(self):

        self.window = Tk()

        self.window.title('Notes')

        self.initFrameAndButtons()

        #self.makeFullScreen()

    def makeFullScreen(self):

        root = self.window

        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(not SHOW_TOPBAR)
        root.geometry("%dx%d+0+0" % (w, h))

    def initFrame(self):

        try:

            self.frame.destroy()

        except:

            pass

        self.frame = Frame(self.window)

        self.frame.pack()

    def initFrameAndButtons(self):

        self.initFrame()

        listOfButtons = []

        self.big  = tkFont.Font(family='helvetica',size=24)

        listOfButtons.append(Button(self.frame,text='New game',command=self.startNewGame))
        
        listOfButtons.append(Button(self.frame,text='QUIT',command=self.quitwin,fg='black',bg='red'))

        
        for i in range(len(listOfButtons)):

            listOfButtons[i]['font']=self.big

            listOfButtons[i].pack(side='top')

    def startNewGame(self):

        import random

        comp = ''

        for i in range(3):

            comp += str(random.choice(range(1,10,1)))

        print comp

        comp = int(comp)

        self.initFrame()

        self.frame.grid()

        import getGuess

        GameOver = False

        f = self.frame

        global counter

        counter = 1

        Label(f,text='Guess').grid(row=counter,column=1)

        Label(f,text='Numbers in the correct place').grid(row=counter,column=2)

        Label(f,text='Numbers in the wrong place').grid(row=counter,column=3)

        counter += 1

        a= StringVar()

        def done():

            def validate():

                if not (len(guess) == 3):

                    alert('INSTRUCTIONS','YOU DID NOT ENTER A THREE DIGIT NUMBER')

                    return

                try:

                    int(guess)

                except:

                    alert('INSTRUCTIONS','A NUMBER SHOULD HAVE DIGITS ONLY')

                    return

            global counter
        
        #while not GameOver:

            #a = (getGuess.getGuess())

            ##now the variable 'a' has all the new numbers. it is a string.

            b = str(a.get())

            numbers = [int(i) for i in b]

            compNum = [int(i) for i in str(comp)]

            correctPlace = 0

            wrongPlace = 0

            Comp = compNum[:]
            User = numbers[:]

            for x in Comp:

                if x in User:

                    if Comp.index(x) == User.index(x):

                        correctPlace += 1

                    else:

                        wrongPlace += 1

            if correctPlace == 3:

                GameOver = True
                self.gameOver()

            print correctPlace,wrongPlace

            Label(f,text=str(a.get())).grid(row=counter,column=1)

            Label(f,text=str(correctPlace)).grid(row=counter,column=2)

            Label(f,text=str(wrongPlace)).grid(row=counter,column=3)

            counter += 1

        Entry(f,textvariable=a,width=3).grid(row=0,column=0)

        Button(f,text='submit',command=done).grid(row=0,column=1)

    def gameOver(self):

        alert('Game over','Congrats! you win!')

        self.initFrameAndButtons()
            

    def quitwin(self):

        self.initFrame()

        self.frame.grid()

        self.frame.grid_propagate(1)

        self.big  = tkFont.Font(family='helvetica',size=24)

        r = self.frame

        c = 0
        

        Label(r,text='Created by Siddharth Kannan',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Written on Python 2.7 and Tkinter 8.5',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='OS: LINUX MINT 14 NADIA',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='This software is licensed under the WTFPL license.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='See the copying file for more details.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Application will quit in 8 seconds.',font=self.big).grid(row=c,column=0)
        c+=1

        self.window.after(8000,self.window.destroy)

CowsAndBulls()

mainloop()       

