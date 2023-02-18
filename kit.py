import os

class SnarfToolkit:
    # {subCorpus; Verify .TXT}
    def makeData(topic):
        text = str(topic)
        if os.path.exists('myData.txt') is False:
            f = open('myData.txt', 'w')
            f.write(text)
            f.close()
        elif os.path.exists('myData.txt') is True:
            os.remove('myData.txt')
            newF = open('myData.txt', 'w')
            newF.write(text)
            newF.close()
            
    # {subCorpus; Read .TXT}
    def readData():
        try:
            abc = open('myData.txt')
            abc_read = abc.read()
            
            return abc_read
        except:
            print("[Error; First you need to create a data file].")