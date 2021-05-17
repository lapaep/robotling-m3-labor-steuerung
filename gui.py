from tkinter import *
import main

m = main.Main()
m.connect()


root = Tk()
root.geometry("400x400")

motorWalkspeed = 0
motorTurnspeed = 0

w = False
s = False
a = False
d = False
boost = False

def keypress(event):
    global w,s,a,d,boost
    if event.char == "w":
        w = True
    elif event.char == "s":
        s = True
    elif event.char == "a":
        a = True
    elif event.char == "d":
        d = True
    elif event.keysym == "space":
        boost = True
    
    m.publish(w,a,s,d,boost)


def keyrelease(event):
    global w,s,a,d,boost
    if event.char == "w":
        w = False
    elif event.char == "s":
        s = False
    elif event.char == "a":
        a = False
    elif event.char == "d":
        d = False
    elif event.keysym == "space":
        boost = False

    m.publish(w,a,s,d,boost)



root.bind("<KeyPress>", keypress)
root.bind("<KeyRelease>", keyrelease)

root.mainloop()
