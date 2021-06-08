import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from json.decoder import JSONDecodeError
from spotify.spotify_creds import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_USER, SPOTIFY_REDIRECT_URI
#from model call the spotify playlist

# Get the username from terminal
cid = SPOTIFY_CLIENT_ID
secret = SPOTIFY_CLIENT_SECRET
username = SPOTIFY_USER
scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-read-private playlist-read-collaborative'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# Get current device
devices = spotifyObject.devices()
deviceID = devices['devices'][0]['id']

# Current track information
track = spotifyObject.current_user_playing_track()
artist = track['item']['artists'][0]['name']
track = track['item']['name']

if artist != "":
    print("Currently playing " + artist + " - " + track)

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']

feeling = 'fun'

# Playlists
def select_and_play(feeling):
    happiness = sp.playlist(playlist_id = '2oFSJfwxmLUqZUU4SgD0I7')
    sadness = sp.playlist(playlist_id = '0LbtLlb9G4M7TFi8OsDYMg')
    #neutral
    worry = sp.playlist(playlist_id = '06Gh1LqdIfG1HMHKa44B7k') #Same playlist as fear
    love = sp.playlist(playlist_id = '37i9dQZF1DX7rOY2tZUw1k')
    anger = sp.playlist(playlist_id = '5c5NfSIO6bMrUSoCZKMudz')
    #surprise
    fear = sp.playlist(playlist_id = '06Gh1LqdIfG1HMHKa44B7k')#same playlist as worry
    fun = sp.playlist(playlist_id = '7xOHp3ZlSBJNJOgsQwF85S')
    relief = sp.playlist(playlist_id = '37i9dQZF1DWXe9gFZP0gtP')
    hate = sp.playlist(playlist_id = '4OGYlQGUpMY6EZsmFdiJ1e')
    enthusiasm = sp.playlist(playlist_id = '5t0hWEUHZ89a8jzBulvuvY')
    boredom = sp.playlist(playlist_id = '37i9dQZF1DWWQRwui0ExPn')
    #feeling_playlists = [happiness, sadness, worry, love, anger, fear, fun, relief, hate, enthusiasm, boredom]
    d= {'happy':happiness, 'sad':sadness, 'worry':worry, 'love':love, 
        'anger':anger, 'fear':fear, 'fun':fun, 
        'relief': relief, 'hate':hate, 'enthusiasm':enthusiasm,
        'boredom':boredom
       }
    return list(d[feeling].get('external_urls').values())
        
# def select_and_play_second(feeling):
#     happy = '2oFSJfwxmLUqZUU4SgD0I7?si=671d061cbcfc4810'
#     sad = '0LbtLlb9G4M7TFi8OsDYMg?si=f6cf8536ee3c4e6f'
#     #neutral
#     worry = '06Gh1LqdIfG1HMHKa44B7k?si=ad744fcfa57c4be3' #Same playlist as fear
#     love = '37i9dQZF1DX7rOY2tZUw1k?si=88404786a9ae4cc6'
#     anger = '5c5NfSIO6bMrUSoCZKMudz?si=211e93362660427b'
#     #surprise
#     fear = '06Gh1LqdIfG1HMHKa44B7k?si=ad744fcfa57c4be3' #same playlist as worry
#     fun = '7xOHp3ZlSBJNJOgsQwF85S?si=f04c656c9241412b'
#     relief = '37i9dQZF1DWXe9gFZP0gtP?si=cefe9eafc2e14d8d'
#     hate = '4OGYlQGUpMY6EZsmFdiJ1e?si=0252727c471f41e8'
#     enthusiasm = '5t0hWEUHZ89a8jzBulvuvY?si=3dd98c1bb2c24bb2'
#     boredom = '37i9dQZF1DWWQRwui0ExPn?si=575ab13eac8c418f'
#     d= {'happy':happy, 'sad':sad, 'worry':worry, 'love':love, 
#         'anger':anger, 'fear':fear, 'fun':fun, 
#         'relief': relief, 'hate':hate, 'enthusiasm':enthusiasm,
#         'boredom':boredom
#        }
#     return d[feeling]

# Loop
while True:
    
    # Main Menu
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Start Book Woofer")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        print()
        playlistID = select_and_play(feeling)
        print()

        # Get search results
        #searchResults = spotifyObject.search(searchQuery,1,0,'artists')
        searchResults2 = spotifyObject.playlist(playlistID)
        spotifyObject.start_playback(deviceID, context_uri=searchResults2)
        # Artist details
        # artist = searchResults['artists']['items'][0]
        # print(artist['name'])
        # print(str(artist['followers']['total']) + " followers")
        # print(artist['genres'][0])
        # print()
        # #webbrowser.open(artist['images'][0]['url'])
        # artistID = artist['id']


        # Album and track details
        # trackURIs = []
        # trackArt = []
        # z = 0

        # Extract album data
        # albumResults = spotifyObject.artist_albums(artistID)
        # albumResults = albumResults['items']

        # for item in albumResults:
        #     print("ALBUM: " + item['name'])
        #     albumID = item['id']
        #     albumArt = item['images'][0]['url']

        #     # Extract track data
        #     trackResults = spotifyObject.album_tracks(albumID)
        #     trackResults = trackResults['items']

        #     for item in trackResults:
        #         print(str(z) + ": " + item['name'])
        #         trackURIs.append(item['uri'])
        #         trackArt.append(albumArt)
        #         z+=1
        #     print()

        # See album art
        # while True:
        #     songSelection = input("Enter a song number to see album art and play the song (x to exit): ") # and play the song
        #     if songSelection == "x":
        #         break
            #trackSelectionList = []
            #trackSelectionList.append(trackURIs[int(songSelection)])
            # spotifyObject.start_playback(deviceID, None, songSelection) # added
            #webbrowser.open(trackArt[int(songSelection)])

    if choice == "1":
        break

    # print(json.dumps(trackResults, sort_keys=True, indent=4))
    