import pandas as pd
from datetime import datetime
import sys

'''
Parse the date as it is read from the excel file.
NOTE: this currently does nothing since the dates
I've been reading in have all been pandas.Timestamp()
but we will need to parse if we find out this doesn't 
always work.

date - unknown type, date as read from excel file
'''
def parse_date(date) -> pd.Timestamp:

    return date


'''
Calculate age based on a date.

date - pandas Timestamp object as read from the excel file
'''
def is_21(date: pd.Timestamp) -> int:
   
    # Function currently does nothing, but it might be necessary 
    # later to parse the date in some way
    date = parse_date(date)

    # Get the current date as pandas timestamp object
    curr_time = pd.Timestamp.now()
    
    # Get time elapsed for year / month / days
    # The reason I didn't just subtract the timestamp / timedelta 
    # objects is because it was calculated in days, and due to 
    # leap years, it was not possible to get an accurate years elapsed
    years_elapsed = curr_time.year - date.year
    months_elapsed = curr_time.month - date.month
    days_elapsed = curr_time.day - date.day
    
    # 21 years have passed, and the month and day of the DOB have passed too
    if years_elapsed >= 21 and months_elapsed <= 0 and days_elapsed <= 0:
        return True

    return False


'''
Main function
'''
def main():
   
    # Make sure input files are specified
    if not (len(sys.argv) == 3):
        print("Usage: " + sys.argv[0] + " <master list> <fraternity list>") 
        return

    
    # Read student database into data frame
    student_database_df = pd.read_excel(sys.argv[2])

    # Read fraternity excel file into data frame
    fraternity_df = pd.read_excel(sys.argv[1])



    for index, row in student_database_df.iterrows():
        
        # Boolean dataframe that matches conditions
        both_names_match = (student_database_df["Last Name"] == row["Last Name"]) & (student_database_df["First Name"] == row["First Name"])        
        
        # Preferred Name and last name match
        preferred_names_match = (student_database_df["Last Name"] == row["Last Name"]) & (student_database_df["Preferred Name"] == row["First Name"])
        
        # Student ID's match
        student_id_match = student_database_df["Student ID"] == row["Student ID"]




if __name__ == '__main__':
    main()

