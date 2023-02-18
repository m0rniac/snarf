# [Corpus; System Components]
import os
import platform

# [Corpus; SNARF Components].
from myLocal import SNARF
from gui import SnarfGUI
from kit import SnarfToolkit


# [Corpus; Screen cleaner].
if platform.system() == "Linux":
    os.system('clear')
elif platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')
    

# [Corpus; INIT].
if __name__ == "__main__":
    # [Corpus; DIR Settings]
    if os.path.isdir('snarfy') ==  False:
        os.mkdir('snarfy')
    elif os.path.isdir('snarfy') == True:
        pass

    # [Corpus; DIR saver].
    if os.path.isdir('myBuilds') is False:
        os.mkdir('myBuilds')
    elif os.path.isdir('myBuids') is True:
        pass
    
    # [Corpus; Exec].
    SnarfGUI.getFriendlyNames()
    SnarfGUI.getShortNames()
    SnarfGUI.initGUI(SnarfGUI.listFriendlyNames())