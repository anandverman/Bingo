from tkinter import *

class button():
    def __init__(self,frame,id,val):
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
        
        self.b=Button(master=frame, **self.property, command=lambda: self.onclick())
        self.b.grid(row=1+int(self.id/5),column=self.id%5)
    def onclick(self):
        self.b['state']=DISABLED
        self.b['bg']='black'
        
        

