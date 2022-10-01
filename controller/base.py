# -*- coding: utf8 -*-

from dao.base import BaseDao
from view.main import MainView
from model.base import BaseModel
from provider.connections.sqlite import Sqlite


class BaseControl(object):
    def __init__(self) -> None:
        self.View: MainView = MainView()
        self.Model: BaseModel = BaseModel()

    def run(self) -> None:
        while True:
            operacao = self.View.show_opmenu()
            if operacao == 5:
                break

            match operacao:
                case 1:
                    self.cadastrar()
                case 2:
                    self.alterar()
                case 3:
                    self.excluir()
                case 4:
                    self.listar()

    def cadastrar(self) -> None:
        for field in self.Model.get_database_fields():
            value: str = input("Informe o campo {0}.: ".format(field))
            if not (value.count):
                continue

            setattr(self.Model, field, value)

        if not BaseDao(Sqlite.get_new_instance()).insert(self.Model):
            print("Erro ao inserir {}".format(self.View.name))
            return

        print("{} registrada com sucesso!".format(self.View.name))
        input("")

    def alterar(self) -> None:
        Model: BaseModel = self.listar(True)
        if not Model:
            return None

        print("Informe os novos dados para atualizar o cadastro...")
        print("")

        for field in Model.get_database_fields():
            value: str = input("Informe o campo {0}.: ".format(field))
            if not (value.count):
                continue

            setattr(Model, field, value)

        if not BaseDao(Sqlite.get_new_instance()).update(Model):
            print("Erro ao inserir {}".format(self.View.name))
            return

        print("\n{} atualizada com sucesso!".format(self.View.name))
        input("")

    def excluir(self) -> None:
        Model: BaseModel = self.listar(True)
        if not Model:
            return None

        if not BaseDao(Sqlite.get_new_instance()).delete(Model):
            print("Erro ao inserir {}".format(self.View.name))
            return

        print("\n{} excluída com sucesso!".format(self.View.name))
        input("")

    def listar(self, result: bool = False) -> BaseModel:

        print("Deseja efetuar filtro na listagem dos cadatros?")
        filtrar: bool = input("(S) Sim - (N) Não ..:").upper() in ["S"]

        DB = Sqlite.get_new_instance()
        BD = BaseDao(DB)

        if filtrar:
            filtro_list: list[str] = self.Model.get_database_fields()
            filtro_list.insert(0, self.Model.get_primary_key())

            print("seleciona um campo abaixo para efetuar o filtro.")
            for k, v in enumerate(filtro_list):
                print("{0} - {1}".format(k, v))

            indice: int = int(input("Informe o índice selecionado..: "))

        cadastro_list: list[BaseModel] = (
            not filtrar
            and BD.get_all(self.Model)
            or BD.get_by_filter(self.Model, where=["true"])
        )

        if not cadastro_list:
            print("nenhuma ocorrência à ser listada.")
            input("Tecle Enter para retornar.: ")
            return None

        for k, v in enumerate(cadastro_list):
            print("{0} - {1}".format(k, v))

        if not result:
            input("\nTecle Enter para retornar.: ")
            return None

        indice: int = int(input("\nIndique o índice do cadastro para seleção..: "))
        return cadastro_list[indice]
