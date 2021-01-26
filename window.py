from tkinter import *
from guiclass import *

window=Tk()
window.title("Bingo")
window.geometry("600x600")
bg=Frame(window,height="600",width="600",bg="black")


frame0=Frame(window,height="600",width="600",)#bg='red'
head_00=Label(frame0,text="BINGO!",font=('System','35')).grid(pady='30',row='0',columnspan='3')
head_01=Label(frame0,text="Play as:")
e_00=Entry(frame0,width='20')
e_00.grid(row='2',column='0',columnspan='2')
e_00.insert(0,"Enter Server's IP")
b_OO=Button(frame0,text='Create a game',font=('','10')).grid(row='1',columnspan='2',column='0',padx='5',pady='5')
b_O1=Button(frame0,text='Join a game',font=('','10')).grid(row='1',column='2',padx='5',pady='2')

b_02=Button(frame0,text='Enter',font=('','8')).grid(row='2',column='2')
b_03=Button(frame0,text='Start Game',font=('','10')).grid(row='3',columnspan='3',pady='5')

frame1=Frame(window,height="600",width="600",bg="blue")
heading=Label(frame1,text="B I N G O",font=('System','26'),bg="#660066",fg='white').grid(row=0,pady='5',columnspan=5,sticky=N)

b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range (0,25):
    b[i]=button(frame1,i, 0)

tileB=Button(frame1,text='B',width='3',font=('Calibri','19'),fg='white',bg='#000000',activebackground="yellow").grid(row='6',column='0',pady='5')
tileI=Button(frame1,text='I',width='3',font=('Calibri','19'),fg='white',bg='#000000',activebackground="yellow").grid(row='6',column='1',pady='5')
tileN=Button(frame1,text='N',width='3',font=('Calibri','19'),fg='white',bg='#000000',activebackground="yellow").grid(row='6',column='2',pady='5')
tileG=Button(frame1,text='G',width='3',font=('Calibri','19'),fg='white',bg='#000000',activebackground="yellow").grid(row='6',column='3',pady='5')
tileO=Button(frame1,text='O',width='3',font=('Calibri','19'),fg='white',bg='#000000',activebackground="yellow").grid(row='6',column='4',pady='5')
status=StringVar()
status.set('Game Started')
e_10=Entry(frame1,width='20',state='readonly',textvariable=status)

e_10.grid(row='7',column='0',columnspan='5')


bg.grid()
frame0.grid(row=0)
#frame1.grid(row=0)
# btn2.grid(row=1,column=1)
window.mainloop()