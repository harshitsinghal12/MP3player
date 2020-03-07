import os
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
from tkinter import *
import tkinter.font as font

root = Tk()
root.minsize(1000,300)



listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index = 0

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname

def playsong(event):
    pygame.mixer.music.play()
    v.set("")

def pausesong(event):
    pygame.mixer.music.pause()
    v.set("")

def resumesong(event):
    pygame.mixer.music.unpause()
    v.set("")

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname

fontsize=font.Font(size=20)

label = Label(root,text='Music Player',bg="black",fg="white")
label['font']=fontsize
label.pack()

listbox = Listbox(root,bg="black",fg="white")
listbox['font']=fontsize
listbox.pack(fill=BOTH,expand= TRUE)
#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()

playbutton = Button(root,text = 'PLAY' ,fg="white",bg="red")
playbutton['font']=fontsize
playbutton.pack(fill=X)

pausebutton=Button(root,text='PAUSE',bg="red",fg="white")
pausebutton['font']=fontsize
pausebutton.pack(fill=X)

resumebutton=Button(root,text='RESUME',bg="red" ,fg="white")
resumebutton['font']=fontsize
resumebutton.pack(fill=X)

nextbutton = Button(root,text = 'NEXT',bg="red",fg="white")
nextbutton['font']=fontsize
nextbutton.pack(fill=X)

previousbutton = Button(root,text = 'PREVIOUS',bg="red",fg="white")
previousbutton['font']=fontsize
previousbutton.pack(fill=X)

stopbutton = Button(root,text="STOP",bg="red",fg="white")
stopbutton['font']=fontsize
stopbutton.pack(fill=X)

playbutton.bind("<Button-1>",playsong)
pausebutton.bind("<Button-1>",pausesong)
resumebutton.bind("<Button-1>",resumesong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()

root.mainloop()
