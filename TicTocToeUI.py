import tkinter as tk
from tkinter import messagebox
import random as r
from GameState import GameState
from MinMax import MinMax
import sys
sys.setrecursionlimit(10**6)

class GameUI:
    def __init__(self):
        self.reset()

    def reset(self):
        self.gameData=GameState()
        self.playerSym=['O','X']
        self.playerSymCol={'O':"deep sky blue",'X':"green"} 
        self.board=[[] for i in range(3)]
        self.drawGameUI()
    
    def drawWinBoard(self,winCels=[]):
        for i in range(3):
            row=winCels[i][0]
            col=winCels[i][1]
            self.board[row][col].config(bg="black")

    def showDialog(self,message):
        messagebox.showinfo(message)

    def click(self,row,col):
        self.board[row][col].config(text=self.playerSym[self.gameData.player],state=tk.DISABLED,disabledforeground=self.playerSymCol[self.playerSym[self.gameData.player]])
        self.playerLabel['text']=f"Player: {self.gameData.player}"
        self.gameData.setBoardState(row,col)
        checkStatus=self.gameData.check()
        
        if checkStatus['player']!=-1:
            self.drawWinBoard(checkStatus['moves'])
            self.showDialog("Congrats!!"+"'"+str(checkStatus['player'])+"' has won")
            self.reset()
        elif self.gameData.isVacant()==False:
            self.showDialog("Tied!!"+"The match ended in a draw")
            self.reset()

        self.gameData.togglePlayer()
        if self.gameData.player==1:
            self.takeBotTurn()

    def takeBotTurn(self):
        move=MinMax(self.gameData).run()
        self.click(move['row'],move['col'])

    def drawButton(self,frame,i,j):
        button=tk.Button(master=frame,padx=1,width=3,text="   ",font=('arial',40,'bold'),command= lambda row=i,col=j:self.click(row,col))
        self.board[i].append(button)
        self.board[i][j].grid(row=i,column=j)

    def drawGameUI(self):
        root=tk.Tk()                  
        root.title("Tic-Tac-Toe")
        self.drawGameInfo(root)
        self.drawBoard(root)
        root.mainloop()

    def drawGameInfo(self,root):
        infoFrame=tk.Frame(master=root)
        infoFrame.pack()
        self.playerLabel = tk.Label(master=infoFrame, text=f"Player: {self.gameData.player}",font=('arial',20,'bold'))
        self.playerLabel.pack()

    def drawBoard(self,root):
        boardFrame=tk.Frame(master=root)
        boardFrame.pack()  

        for i in range(3):
            for j in range(3):
                self.drawButton(boardFrame,i,j)
               
        
        
GameUI()