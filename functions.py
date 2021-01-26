from socket import gethostbyname,gethostname
#from game import *

isserver=False
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
    global isserver
    isserver=False

def start(player,frame0,frame1):
    frame0.grid_forget
    frame1.grid(row=0)
    if(isserver==True):
        player.serve()
    elif(isserver==False):
        player.connect()
        player.sendsrv()
    
