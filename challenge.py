pathInput1 = 'input1.txt'
pathInput2 = 'input2.txt'
pathOutput = 'output.txt'
Umax = 10
Ttask = 5
serversTicks = []

def debug(line, session, servers):
    print("-"* 10)
    if line:
        print("Input:", int(line))
    else:
        print("Input:", "#")
    print("Session:", session)
    print("Servers:", servers)      
    print("Servers Ticks:", serversTicks)
    print("$" + str(sum(serversTicks)))

# Output Write
def outputWrite(output, users):
    while 0 in users: users.remove(0)
    if len(users) > 0:
        out = ', '.join(str(i) for i in users)
        output.write(out + "\n")
    print('Output:', users)
    
# Servers Distribution
def serversDistrib(servers, session):
    if len(session) % Umax > 0:     
        serversNeed = int(len(session) / Umax) + 1
    else:
        serversNeed = int(len(session) / Umax)
    
    if len(servers) == 0 and serversNeed > 0:
        for i in range(serversNeed):
            servers.append(0)
        if servers != []:
            servers = [i+1 for i in servers]
        return servers
        
    if len(servers) > serversNeed:
        if servers != []:
            servers = [i+1 for i in servers]
        while(serversNeed != len(servers)):
            if servers == []:
                break
            maxValueServer = 0
            for i in servers:
                if i > maxValueServer:
                    maxValueServer = i
            serversTicks.append(maxValueServer)
            servers.remove(maxValueServer)
            serversNeed -+ 1
        
        return servers
    
    elif len(servers) < serversNeed:
        if servers != []:
            servers = [i+1 for i in servers]
        for i in range(serversNeed - len(servers)):
            servers.append(0)
        return servers
    
    else:
        if servers != []:
            servers = [i+1 for i in servers]
        return servers

def usersOutput(users, session):
    # "for" to be Fixed...
    for i in range(len(session)):
        users.append(0)
    
    if len(session) < sum(users):
        for i, item1 in enumerate(users):
            while(len(session) < sum(users) and users[i] > 0):
                users[i] -= 1
            
    if len(session) > sum(users):
        for i, item2 in enumerate(users):
            while(len(session) > sum(users) and users[i] < Umax):
                users[i] += 1

# Main
with open(pathInput1) as input1, open(pathOutput, 'w') as output:
    line = input1.readline()
    servers = []
    session = []
    users = []
    while(line or len(session)):
        #Session per User
        if line:
            if(int(line) >= 0):
                for i in range(int(line)):
                    session.append(0)
                
        if session != []:
            session = [i+1 for i in session]
        
        while Ttask+1 in session: session.remove(Ttask+1)           
        
        # Server distribution for users
        servers = serversDistrib(servers, session)
           
        # Users Output
        usersOutput(users, session)

        # Last Check
        if sum(users) == Umax:
            users = []
            users.append(Umax)
        
        # Output Write
        outputWrite(output, users)        
        
        # Prints
        #debug(line, session, servers)        
        
        line = input1.readline()
    output.write("$" + str(sum(serversTicks)))
