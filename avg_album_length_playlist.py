import spotipy
import csv
import boto3
from datetime import datetime


#rap_caviar_uri = spotify:playlist:37i9dQZF1DX0XUsuxWHRQd

spotipy_object = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())



def spotify_playlists():
    playlists = {'rap_caviar': 'spotify:playlist:37i9dQZF1DX0XUsuxWHRQd'}
    return playlists

def get_artists_from_playlist(playlist_uri):
    '''
    :param playlist_uri: Playlist to analyse
    :return: A dictionary(artist uri : artist name) of all primary artists in a playlist.
    '''
    artists = {}
    playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_uri)
    for song in playlist_tracks['items']:
        if song['track']:
            print(song['track']['artists'][0]['name'])
            artists[song['track']['artists'][0]['uri']] = song['track']['artists'][0]['name']
    return artists

PLAYLIST = 'rap_caviar'

def gather_data_local():

    final_data_dictionary = {
    'Year Released': [],
    'Album Length': [],
    'Album Name':  [],
    'Artist': []}


    with open("rapcaviar_albmus.csv","w") as file:
        header = list(final_data_dictionary.keys())
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        albums_obtained = []

        artists = get_artists_from_playlist(spotify_playlists()[PLAYLIST])
        #for artist in artists.keys()
        for artist in list(artists.keys()):
            artists_albums = spotipy_object.artist_albums(artist, album_type='album', limit=50)
            
            for album in artists_albums['items']:
                if 'GB' and 'US' in album['available_markets']:
                    key = album['name'] + album['artists'][0]['name'] + album['release_date'][:4]

                    if key not in albums_obtained:
                        albums_obtained.append(key)
                        album_data = spotipy_object.album(album['uri'])

                        albums_length_ms = 0
                        for song in album_data['tracks']['items']:
                            album_length_ms = song['duration_ms'] + album_length_ms

                        writer.writerow({'Year Released': album_data['release_date'][:4],
                                         'Album Length': album_length_ms,
                                         'Album Name': album_data['name'],
                                         'Artist': album_data['artists'][0]['name']})
                        final_data_dictionary['Year Released'].append(album_data['release_date'][:4])
                        final_data_dictionary['Album Length'].append(album_length_ms)
                        final_data_dictionary['Album Name'].append(album_data['name'])
                        final_data_dictionary['Artist'].append(album_data['artists'][0]['name'])

    return final_data_dictionary

    
def gather_data():
    pass

def lambda_handler(event, context):
    gather_data()

if __name__ == '__main__':
    data = gather_data_local()