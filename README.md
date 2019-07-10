# PyRandSound
Student projet to generate random sounds using the Pygame Mixer

## Installation  
apt-get install pip  
pip install virtualenv  
virtualenv <nom_de_lenv>  
pip install pygame nose  
source <nom_de_lenv>/bin/activate  

pip install git+https://github.com/herawo/PyRandSound

## Usage
```python
from PyRandSound.player import Player
from PyRandSound.effects.random_timing import RandomTiming
from PyRandSound.effects.volume_oscillator import VolumeOscillator

effect1 = RandomTiming('sounds/sound5.wav', 2, [2, 5])
effect2 = RandomTiming('sounds/sound6.wav', 5, [5, 10])
player = Player()
player.add_effect(effect1)
player.add_effect(effect2)
player.play()
```


## Run test  
cd PyRandSound/test  
nosetests  
