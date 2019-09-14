#3-10. Every Function

cities = ['Manteca', 'Arcata', 'Fresno', 'Twain Harte', 'Sonora', 'Soulsbyville', 'Boise']

print(cities)

# temporary alphabetical
print(sorted(cities))
print(cities)

# temporary alphabetical reverse
print(sorted(cities, reverse=True))

# permanent alphabetical
cities.sort()
print(cities)

# permanent reverse alphabtical
cities.sort(reverse=True)
print(cities)