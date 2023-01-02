'''
Writing Name randomizer inspired by:
https://wheelofnames.com/ 
'''
from tkinter import *
from tkinter import messagebox
import random 


root = Tk()
root.title("Name Randomizer GUI")
root.geometry("1000x600")

global name_list 
name_list = []


def print_out(text_input):
    name_list.append(text_input)
    my_label.config(text = text_input )
    # print(name_list)
    e3.delete(0,'end')


def randomize_name():
    len_list = len(name_list)
    return random.randint(0,len_list-1)


def winner_window():
    global pop
    pop = Toplevel(root) # new pop up window
    pop.geometry("400x400")
    pop.title("Winner")
    winner_num = randomize_name()
    q_label = Label(pop, text= "The winner is " + name_list[winner_num] + " !")
    q_label.pack()


# Name label and to get the data
name_label = Label(root, text= "Name: ")
name_label.grid(row=1,column=0,pady=40)
e3 = Entry(root,width=35,borderwidth=5)
e3.grid(row=1,column=1,pady=40)

# add button to get the data
add_button = Button(root, text = "Add",command=lambda: print_out(e3.get()))
add_button.grid(row=1,column=2,pady=40)

# label 
my_label = Label(root,text="")
my_label.grid(row=2,column=2,pady=40)

# add button to get the data
add_button = Button(root, text = "Randomize",command=winner_window)
add_button.grid(row=2,columnspan=2,pady=40)
root.mainloop()