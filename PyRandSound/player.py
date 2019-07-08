from .effects._base import Effect


class Player(object):
    effects = []

    def play(self):
        if not self._is_ready():
            ready = self._set_effects_ready(force=True)
            if not ready:
                raise Exception('Could not allocate channels to effect,
                                'try force=True if not already given')
        for effect in self.effects:
            effect.play()

    def add_effect(self, effects):
        # Must supply a list of effect,
        # if not convert value into a single value list
        try:
            iter(some_object)
        except TypeError:
            effects = [effects,]
        # effect given must be a subclass of class Effect
        errors = []
        for effect in effects:
            if issubclass(type(effect), Effect):
                errors.append('Object %s is not a subclass of Effect' % effect)
        if errors:
            raise Exception('\n'.join(errors))
        self.effects.append(effects)

    def _is_ready(self):
        for effect in self.effects:
            if effect.channel is None:
                return False
        return True

    def _set_effects_ready(self, force=False):
        try:
            for not_ready_effect in self._get_not_ready_effects():
                not_ready_effect.set_ready(force=force)
            return True
        except:
            return False

    def _get_not_ready_effects(self):
        not_ready_effects = []
        for effect in self.effects:
            if effect.channel is None:
                not_ready_effects.append(effect)
        return not_ready_effects
