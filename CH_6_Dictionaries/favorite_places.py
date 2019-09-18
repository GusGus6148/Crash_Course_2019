favorite_places = {
    'Doug': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': 'hawaii',
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    if type(places) == list:
        for place in places:
            print("- " + place.title())
    else:
        print("- " + places)

