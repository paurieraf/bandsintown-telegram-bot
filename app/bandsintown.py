import os
from bandsintown import Client

class BandsInTown:
    def __init__(self):
        client = Client(os.getenv('BANDS_IN_TOWN_APP_ID'))

    def fetch_artist(self, artist_name):
        return 'artist_test'