import os
import sys
import json
import spotipy
import webbrowser
import pdb
import spotipy.util as util
from dotenv import load_dotenv
from os.path import join, dirname
from json.decoder import JSONDecodeError

# Load envirnment
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
"CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID")
"CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET")

# Get username from terminal
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

#Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

#Define Automated test for device
def parse_response_devices(raw_response):
    devices = raw_response["devices"][0]
    result = [{
        "id": devices["id"],
        "is_active": devices["is_active"],
        "is_private_session": devices["is_private_session"],
        "is_restricted": devices["is_restricted"],
        "name": devices["name"],
        "type": devices["type"],
        "volume_percent": devices["volume_percent"]
    }]
    return result

#Define Automated test for artist
def parse_response_artist(raw_response):
    artists = raw_response["artists"]["items"][0]
    result = [{
       "genres": artists["genres"][0],
       "id": artists["id"],
       "name": artists["name"],
       "type": artists["type"],
       "uri": artists["uri"]
    }]
    return result
# Create our spotifyObject with permissions
spotifyObject=spotipy.Spotify(auth=token)

# Get current device
devices = spotifyObject.devices()
#print(json.dumps(devices,sort_keys =True, indent = 4))
deviceID = devices['devices'][0]['id']
deviceType = devices['devices'][0]['type']

# User information
user = spotifyObject.current_user()
displayName= user['display_name']
followers = user['followers']['total']

# Get Playlist
sp = spotipy.Spotify(auth=token)
playlists = sp.user_playlists(user['id'])

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
    print("2 - New        | List out New Release tracks and play")
    print("3 - Status     | Display current playing track and user info")
    print("4 - Playlist   | Display user's playlist")
    print("5 - Exit       | Exit the application")
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
        results = searchResults['artists']['total']
        if results == 0:
            print("--------------------------------------------------")
            print ("Invalid Input! Please enter a valid artist name!(eg.Taylor Swift) ")
            print("--------------------------------------------------")
            break
        else:
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


    # Get new releases
    if choice == "2":
        trackURIs =[]
        trackArt = []
        z = 0

        newReleases = spotifyObject.new_releases(country=None, limit=20, offset=0)
        newReleases = newReleases['albums']['items']
        #print(newReleases)
        #print (json.dumps(newReleases,sort_keys =True, indent = 4))
        for item in newReleases:
            songID = item['id']
            songName = item['name']
            songURI = item['uri']
                #Extract tracks data
            trackResults =spotifyObject.album_tracks(songID)
            trackResults= trackResults['items']

            for item in trackResults:
                print(str(z)+": " + songName)
                trackURIs.append(item['uri'])
                z+=1
            print()
        #Listen to new released songs
        while True:
            songSelection = input("Enter a song number to see the album art and play the song(x to exit):")
            if songSelection == "x":
                break
            trackSelectionList =[]
            trackSelectionList.append(trackURIs[int(songSelection)])
            spotifyObject.start_playback(deviceID,None,trackSelectionList) #added
            #webbrowser.open(trackArt[int(songSelection)])

    if choice == "3":
        # Current track information
        track = spotifyObject.current_user_playing_track()
        #print(json.dumps(user,sort_keys =True, indent = 4))
        if track:
            artist = track['item']['artists'][0]['name']
            track = track['item']['name']

            if artist != "":
                print(displayName +"'s current status")
                print(">>>> Your Spotify is currently playing:  " + artist + " - " + track)
                print(">>>> Playing device: " + deviceType )
                print(">>>> Your region: " + user['country'])
                print(">>>> Subscription Status: " + user['product'])
                print(">>>> Your Device Id: " + deviceID)
        else:
            print ("Your are not currently playing any music")


    # Show user's playlist
    if choice == "4":
        print("----------------------------------")
        print("Here is the list of your playlist:")
        print("----------------------------------")
        for playlist in playlists['items']:
            print("+ " + playlist['name'])
            #print(json.dumps(playlists,sort_keys =True, indent = 4))
    # End Program
    if choice == "5":
        break
    if choice != "1"or"2"or"3"or"4"or"5":
        print(">>>>>>Please enter a valid choice!!!!!!<<<<<<")
