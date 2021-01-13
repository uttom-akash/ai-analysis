import tkinter as tk

class GameState:
    def __init__(self,level=0,player=0):
        self.level=level # 0=easy, 1=hard
        self.player=player
        self.boardState=[[-1 for j in range(3)] for i in range(3)]

    def setLevel(self,level):
        self.level=level
        
    def togglePlayer(self):
        self.player=(self.player+1)%2

    def setBoardState(self,player,r,c):
        self.boardState[r][c]=player

    def check(self):
        for i in range(3):
            # row check
            if self.boardState[i][0] !=-1 and self.boardState[i][0]==self.boardState[i][1] and self.boardState[i][1]==self.boardState[i][2]:
                return {'player':self.boardState[i][0] ,'moves': [(i,0),(i,1),(i,2)]}
            # column check
            if self.boardState[0][i]!=-1 and self.boardState[0][i]==self.boardState[1][i] and self.boardState[1][i]==self.boardState[2][i]:
                return {'player':self.boardState[0][i] ,'moves':[(0,i),(1,i),(2,i)]}
        
        if self.boardState[0][0]!=-1 and self.boardState[0][0]==self.boardState[1][1] and self.boardState[1][1]==self.boardState[2][2]:
            return {'player':self.boardState[0][0] ,'moves':[(0,0),(1,1),(2,2)]}
        if self.boardState[0][2]!=-1 and self.boardState[0][2]==self.boardState[1][1] and self.boardState[1][1]==self.boardState[2][0]:
            return {'player':self.boardState[0][2] ,'moves':[(0,2),(1,1),(2,0)]}
        return {'player': -1 ,'moves':[]}
    
    def isVacant(self):
        for row in range(3):
            for col in range(3):
                if self.boardState[row][col]==-1:
                    return True
        return False   