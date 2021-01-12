from UI import UI
from GameState import GameState
from GameSettings import GameSettings
from tkinter import *
from tkinter import messagebox
from MinMax import MinMax
from UiPath import Path
import time

class BoardUI(UI):
    def __init__(self,master,handleNavigation,settings=None):
        if settings==None:
            settings=GameSettings()

        self.master=master
        self.settings=settings
        self.navigate=handleNavigation
        self.gameData=GameState(settings.initialLevel,settings.initialPlayer)
        self.playerSym=['O','X']
        self.playerSymCol={'O':"blue",'X':"black"}
        self.player=['You','Computer']
        self.levelLab=['Easy','Hard']
        self.board=[[],[],[]]

    def draw(self):
        self.frame=Frame(master=self.master)
        self.frame.pack()
        self.drawGameInfo()
        self.drawBoard()
        self.takeGameDecision()

    def drawGameInfo(self):
        infoFrame=self.infoFrame=Frame(master=self.frame,padx=20,pady=20)
        infoFrame.pack()
        
        self.levelLabel = Label(master=infoFrame, text=f"Level: {self.levelLab[self.gameData.level]}",font=('arial',10,'bold'))
        self.levelLabel.pack()

        self.playerLabel = Label(master=infoFrame, text=f"Player: {self.player[self.gameData.player]}",font=('arial',10,'bold'))
        self.playerLabel.pack()
    
    def drawBoard(self):
        boardFrame=Frame(master=self.frame)
        boardFrame.pack()  
        for i in range(3):
            for j in range(3):
                self.drawButton(boardFrame,i,j)
    
    def drawButton(self,frame,i,j):
        button=Button(master=frame,padx=1,width=3,text="   ",font=('arial',40,'bold'),command= lambda row=i,col=j:self.click(row,col))
        self.board[i].append(button)
        self.board[i][j].grid(row=i,column=j)
    
    def updateButton(self,player,row,col):
        if player==-1:
            text="   "
            state=ACTIVE
            disabledforeground='white'
        else :
            text= self.playerSym[player]
            state=DISABLED
            disabledforeground=self.playerSymCol[self.playerSym[player]]
        bg='white'
        self.board[row][col].config(text=text,state=state,disabledforeground=disabledforeground,bg=bg)

    def updateGameInfo(self):
        self.playerLabel['text']=f"Player: {self.player[self.gameData.player]}"
        self.levelLabel['text']=f"Level: {self.levelLab[self.gameData.level]}"
        

    def click(self,row,col):
        previousPlayer=self.gameData.player
        self.gameData.togglePlayer()

        self.gameData.setBoardState(previousPlayer,row,col)
        self.updateButton(previousPlayer,row,col)
        self.updateGameInfo()
        self.takeGameDecision()

    def takeGameDecision(self):
        gameStatus=self.gameData.check()
        message="Do you want to play again?"
        userResponse=True
        if gameStatus['player']!=-1: # if anyone win 
            self.drawWinningBoard(gameStatus['moves'],gameStatus['player'])
            if gameStatus['player']==0:
                message="Congrats!!"+"'"+self.player[0]+"' have won the game!\n"+message
            else :
                message= 'Sorry, You have lost the game!\n'+message
            userResponse=self.showDialog(title="Tic tac toe",message=message)
            self.navigate(Path.settings)
        elif self.gameData.isVacant()==False: # if draw
            message="Tied!!"+"The match ended in a draw\n"+message
            userResponse= self.showDialog(title='Tic tac toe' ,message=message)
            self.navigate(Path.settings)
        elif self.gameData.player==1: # if player one(comp)'s turn
            self.takeBotTurn()
        
        if userResponse==False:
            exit()

    def drawWinningBoard(self,winCels=[],winningPlayer=0):
        self.infoFrame.destroy()
        if winningPlayer==0:
            bgCol= 'green'
        else :
            bgCol= 'red'

        for i in range(3):
            row=winCels[i][0]
            col=winCels[i][1]
            self.board[row][col].config(bg=bgCol)

    def showDialog(self,title='Game Result',message=''):
        resp=messagebox.askyesno(title=title, message=message)
        return resp

    def takeBotTurn(self):
        move=MinMax(self.gameData).run()
        self.click(move['row'],move['col'])

    def cleanup(self):
        self.frame.destroy()