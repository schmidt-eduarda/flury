# -*- coding: utf8 -*-

from view.main import MainView


class EmpresaView(MainView):
    def __init__(self):
        super().__init__()
        self.name: str = "Empresa"
