
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


# MEAT cutting time calculator
"""The purpose of this program is to calculate the time it takes to execute a certain number of cuts and to track progress.
data:
#pounds per head | edible talo 88 inedible 98 #2 tallo 8.8 greece 9 meat bone 10lbs blood 8.8lbs | tallos inventories every night | 288/hr 244.8 month.avg. 269chain speed actual 260, 299 chain speed actual 263 | 265 harvestfloor"""

times = { #dict[nameof cut : [time it takes to make each cut(in sec)]]
    "Create_New" : [],
    "Trachea Cut" : [3],
    "Stomach Cut" : [5.5]}

dt_ed = [103.07, 98.52, 99.03, 100.71, 95.41, 97.50, 96.55, 96.77, 96.20, 94.25, 106.41, 100.92, 93.44, 95.34, 108.47, 95.71, 103.84, 99.99, 99.52, 96.87, 106.39, 100.36, 99.50, 95.27, 98.13, 101.03, 103.83, 96.06, 99.45, 98.56, 99.52, 103.51, 97.21, 98.28, 92.82, 96.52, 100.63, 110.46]  # Daily total edible
dt_id = [89.59, 91.26, 93.76, 84.51, 90.36, 87.91, 80.75, 83.34, 84.06, 78.26, 79.23, 86.48, 86.04, 85.69, 81.3, 85.66, 89.02, 84.53, 85.49, 103.45, 80.81, 84.24, 92.75, 84.24, 95.95, 87.53, 84.47, 99.21, 90.92, 84.19, 83.56, 81.85, 90.09, 88.12, 84.54, 89.06, 88.76, 93.91] # Daily total in-edible

rt_ed = np.cumsum(dt_ed) #running sums
rt_id = np.cumsum(dt_id)

ed_g = 75 #edible daily goal 


"""
dt_ed_RAW = [103.07, 98.52, 99.03, 100.71, 95.41, 97.50, 96.55,, 96.77, 96.20, 94.25, 106.41, 100.92, 93.44, 95.34, 108.47, 95.71, 103.84, NA, 99.99, 99.52, 96.87, 106.39, 100.36, 99.50, 95.27, 98.13, 101.03, 103.83, 96.06, 99.45, 98.56, 99.52, 103.51, 97.21, 98.28, 92.82, 96.52, 100.63, 110.46]
dt_id_RAW = [, 89.59, 91.26, 93.76, 84.51, 90.36, 87.91, 80.75, 83.34, 84.06, 78.26, 79.23, 86.48, 86.04, 85.69, 81.3, 85.66, 89.02, NA, 84.53, 85.49, 103.45, 80.81, 84.24, 92.75, 84.24, 95.95, 87.53, 84.47, 99.21, 90.92, 84.19, 83.56, 81.85, 90.09, 88.12, 84.54, 89.06, 88.76, 93.91]
#numpy:
i = np.where(dt_ed == 'NA')[0] #targeting specifically 'NA'
dt_ed[i] = np.nan #89.02, np.nan, 84.53...
dt_ed_RAW = list(filter(None, dt_ed_RAW)) #gets rid of extra gaps/spaces, or commas
dt_id_cleaned = np.nan_to_num(dt_id_raw, nan=0)  # Replace missing values with 0
dt_id_cleaned = dt_id_raw[~np.isnan(dt_id_raw)] #remove missing values
print(dt_ed)
#pandas:
dt_id_series = pd.Series(dt_id_RAW) 
dt_id_series = dt_id_series.replace('NA', np.nan) #better
dt_ed_RAW = [x for x in dt_ed_RAW if x] #gets rid of extra gaps/spaces, or commas
print(dt_edp)

#--- still need to figure out how to get rid of excess commas and still make them match
"""



def addrt(ed,id): #rtet = running total edible tallow
    global rt_ed #why is this not blue????
    global rt_id
    rt_ed += ed
    rt_id += id

# def daily_goals(et=75,it=80): #pph_et_g = pounds per head edible tallow goal
#     global ed_g
#     global id_g
#     ed_g = et
#     id_g = it
ed_g = 100 #normally is 75
id_g = 80

def quartly_goals(d=62): #d=day(s) 
    global ed_qg
    global id_qg
    ed_qg = ed_g * d
    id_qg = id_g * d

def menu():
    """Displays menu."""

    m_in = input(print("""
    Menu: 
    Time Calculator (1) 
    Tracker (2)\n"""))

    if m_in == "1":
        t_calc()
    elif m_in == "2":
        tracker()
    else:
        print("Please put in the number of the menu item you would like to execute: ")
        menu()

def tracker():
    """info generator (quota/above or below, count and weight"""
    def reach_goal(x,y): 
        try: 
            if x >= y:
                print("Great job! You've met your goal!!")
            elif x <= y:
                print("Lets reach the goal tommorrow!")
        except TypeError:
            print("please input integer and try again")
            tracker()
    ed = input(print("Good job on perferming a hard days work! Please input your pounds per head (pph) of edible tallow for the day here: "))
    reach_goal(int(ed),ed_g)
    dt_ed.append(ed)    # add to list

    id = input(print("That's great! Now please put your pounds per head (pph) of in-edible tallow for the day here: "))
    reach_goal(int(id),id_g)
    addrt(int(ed),int(id))
    dt_id.append(id)    # add to list

    display_charts()
    menu()

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


def display_charts():
    """chart #1: each day meat the goal, excess red or green"""
    #plt.style.use("ggplot") #changes style
    ar = np.array(dt_ed[-10:])
    ar = ar[::-1]
    ar = ar.astype(float)
    x = np.arange(len(ar))[::-1]
    goal = ed_g * np.ones(len(ar))
    goal2 = np.repeat(ed_g, len(ar))

    hgreen = ar - ed_g
    x1 = ar < ed_g
    hgreen[x1] = 0

    plt.bar(x,hgreen, bottom=hgreen,color="blue") # cuz green gets cut off
    hgray = ar
    x2 = ar >= ed_g
    hgray[x2] = ed_g
    plt.bar(x, hgray)  # need to mark either up to 75 or up to n in ar

    plt.bar(x, hgreen, bottom=hgray, color='green')
    y = ar > ed_g #maskface of Trues everywhere daily total is less than daily goal
    hreds = ed_g - ar #finding by how much
    hreds[y] = 0 #clearing the days where they didn't go under the daily goal. 
    plt.bar(x, hreds, bottom=ar, color='red') #need to find the goal - ar at those parts
    plt.xlabel('Days')
    plt.ylabel('Edible-Tallow')
    plt.title('Past Previous 10 Days')
    plt.legend()
    plt.show()



    """we got bar yellow, green shaving the tops off whereever it's past 75, the we got red to fill the gaps: bottom= list of values that are under 75, top= list of values that are 75- what ever the list of bottoms are. """

    # plt.fill_between(range(len(dt_ed)), rt_ed, ed_g, where=(rt_ed >= ed_g), color='green', alpha=0.2, label='Goal Met')
    # plt.axhline(y=ed_g, color='r', linestyle='--', label='Daily Goal')
    # plt.plot(dt_ed, cumulative_goal, color='r', linestyle='--', label='Daily Goal Accumulation')
    # plt.legend()
    # plt.grid(True)

menu()

"""
    plt.figure(figsize=(8, 6))
    plt.plot(rt_ed, label='Running Total')
    plt.axhline(y=ed_g, color='r', linestyle='--', label='Daily Goal')
    plt.axhline(y=ed_qg, color='g', linestyle='--', label='Quartly Goal')
    plt.xlabel('Days')
    plt.ylabel('Total')
    plt.title('Running Total vs. Goals (Without Dates)')
    plt.xticks(np.arange(len(rt_ed)))  # Set x-axis labels based on data length
    plt.legend()
    plt.grid(True)


    # Plotting (without dates on x-axis)
    plt.figure(figsize=(8, 6))
    plt.plot(running_total, label='Running Total')
    plt.axhline(y=daily_goal, color='r', linestyle='--', label='Daily Goal')
    plt.axhline(y=annual_goal, color='g', linestyle='--', label='Annual Goal')

    # Customize the plot (adjust x-axis labels if needed)
    plt.xlabel('Days')
    plt.ylabel('Total')
    plt.title('Running Total vs. Goals (Without Dates)')
    plt.xticks(np.arange(len(daily_totals)))  # Set x-axis labels based on data length
    plt.legend()
    plt.grid(True)
    

    plt.show()
    """



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

#read/write into file dt_ed and dt_id
#be able to set new goal from the user. 
#Next, create a list for the users to pick and choose from | and make sure when they're about to pic, they know how long it takes to make the cut. 
#inthe future could add date/time on graph in create a list to hold date/time. 
## import tkinter 
# from tkinter.constants import * #might  use tkinter, need it for the buttons... (eventually)
