def build_profile(first, last, **user_info):
    """Build a dictionary contianing everything we know about a user."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field= 'physics')

print(user_profile)

user_profile_1 = build_profile('douglas', 'tucker', age=33, height="6ft", location='boise', degree='physics', )

print(user_profile_1)