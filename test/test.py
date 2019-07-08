from PyRandSound.player import Player
from PyRandSound.effects.random_timing import RandomTiming

def test_2_random_timing():
    effect1 = RandomTiming('sounds/sound5.wav', 2, [2, 5])
    effect2 = RandomTiming('sounds/sound6.wav', 5, [5, 10])

    player = Player()
    player.add_effect(effect1)
    player.add_effect(effect2)
    player.play()
