#The football.csv file contains the results from the English Premier League.
# The columns labeled Goals and Goals Allowed contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in for and against goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import pandas as pd
import os

data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'football.csv'))

# add a column of absolute difference btw for and against goals
data['diff'] = abs(data.Goals - data['Goals Allowed'])

# get the row with the lowest difference as a Series
min_diff_team = data.iloc[data['diff'].idxmin(axis=0)]

print "Team with the smallest difference in 'for' and 'against' goals:"
print min_diff_team.Team
