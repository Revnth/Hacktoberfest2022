# Importing tkinter and random modules
from tkinter import *
import random


window = Tk()
window.configure(bg="#080808")

window.geometry("550x350")

window.title("virtual dice ")



# Creating function to roll the dices
def roll_dices():
	#dot codes
	dice_dots = ['\u2680', '\u2681',
				'\u2682', '\u2683',
				'\u2684', '\u2685']
	
	label.configure(
		text=f'{random.choice(dice_dots)}')
	label.pack()


#button for rolling
roll_button = Button(window, text="GENERATE",width=30, height=1,font=15, bg="#08b106",bd=3, command=roll_dices)

#position
roll_button.pack(padx=2, pady=10)

#Label
label = Label(window, font=("Helvetica", 200),
			bg="#080808", fg="#00CC66")

window.mainloop()
