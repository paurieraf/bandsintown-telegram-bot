from datetime import datetime


def create_artist_response(artist):
    print('CREATE_ARTIST_RESPONSE', str(artist))
    response = '{} - {}'.format(artist.id, artist.name)
    return response


def create_artist_events_response(artist_events):
    print('CREATE_ARTIST_EVENTS_RESPONSE', str(artist_events))
    response = ''
    country = ''
    for artist_event in artist_events:
        event_datetime = datetime.strptime(
            artist_event.datetime, '%Y-%m-%dT%H:%M:%S')

        # .strftime("%Y-%m-%d %H:%M")
        if country != artist_event.venue.country:
            response = response + '\n' + '- ' + artist_event.venue.country
            country = artist_event.venue.country

        response = response + '\n' + \
            '{}@{}, {} {}'.format(event_datetime,
                                  artist_event.venue.name, artist_event.venue.city, artist_event.venue.region)

        if len(artist_event.description) > 0:
            response = response + '\n       ' + artist_event.description

        response = response + '\n       INFO:' + artist_event.url

        if len(artist_event.on_sale_datetime) > 0:
            tickets_available_at_datetime = datetime.strptime(
                artist_event.on_sale_datetime, '%Y-%m-%dT%H:%M:%S')
            response = response + '\n    Tickets available:' + \
                tickets_available_at_datetime

        response = response + '\n\n'

    return response
