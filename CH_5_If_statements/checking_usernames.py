current_users = ['gusgus', 'frogger', 'Dtucker', 'miranda', 'admin']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

new_users = ['Gusgus', 'frogger', 'firefly', 'parsival', 'gregory']

for user in new_users:
    if user.lower() in current_users_lower:
        print("Username already in use, please choose another name")
    else:
        print("Username accepted")
