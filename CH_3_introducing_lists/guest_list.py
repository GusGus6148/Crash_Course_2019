guests = ['mom', 'dad', 'marie', 'niel armstrong', 'einstein', 'Gregory']

print(len(guests))


message = "would you like to come over for dinner " + guests[0].title()
print(message)
message = "would you like to come over for dinner " + guests[1].title()
print(message)
message = "would you like to come over for dinner " + guests[2].title()
print(message)
message = "would you like to come over for dinner " + guests[3].title()
print(message)
message = "would you like to come over for dinner " + guests[4].title()
print(message)
message = "would you like to come over for dinner " + guests[5].title()
print(message)

print("Einstein")

guests[4]= "steven hawking"

message = "would you like to come over for dinner " + guests[0].title()
print(message)
message = "would you like to come over for dinner " + guests[1].title()
print(message)
message = "would you like to come over for dinner " + guests[2].title()
print(message)
message = "would you like to come over for dinner " + guests[3].title()
print(message)
message = "would you like to come over for dinner " + guests[4].title()
print(message)
message = "would you like to come over for dinner " + guests[5].title()
print(message)

print("Good news everyone, i've found a bigger table for dinner")

guests.insert(0, 'Trevor')
guests.insert(3, 'justin')
guests.append('Michelle')

message = "would you like to come over for dinner " + guests[0].title()
print(message)
message = "would you like to come over for dinner " + guests[1].title()
print(message)
message = "would you like to come over for dinner " + guests[2].title()
print(message)
message = "would you like to come over for dinner " + guests[3].title()
print(message)
message = "would you like to come over for dinner " + guests[4].title()
print(message)
message = "would you like to come over for dinner " + guests[5].title()
print(message)
message = "would you like to come over for dinner " + guests[6].title()
print(message)
message = "would you like to come over for dinner " + guests[7].title()
print(message)
message = "would you like to come over for dinner " + guests[8].title()
print(message)

print("Sorry everyone there is only room for two at the table")

removed = guests.pop(0)
print("Sorry, but there isnt enough room for you to come " + removed + ".")
removed = guests.pop(0)
print("Sorry, but there isnt enough room for you to come " + removed + ".")
removed = guests.pop(0)
print("Sorry, but there isnt enough room for you to come " + removed + ".")
removed = guests.pop(0)
print("Sorry, but there isnt enough room for you to come " + removed + ".")
removed = guests.pop(1)
print("Sorry, but there isnt enough room for you to come " + removed + ".")
removed = guests.pop(1)
print("Sorry, but there isnt enough room for you to come " + removed + ".")
removed = guests.pop(1)
print("Sorry, but there isnt enough room for you to come " + removed + ".")

print("good news, there is still room for you to come " +guests[0].title() + ".")
print("good news, there is still room for you to come " +guests[1].title() + ".")

del guests[0]
del guests[0]

print(guests)

