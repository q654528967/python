from pyecharts.charts import Bar

dataBase = [
    {'city': 'bj', 'temp': 6},
    {'city': 'sh', 'temp': 1},
    {'city': 'cs', 'temp': -1},
    {'city': 'db', 'temp': -7},
    {'city': 'hy', 'temp': 3}
]
chart = Bar()
cities = list(map(lambda x: x['city'], dataBase))
print(cities)
temps = list(map(lambda x: x['temp'], dataBase))
chart.add_xaxis(cities).add_yaxis('气温', temps).render('temp.html')
