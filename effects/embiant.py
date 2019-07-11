from pygame import mixer
from ._base import EffectsBase
import time

class Embiant(EffectsBase):
    name = 'Embiant sound'

    def play(self):
        sound = mixer.Sound(self.path)
        self.channel.play(sound)
        time.sleep(sound.get_length())
        if self.continue_looping():
            self.play()
        return
