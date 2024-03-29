import linsimpy
tse = linsimpy.TupleSpaceEnvironment()
# 'izadora','iza',True,1,2,3
# ("USER", nick, user, status, latitude, longitude, distancia)
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
    tse.out(("USER", nick, [user, status, latitude, longitude, distancia]))

    user = tse.rdp(("USER",nick,[user, status, latitude, longitude, distancia]))
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
def readUser(nick):
    try:
        user = tse.rdp(("USER",nick, object))
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
def updateStatus(nick,status):
    tsOnline = []
    tsOffline = []
    user = tse.inp(("USER",nick,object))
    tsUser = list(user[2])
    tsUser[1] = status
    tse.out(("USER",nick,tsUser))
    
    if(status == True):
        try:
            offline   = tse.inp(("OFFLINE",object))
            tsOffline = list(offline[1])
            tsOffline.remove(nick)
            tse.out(("OFFLINE",tuple(tsOffline)))

            online    = tse.inp(("ONLINE",object))
            tsOnline  = list(online[1])
            tsOnline.append(nick)
            tse.out(("ONLINE",tuple(tsOffline)))
        except:
            tsOnline = [nick]
            tse.out(("ONLINE",tuple(tsOnline)))
    else:
        try:
            online   = tse.inp(("ONLINE",object))
            tsOnline = list(online[1])
            tsOnline.remove(nick)
            tse.out(("ONLINE",tuple(tsOnline)))

            offline    = tse.inp(("OFFLINE",object))
            tsOffline  = list(offline[1])
            tsOffline.append(nick)
            tse.out(("OFFLINE",tuple(tsOffline)))
        except:
            tsOffline = [nick]
            tse.out(("OFFLINE",tuple(tsOnline)))

    dataUser = tse.rdp(("USER",nick,object))
    return dataUser      

