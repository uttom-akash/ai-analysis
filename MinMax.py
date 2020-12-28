import math 


class MinMax:
  def __init__(self,state):
    self.gameState=state

  def run(self,bot=1,player=0):   
    self.bot=bot
    self.player=player
    mxScore=-1000
    bestMove={}
    for row in range(3):
      for col in range(3):
         if self.gameState.boardState[row][col]==-1:
            self.gameState.boardState[row][col]=self.bot
            score=max(mxScore,self.minmax(1,False,-10000,10000))
            self.gameState.boardState[row][col]=-1

            if score > mxScore:
              mxScore=score
              bestMove={'row':row,'col':col}
    return bestMove
    

  def minmax(self,depth,maximizer,alpha,beta):
    score=self.evaluate()
    if score==10:
      return score-depth
    if score==-10:
      return score+depth
    if self.gameState.isVacant()==False:
      return 0

    if maximizer:
      mxScore=-1000
      for row in range(3):
        for col in range(3):
          if self.gameState.boardState[row][col]==-1:
            self.gameState.boardState[row][col]=self.bot
            score=self.minmax(depth+1,False,alpha,beta)
            mxScore=max(mxScore,score)
            self.gameState.boardState[row][col]=-1
            alpha=max(alpha,mxScore)
            if alpha>=beta:
              return mxScore
      return mxScore
    else :
      minScore=1000
      for row in range(3):
        for col in range(3):
          if self.gameState.boardState[row][col]==-1:
            self.gameState.boardState[row][col]=self.player
            score=self.minmax(depth+1,True,alpha,beta)
            minScore=min(minScore,score)
            self.gameState.boardState[row][col]=-1
            beta=min(beta,minScore)
            if alpha>=beta:
              return minScore
      return minScore
      
  def evaluate(self):
    gameResult=self.gameState.check()
    if gameResult['player']==self.bot:
      return 10
    elif gameResult['player']==self.player:
      return -10
    else:
       return 0