locations = []


while True:
    location = input("if you could visit one place in the world, where would you go?"
                     + "(type 'quit to exit): ")
    if location == 'quit':
        break

    else:
        locations.append(location)

print("\nHere is a list of the locations people would like to visit someday:")
for location in locations:
    print("-" + location)