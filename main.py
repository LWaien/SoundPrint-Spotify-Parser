import events
import calculatedist as dist
import progressbar as pb


artists = ["Drake","Lil Baby"]

def getConcertList(artists):
    for artist in artists:
        event_list = events.getevents(artist)
        length = len(event_list)
        pb.printProgressBar(0, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
        #print(event_list)
        counter = 0 
        for event in event_list:
            if event[0] and event[2] is not None:
                event.append(dist.getDist(event[0],event[2]))
            pb.printProgressBar(counter + 1, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
            counter += 1
    #print(event_list)

getConcertList(artists)