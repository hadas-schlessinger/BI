from matplotlib.cm import viridis
from matplotlib.colors import to_hex
import matplotlib.cm
import pandas as pd
import gmaps
import gmaps.datasets
import gmaps.geojson_geometries
import gmplot
import numpy as np
import geopandas as gpd
import descartes
from shapely.geometry import Point
import matplotlib.pyplot as plt
import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import seaborn as sns
import os
import subprocess
import time
from selenium import webdriver


def generate_airports():
    try:
        airport = pd.read_excel('app/flights_data.xlsx', 'airports')
        airport.head()
        color_set = ["#5DADE2", "#F1C40F", "#E74C3C", "#3D3228", "#ECF0F1", "#73FF5B"]
        zones = airport['General_Time_Zone']
        unique_zones = zones.unique()
        plt.figure(figsize=(30, 20))
        m = Basemap(projection='gall')
        m.fillcontinents(color="#0D9C29", lake_color="blue")
        m.drawmapboundary(fill_color="#5D9BFF")
        m.drawcountries(color='#585858', linewidth=1)
        m.drawstates(linewidth=0.2)
        m.drawcoastlines(linewidth=1)
        i = 0
        for cont in unique_zones:
            X, Y = m(list(airport[airport.General_Time_Zone == cont].LONG),
                     list(airport[airport.General_Time_Zone == cont].LAT))
            m.scatter(X, Y, color=color_set[i], s=10, zorder=2)
            i += 1
        plt.savefig('app/airports.png')
    except Exception  as e:
        print(e)


        # latitudes = dataset.loc[:, 'LAT']
        # longitudes = dataset.loc[:, 'LONG']
        # countries = dataset['country']
        # unique_states = countries.unique()
        # m = folium.Map()
        # for index, row in dataset.iterrows():
        #     folium.CircleMarker([[row['LAT'], row['LONG']]],
        #                         radius=15,
        #                         popup=row['name'],
        #                         fill_color="#3db7e4",  # divvy color
        #                         ).add_to(m)
        #
        # ds = dataset[['LAT', 'LONG']].as_matrix()
        #
        # # plot heatmap
        # m.add_children(plugins.HeatMap(ds, radius=15))
        #
        #
        # delay = 5
        # fn = 'testmap.html'
        # tmpurl = 'file://{path}/{mapfile}'.format(path=os.getcwd(), mapfile=fn)
        # m.save(fn)
        #
        # browser = webdriver.Firefox()
        # browser.get(tmpurl)
        # # Give the map tiles some time to load
        # time.sleep(delay)
        # browser.save_screenshot('map.png')
        # browser.quit()



        # min_latitude = latitudes.min()
        # max_latitude = latitudes.max()
        # min_longitude = longitudes.min()
        # max_longitude = longitudes.max()


        # data_points = [Point(xy) for xy in zip(longitudes, latitudes)]
        # data_points_unique = data_points.unique()
        # colormap = matplotlib.cm.rainbow(np.linspace(0, 1, len(data_points_unique)))
        #
        # colors = []
        # for i, state in enumerate(countries):
        #     colors.append(colormap[np.where(unique_states == state)[0][0]])
        #
        # world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        # ax = world.plot(color='lightgrey', linewidth=0.5, edgecolor='black', figsize=(20, 12))
        #
        # geo_df = gpd.GeoDataFrame(dataset, crs={'init': 'epsg:4326'}, geometry=data_points)
        # geo_df.plot(markersize=10, c=colors, ax=ax)
        #
        # ax.axis('off')
        # ax.set_xlim(min_longitude - 10, max_longitude + 10)
        # ax.set_ylim(min_latitude - 10, max_latitude + 5)
        # plt.savefig('app/world.jpg')
    except Exception  as e:
        print(e)




def generate_routes():
    pass


def generate_popularity():
    pass

