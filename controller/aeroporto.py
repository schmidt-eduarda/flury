# -*- coding: utf8 -*-

from controller.base import BaseControl
from view.aeroporto import AeroportoView
from model.aeroporto import AeroportoModel


class AeroportoControl(BaseControl):
    def __init__(self) -> None:
        super().__init__()
        self.View: AeroportoView = AeroportoView()
        self.Model: AeroportoModel = AeroportoModel()
