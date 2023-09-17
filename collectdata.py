import requests

def gatherLibData(access_token):
    print("Retrieving user's library... ")
    limit = 50
    offset = 0

    libdata = []
    while True:
        # Send a GET request to the endpoint with the limit and offset
        params = {
            'market':'US',
            'limit': limit,
            'offset': offset
        }
        tracks = requests.get('https://api.spotify.com/v1/me/tracks', headers={'Authorization': 'Bearer ' + access_token}, params=params)
        tracks_data = tracks.json()

        
        # Iterate over each track and display the track name and artists
        for item in tracks_data['items']:
            
            track = item['track']
            #print(track)
            artist_name = [artist['name'] for artist in track['artists']]
            artist_id = [artist['id'] for artist in track['artists']]

            #if multiple artists on the song, just return the main one ie.the first artist
            info = {'artist_name':artist_name[0],'artist_id':artist_id[0]}
            libdata.append(info)

        

        # Increment the offset by the limit to get the next page
        offset += limit

        # If there are no more items, exit the loop
        if len(tracks_data['items']) < limit:
            break
    
    #print(libdata)
    return libdata

def gatherTopArtists(access_token):
    print("Retrieving user's top artists...")
    topartists_response = requests.get('https://api.spotify.com/v1/me/top/artists?time_range=short_term', headers={'Authorization': 'Bearer ' + access_token})
    topartists_data = topartists_response.json()
    #print(topartists_data)
    return topartists_data

def gatherTopSongs(access_token):
    print("Retrieving user's top artists...")
    topsongs_response = requests.get('https://api.spotify.com/v1/me/top/tracks?time_range=short_term', headers={'Authorization': 'Bearer ' + access_token})
    topsongs_data = topsongs_response.json()
    #print(topartists_data)
    return topsongs_data
