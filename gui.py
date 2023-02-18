# [Corpus; GUI Components].
import os
import json
import datetime
import requests
import uuid
from tkinter import *
from tkinter import ttk

# [Corpus; SNARF Components].
from myLocal import SNARF
from builder import SnarfBuilder

# [Corpus; INIT]
class SnarfGUI:
    # {subCorpus; Local fuctions}
    """ A """
    def getFriendlyNames():
        """ Verify """
        if os.path.exists('./snarfy/dataFN.txt') is False:
            mk = open('./snarfy/dataFN.txt', 'w')
            mk.write('')
            mk.close()
        elif os.path.exists('./snarfy/dataFN.txt') is True:
            os.remove('./snarfy/dataFN.txt')
            mk = open('./snarfy/dataFN.txt', 'w')
            mk.write('')
            mk.close()

        """ Lecture """
        with open('./myLocal/voices_list.json', 'r') as f:
            route = json.load(f)

        """ Capture """
        n = 0
        for voice in range(0, len(route)):
            setName = route[n]["FriendlyName"]

            abc = open('./snarfy/dataFN.txt', 'a+')
            abc.write(str(setName) + '\n')
            abc.close()

            n = n + 1
    """ Lecture """
    def listFriendlyNames():
        newBase = open('./snarfy/dataFN.txt', 'r')
        rd = newBase.read()
        toList = rd.split('\n')
        toList.pop()
        
        return toList
    
    """ B """
    def getShortNames():
        """ Verify """
        if os.path.exists('./snarfy/dataSN.txt') is False:
            mk = open('./snarfy/dataSN.txt', 'w')
            mk.write('')
            mk.close()
        elif os.path.exists('./snarfy/dataSN.txt') is True:
            os.remove('./snarfy/dataSN.txt')
            mk = open('./snarfy/dataSN.txt', 'w')
            mk.write('')
            mk.close()

        """ Lecture """
        with open('./myLocal/voices_list.json', 'r') as f:
            route = json.load(f)

        """ Capture """
        n = 0
        for z in range(0, len(route)):
            setName = route[n]["ShortName"]

            abc = open('./snarfy/dataSN.txt', 'a+')
            abc.write(str(setName) + '\n')
            abc.close()

            n = n + 1
    """ Lecture """
    def listShortNames():
        newBase = open('./snarfy/dataSN.txt', 'r')
        rd = newBase.read()
        toList = rd.split('\n')
        toList.pop()
        
        return toList

    # {subCorpus; GUI}
    def initGUI(listValues):
        # [Corpus; VERSION].
        version = "0.0.1"

        # {subCorpus; Window Settings}
        root = Tk()
        root.resizable(0, 0)
        #root.geometry('1024x640')
        root.iconbitmap('./myLocal/logo.ico')
        root.title(' SNARF   |   ' + version)

        # {A; Choose voice}
        frameOne = LabelFrame(root, text = "List of voices:", bg = "#777777", fg = "white", padx = 35, pady = 15)
        frameOne.grid(row = 0, column = 0)
        
        
        """ Network Verification """
        try:
            req = requests.get("https://m0rniac.vercel.app/projects", timeout = 4)
        except (requests.ConnectionError, requests.Timeout):
            frameOne.config(text = "Oops! You need an internet connection", bg = "Red", fg = "White")
        else:
            frameOne.config(text = "Good, you have an internet connection", fg = "#00ff00")
        
        
        def selectVoice():
            co = combo.get()
            frameOne.config(text = "Voice '" + str(co) + "' loaded correctly.", fg = "Cyan")
            
            file = open('./snarfy/dataFN.txt', 'r')
            fileRd = file.read()
            locate = fileRd.split('\n')
            locate.pop()
            
            finder = locate.index(co)
            newFile = open("./snarfy/dataSN.txt", 'r')
            newRead = newFile.read()
            mSplit = newRead.split('\n')
            mSplit.pop()
                
            voiceName = mSplit[finder]
            return str(voiceName)
        
        cfg = StringVar()
        combo = ttk.Combobox(frameOne, textvariable = cfg, values = listValues, state = "readonly")
        combo.current(0)
        combo.pack(ipadx = 200, ipady = 0)
        
        btnSubmit = Button(frameOne, text = "Select voice", command = selectVoice)
        btnSubmit.pack(padx = 0, pady = 6, ipadx = 10, ipady = 0)
        
        
        # {B; SPACE (No important)}
        spaceFrame = LabelFrame(frameOne)
        spaceFrame.pack(padx = 0, pady = 10)
        
        
        # {C; Voice Settings}
        def rateValue(vol=''):
            aval = scaleRate.get()
            frameOne.config(text = "You are selecting '" + str(aval) + "' of rate", fg = "White")
            return aval
        def pitchValue(vol=''):
            aval = scalePitch.get()
            frameOne.config(text = "You are selecting '" + str(aval) + "' of pitch.", fg = "White")
            return aval
        def volumeValue(vol=''):
            aval = scaleVolume.get()
            frameOne.config(text = "You are selecting '" + str(aval) + "' of volume.", fg = "White")
            return aval
        
        scaleRate = Scale(frameOne, label = "Rate of voice:", from_ = 1, to = 20, orient = HORIZONTAL, length = 200, showvalue = 0, tickinterval = 2, command = rateValue)
        scaleRate.pack(padx = 0, pady = 2, ipadx = 140, ipady = 0)
        
        scalePitch = Scale(frameOne, label = "Pitch of voice:", from_ = 1, to = 20, orient = HORIZONTAL, length = 200, showvalue = 0, tickinterval = 2, command = pitchValue)
        scalePitch.pack(padx = 0, pady = 2, ipadx = 140, ipady = 0)
        
        scaleVolume = Scale(frameOne, label = "Volume of voice:", from_ = 1, to = 10, orient = HORIZONTAL, length = 200, showvalue = 0, tickinterval = 1, command = volumeValue)
        scaleVolume.pack(padx = 0, pady = 6, ipadx = 60, ipady = 0)
        
        def lastUpdate():
            inputUser = usrInput.get("1.0",'end-1c')
            
            datetimeVal = datetime.datetime.now()
            frameOne.config(text = "Last request added: " + str(datetimeVal), fg = "#E3E3E3")
            
            return inputUser
        
        def openDir():
            if os.path.isdir('myBuilds') is False:
                frameOne.config("Error, no dir exists")
            elif os.path.isdir('myBuilds') is True:
                print("DIR")
        
        # {D; Text Input}
        usrInput = Text(frameOne, height = 15, width = 80)
        usrInput.insert(END, "Hi there! write here!")
        usrInput.pack(padx = 0, pady = 5)
        
        btnBuild = Button(frameOne, text = "Add to request queue", command = lastUpdate)
        btnBuild.pack(padx = 5, pady = 5)
        
        
        hello = SnarfBuilder()
        def daConstructor():
            hello.mainBuilder(selectVoice(), rateValue(), pitchValue(), volumeValue(), lastUpdate())
            return frameOne.config(text = "Builded correctly.", fg = "yellow")
            
        def initConstructor():
            hello.startBuild(selectVoice(), rateValue(), pitchValue(), volumeValue(), lastUpdate())
            return frameOne.config(text = "Builded correctly", fg="yellow")
        
        # {subCorpus; Builder}
        btnConvert = Button(frameOne, text = "Convert", fg = "White", bg = "Black", command = lambda: [daConstructor(), initConstructor()])
        btnConvert.pack()
        
        #btnDir = Button(frameOne, text = "Show Audio DIR", fg = "Black", bg = "Yellow", command = openDir)
        #btnDir.pack()
        
        # [Corpus; Render].
        root.mainloop()
