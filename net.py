from random import randint
import socket
from bingo import Bingo


class game():
    
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.29.102"
        self.port = 5505
        self.addr = (self.host, self.port)
        self.isserver=None
        self.player=Bingo()
    def setip(self,input):
        self.host=input
        # print(type(self.host))
    def wincheck(self):
        return self.player.countstrike>4

    def socksend(self,sock):
        val=int(input("Enter number: "))
        self.player.turn(val)
        self.player.winConditions()
        self.player.showgrid()
        print(f"Strikes: {self.player.countstrike} ")                        
        msg=str(val)+":"+str(self.wincheck())
        sock.send(str.encode(msg))
        if self.wincheck():
            print("YOU WIN !! :)")
            return True
        

    def sockrecv(self,sock):
        reply=sock.recv(2048).decode()
        arr=reply.split(":")
        self.player.turn(int(arr[0]))
        self.player.winConditions()
        self.player.showgrid()
        print(f"Strikes: {self.player.countstrike} ")
        if arr[1]=='True':
            print("YOU LOSE !! :(")
            return True
        if self.wincheck():
            print("YOU WIN !! :)")
            msg=":"+str(self.wincheck(self.player))
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
        while True:
            conn, addr=self.server.accept() 
            print("Connected to: ", addr)
            print('Game Start')
            tr=str(randint(0,1))
            conn.send(str.encode(tr))
            self.player.showgrid()
            while True:                                            
                tr = int(tr)
                if tr==0:
                    self.socksend(sock=conn)
                    tr=+1
                if self.sockrecv(sock=conn):
                    break
                if self.socksend(sock=conn):
                    break

            print(f'Connection Closed by {addr}')
            conn.close()

    def connect(self):
        self.server.connect(self.addr)
        print('Connected to server :)')


    def sendsrv(self):       
        tr=(self.server.recv(1024).decode())
        tr=int(tr)
        while True:
            self.player.showgrid()
            if tr==1:
                self.socksend(sock=self.server)
                tr=-1
            if self.sockrecv(sock=self.server):
                break
            if self.socksend(sock=self.server):
                break    
        self.server.close()