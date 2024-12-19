
"""This converts any file type into a csv file type by hitting the play button."""

import pandas as pd

def convert_to_csv(x):
    file = input(print('What is the name of the excel file? '))
    df = pd.read_excel('/Users/nicholashanks/Documents/GitHub/JBS/' + file + ".xlsx")
    csv_file = input(print('What would you like to name the csv file? '))
    df.to_csv('/Users/nicholashanks/Documents/GitHub/JBS/' + csv_file + ".xlsx", index=False) 
    
convert_to_csv()

# create lambda function to make sure there isn't already a file that has the same name the user is wanting to use? 

