# [Corpus; Async Components].
import os
import uuid
import asyncio


# [Corpus; SNARF Components].
from myLocal import SNARF

# [Corpus; Main Class].
class SnarfBuilder:
    # [Corpus; Main].
    def __init__(self) -> None:
        pass
    
    async def mainBuilder(self, selectVoice, rateValue, pitchValue, volumeValue, lastUpdate):
        self.selectVoice = selectVoice
        self.rateValue = rateValue
        self.pitchValue = pitchValue
        self.volumeValue = volumeValue
        self.lastUpdate = lastUpdate
        
        # {subCorpus; DIR}
        if os.path.isdir('myBuilds') is False:
            os.mkdir('myBuilds')
        elif os.path.isdir('myBuilds') is True:
            pass
        
        # {subCorpus; Save Settings}
        speech = SNARF()
        n = uuid.uuid1()
        filename = './myBuilds/snarfAudio_' + str(n) + '.mp3'
        
        """ Set Voice """
        await speech.setVoice(selectVoice)
        
        """ Other Settings """
        await speech.setRate(rateValue)
        await speech.setPitch(pitchValue)
        await speech.setVolume(volumeValue)
        
        """ Synthesize """
        await speech.synthesize(lastUpdate.strip(), filename)
        
    # [Corpus; INIT]
    def startBuild(self, selectVoice, rateValue, pitchValue, volumeValue, lastUpdate):
        self.selectVoice = selectVoice
        self.rateValue = rateValue
        self.pitchValue = pitchValue
        self.volumeValue = volumeValue
        
        snarf_loop = asyncio.get_event_loop()
        snarf_loop.run_until_complete(self.mainBuilder(selectVoice, rateValue, pitchValue, volumeValue, lastUpdate))

# [Corpus; Auto-Exec].
#hello_world = SnarfBuilder()