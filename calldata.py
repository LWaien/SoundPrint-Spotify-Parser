import requests
import concertdata
from collections import Counter

import random
import score

def processLibraryData(libdata, concert_data):
    
    counts = Counter(tuple(d.items()) for d in libdata)

    # Create a distinct list of artists with count greater than two from user's library
    distinct_list = [dict(items) for items, count in counts.items() if count > 2]
    final_list = libList(distinct_list,concert_data)

    #if the list is smaller than five, we loosen the criteria and just find anything with more 2 or more saves in the library
    if len(final_list) < 5:
        print("Loosening criteria to try and find more concerts")
        distinct_list = [dict(items) for items, count in counts.items() if count > 1]
        #getting a list of artists and their highest scored concerts
        final_list = libList(distinct_list,concert_data)

    #iterating through a final list of distinct artist concerts and converting that data into a singular dictionary which is concert = artist['concerts']
    concerts = []
    for artist in final_list:
        #pulling sublist of concerts into one singular dict
        concert = artist['concerts']
        concert['artist'] = artist['artist_name']
        concert['artist_id'] = artist['artist_id']
        concerts.append(concert)

    #rescoring concerts relative to each other
    concerts = score.score(concerts)
    return concerts

    

def processTopArtists(topartists_data, access_token):

    topartists = []
    for artist in topartists_data['items']:
        concerts = concertdata.getConcerts(artist['id'])
        if concerts:
            #This returns all concerts ranked. But we don't need this currently. Instead we just return the best ranked concert (concerts[0])
            #info = {'artist_name':artist['name'],'artist_id':artist['id'],'artist_popularity':artist['popularity'],'concert':concerts}

            concert = concerts[0]
            concert['artist'] = artist['name']
            concert['artist_id'] = artist['id']
            topartists.append(concerts[0])
        
    #Randomly pick 3 from the list of top artist concerts
    if len(topartists) > 3:
        topartists = random.sample(topartists,3)

    return topartists



def libList(distinct_list,concert_data):
    final_list = []
    list_size = 9
    #looking to reach quota of concerts. Runs until quota is met or list of distinct artists is empty
    while len(final_list) < list_size and distinct_list:
        
        #randomly select so that there is no pattern to artists being chosen
        artist = distinct_list[random.randrange(len(distinct_list))]

        #Flag checker to see if artist has already been selected by top artists concert recommender
        duplicate = False
        for item in concert_data:
            artist_data = item['artist_id']
            if artist_data == artist['artist_id']:
                print(item['artist'])
                duplicate = True
            
        if duplicate == False:
            concerts = concertdata.getConcerts(artist['artist_id'])
            if concerts:
                print(len(final_list)/list_size)
                #adding the highest scored concert for each artist
                artist['concerts'] = concerts[0]
                final_list.append(artist)
        distinct_list.remove(artist)

        #stop loop if quota is reached so we don't process more data.
        if len(final_list) >= list_size:
            break
            
    return final_list