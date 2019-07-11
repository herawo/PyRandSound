from pygame import mixer


class EffectsBase(object):
    name = None

    def __init__(self, path, loop=False):
        self.path = path
        self.loop = loop
        self.channel = None

    def play(self):
        raise Exception("Not implemented method")

    def set_ready(self, channels=None):
        if not mixer.get_init():
            mixer.init()
        if channels is None:
            self.channel = mixer.find_channel()
        else:
            self.channel = mixer.Channel(channels.pop())

    def continue_looping(self):
        if self.loop:
            if type(self.loop) is int:
                if self.loop <= 1:
                    self.loop = False
                else:
                    self.loop -= 1
            return True
        return False
