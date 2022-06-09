import spotipy
import csv
import boto3
from datetime import datetime


rap_caviar_uri = spotify:playlist:37i9dQZF1DX0XUsuxWHRQd

spotipy_object = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

final_data_dicitonary = {
    'Year Released': [],
    'Album Length': [],
    'Album Name':  [],
    'Artist': []

}

PLAYLIST = 'rap_caviar'

def gather_data_local():
    pass

def gather_data():
    pass

def lambda_handler(event, context):
    gather_data()

if __name__ == '__main__':
    data = gather_data_local()