from pygame import mixer
from ._base import EffectsBase
import time
import threading
import random


class RandomTiming(EffectsBase):
    name = 'Random Timing'

    def __init__(self, path, loop, timing=[1, 10]):
        super(RandomTiming, self).__init__(path, loop)
        self.timing = timing

    def play(self):
        rand = random.randrange(self.timing[0], self.timing[1])
        t = threading.Timer(rand, self._play_sound)
        t.start()
        return

    def _play_sound(self):
        sound = mixer.Sound(self.path)
        self.channel.play(sound)
        if self.continue_looping():
            self.play()
        return
