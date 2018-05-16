import os
from collections import namedtuple
from bandsintown import Client


class BandsInTown:
    def __init__(self):
        self.client = Client(os.getenv('BANDS_IN_TOWN_APP_ID'))
        self.Artist = namedtuple('Artist', ['id', 'name', 'url', 'facebook_page_url',
                                            'upcoming_event_count', 'tracker_count', 'mbid', 'image_url', 'thumb_url'])
        self.Venue = namedtuple(
            'Venue', ['name', 'country', 'region', 'city', 'latitude', 'longitude'])
        self.Offer = namedtuple(
            'Offer', ['status', 'type', 'url'])
        self.ArtistEvent = namedtuple(
            'ArtistEvent', ['id', 'description', 'artist_id', 'datetime', 'lineup', 'offers', 'on_sale_datetime', 'url', 'venue'])

    def fetch_artist(self, artist_name):
        """Fetch an artist based on a given name"""
        return self.convert_artist_dict_to_namedtuple(
            self.client.artists(artist_name))

    def fetch_artist_events(self, artist_name, country=None):
        """Fetch an artist based on a given name"""

        if country is None:
            return self.convert_artist_events_dict_to_namedtuple(
                self.client.artists_events(artist_name, date="upcoming"))

        artist_events_namedtuple = self.convert_artist_events_dict_to_namedtuple(
            self.client.artists_events(artist_name, date="upcoming"))
        artist_events_country_namedtuple = []
        for artist_event in artist_events_namedtuple:
            if artist_event.venue.country == country:
                artist_events_country_namedtuple.append(artist_event)

        return artist_events_country_namedtuple
        # for event in self.client.artists_events(artist_name):
        #     print('----------------------------------------------------------')
        #     print(event)

        # return self.client.artists_events(artist_name)

    def convert_artist_dict_to_namedtuple(self, artist_dict):
        print('CONVERT_ARTIST_DICT_TO_NAMEDTUPLE_ARTIST_DICT', artist_dict)
        artist = self.Artist(artist_dict['id'], artist_dict['name'], artist_dict['url'], artist_dict['facebook_page_url'],
                             artist_dict['upcoming_event_count'], artist_dict['tracker_count'], artist_dict['mbid'], artist_dict['image_url'], artist_dict['thumb_url'])
        return artist

    def convert_artist_events_dict_to_namedtuple(self, artist_events_dict):
        print('CONVERT_ARTIST_EVENTS_DICT_TO_NAMEDTUPLE_ARTIST_EVENTS_DICT',
              artist_events_dict)
        artist_events = []
        for artist_event in artist_events_dict:
            artist_lineup = []
            offers = []
            for artist in artist_event['lineup']:
                artist_lineup.append(artist)
            for offer in artist_event['offers']:
                offers.append(self.Offer(
                    offer['status'], offer['type'], offer['url']))
            venue = self.Venue(artist_event['venue']['name'], artist_event['venue']['country'], artist_event['venue']
                               ['region'], artist_event['venue']['city'], artist_event['venue']['latitude'], artist_event['venue']['longitude'])
            event = self.ArtistEvent(artist_event['id'], artist_event['description'], artist_event['artist_id'], artist_event['datetime'],
                                     artist_lineup, offers, artist_event['on_sale_datetime'], artist_event['url'], venue)
            artist_events.append(event)

        return artist_events
