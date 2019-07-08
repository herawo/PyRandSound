from pygame import mixer
from ._base import Effect
import time
import threading


class RandomTiming(Effect):
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
        time.sleep(sound.get_length())
        if self.continue_loop():
            self.play()
        return
