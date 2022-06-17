from tkinter import *
from guiclass import *
from functions import *



window=Tk()
window.title("Bingo")
window.geometry("585x500")
bg=Frame(window,height="500",width="600",bg="black")
bg.grid()
status=StringVar()


frame0=Frame(window,height="600",width="600")
head_00=Label(frame0,text="BINGO!",font=('System','35')).grid(pady='30',row='0',columnspan='3')

e_00=Entry(frame0,width='20')

e_00.insert(0,"Enter Server's IP")
b_OO=Button(frame0,text='Create a game',font=('','10'),command=lambda: create(player,b_03)).grid(row='1',columnspan='2',column='0',padx='5',pady='5')
b_O1=Button(frame0,text='Join a game',font=('','10'),command=lambda: join(e_00,b_02,b_03)).grid(row='1',column='2',padx='5',pady='2')
b_02=Button(frame0,text='Enter',font=('','8'),command=lambda: enter(e_00,player))

b_03=Button(frame0,text='Start Game',font=('','10'),command=lambda:start1(frame0,frame1,player,window,status,b_10))



frame1=Frame(window,height="600",width="600",bg="black")
heading=Label(frame1,text="B I N G O",font=('System','26'),bg="#000000",fg='white').grid(row=0,pady='5',columnspan=5,sticky=N)

b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range (0,25):
    b[i]=button(frame1,i,player.player.grid[i],status)

btnproperty={'width':'3','font':('Calibri 19'),'fg':'white','bg':'#000000'}
tileB=Button(frame1,text='B',**btnproperty)
tileB.grid(row='6',column='0',pady='5')
tileI=Button(frame1,text='I',**btnproperty)
tileI.grid(row='6',column='1',pady='5')
tileN=Button(frame1,text='N',**btnproperty)
tileN.grid(row='6',column='2',pady='5')
tileG=Button(frame1,text='G',**btnproperty)
tileG.grid(row='6',column='3',pady='5')
tileO=Button(frame1,text='O',**btnproperty)
tileO.grid(row='6',column='4',pady='5')
status.set('Game Started')
e_10=Entry(frame1,width='20',state='readonly',textvariable=status)
e_10.grid(row='7',column='0',columnspan='5')


b_10=Button(frame1,text='Quit',font=('','10'),width='8',command=lambda:window.destroy())
def update():
    global b
    global tileB
    global tileI
    global tileN
    global tileG
    global tileO

    updatebuttons(b,player)
    updatebingo(player,tileB,tileI,tileN,tileG,tileO)
    window.after(50,update)


window.after(50,update)


frame0.grid(row=0,column=0,sticky='ns')

