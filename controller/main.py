# -*- coding: utf8 -*-

from view.main import MainView
from controller.voo import VooControl
from controller.base import BaseControl
from controller.empresa import EmpresaControl
from controller.aeronave import AeronaveControl
from controller.aeroporto import AeroportoControl


class MainControll(object):
    def __init__(self):
        pass

    def run(self):
        operation_dict: dict[int, BaseControl] = {
            1: AeroportoControl,
            2: AeronaveControl,
            3: EmpresaControl,
            4: VooControl,
        }

        while True:
            operacao = MainView().show_menu()
            if operacao == 5:
                break

            if not operacao in operation_dict.keys():
                continue

            Control: BaseControl = operation_dict[operacao]
            Control().run()
