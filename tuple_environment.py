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

def updateStatus(data):
    #data[0] = nick
    status = data[1]
    statusOnline  =[]
    statusOffline =[]
    if(status == True):
        try:
            online = tse.inp(("ONLINE",object))
            statusOnline = list(online[1])
            statusOnline.append(tuple(data))
            tse.out(("ONLINE",statusOnline))
            statusOnline = tse.rdp(("ONLINE",object))
            print(statusOnline) 
        except:
            tse.out(("ONLINE",tuple(data)))
            statusOnline = tse.rdp(("ONLINE",object))
            print(statusOnline) 
    else:
        try:
            offline = tse.inp(("OFFLINE",object))
            statusOffline = list(offline[1])
            statusOffline.append(tuple(data))
            tse.out(("OFFLINE",statusOffline))
            statusOffline = tse.rdp(("OFFLINE",object))
            print(statusOffline) 

        except:
            tse.out(("OFFLINE",tuple(data)))
            statusOffline = tse.rdp(("OFFLINE",object))
            print(statusOffline) 
            
updateStatus(['iza',True])
updateStatus(['hoza',False])