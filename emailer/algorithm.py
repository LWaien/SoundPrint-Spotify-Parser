import datetime

#data = [[['TD Garden', "Drake: It's All A Blur Tour", 'Boston', '2023-07-11T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=3vMJ8i2ox8aPsyJmo6C7Ee&u=https%3A%2F%2Fwww.ticketmaster.com%2Fdrake-its-all-a-blur-tour-boston-massachusetts-07-11-2023%2Fevent%2F01005E68E203620B%3Futm_content%3Dhotevent', None, None, 73.68443316837032], ['TD Garden', "Drake: It's All A Blur Tour", 'Boston', '2023-07-12T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=5rRhTwLkJqhCmcavACnGJo&u=https%3A%2F%2Fwww.ticketmaster.com%2Fdrake-its-all-a-blur-tour-boston-massachusetts-07-12-2023%2Fevent%2F01005E6AF96CA3B0%3Futm_content%3Dhotevent', None, None, 73.68443316837032], ['Centre Bell', "Drake: It's All A Blur Tour", 'Montreal', '2023-07-14T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=6kjKNTT1nB60QEEaGZt67E&u=https%3A%2F%2Fwww.ticketmaster.ca%2Fdrake-its-all-a-blur-tour-montreal-quebec-07-14-2023%2Fevent%2F31005E6709206E84%3Futm_content%3Dhotevent', None, None, 221.83179882992425], ['Centre Bell', "Drake: It's All A Blur Tour", 'Montreal', '2023-07-15T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=4yQG99Dt9cnmqkMUdTUJlu&u=https%3A%2F%2Fwww.ticketmaster.ca%2Fdrake-its-all-a-blur-tour-montreal-quebec-07-15-2023%2Fevent%2F31005E67094E6E96%3Futm_content%3Dhotevent', None, None, 221.83179882992425], ['Barclays Center', "Drake: It's All A Blur Tour", 'Brooklyn', '2023-07-17T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=6diAk2dvz4KR04PjoKi1uD&u=https%3A%2F%2Fwww.ticketmaster.com%2Fdrake-its-all-a-blur-tour-brooklyn-new-york-07-17-2023%2Fevent%2F30005E68EE091B9A%3Futm_content%3Dhotevent', None, None, 141.2102255188538], ['Barclays Center', "Drake: It's All A Blur Tour", 'Brooklyn', '2023-07-18T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=5jLHobG5M4dYA1W3FEoBnI&u=https%3A%2F%2Fwww.ticketmaster.com%2Fdrake-its-all-a-blur-tour-brooklyn-new-york-07-18-2023%2Fevent%2F30005E6A98640C56%3Futm_content%3Dhotevent', None, None, 141.2102255188538], ['Barclays Center', "Drake: It's All A Blur Tour", 'Brooklyn', '2023-07-20T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=1MgvSgiacz87ANCzvY4YM5&u=https%3A%2F%2Fwww.ticketmaster.com%2Fdrake-its-all-a-blur-tour-brooklyn-new-york-07-20-2023%2Fevent%2F30005E6A98740C5A%3Futm_content%3Dhotevent', None, None, 141.2102255188538], ['Barclays Center', "Drake: It's All A Blur Tour", 'Brooklyn', '2023-07-21T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=5TtzkyKBRqf4dpHVZr3SPD&u=https%3A%2F%2Fwww.ticketmaster.com%2Fdrake-its-all-a-blur-tour-brooklyn-new-york-07-21-2023%2Fevent%2F30005E6A98800C5C%3Futm_content%3Dhotevent', None, None, 141.2102255188538], ['Madison Square Garden', "Drake: It's All A Blur Tour", 'New York', '2023-07-23T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=6FW3fte7YMa6cctYR5WJ9v&u=https%3A%2F%2Fwww.ticketmaster.com%2Fdrake-its-all-a-blur-tour-new-york-new-york-07-23-2023%2Fevent%2F3B005E6ABEAF3CE8%3Futm_content%3Dhotevent', None, None, 139.31198492982347], ['Madison Square Garden', "Drake: It's All A Blur Tour", 'New York', '2023-07-25T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=4Dj583x2E2cD7AoKXv4Bqv&u=https%3A%2F%2Fwww.ticketmaster.com%2Fdrake-its-all-a-blur-tour-new-york-new-york-07-25-2023%2Fevent%2F3B005E6ABEB83CEB%3Futm_content%3Dhotevent', None, None, 139.31198492982347], ['Madison Square Garden', "Drake: It's All A Blur Tour", 'New York', '2023-07-26T19:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=5haBbmUXlU8EagO6vsy7o6&u=https%3A%2F%2Fwww.ticketmaster.com%2Fdrake-its-all-a-blur-tour-new-york-new-york-07-26-2023%2Fevent%2F3B005E6ABEC43CF4%3Futm_content%3Dhotevent', None, None, 139.31198492982347], ['Wells Fargo Center', 'Drake with 21 Savage at Wells Fargo Center (July 31, 2023)', 'Philadelphia', '2023-07-31T19:00:00-0400', 'https://www.songkick.com/concerts/40982684-drake-at-wells-fargo-center?utm_source=8123&utm_medium=partner&utm_content=&utm_campaign=artist', None, None, 217.81898863782735], ['Wells Fargo Center', 'Drake with 21 Savage at Wells Fargo Center (August 1, 2023)', 'Philadelphia', '2023-08-01T19:00:00-0400', 'https://www.songkick.com/concerts/40996663-drake-at-wells-fargo-center?utm_source=8123&utm_medium=partner&utm_content=&utm_campaign=artist', None, None, 217.81898863782735]], [['Ocean City Inlet', 'Oceans Calling', 'Ocean City', '2023-09-29T20:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=4QHRi5pQitzIDy3wR6WErg&u=https%3A%2F%2Fon.fgtix.com%2Ftrk%2FjpFM', None, None, 240.37136572096173]], [['Charlotte Motor Speedway', 'Breakaway Carolina 2023', 'Concord', '2023-09-29T16:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=1RF2E9Ma5drhxoumVzyeHv&u=https%3A%2F%2Fwww.universe.com%2Fevents%2Fbreakaway-carolina-2023-tickets-Y1CLXN%3Fref%3Dticketmaster', None, None, 74.94747589503976]], [['Elsewhere - Rooftop', 'Grapetooth', 'New York', '2023-08-01T19:00:00-0400', 'https://dice.fm/partner/spotify/event/62332-grapetooth-1st-aug-elsewhere-rooftop-new-york-tickets', None, None, 139.31198492982347], ['Otis Mountain', 'Grapetooth at Otis Mountain (September 9, 2023)', 'Westport', '2023-09-09T23:00:00-0400', 'https://www.songkick.com/concerts/41179307-grapetooth-at-otis-mountain?utm_source=8123&utm_medium=partner&utm_content=&utm_campaign=artist', None, None, 96.5686596145404]], [['Centre Bell', 'Arctic Monkeys', 'Montreal', '2023-09-02T20:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=6evYrtchl1yuReeNKx8orj&u=https%3A%2F%2Fwww.ticketmaster.ca%2Farctic-monkeys-montreal-quebec-09-02-2023%2Fevent%2F31005D3CD5742E65', None, None, 221.83179882992425], ['TD Garden', 'Arctic Monkeys', 'Boston', '2023-09-03T20:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=3UKbrHICeklobvQT5rqY0d&u=https%3A%2F%2Fwww.ticketmaster.com%2Farctic-monkeys-boston-massachusetts-09-03-2023%2Fevent%2F01005D3BAD6923AE', None, None, 73.68443316837032], ['TD Pavilion at the Mann', 'Arctic Monkeys', 'Philadelphia', '2023-09-05T20:00:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=3xKwMEzfxScck7l9fhhGtx&u=https%3A%2F%2Fwww.ticketmaster.com%2Farctic-monkeys-philadelphia-pennsylvania-09-05-2023%2Fevent%2F02005D3CD1238552', None, None, 217.81898863782735]], [['MGM Music Hall at Fenway', "RÜFÜS DU SOL SUMMER '23 TOUR", 'Boston', '2023-08-01T19:30:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=3z8AIQGW6TFcfyiFmPORNJ&u=https%3A%2F%2Fwww.ticketmaster.com%2Frufus-du-sol-summer-23-tour-boston-massachusetts-08-01-2023%2Fevent%2F01005E680FAD81AC%3Futm_content%3Dhotevent', None, None, 73.68443316837032], ['MGM Music Hall at Fenway', "RÜFÜS DU SOL SUMMER '23 TOUR", 'Boston', '2023-08-02T19:30:00-0400', 'https://ticketmaster.evyy.net/c/296934/271177/4272?sharedId=artist&subId1=null&subId3=6cqE8vgCsgLPur5rhW0zih&u=https%3A%2F%2Fwww.ticketmaster.com%2Frufus-du-sol-summer-23-tour-boston-massachusetts-08-02-2023%2Fevent%2F01005E680FAF81AF%3Futm_content%3Dhotevent', None, None, 73.68443316837032]]]



def convert_time(date):
    date = date.split('T')
    date = date[0]
    date = date.split('-')
    year = date[0]
    month = date[1]
    day = date[2]

    return str(month)+"-"+str(day)+f" ({year})"
#pick the best concert by date distance for each artist

#find date distance for each entry
def returnTop(data):
    #print(data)
    testdata=[]
    for artist in data:
        event = artist[0]
        info ={
                'venue':event[0],
                'title':event[1],
                'location':event[2],
                'date':convert_time(event[3]),
                'url':event[4],
                'distance':event[-1]
            }
        testdata.append(info)


    seen = set()
    new_l = []
    for d in testdata:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)


    for x in new_l:
        print(x['title'],x['date'])

    #print([*set(testdata)])



