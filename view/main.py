# -*- coding: utf8 -*-

from os import system


class MainView(object):
    def __init__(self):
        self.name: str = "Base"

    def show_menu(self) -> int:
        system("cls")
        print(
            """
            *-* FLURY COMPANHIAS AÉREAS *-*

            1 - Cadastro de Aeroportos
            2 - Cadastro de Aeronaves
            3 - Cadastro de Empresas
            4 - Cadastro de Voos

            5 - Sair
            """
        )

        return int(input("Escolha uma opção..: "))

    def show_opmenu(self) -> int:
        system("cls")
        print(
            """
            *-* CONTROLE / CADASTRO DE {0} *-*

            1 - Cadastrar Novo
            2 - Alterar Cadastro
            3 - Excluir Cadastro
            4 - Visualiar Relatóro

            5 - Sair
            """.format(
                self.name.upper()
            )
        )

        return int(input("Escolha uma opção..: "))
