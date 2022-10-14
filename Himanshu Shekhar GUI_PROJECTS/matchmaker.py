import random
import time
from tkinter import Tk ,Button,DISABLED


def show_symbol(x,y):
    global first
    global previousx, previousy
    buttons[x,y]['text']=button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previousx=x
        previousy=y
        first=False
    elif previousx!=x or previousy!=y:
        if buttons[previousx,previousy]['text']!=buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text']=' '
            buttons[x,y]['text']=' '

        else:
            buttons[previousx,previousy]['command']=DISABLED
            buttons[x,y]['command']=DISABLED
        first=True

win=Tk()
win.resizable(width=False,height=True)
win.title("Matchmaker")

first=False
previousx=0
previousy=0

buttons={}
button_symbols={}
symbols=[u'\u2702',u'\u2703',u'\u2704',u'\u2705',u'\u2706',u'\u2707',u'\u2708',
            u'\u270C',u'\u270A',u'\u270D',u'\u2709',u'\u270E',u'\u270F',u'\u270B',
            u'\u2702',u'\u2703',u'\u2704',u'\u2705',u'\u2706',u'\u2707',u'\u2708',
            u'\u270C',u'\u270A',u'\u270D',u'\u2709',u'\u270E',u'\u270F',u'\u270B']
random.shuffle(symbols)




for x in range(7):
    for y in range(4):
        button= Button(command = lambda x=x,y=y : show_symbol(x,y),width=10,height=6)
        button.grid( column =x,row=y)
        buttons[x,y]=button
        button_symbols[x,y]=symbols.pop()


win.mainloop()
