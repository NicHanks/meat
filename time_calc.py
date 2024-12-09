
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



import tkinter 
from tkinter.constants import * 
tk = tkinter.Tk() 
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2) 
frame.pack(fill=BOTH,expand=1) 
label = tkinter.Label(frame, text="Hello, World") 
label.pack(fill=X, expand=1) 
button = tkinter.Button(frame,text="Exit",command=tk.destroy) 
button.pack(side=BOTTOM) 
tk.mainloop()


# MEAT cutting time calculator
"""The purpose of this program is to calculate the time it takes to execute a certain number of cuts, and track progress towards next quarter's quota."""

#times it takes to make each cut.
times = { # nameof cut : [time it takes to make each cut(in sec)]
    "Create_New" : [],
    "Trachea Cut" : [3],
    "Stomache Cut" : [5.5]
}

def menu():
    """Displays menu."""

    input = input(print("""\n
    Menu: \n
    Time Calculator (1) \n
    Tracker (2)\n
    Punch in (3)\n
    Punch out (4)\n
    Creat a new cut (name of the cut and the time needed to make the cut is required) (5) \n
    """))
    if input == 1:
        t_calc()
    elif input == 2:
        tracker()
    elif input == 3:
        clock_in()
    elif input == 4:
        clock_out()
    elif input == 5:
        new_cut()
    else:
        print("I'm sorry, please put in the number in integer format of the menu item you would like to execute: ")
        menu()

def tracker():
    """As well as, info generator (quota/above or below, count and weight"""
    weight_quota = 2000 #int in pounds
    pieces_quota = 700 #pieces
    meat = input(print("""Current progress: \n 
    Total weight (1)\n
    weight of each piece (2)
    (1)\n
    """))
    meat.Capitalize()
    meat_info = meats[meat]
    if input == 1:
        w = input(print("What's the total weight? "))
        cut = input(print("What is the type of cut? "))
        ans = w * cut
        print(f"The total amount is: {ans}")
    else input == 2:
        d 

def t_calc():
    """Return a function that can calculate how long it's going to take"""

    print(f"Her are your pre-loaded cuts: {times.keys()}")
    input = input(print("Which one would you like to use? "))
    if input == "Create New Cut":
        name = input(print("What's the name of the cut? "))
        time = input(print("How long does it take to complete the cut? "))
        times[name] = [time]
        input(print("cut added: (hit enter to continue) "))
        t_calc()
    elif input == times.keys():
        n = input(print("How many of these cuts do you plan on making? "))
        total = times[input] * n
        input(print(f"the {input} will take {total} to complete at {times[input]} per cut! (hit enter to continue)"))
    else: 
        input = input(print("Sorry, that didn't work. Please try again or type 'back' to head back. "))
        if input == 'back':
            menu()
        else:
            t_calc()
        

#     def number_of_slices(number_of_slices):
#         """Calculates time it takes to cut"""
#         total_time = time_it_takes_to_slices * number_of_slices
#         return total_time

#     # Return inner_echo
#     return number_of_slices

# # easy cut
# cut1 = create_type_of_slice(3)

# # tougher cut to do so it takes more time
# cut2 = create_type_of_slice(9)

# # Calculates time to do 3 cuts with a "cut1" type
# print(cut1(3), cut2(8),cut1(50000000),"seconds")

# name_of_cut = input(print("Okay, now, tell me the name of the cut: "))
# time_to_make_that_cut = int(input(print("That's great! Now tell me how long it takes to make that cut: (in seconds) ")))
# number_of_cuts = int(input(print("Now one last thing, how many cuts do you plan to make? ")))
# users_cut = create_type_of_slice(time_to_make_that_cut)


# user = create_type_of_slice(name_of_cut)
# print(f"Congratulations on using nic's software! to complete {number_of_cuts} {name_of_cut} cuts it would take {str(users_cut(number_of_cuts))} seconds. ")

#Next, create a list for the users to pick and choose from | and make sure when they're about to pic, they know how long it takes to make the cut. 
