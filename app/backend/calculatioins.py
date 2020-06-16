
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go


def generate_airports(calc):
    if calc:
        airport = pd.read_excel('app/flights_data.xlsx', 'airports')
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



def generate_routes(airport):
    routes = pd.read_excel('app/flights_data.xlsx', 'routes')
    routes = pd.DataFrame(routes)
    return list(_filter(airport, routes))


def generate_popularity():
    print('executing')
    routes = pd.read_excel('app/flights_data.xlsx', 'routes')
    routes = pd.DataFrame(routes)
    airports = routes['From'].unique()

    common_routes = []

    for airport in airports:
        common_routes.append(len(list(_filter(airport, routes))))

    top_10_len = sorted(range(len(common_routes)), key=lambda i: common_routes[i])[-10:]
    airports = airports[top_10_len]
    lengths = []
    for index in top_10_len:
        lengths.append(common_routes[index])

    fig = go.Figure(
        data=[go.Bar(x=airports, y=lengths)],
        layout=dict(title=dict(text="Top 10 airports"))
    )

    fig.show()


def _filter(airport, routes):
    filter = routes.loc[lambda df: df.From == airport]
    return filter.loc[:, 'To']
