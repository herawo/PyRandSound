from pygame import mixer
from ._base import EffectsBase
from ..modificators import *
import random
import time


class VolumeOscillator(EffectsBase):
    name = 'VolumeOscillator'

    def __init__(self, path, loop, step=0.05):
        super(VolumeOscillator, self).__init__(path, loop)
        self.step = step

    def play(self, modificator='relu'):
        x = self.channel.get_volume()
        sound = mixer.Sound(self.path)
        self.channel.play(sound)

        while(self.channel.get_busy()):
            rand = random.random()
            if rand < eval(modificator)(x):
                x = x - self.step
            else:
                x = x + self.step
            time.sleep(self.step)
            self.channel.set_volume(x)
        if self.continue_looping():
            self.play()
