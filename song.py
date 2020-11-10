class Song:
    """Class to represent a song

    Attributes:
        title(str): The title of the song.
        artist(Artist): An artist object representing the songs creator.
        duration(str): The duration of the song in soconds. May be zero.
        """
    # docstring like the one above and below should always use three quotations like so: """ docstring"""
    def __init__(self, title, artist, duration=0):
        """ Song init method

        Arguments:
            title(str): Innitializes the 'title' attribute.
            artist(Artist): At Artist object representing the song's creator.
            duration (Optional)[int]: Value for the 'duration' attribute. Defaults to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

# help(Song) # call on the docstring of a particular class
# help(Song.__init__) # specifying help info for only the __init__ documentation
# help(Song.__init__.__doc__)
# Song.__init__.__doc__ = """ Updated doc string """ # easy to update a docstring

class Album:
    """Class to represent an Album, using it;s track list

    Attributes:
        album_name(str): The name of the album.
        release_year(int): The release year of the album.
        artist(Artist): The artist of the album. Defualt value, if not specified: various artist.
        tracks(List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.

   """

    def __init__(self, name, year, artist=None):
       self.name = name
       self.year = year
       if artist is None:
           self.artist = Artist("various artist")
       else:
            self.artist = artist
        
       self.tracks = []

    def add_song(self, song, position=None): #method and the arguments within parameters
        """ Adds a song to the tracklist

        Args: 
            song (Song): a song to add.
            position (Optional[int]): If specified, the song will be added to that position within the 
            tracklist - inserting it between songs if necessary. Otherwise, songs are added to end of list.
            
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """ Basic class to store artist's details.

    Attributes: 
        name (str): The name of the artist.
        album (List[Album]): A list of the albums by this artist.
            The List only includes those albums within this collection, 
            it is not an exhaustive list of the artist's published albums
        
    Methods:
        add_album: Used to add an new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.
        
        Arguments:
            album(Albums): Album object to add to the list.
                If the album is already present, it will not be duplicated (still need to implement)
        
        """
        self.albums.append(album)
        
def find_object(field, object_list):
    """Check 'object_list' to see if an object with 'name' attribute equals to 'field' exists, return it if so
    """
    for item in object_list:
        if item.name == field:
            return item
    return None  # else return none if there wasn't a name attribute that was equal to the field attribute

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # retrieve the artist object if there is one,
                # otherwise create a new artist object and add it to the artist list.
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist
                # Retrieve the album object if there is one,
                # otherwise create a new album object and store it in the artist's collection.
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                        file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)

# Object oriented programming uses classes, objects, encapsulation, deligation, composition, and inheritance.
# Deligation is passing on a task to a function that is better suited to deal with the specified task.