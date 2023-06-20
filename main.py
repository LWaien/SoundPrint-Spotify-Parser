import events
import calculatedist as dist
import progressbar as pb

distanceThresh = 300 #anything over this distance (miles) will not be presented to the user



def getConcertList(artists):
    artistlen = len(artists)+1
    index = 1
    allconcerts = []
    for artist in artists:
        print(f"Getting events for artist {index} of {artistlen}...")
        event_list = events.getevents(artist)
        counter = 0 
        for event in event_list:
            if event[2] is not None:
                distance = dist.getDist(event[2])
                if distance <= distanceThresh:
                    event.append(distance)
            counter += 1
        index += 1
        filteredList = filterList(event_list)
        allconcerts.append(filteredList)
    return allconcerts


def filterList(event_list):
    newlist = []
    for event in event_list:
        if len(event) == 8:
            newlist.append(event)
    
    return newlist