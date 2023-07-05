import requests
import calculatedist
import score
import time

threshold = 300

def getArtistConcerts(artistId):
    #print("Requesting concerts")
    time.sleep(0.5)
    url = "https://spotify-scraper.p.rapidapi.com/v1/artist/concerts"
    parameters = {"artistId": artistId}
    headers = {"X-RapidAPI-Key": "4cb897967cmshd1ea0ddcb68d80cp175d35jsn3fc529a8f8c2",
               "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"}
    response = requests.request(
        "GET", url, headers=headers, params=parameters)

    #print(response)
    return response.json().get('concerts')


def parseJson(j):
    #print("Parsing json")
    allevents = []
    if j:
        for event in j:
            venue, title, location, date, url = event['venue'], event['title'], event['location'], convert_time(event['date']), event['ticketers'][0]['url']

            '''
            #if ticketing prices available, check values
            if event['ticketing']:
                #if both values present, process USD prices and ignore foreign currencies (for the time being)
                if event['ticketing'][0]['minPrice'] and event['ticketing'][0]['maxPrice']:
                    minPrice = processPrice(event['ticketing'][0]['minPrice'])
                    maxPrice = processPrice(event['ticketing'][0]['maxPrice'])
            else:
                minPrice = None
                maxPrice = None
            '''

            #pulling latitudes and longitudes to use for calculating distance from location
            lat,long = event['lat'],event['lon']
            distance = calculatedist.getDist(lat,long)
            
            if distance:
                if distance < threshold:
                    data = {'venue':venue,'title':title,'location':location,'date':date,'url':url,'distance':distance}

                    allevents.append(data)
        return allevents
    else:
        return None


def processPrice(price):
    #print("Processing prices")
    #returns None for any non-US currency since conversions are not supported for this platform yet. 
    if len(price)>0 and price[0] == "$":
        #return re.sub("[^0-9,.]", "", str(price))
        return str(price[1:])

    else:
        return None
    

def getConcerts(id):
    #print("Getting events")
    json = getArtistConcerts(id)
    events = parseJson(json)
    if events:
        concerts = score.score(events)
        return concerts
    else:
        return []


def convert_time(date):
    date = date.split('T')
    date = date[0]
    date = date.split('-')
    year = date[0]
    month = date[1]
    day = date[2]

    return str(month)+"-"+str(day)+"-"+str(year)