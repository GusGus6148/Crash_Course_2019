def cars(manufacturer, model, **car_info):
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile


car_0 = cars('Subaru', 'outback', color="Blue", condition="new")

print(car_0)