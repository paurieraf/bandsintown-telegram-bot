from datetime import datetime


def create_artist_response(artist):
    print('CREATE_ARTIST_RESPONSE', str(artist))
    response = ''
    response = response + '<b> {} </b> \n'.format(artist.name)
    response = response + 'Upcoming events: {} \n '.format(artist.upcoming_event_count)
    response = response + 'ℹ INFO: {}'.format(artist.url)
     
    return response


def create_artist_events_response(artist_events, artist_name):
    print('CREATE_ARTIST_EVENTS_RESPONSE', str(artist_events))
    response = ''
    country = ''

    if len(artist_events) == 0:
        return '❌ There are not upcoming events of <b>' + artist_name + '</b>'

    for artist_event in artist_events:
        event_datetime = datetime.strptime(
            artist_event.datetime, '%Y-%m-%dT%H:%M:%S')
        event_datetime_string = event_datetime.strftime('%d-%m-%Y %H:%M')

        # .strftime("%Y-%m-%d %H:%M")
        if country != artist_event.venue.country:
            response = response + '\n\n' + '🌍 <b>' + artist_event.venue.country + '</b>'
            country = artist_event.venue.country

        response = response + '\n' + \
            '🕓 {} \n @ {}, {} {}'.format(event_datetime_string,
                                         artist_event.venue.name, artist_event.venue.city, artist_event.venue.region)

        # Commented due to the unnecessary text size
        # if len(artist_event.description) > 0:
        #     response = response + '\n' + artist_event.description

        response = response + '\nℹ INFO: ' + artist_event.url

        if len(artist_event.on_sale_datetime) > 0:
            tickets_available_at_datetime = datetime.strptime(
                artist_event.on_sale_datetime, '%Y-%m-%dT%H:%M:%S')
            tickets_available_at_datetime_string = tickets_available_at_datetime.strftime(
                '%d-%m-%Y %H:%M')
            response = response + '\n    Tickets available: ' + \
                tickets_available_at_datetime_string

        response = response + '\n'

    return response
