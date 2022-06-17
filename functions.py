from socket import gethostbyname,gethostname

isserver=False
isstart=False
ui=0
gameobj=0  

def create(player,b_03):
    ip=gethostbyname(gethostname())
    player.setip(ip)
    b_03.grid(row='3',columnspan='3',pady='5')
    global isserver
    isserver=True

def join(e_00,b_02,b_03):
    e_00.grid(row='2',column='0',columnspan='2')
    b_02.grid(row='2',column='2')
    b_03.grid(row='3',columnspan='3',pady='5')
    global isserver
    isserver=False

def enter(e_00,player):
    ip=e_00.get()
    player.setip(ip)
    print(ip)

def updatebuttons(b,player):
    for i in range (0,25):
        b[i].update(player.player.grid[i])
def updatebingo(player,tileB,tileI,tileN,tileG,tileO):
    if player.player.countstrike>0:
        tileB['bg']='green'
    if player.player.countstrike>1:
        tileI['bg']='green'
    if player.player.countstrike>2:
        tileN['bg']='green'
    if player.player.countstrike>3:
        tileG['bg']='green'
    if player.player.countstrike>4:
        tileO['bg']='green'

def end(player,status,sockobj,b_10):
    if player.iswin!=-1:
        if(player.iswin):
            status.set('You WIN!!^o^')
        else:
            status.set('You LOSE >_<')
        sockobj.close()
        b_10.grid(row='8',column='1',pady='20',columnspan=3)
    return
                

def start1(frame0,frame1,player,window,status,b_10):
    global gameobj
    global ui
    gameobj=player
    ui=window
    frame0.grid_forget()
    frame1.grid(row=0,sticky='ns')
    if(isserver==True):
        player.serve()
        comm(window,player,status,b_10)
    elif(isserver==False):
        player.connect()
        comm(window,player,status,b_10)
    
    

def comm(window,player,status,b_10):
    if(player.isserver==1):
        sockobj=player.conn
    else:
        sockobj=player.server

    if player.tr==player.isserver:
        player.sockrecv(sock=sockobj)
        player.tr=-1

    if player.val==0:
        window.after(200,lambda:comm(ui,gameobj,status,b_10))
    else:
        player.socksend(sock=sockobj,val=player.val)
        end(player,status,sockobj,b_10)
        player.val=0
        window.after(200,lambda:comm(ui,gameobj,status,b_10))
        player.sockrecv(sock=sockobj)
        status.set("Your turn")
        end(player,status,sockobj,b_10)
    end(player,status,sockobj,b_10)

