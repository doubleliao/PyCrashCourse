"""
sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair amount of
rainfall. In the data file sitka_weather_2018_simple.csv is a header called PRCP,
which represents daily rainfall amounts. Make a visualization focusing on the
data in this column. You can repeat the exercise for Death Valley if you're curious
how little rainfall occurs in a desert.
    
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '/Users/lalazhou/Code/PyCrashCourse/Lab/Project2/16/data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    
    # Get dates, and high and low temperatures from this file.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            prcp = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            prcps.append(prcp)

# Plot the rainfall amount.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='blue')

# Format plot.
title = "Daily rainfall amounts, - 2018\nSitka"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("rainfall amounts", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
    