import linsimpy
tse = linsimpy.TupleSpaceEnvironment()


def checkNick(nick):
    try:
        tse.rdp(("NICK", nick))
        return True
    except:
        return False
def createUser(data):
    user = data[0]
    nick = data[1]
    status = data[2]
    latitude = data[3]
    longitude = data[4]
    distancia = data[5]

    tse.out(("NICK",nick))
    tse.out(("USER", nick, user, status, latitude, longitude, distancia))

    user = tse.rdp(("USER",nick,user, status, latitude, longitude, distancia))
    print(f"User created {user}")
    if(status == True):
        try:
            online = tse.inp(("ONLINE",object))
            tsOnline = list(online[1])
            tsOnline.append(nick)
            tse.out(("ONLINE",tuple(tsOnline)))
        except:
            tsOnline = [nick]
            tse.out(("ONLINE",tuple(tsOnline)))
    else:
        try:
            offline = tse.inp(("OFFLINE",object))
            tsOffline = list(offline[1])
            tsOffline.append(nick)
            tse.out(("OFFLINE",tuple(tsOffline)))
        except:
            tsOffline = [nick]
            tse.out(("OFFLINE",tuple(tsOffline)))
        
def updateUser(data):
    user = data[0]
    nick = data[1]
    status = data[2]
    latitude = data[3]
    longitude = data[4]

def readUser(nick):
    try:
        user = tse.rdp(("USER",nick))
        return user
    except:
        return("User not found")

def listOnline():
    try:
        online = tse.rdp(("ONLINE",object))    
        print(online)
        return list(online[1])
    except: 
        print(f"Tuple matching not found")
def listOffline():
    try:
        offline = tse.rdp(("OFFLINE",object))    
        print(offline)
        return list(offline[1])
    except: 
        print(f"Tuple matching not found")

def updateStatusOnline(nick):
    
    statusOnline =[]
    try:
        online = tse.inp(("ONLINE",object))
        statusOnline = list(online[1])
        statusOnline.append(nick)
        tse.out(("ONLINE",statusOnline))
        statusOnline = tse.rdp(("ONLINE",object))
        return statusOnline[1]
    except:
        tse.out(("ONLINE",nick))
        statusOnline = tse.rdp(("ONLINE",object))
        return statusOnline[1]

def updateStatusOffline(nick):
    statusOffline =[]
    try:
        offline = tse.inp(("OFFLINE",object))
        statusOffline = list(offline[1])
        statusOffline.append(nick)
        tse.out(("OFFLINE",statusOffline))
        statusOffline = tse.rdp(("OFFLINE",object))
        return statusOffline[1]
    except:
        tse.out(("OFFLINE",tuple(nick)))
        statusOffline = tse.rdp(("OFFLINE",object))
        return statusOffline[1]