# -*- coding: utf8 -*-

from view.empresa import EmpresaView
from model.empresa import EmpresaModel
from controller.base import BaseControl


class EmpresaControl(BaseControl):
    def __init__(self) -> None:
        super().__init__()
        self.View: EmpresaView = EmpresaView()
        self.Model: EmpresaModel = EmpresaModel()
