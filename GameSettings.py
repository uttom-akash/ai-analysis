class GameSettings:
    def __init__(self):
        self.initialLevel =0 # 0=easy, 1=hard
        self.initialPlayer=0 # 0=player, 1=computer

    def setLevel(self,l):
        self.initialLevel=l
    
    def setPlayer(self,p):
        self.initialPlayer=p
        