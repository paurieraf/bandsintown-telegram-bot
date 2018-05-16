def create_artist_response(artist):
    print('CREATE_ARTIST_RESPONSE', str(artist))
    response = '{}{}'.format(artist.id, artist.name)
    return response


def create_artist_events_response(artist_events):
    print('CREATE_ARTIST_EVENTS_RESPONSE', str(artist_events))
    response = ''
    for artist_event in artist_events:
        response = response + '{}{}'.format(artist_event.id, artist_event.description)
    return response
