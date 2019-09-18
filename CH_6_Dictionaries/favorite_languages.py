favorite_languages = {
    'jen': 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

# .key() would be the default method and can be left off
for name in favorite_languages.keys():
    print(name.title())



friends = ['phil', 'sarah']

for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + '!')

if 'erin'  not in favorite_languages.keys():
    print("Erin, Please take our poll!")

print("\n")
print(favorite_languages.keys())


print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())