usernames = ['gusgus', 'frogger', 'Dtucker', 'miranda', 'firefly', 'admin']

if usernames:
    for user in usernames:
        if user == "admin":
            print("hello admin, would you like to see a status report?")
        else:
            print("greetings " + user + "! thank you for logging in.")

else:
    print("we need to find some users!")
