from datetime import datetime


def create_artist_response(artist):
    print('CREATE_ARTIST_RESPONSE', str(artist))
    response = '{} - {}'.format(artist.id, artist.name)
    return response


def create_artist_events_response(artist_events):
    print('CREATE_ARTIST_EVENTS_RESPONSE', str(artist_events))
    response = ''
    for artist_event in artist_events:
        event_datetime = datetime.strptime(
            artist_event.datetime, '%Y-%m-%dT%H:%M:%S')
        # .strftime("%Y-%m-%d %H:%M")
        response = response + '\n' + \
            '{}: {} - {}:{}'.format(event_datetime,
                                    artist_event.id, artist_event.venue.country, artist_event.venue.name)
    return response
