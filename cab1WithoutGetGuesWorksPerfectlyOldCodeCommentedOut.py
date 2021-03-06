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

        self.initMenu()

        #self.makeFullScreen()

    def initMenu(self):

        menubar = Menu(self.window)

        filemenu = Menu(menubar,tearoff = 0)

        filemenu.add_command(label='Start a new game',command=self.startNewGame,accelerator='N')
        filemenu.add_command(label='Quit',command=self.quitwin,accelerator='Escape')
        
        helpmenu = Menu(menubar,tearoff=0)

        helpmenu.add_command(label='Help',command=self.showHelp)
        helpmenu.add_command(label='About',command=self.showCredits)

        menubar.add_cascade(label='File',menu=filemenu)
        menubar.add_cascade(label='Help',menu=helpmenu)

        self.window.config(menu=menubar)

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

        comp += str(random.choice(range(1,10,1)))

        for i in range(2):

            comp += str(random.choice(range(10)))

        comp = int(comp)

        comp = 277

        #print comp

        self.initFrame()

        self.frame.grid()
        
        GameOver = False

        f = self.frame

        global counter

        counter = 1

        Label(f,text='Guess',width=15).grid(row=counter,column=1)

        Label(f,text='BULLS',width=15).grid(row=counter,column=2)

        Label(f,text='COWS',width=15).grid(row=counter,column=3)

        counter += 1

        a= StringVar()           

        def validate(ev=None):

            '''function will check if or not the given three digit string
                which is now inside the string var 'a' and will be obtained
                by a.get() is a valid three digit number or not.


                it will first check if there are three digits. if there are then
                it will check if these three characters are digits.

                if both these conditions are satisfied then it will call the function
                done() which will add to the output thus giving useful information
                to the user.

                if not then the relevant error message is shown and then we wait for
                the next input from the user.'''

            flag = True

            guess = str(a.get())

            if not (len(guess) == 3):

                alert('INSTRUCTIONS','YOU DID NOT ENTER A THREE DIGIT NUMBER')

                flag = False

            else:

                try:

                    int(guess)

                except:

                    alert('INSTRUCTIONS','A NUMBER SHOULD HAVE DIGITS ONLY')

                    flag = False

            if flag:

                done()

            else:

                a.set('')

                return


        def done():

            '''this function will be called when it is decided that the user
                entered a valid three digit number.

                this function will check the relevant cows and bulls thing and
                then update the output for the user.'''

            b = str(a.get())

            numbers = [int(i) for i in b]

            compNum = [int(i) for i in str(comp)]

            bulls = 0

            cows = 0


            bulls, cows = bulls_and_cows(b,comp)
            
            if  str(a.get()) == str(comp):

                GameOver = True
                self.gameOver()

            #print correctPlace,wrongPlace

            global counter

            Label(f,text=str(a.get())).grid(row=counter,column=1)

            Label(f,text=str(bulls)).grid(row=counter,column=2)

            Label(f,text=str(cows)).grid(row=counter,column=3)

            counter += 1

            a.set('')


##            Comp = compNum[:]
##            User = numbers[:]
##
##            print 'considering:',User
##
##            print 'against',Comp
##
##
##            person = User
##
##            machine = Comp


        def digits(number):

            '''will return the list of digits in a number'''
            
            return [int(d) for d in str(number)]

        def bulls_and_cows(guess, target):

            '''returns a tuple of the number of bulls and the cows
               when guess is the number that is given by the user and
                target is the number randomly selectedby the computer'''
            
            guess, target = digits(guess), digits(target)
            
            bulls = [d1 == d2 for d1, d2 in zip(guess, target)].count(True)
            
            cows = 0
            
            for digit in set(guess):
                
              cows += min(guess.count(digit), target.count(digit))
              
            return bulls, cows - bulls



            

##            for i in range(3):
##
##                if machine[i] == person[i]:
##
##                    bulls += 1'


##FIX 2. DOES NOT WORK WHEN THERE ARE REPEATED DIGITS IN THE NUMBER GUESSED BY USER AND BY COMPUTER:

##            LIKE 277 AND 477. THERE IS DOUBLE COUNTING. AND IT SHOWS 2 BULLS AND 2 COWS
##
##            for x in range(3):
##
##                print 'x:',x
##
##                for y in range(3):
##
##                        print 'y:',y
##
##                        if x == y and machine[x] == person[y]:
##
##                            print 'bull'
##
##                            bulls += 1
##
##                        if not (x == y) and machine[x] == person[y]:
##
##                                print machine[x],':',person[y]
##
##                                print 'cow'
##
##                                cows += 1


##FIX 1


##            for x in machine:
##
##                for y in person:
##
##                    if machine.index(x) == person.index(y):
##
##                        continue
##
##                    else:
##
##                        if  x == y:
##
##                            cows += 1


##CODE THAT DOES NOT WORK WHEN THERE ARE REPEATED DIGITS IN THE NUMBER RANDOMLY SELECTED BY COMPUTER

            
##            for x in User:
##
##                if x in Comp:
##
##
##                    if Comp.index(x) == User.index(x):
##
##                        bulls += 1
##
##                        print x,' in correct place'
##
##                    else:
##
##                        print x,' in wrong place'
##
##                        cows += 1


        d = Entry(f,textvariable=a,width=3)

        d.grid(row=0,column=0)

        d.focus()        
        
        self.window.bind('<Return>',validate)

        Button(f,text='submit',command=validate).grid(row=0,column=1)

        Button(f,text='Main Menu',command=self.initFrameAndButtons).grid(row=0,column=2)

    def gameOver(self):

        alert('Game over','Congrats! you win!')

        self.initFrameAndButtons()


    def showHelp(self):

        pass


    def showCredits(self):

        pass
            

    def quitwin(self):

        self.window.destroy()

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

##        self.window.after(8000,self.window.destroy)

CowsAndBulls()

mainloop()       

