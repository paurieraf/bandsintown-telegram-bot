def create_artist_response(artist):
    print('CREATE_ARTIST_RESPONSE', str(artist))
    response = '{}{}'.format(artist.id, artist.name)
    return response


def create_artist_event_response(artist_event):
    print('CREATE_ARTIST_EVENT_RESPONSE', str(artist_event))
    response = '{}{}'.format(artist_event.id, artist_event.description)
    return response
