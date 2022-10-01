# -*- coding: utf8 -*-

from view.voo import VooView
from model.voo import VooModel
from controller.base import BaseControl


class VooControl(BaseControl):
    def __init__(self) -> None:
        super().__init__()
        self.View: VooView = VooView()
        self.Model: VooModel = VooModel()
