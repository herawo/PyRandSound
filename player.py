from .effects._base import EffectsBase


class Player(object):
    effects = []
    channels = [0,1,2,3,4,5,6]

    def play(self):
        if not self._is_ready():
            ready = self._set_effects_ready()
            if not ready:
                raise Exception('Could not allocate channels to effect')
        for effect in self.effects:
            effect.play()

    def add_effect(self, effects):
        """
        args:
            effects: Effect or List, a list of Effect objects, can also be a
                     lonely Effect object
        """
        # Must supply a list of effect,
        # if not convert value into a single value list
        try:
            iter(effects)
        except TypeError:
            effects = [effects,]
        # effect given must be a subclass of class Effect
        errors = []
        for effect in effects:
            if not issubclass(type(effect), EffectsBase):
                errors.append('Object %s is not a subclass of Effect' % effect)
        if errors:
            raise Exception('\n'.join(errors))
        self.effects += effects

    def _is_ready(self):
        for effect in self.effects:
            if effect.channel is None:
                return False
        return True

    def _set_effects_ready(self):
        try:
            for not_ready_effect in self._get_not_ready_effects():
                not_ready_effect.set_ready(channels=self.channels)
            return True
        except Exception as e:
            import pdb; pdb.set_trace()
            return False

    def _get_not_ready_effects(self):
        not_ready_effects = []
        for effect in self.effects:
            if effect.channel is None:
                not_ready_effects.append(effect)
        return not_ready_effects
