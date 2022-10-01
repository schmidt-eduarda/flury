# -*- coding: utf8 -*-


class SingletonSample(object):
    def __init__(self, cls):
        self._cls = cls

    def get_new_instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError(
            "Clase Singleton precisa ser acessada pelo método `get_new_instance()`."
        )

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)
