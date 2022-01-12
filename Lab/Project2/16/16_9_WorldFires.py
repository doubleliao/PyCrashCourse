import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = '/Users/lalazhou/Code/PyCrashCourse/Lab/Project2/16/data/world_fires_7_day.csv'

row_number_max = 20000

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
        
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    
    # Get dates, and high and low temperatures from this file.
    lats, lons, bris, hover_texts = [], [], [], []
    row_number = 0
    
    for row in reader:
        
        lat = float(row[0])
        lon = float(row[1])
        bri = float(row[2])
        hover_text = f"brightness: {bri}     date: {datetime.strptime(row[5], '%Y-%m-%d')}"
        hover_texts.append(hover_text)
        lats.append(lat)
        lons.append(lon)
        bris.append(bri)
            
        row_number += 1
        if row_number == row_number_max:
            break
            

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [bri/20 for bri in bris],
        'color': bris,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'brightness'}
    },
}]
my_layout = Layout(title='Fires Brightness')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='fire_brightness.html')
    