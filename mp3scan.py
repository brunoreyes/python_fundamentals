import os
import fnmatch  # returns matches corresponding to a pattern but doesn;t compile, making it fast
import id3reader_p3 as id3reader

# utilizing a generator to search for all music on my computer using an imported file to read mp3 metatags

def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)  # create absolute path
            yield os.path.join(absolute_path, file)

my_music_files = find_music('music', 'emp3')

error_list = []
for f in my_music_files:
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
        id3r.get_value('performance'),
        id3r.get_value('album'),
        id3r.get_value('track'),
        id3r.get_value('title')
        ))
    except:
        error_list.append(f)


for error_file in error_list:
    print(error_file)
