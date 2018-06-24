import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from dotenv import load_dotenv
from os.path import join, dirname
from json.decoder import JSONDecodeError

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID"))
print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))

# Get username from terminal
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

#Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

# Create our spotifyObject with permissions
spotifyObject=spotipy.Spotify(auth=token)

# Loop
while True:
    # Main menu
    print()
    print("-----------------------------------")
    print("---- Welcome to My Spoty " + displayName + "! " + "----")
    print(">>>> You have " + str(followers) + " followers <<<<")
    print()
    print("Operation      | Description")
    print("1 - Search     | Search an artist's tracks and play track")
    print()
    choice = input("Please choose one of the options: ")

    # Search for an artist
    if choice == "1":
        print()
        searchQuery = input("Ok, What's name of the artist (eg.Sam Smith)?: ")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
        #print (json.dumps(searchResults,sort_keys =True, indent = 4))

        # Artist Details
        artist = searchResults['artists']['items'][0]
        print(">>>> Artist Name:" + artist['name'])
        print(">>>> This artist has " + str(artist['followers']['total']) + " followers")
        print(">>>> Genres: " + artist['genres'][0])
        print()
        artistID = artist['id']
        print("Listing Albums below:")
        print("--------------------------------------------------")

        #Album and track details
        trackURIs =[]
        trackArt = []
        z = 0

        #Extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("ALBUM " + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']


            #Extract tracks data
            trackResults =spotifyObject.album_tracks(albumID)
            trackResults= trackResults['items']

            for item in trackResults:
                print(str(z)+": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()

        #See album Art and play the song
        while True:
            songSelection = input("Enter a song number to see the album art and play the song(x to exit):")
            if songSelection == "x":
                break
            trackSelectionList =[]
            trackSelectionList.append(trackURIs[int(songSelection)])
            spotifyObject.start_playback(deviceID,None,trackSelectionList) #added
            webbrowser.open(trackArt[int(songSelection)])
