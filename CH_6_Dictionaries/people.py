people = []

person_0 = {'first_name': 'Douglas', 'last_name': 'Tucker', 'age': 33, 'city': 'Boise'}
person_1 = {'first_name': 'albert', 'last_name': 'einstien', 'age': 55, 'city': 'princeton'}
person_2 = {'first_name': 'marie', 'last_name': 'curry', 'age': 37, 'city': 'paris'}

people.append(person_0)
people.append(person_1)
people.append(person_2)

for person in people:
    print("\nfirst name: " + person['first_name'])
    print("last name: " + person['last_name'])
    print("age: " + str(person['age']))
    print("city: " + person['city'])






