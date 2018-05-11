import os
from bandsintown import Client

class SongKick:
    def __init__(self):
        client = Client(os.getenv('SONGKICK_APP_ID'))

    def fetch_artist(self, artist_name):
        return 'artist_test'