from pygame import mixer


class EffectsBase(object):
    name = None

    def __init__(self, path, loop):
        self.path = path
        self.loop = False
        self.channel = None

    def play(self):
        raise Exception("Not implemented method")

    def set_ready(self, force=False):
        if not mixer.get_init():
            pygame.mixer.init()
        self.channel = mixer.find_channel(force=force)

    def continue_looping(self):
        if self.loop:
            if type(self.loop) is int:
                if self.loop == 1:
                    self.loop = False
                else:
                    self.loop -= 1
                return True
        return False
