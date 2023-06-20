import requests
import time
import re


def artistId(artistname):
    url = "https://spotify-scraper.p.rapidapi.com/v1/artist/search"
    querystring = {"name": artistname}
    headers = {"X-RapidAPI-Key": "4cb897967cmshd1ea0ddcb68d80cp175d35jsn3fc529a8f8c2",
               "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"}

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json().get('id')


def getArtistConcerts(artistId):
    url = "https://spotify-scraper.p.rapidapi.com/v1/artist/concerts"
    parameters = {"artistId": artistId}
    headers = {"X-RapidAPI-Key": "4cb897967cmshd1ea0ddcb68d80cp175d35jsn3fc529a8f8c2",
               "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"}
    response = requests.request(
        "GET", url, headers=headers, params=parameters)

    return response.json().get('concerts')


def parseJson(j):
    allevents = []
    if j != None:
        for event in j:
            data = []
            venue = event['venue']
            title = event['title']
            location = event['location']
            date = event['date']
            url = event['ticketers'][0]['url']
            if event['ticketing']:
                minPrice = processPrice(event['ticketing'][0]['minPrice'])
                maxPrice = processPrice(event['ticketing'][0]['maxPrice'])
            else:
                minPrice = None
                maxPrice = None
            

            data.append(venue)
            data.append(title)
            data.append(location)
            data.append(date)
            data.append(url)
            data.append(minPrice)
            data.append(maxPrice)
            #print(data)
            allevents.append(data)
        return allevents
    else:
        return "No upcoming events"


def getevents(artist):
    id = artistId(artist)
    time.sleep(2)
    js = getArtistConcerts(id)
    events = parseJson(js)

    return events

def processPrice(price):
    #returns None for any non-US currency since conversions are not supported for this platform yet. 
    if len(price)>0 and price[0] == "$":
        return re.sub("[^0-9,.]", "", str(price))
    else:
        return None