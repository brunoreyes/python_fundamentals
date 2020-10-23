from demo import albums  #With just this line of code, nothing will appear in the terminal
# we can take data from local files using from (place) import (data)

# print(albums) #To check data was taken we print(data)

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title)) #enumerate to print the index + 1 and title of album

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX] # SONGS_LIST_INDEX gets to songs in index 3 of album
    else:
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX] # SONGS_TITLE_INDEX gets songs in index 1 of songs
    # else:
    #     break #comment out this code so when user chooses invalid number, they are propted to choose album
        print("Playing {}".format(title))
    print("=" * 40) #this is a line to seperate the currently playing song from the prompt to choose another
