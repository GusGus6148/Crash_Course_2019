def show_magicians(magicians_list):
    '''Print the name of each magician'''
    for magician in magicians_list:
        print(magician)


def make_great(magicians_list):
    """Add 'the Great' to each magician"""
    great_magicians = []

    while magicians_list:
        magician = magicians_list.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians_list.append(great_magician)






magicians = ['greg', 'steven', 'samantha']
magicians_copy = magicians[:]

show_magicians(magicians)

make_great(magicians_copy)
show_magicians(magicians_copy)

show_magicians(magicians)

