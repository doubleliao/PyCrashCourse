
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '/Users/lalazhou/Code/PyCrashCourse/Lab/Project2/16/data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    print(header_row)
    dates_index = header_row.index('DATE')
    highs_index = header_row.index('TMAX')
    lows_index = header_row.index('TMIN')
    names_index = header_row.index('NAME')
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    # Get dates, and high and low temperatures from this file.
    dates, highs, lows, names = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[dates_index], '%Y-%m-%d')
        try:
            high = int(row[highs_index])
            low = int(row[lows_index])
            name = str(row[names_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            if name not in names:
                names.append(name)


# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.9)
ax.plot(dates, lows, c='blue', alpha=0.9)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = f"Daily high and low temperatures, - 2018\n {name}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()