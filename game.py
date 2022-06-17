from random import randint
import socket
from bingo import Bingo

 
class game():
    
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 5505
        self.addr = (self.host, self.port)
        self.isserver=None
        self.player=Bingo()
        self.val=0
        self.tr=int(randint(0,1))
        self.iswin=-1

    def checkval(self,val):
        if(val==0):
            return
            
    def setip(self,ip):
        self.host=ip
        self.addr = (self.host, self.port)
    def wincheck(self):
        return self.player.countstrike>4

    def socksend(self,sock,val):
        self.val=val
        self.player.turn(self.val)
        self.player.winConditions()
        self.player.showgrid()
        print(f"Strikes: {self.player.countstrike} ")                        
        msg=str(self.val)+":"+str(self.wincheck())
        sock.send(str.encode(msg))
        self.val=0
        if self.wincheck():
            self.iswin=1
            print("YOU WIN !! :)")
            return True
        

    def sockrecv(self,sock):
        
        reply=sock.recv(2048).decode()
        arr=reply.split(":")
        print(arr)
        print(arr[0])
        self.player.turn(int(arr[0]))
        self.player.winConditions()
        self.player.showgrid()
        print(f"Strikes: {self.player.countstrike} ")
        if arr[1]=='True':
            self.iswin=0
            print("YOU LOSE !! :(")
            return True
        if self.wincheck():
            self.iswin=1
            print("YOU WIN !! :)")
            msg=":"+str(self.wincheck())
            sock.send(str.encode(msg))
            return True
        
    def serve(self):
        try:
            self.server.bind((self.host,self.port))

        except socket.error as e:
            print(str(e))
            return
        self.server.listen(1)
        print(f"[LISTENING] Server is listening on {self.host}")
        print("Waiting for Connection...")
        self.conn, self.addr2=self.server.accept() 
        print("Connected to: ", self.addr2)
        print('Game Start')
        self.conn.send(str.encode(str(self.tr)))
        self.player.showgrid()
        self.isserver=1
        print(bool(self.isserver))

    def connect(self):
        self.server.connect(self.addr)
        print('Connected to server :)')
        self.tr=int(self.server.recv(1024).decode())
        self.player.showgrid()
        self.isserver=0
        print(bool(self.isserver))

