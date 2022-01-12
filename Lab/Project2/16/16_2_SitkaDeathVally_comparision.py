import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename_sitka = '/Users/lalazhou/Code/PyCrashCourse/Lab/Project2/16/data/sitka_weather_2018_simple.csv'
filename_death = '/Users/lalazhou/Code/PyCrashCourse/Lab/Project2/16/data/death_valley_2018_simple.csv'

with open(filename_sitka) as f_s:
    reader_s = csv.reader(f_s)
    header_row_s = next(reader_s)
    
    # Get dates, and high and low temperatures from this file.
    dates, s_highs, s_lows = [], [], []
    for row in reader_s:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        s_high = int(row[5])
        s_low = int(row[6])
        dates.append(current_date)
        s_highs.append(s_high)
        s_lows.append(s_low)

with open(filename_death) as f_d:
    reader_d = csv.reader(f_d)
    header_row_d = next(reader_d)
    
    # Get dates, and high and low temperatures from this file.
    dates, d_highs, d_lows = [], [], []
    for row in reader_d:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            d_high = int(row[4])
            d_low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            d_highs.append(d_high)
            d_lows.append(d_low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, s_highs, c='red', alpha=0.5)
ax.plot(dates, s_lows, c='blue', alpha=0.5)
plt.fill_between(dates, s_highs, s_lows, facecolor='blue', alpha=0.4)
ax.plot(dates, d_highs, c='red', alpha=0.5)
ax.plot(dates, d_lows, c='blue', alpha=0.5)
plt.fill_between(dates, d_highs, d_lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures, - 2018\nSitka and Death Valley", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10,130)

plt.show()


