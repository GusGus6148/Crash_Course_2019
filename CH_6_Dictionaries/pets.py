pets = []

August = {'kind': 'dog', 'owner_name': 'Douglas'}
sammy = {'kind': 'cat', 'owner_name': 'David'}
JJ = {'kind': 'cat', 'owner_name': 'Oliver'}

pets.append(August)
pets.append(sammy)
pets.append(JJ)

for pet in pets:
    print("\nkind: " + pet['kind'])
    print("belongs to: " + pet['owner_name'])


