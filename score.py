from datetime import datetime

#final values will be concert['daysuntil_score'] and concert['distance_score'] with a final score of event['score']


def score(concerts):
    #print(concerts)
    concerts_scored_dist = scoreDistance(concerts)
    concerts_scored_dates = scoreDates(concerts_scored_dist)
    concerts_finalScores = weightedScores(concerts_scored_dates)
    rankedConcerts = rankConcerts(concerts_finalScores)
    return rankedConcerts

def rankConcerts(concerts):
   rankedConcerts = sorted(concerts, key=lambda x: x["score"])
   return rankedConcerts

def weightedScores(concerts):
    final_concerts = []
    for concert in concerts:
        distScore = concert['distance_score']
        daysUntilScore = concert['daysuntil_score']

        #final key/value with a weighted score with an emphasis on closer concerts (70/30)
        concert['score'] = (distScore*0.85) + (daysUntilScore*0.15)
        final_concerts.append(concert)
    return final_concerts

def scoreDates(concerts):
    #getting a list of concerts with a days_until key/value pair
    concertsWithUntil = getTimeUntil(concerts)
    maxTimeUntil = getMaxUntil(concertsWithUntil)
    concertsScoredDate = []
    for concert in concertsWithUntil:
        daysuntil = concert['days_until']
        #Handling a case where max days until = 0. This would care an error due to division by 0 so we set equal 0
        if maxTimeUntil == 0:
            concert['daysuntil_score'] = 0
        else:
            concert['daysuntil_score'] = daysuntil / maxTimeUntil
        concertsScoredDate.append(concert)
    return concertsScoredDate

def getMaxUntil(concerts):
    #finding maximum number of days until concert in an artist's list of concerts
    maxuntil = 0
    for concert in concerts:
        daysUntil = concert['days_until']
        if daysUntil > maxuntil:
            maxuntil = daysUntil
    return maxuntil

def getTimeUntil(concerts):
    concertsDaysUntil = []
    for concert in concerts:
        concertDate = concert['date']
        target_date = datetime.strptime(concertDate, "%m-%d-%Y").date()

        # Get today's date
        today = datetime.now().date()

        # Calculate the difference in days
        days_until = (target_date - today).days

        #adding key value to concert
        concert['days_until'] = days_until

        #appendind concert to a master list and returning
        concertsDaysUntil.append(concert)

    return concertsDaysUntil



def scoreDistance(concerts):
    max_dist = getMaxDist(concerts)
    concertsScoredDistance = []
    for concert in concerts:
        #better scores are lower because it represents a proportion of the maximum distance
        distance = concert['distance']
        concert['distance_score'] = distance / max_dist
        concertsScoredDistance.append(concert)
    return concertsScoredDistance

def getMaxDist(concerts):
    maxDistance = 0
    for concert in concerts:
        distance = concert['distance']
        if distance > maxDistance:
            maxDistance = distance
    return maxDistance