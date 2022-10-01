# -*- coding: utf8 -*-

from view.aeronave import AeronaveView
from controller.base import BaseControl
from model.aeronave import AeronaveModel


class AeronaveControl(BaseControl):
    def __init__(self) -> None:
        super().__init__()
        self.View: AeronaveView = AeronaveView()
        self.Model: AeronaveModel = AeronaveModel()
