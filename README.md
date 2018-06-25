# My Spotipy (Python)

Spotify API client application for users to search for artists, play tracks and show playlist details.

## Prerequisites

Create a [Spotify Client application](https://developer.spotify.com/dashboard/applications/), and note its Client Id and Client Secret, and store them in environment variables called `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`.

Install desktop [Spotify Client terminal](https://www.spotify.com/us/download/other/), direct to profile page after installation. When you're on your account and find your account shairng link, click `more` and then `share` and then `copy profile link`, the characters after /user will be the `user_id` (eg.xxxxxxxxxxxxxx). Please leave your client terminal open when you operate the application.

Important Note: You have to a spotify premium subscriber in order to use the spotify API. 


(sample link:https://open.spotify.com/user/xxxxxxxxxxxxxx)


This repo uses the "dotenv" approach, but feel free to use whatever approach works for you.

## Installation

Install package dependencies:

Other packages installation
```
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
# or
pipenv install -r requirements.txt
```
Latest version Spotipy installation(Mac)
```
pip install git+https://github.com/plamere/spotipy.git --upgrade
# or
pip3 install git+https://github.com/plamere/spotipy.git --upgrade
# or
pipenv install git+https://github.com/plamere/spotipy.git --upgrade
```
Latest version Spotipy installation(Windows)
```
Find your python site-packages\spotipy and replace the client.py in the site-packages and replace 
it with the client.py in My-Spotipy-master folder.
```

If using Pipenv, the following commands assume you are running them from within a `pipenv shell`.

## Usage

Run the app:

```sh
python3 spotifyxxx.py user_id
# or
python spotifyxxx.py user_id
```
Important Note: When you enter the command line above, there would be a pop up window ask you for perimission to 
access your spotify account, after you click `Okay`, copy the redirect url at the top of you browser and paste it 
to your command line in order to properly start the application.
