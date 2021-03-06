#importing modules, all preinstalled normally
from threading import Thread
from tkinter import *
from random import randint
from time import sleep, time

"""
██████╗ ███████╗ █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗   ████████╗███████╗███████╗████████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║   ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██████╔╝█████╗  ███████║██║        ██║   ██║██║   ██║██╔██╗ ██║█████╗██║   █████╗  ███████╗   ██║   
██╔══██╗██╔══╝  ██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════╝██║   ██╔══╝  ╚════██║   ██║   
██║  ██║███████╗██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║      ██║   ███████╗███████║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝      ╚═╝   ╚══════╝╚══════╝   ╚═╝   
"""
print('Credits to https://github.com/xtekky')

#defining a class
class Reactiontest:
    
    #setting up GUI
    def __init__(self):
        self.window = Tk()
        self.window.geometry('1031x580') #window dimasion
        self.window.title("Reaciton Time Test - Credits to Github xtekky") #window title
        self.window.config(bg='#2b353f')
        self.scores = []
        self.react_ready = False
        self.start_time = None
        self.valid_round = True
        self.round = 0

        # setting up a startt button
        self.start_button = Button(self.window, text='CLICK TO START', fg='#1E272E', bg='WHITE', font='Calibri 26 bold', bd=0, width=20, command= lambda: (self.start(), self.start_button.place_forget()))
        self.start_button.place(relx=.340625, rely=.425)

        # displaying GUI
        self.window.mainloop()

    #reset function if user clicks too early
    def reset(self):
        self.window.unbind("<Button-1>")
        self.start_button.place(relx=.340625, rely=.425)
        self.scores = []
        self.round = 0
        self.valid_round = True

    #start function - when user presses start button
    def _start(self):
        sleep(randint(750, 2250) / 1000)
        if self.valid_round:
            self.window.config(bg='#576574')
            self.start_time = time()
            self.react_ready = True

    def start(self):
        if self.round != 1:
            self.window.bind("<Button-1>", lambda event: self.register())
            Thread(target=self._start).start()
        else:
            self.end()

    # register function
    def register(self):
        if self.react_ready:
            self.scores.append(time() - self.start_time)
            self.window.config(bg='#1E272E')
            self.react_ready = False
            self.round += 1
            self.start()

        else:
            self.valid_round = False
            self.early()

    # function if user clicks too early
    def _early(self):
        self.window.config(bg='#1E272E')
        warning = Label(self.window, text="!", bg='white', fg='#1E272E', font='Calibri 60 bold', width=2)
        warning.place(relx=.27, rely=.4)
        early = Label(self.window, text="You clicked too early!\nRestarting in 1 second...", justify=LEFT, bg='#1E272E', fg='WHITE', font='Calibri 30 bold')
        early.place(relx=.37, rely=.4)
        sleep(1)
        warning.place_forget()
        early.place_forget()
        self.reset()

    def early(self):
        Thread(target=self._early).start()\

    #function to replay test when finished
    def end(self):
        score_items = []
        score_avg = Label(self.window, text=" ".join(f'REACTION TIME: {int((sum(self.scores) / 1) * 1000)}ms'), bg='#1E272E', fg='WHITE', font='Calibri 24 bold')
        score_avg.place(relx=.25, rely=.35)
        restart = Button(self.window, text="▶", bg='#1E272E', fg='WHITE', font='Calibri 30', height=1, bd=0, command=lambda: ([item.place_forget() for item in score_items], self.reset()))
        restart.place(relx=.691, rely=.32)
        score_items.extend((score_avg, restart))
        self.window.unbind("<Button-1>")


#starting script
if __name__ == '__main__':
    Reactiontest()
    
    
