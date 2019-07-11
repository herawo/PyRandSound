from pygame import mixer
from ._base import EffectsBase
from ..modificators import *
import random
import time


class VolumeOscillator(EffectsBase):
    name = 'VolumeOscillator'

    def __init__(self, path, loop, step=0.05):
        """
        args:
            path : String, the relative or full path to the .wav file
            loop : int or boolean, True for eternal loop,
                                   int for fix number of loops
                                   False for no loop at all
            step: float, the more it's high, the less continuous the sound
                         oscillaitons will be
        """
        super(VolumeOscillator, self).__init__(path, loop)
        self.step = step

    def play(self, modificator='relu'):
        """
        args:
            modificator: String, the name of the method defining the probabilty
                                 repartition for oscillations
        """
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
