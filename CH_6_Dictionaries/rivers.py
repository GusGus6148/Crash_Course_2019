rivers = {'nile': "egypt", 'colorado': "the United States", }

for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title() + ".")

print("")
for river in rivers.keys():
    print(river)

print("")
for country in rivers.values():
    print(country.title())