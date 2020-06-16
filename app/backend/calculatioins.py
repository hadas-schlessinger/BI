import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go


def generate_airports(calc):
    if calc:
        airport = pd.read_excel('./flights_data.xlsx', 'airports')
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


def generate_routes(airport):
    routes = pd.read_excel('./flights_data.xlsx', 'routes')
    routes = pd.DataFrame(routes)
    return list(_filter(airport, routes))


def generate_popularity():
    print('executing')
    routes = pd.read_excel('./flights_data.xlsx', 'routes')
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

    plt.figure(figsize=(20,20))

    plt.bar(airports, lengths)
    plt.savefig('top_10.png')


def _filter(airport, routes):
    filter = routes.loc[lambda df: df.From == airport]
    return filter.loc[:, 'To']
