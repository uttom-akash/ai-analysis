from tkinter import  *
from tkinter import messagebox
import random as r
from GameState import GameState
from MinMax import MinMax
from UiPath import Path
from GameSettingsUi import GameSettingsUi
from UI import UI
from BoardUI import BoardUI
import sys
import threading
sys.setrecursionlimit(10**6)


class GameUI:
    def __init__(self):
        self.path=Path.settings
        self.currentUi=UI()
        self.settings=None
        thread=threading.Thread(target=self.initGameUI)
        thread.start()
        
    def onSubmitFromSettings(self,settings):
        self.settings=settings
        self.handleNavigation(Path.board)

    def handleNavigation(self,path):
        self.path=path
        self.drawGameUi()
        
    def initGameUI(self):
        self.gameData=GameState()
        self.board=[[],[],[]]
        self.root=Tk()                  
        self.root.title("Tic Tac Toe")
        self.drawGameUi()
        self.root.mainloop()
    
    def drawGameUi(self):
        self.currentUi.cleanup()
        if self.path==Path.settings:
            self.currentUi=GameSettingsUi(self.root,onSubmit=self.onSubmitFromSettings,settings=self.settings,)
            self.currentUi.draw()
        else :
            self.currentUi= BoardUI(self.root,handleNavigation=self.handleNavigation,settings=self.settings)
            self.currentUi.draw()
    
GameUI()