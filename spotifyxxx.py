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
