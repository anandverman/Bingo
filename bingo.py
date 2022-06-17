import random

class Bingo:
    def __init__(self):
        self.grid=list(range(1,26))
        random.shuffle(self.grid)
        self.countstrike=0

    def showgrid(self):
        for i in range(0,25):
            if i%5==0:
                print("\n")
            print("%3d" %(self.grid[i]),end=' ')
        print()

    def turn(self,val):
        for i, num in enumerate(self.grid):
            if num==val:
                self.grid[i]= -1 * num
    
    def winConditions(self):
        totalcount=0
        for i in range(0,5):
            count=0
            for j in range(0,5):
                if self.grid[i*5+j]< 0:
                    count+=1
            if count==5:
                totalcount+=1
            count=0
            for j in range(0,5):
                if self.grid[i+j*5]< 0:
                    count+=1
            if count ==5:
                totalcount+=1
        count=0
        for i in range(0,5):
            if self.grid[i*5+i]< 0:
                count+=1
        if count==5:
                totalcount+=1
        count=0
        for i in range(0,5):
            if self.grid[i*5+(4-i)]< 0:
                count+=1
        if count==5:
                totalcount+=1
        self.countstrike=totalcount
        return totalcount
    
    def checkbingo(self):
        return self.countstrike >5 

    
    def startGame(self):
        while not self.checkbingo():
            self.showgrid()
            print(f"Strikes: {self.countstrike} ")
            val=int(input("Enter number: "))
            self.turn(val)
            self.winConditions()            
        else:
            self.showgrid()
            print(f"Strikes: {self.countstrike} ")
            print("You WIN !!")
           


if __name__ == "__main__":
    bingo=Bingo()
    bingo.startGame()
