import requests

def getLibraryData(access_token):
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
            track_name = track['name']
            artist_name = [artist['name'] for artist in track['artists']]
            artist_id = [artist['id'] for artist in track['artists']]

            #if multiple artists on the song, just return the main one ie.the first artist
            info = {'track_name':track_name,'artist_name':artist_name[0],'artist_id':artist_id[0]}
            libdata.append(info)

        

        # Increment the offset by the limit to get the next page
        offset += limit

        # If there are no more items, exit the loop
        if len(tracks_data['items']) < limit:
            break

    return libdata

def getTopArtists(access_token):
    print("Retrieving user's top artists...")
    topartists_response = requests.get('https://api.spotify.com/v1/me/top/artists', headers={'Authorization': 'Bearer ' + access_token})
    topartists_data = topartists_response.json()

    topartists = []
    for artist in topartists_data['items']:
        ### use a shorter time frame for top artists to get things the user might be more into lately and hasnt seen yet
        ####Create dictionaries and append them to list. You can then sort them using the sorted() function built into python by popularity or 
        ###whatever. ALSO add parameters for length of top artists (time back) and do data scraping basing on all library songs etc. You should also do 
        ### something with the recommendation section of the api. Top songs could also be a good indicator for concert
        info = {'artist_name':artist['name'],'artist_id':artist['id'],'artist_popularity':artist['popularity']}
        topartists.append(info)
        #print(i['name']," - ",i['popularity']," - ",i['id'])
    #print(playlists_response)
    return topartists