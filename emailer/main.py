import events
import calculatedist as dist

distanceThresh = 300 #anything over this distance (miles) will not be presented to the user



def getConcertList(artists):
    artistlen = len(artists)+1
    index = 1
    allconcerts = []
    for artist in artists:
        print(index/artistlen)
        event_list = events.getevents(artist)
        for event in event_list:
            try:
                if event[2]:
                    distance = dist.getDist(event[2])
                    if distance <= distanceThresh:
                        event.append(distance)
                        filteredList = filterList(event_list)
                        allconcerts.append(filteredList)
            except:
                pass 
        index += 1 
    return allconcerts


def filterList(event_list):
    newlist = []
    for event in event_list:
        if len(event) == 8:
            newlist.append(event)
    
    return newlist