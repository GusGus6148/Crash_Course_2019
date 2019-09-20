def make_album(artist_name, album_title, tracks=''):
    info = {'artist': artist_name, 'title': album_title}
    if tracks:
        info['tracks'] = tracks
    return info


while True:
    artist_name = input("Please select artists name: ")
    album_title = input("Please select album title")
    album = make_album(artist_name, album_title)
    print(album)
    check = input('do you wish to continue? (y/n) ')
    if check == 'n':
        break


album_0 = make_album('George Straight', 'lonely boys')
print(album_0)


album_1 = make_album('Pink', 'lost girls', 6)
print(album_1)

album_2 = make_album('Taylor Swift', 'Red', 1)
print(album_2)