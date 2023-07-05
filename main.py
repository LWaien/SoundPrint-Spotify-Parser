import calldata 

distanceThresh = 300 #anything over this distance (miles) will not be presented to the user

def getConcertList(access_token):

    #declare concert_data which will store top artist concerts and then library-based concerts 
    concert_data = calldata.getTopArtists(access_token)
    libdata = calldata.getLibraryData(access_token,concert_data)
    for concert in libdata:
        concert_data.append(concert)
    return concert_data

