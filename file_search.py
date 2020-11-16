import fnmatch
import os

def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directores, artist_name)
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
         for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir): # the underscore satisfied returning a value
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):  # we want just the path and not the name of the album
        # so here we are just getting the first index which are solely the paths
            yield song

album_list = find_albums("music", "black*")
songs_list = find_songs(album_list)


for song in songs_list:
    print(song)