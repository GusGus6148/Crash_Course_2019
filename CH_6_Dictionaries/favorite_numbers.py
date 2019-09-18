favorite_numbers = {
    'Bob': [42, 7],
    'Steve': 37,
    'Doug': 7,
    'Dawn': [3, 8, 9, 17],
    'Peter': 111,
    }


for person, numb in favorite_numbers.items():
    print(person + "'s favorite numbers are:")

    if type(numb) == list:
        for number in numb:
            print(" -" + str(number))
    else:
        print("- " + str(numb))
