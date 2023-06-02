playlist = []


def add_song():
    added_song = input("enter the name of the song you wish to add: ")
    list.append(playlist, added_song)
    print(added_song + " has been added to the playlist")


def remove_song():
    removed_song = input("enter the name of the song you wish to remove: ")
    # check if song not in playlist
    if removed_song not in playlist:
        print("The song entered is not in the list dumb ass")
        return

    list.remove(playlist, removed_song)
    print(removed_song + " has been removed from the list")


def view_playlist():
    print(playlist)


def main():
    while True:
        print("Spotify playlist")
        print("1.Add a song")
        print("2.Remove a song")
        print("3.View playlist")
        print("4.Exit")
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            add_song()
        elif user_input == 2:
            remove_song()
        elif user_input == 3:
            view_playlist()
        elif user_input == 4:
            break
        else:
            print("choose again stupid")


if __name__ == '__main__':
    main()
