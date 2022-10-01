# -*- coding: utf8 -*-

from view.main import MainView


class AeroportoView(MainView):
    def __init__(self):
        super().__init__()
        self.name: str = "Aeroporto"
