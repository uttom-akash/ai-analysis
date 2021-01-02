from tkinter import *
from GameSettings import GameSettings as Settings
from UiPath import Path
from UI import UI

class GameSettingsUi(UI):
    def __init__(self,master,onSubmit,settings=None):
        if settings==None:
            settings=Settings()

        self.master=master
        self.settings=settings
        self.submit=onSubmit

    def draw(self):
        frame=self.frame=Frame(master=self.master,padx=20,pady=20)
        frame.pack()

        # inital level 
        Label(frame,text="""Select Level""",justify = LEFT,padx = 20,font=('arial',10,'bold')).pack(anchor=W)
        level=IntVar()
        level.set(self.settings.initialLevel)
        Radiobutton(master=frame,text='Easy',padx = 20,variable=level,value=0,command=lambda : self.settings.setLevel(level.get())).pack(anchor=W)
        Radiobutton(master=frame,text='Hard',padx = 20,variable=level,value=1,command=lambda : self.settings.setLevel(level.get())).pack(anchor=W)

        # initial player
        Label(frame,text="""Select player to play first""",padx = 20,pady=5,font=('arial',10,'bold')).pack()
        player=IntVar()
        player.set(self.settings.initialPlayer)
        Radiobutton(master=frame,text='You',padx = 20,variable=player,value=0,command=lambda : self.settings.setPlayer(player.get())).pack(anchor=W)
        Radiobutton(master=frame,text='Computer',padx = 20,variable=player,value=1,command=lambda : self.settings.setPlayer(player.get())).pack(anchor=W)

        # Ok
        Button(master=frame,padx=20,width=3,text='Save',command=lambda :self.submit(self.settings)).pack()
    
    def cleanup(self):
        self.frame.destroy()


