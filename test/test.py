from PyRandSound.player import Player
from PyRandSound.effects.random_timing import RandomTiming
from PyRandSound.effects.volume_oscillator import VolumeOscillator
import unittest

class SoundTests(unittest.TestCase):
    # def test_random_timing(self):
    #     effect1 = RandomTiming('test/sounds/sound5.wav', 2, [2, 5])
    #     effect2 = RandomTiming('test/sounds/sound6.wav', 5, [5, 10])
    #     player = Player()
    #     player.add_effect(effect1)
    #     player.add_effect(effect2)
    #     player.play()
    #
    # def test_volume_oscilating(self):
    #     effect3 = VolumeOscillator('test/sounds/sound4.wav', True)
    #     player = Player()
    #     player.add_effect(effect3)
    #     player.play()

    def test_mixed(self):
        effect2 = RandomTiming('test/sounds/sound6.wav', 5, [5, 10])
        effect3 = VolumeOscillator('test/sounds/sound4.wav', True)
        player = Player()
        player.add_effect(effect2)
        player.add_effect(effect3)
        player.play()
