
while True:
    age = input("How old are you? ")

    if age == 'quit':
        break

    else:
        age = int(age)
        if age < 3:
            print("your ticket will be free")
        elif age < 12:
            print("your ticket will be $10")
        else:
            print("your ticket will be $15")