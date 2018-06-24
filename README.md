# My Spotipy (Python)

Spotify API client application for users to search for artists, play tracks and show playlist details.

## Prerequisites

Create a [Spotify Client application](https://developer.spotify.com/dashboard/applications/), and note its Client Id and Client Secret, and store them in environment variables called `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`.

Install desktop [spotify client terminal](https://www.spotify.com/us/download/other/), direct to profile page after installation. When you're on your account and find your account shairng link, click `more` and then `share` and then `copy profile link`, the characters after /user will be the `user_id` (eg.xxxxxxxxxxxxxx).


(sample link:https://open.spotify.com/user/xxxxxxxxxxxxxx)


This repo uses the "dotenv" approach, but feel free to use whatever approach works for you.

## Installation

Install package dependencies:
```
###Latest version Spotipy installation
pip install spotipy==2.4.4
# or 
pip3 install spotipy==2.4.4
# note: you have to install spotipy using this spacific command, otherwise you would install an older 
version of spotipy, in the older version, some functions are not working properly.


###Other packages installation
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
# or
pipenv install -r requirements.txt
```

If using Pipenv, the following commands assume you are running them from within a `pipenv shell`.

## Usage

Run the app:

```sh
python3 spotifyxxx.py user_id

Important Note: When you run the application, there would be a pop up window ask you for perimission to 
access your spotify account, after you click `Okay`, copy the redirect url at the top of you browser and paste it 
to your command line in order to properly start the application.
