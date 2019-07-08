from pygame import mixer
from ._base import Effect
from ..modificators import *


class VolumeOscillator(Effect):
    name = 'VolumeOscillator'

    def __init__(self, path, loop, step=0.05):
        super(VolumeOscillator, self).__init__(path, loop)
        self.step = step

    def play(self, modificator='relu'):
    	x = self.channel.get_volume()
    	sound = mixer.Sound(self.path)
    	channel.play(sound)

    	while(channel.get_busy()):
    		rand = random.random()
    		if rand < eval(modificator)(x):
    			x = x - self.step
    		else:
    			x = x + self.step
    		time.sleep(self.step)
    		channel.set_volume(x)
        if self.continue_loop():
            self.play()
