from tkinter import *
from game import *

player=game()
class button():
    def __init__(self,frame,id,val,status):
        self.id=id
        self.property = {
            'text':val,
            'bg':"#660066",
            'width':3,
            'fg':"white",
            'activebackground':"blue",
            'activeforeground':"grey",
            'font':"Calibri 19"
            
        }
        self.val=val
        self.b=Button(master=frame, **self.property, command=lambda: self.onclick(status))
        self.b.grid(row=1+int(self.id/5),column=self.id%5)
        
    def update(self,val):
        if val+int(self.b['text'])==0:
            self.b['state']=DISABLED
            self.b['bg']='black'
            
    def onclick(self,status):
        status.set("Opponent's Turn")
        player.player.turn([int(self.val)])
        self.b['state']=DISABLED
        self.b['bg']='black'
        player.val=self.val
        
        
        

