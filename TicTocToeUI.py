import tkinter as tk
from tkinter import messagebox
import random as r
from GameState import GameState
from MinMax import MinMax
import sys
sys.setrecursionlimit(10**6)

class GameUI:
    def __init__(self):
        self.playerSym=['O','X']
        self.playerSymCol={'O':"deep sky blue",'X':"green"} 
        self.initGameUI()
        
    def initGameUI(self):
        self.gameData=GameState()
        self.board=[[],[],[]]
        self.root=tk.Tk()                  
        self.root.title("Tic-Tac-Toe")
        self.drawGameInfo()
        self.drawBoard()
        self.root.mainloop()
    
    def drawGameInfo(self):
        infoFrame=tk.Frame(master=self.root)
        infoFrame.pack()
        
        tk.Label(infoFrame,text="""Select Level:""",justify = tk.LEFT,padx = 20).pack()
        level=tk.IntVar()
        level.set(0)
        tk.Radiobutton(master=infoFrame,text='Easy',padx = 20,variable=level,value=0,command=lambda : self.gameData.setLevel(level.get())).pack()
        tk.Radiobutton(master=infoFrame,text='Hard',padx = 20,variable=level,value=1,command=lambda : self.gameData.setLevel(level.get())).pack()

        self.playerLabel = tk.Label(master=infoFrame, text=f"Player: {self.gameData.player}",font=('arial',20,'bold'))
        self.playerLabel.pack()

    def drawBoard(self):
        boardFrame=tk.Frame(master=self.root,padx=5)
        boardFrame.pack()  
        for i in range(3):
            for j in range(3):
                self.drawButton(boardFrame,i,j)
    
    def drawButton(self,frame,i,j):
        button=tk.Button(master=frame,padx=1,width=3,text="   ",font=('arial',40,'bold'),command= lambda row=i,col=j:self.click(row,col))
        self.board[i].append(button)
        self.board[i][j].grid(row=i,column=j)

    def reset(self):
        self.gameData=GameState()
        self.updateGameInfo()
        self.resetBoard()

    def updateGameInfo(self):
        self.playerLabel['text']=f"Player: {self.gameData.player}"
    
    def resetBoard(self):
        for row in range(3):
            for col in range(3):
                self.updateButton(-1,row,col)

    def updateButton(self,player,row,col):
        if player==-1:
            text="   "
            state=tk.ACTIVE
            disabledforeground='white'
        else :
            text= self.playerSym[player]
            state=tk.DISABLED
            disabledforeground=self.playerSymCol[self.playerSym[player]]
        bg='white'
        self.board[row][col].config(text=text,state=state,disabledforeground=disabledforeground,bg=bg)

    def takeGameDecision(self):
        gameStatus=self.gameData.check()
        if gameStatus['player']!=-1:
            self.drawWinBoard(gameStatus['moves'])
            self.showDialog("Congrats!!"+"'"+str(gameStatus['player'])+"' has won")
            self.reset()
        elif self.gameData.isVacant()==False:
            self.showDialog("Tied!!"+"The match ended in a draw")
            self.reset()
        if self.gameData.player==1:
            self.takeBotTurn()

    def drawWinBoard(self,winCels=[]):
        for i in range(3):
            row=winCels[i][0]
            col=winCels[i][1]
            self.board[row][col].config(bg="black")

    def showDialog(self,message):
        messagebox.showinfo(message)

    def click(self,row,col):
        previousPlayer=self.gameData.player
        self.gameData.togglePlayer()
        self.gameData.setBoardState(previousPlayer,row,col)
        self.updateButton(previousPlayer,row,col)
        # self.gameData.togglePlayer()
        self.updateGameInfo()
        self.takeGameDecision()

    def takeBotTurn(self):
        move=MinMax(self.gameData).run()
        self.click(move['row'],move['col'])

    
GameUI()