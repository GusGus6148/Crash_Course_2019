cities = {
    "Manteca": {'country': 'USA', 'population': 120000, 'fact': 'home town'},
    "Fresno": {'country': 'USA', 'population': 1200000, 'fact': 'College'},
    "Boise": {'country': 'USA', 'population': 180000, 'fact': 'New home'},
}

for city, info in cities.items():
    print(city)
    print("\t" + info['country'])
    print("\t" + str(info['population']) + " people")
    print("\t" + info['fact'])
