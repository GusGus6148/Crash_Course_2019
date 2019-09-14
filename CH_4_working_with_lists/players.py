players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


print("the first three players in the list are: " + str(players[:3]))

print("the three players in the middle of the list are: " + str(players[1:4]))

print("the three players at the ned of the list are: " + str(players[-3:]))
