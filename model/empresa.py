# -*- coding: utf8 -*-

from model.base import BaseModel


class EmpresaModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()

        self.nome: str = ""
        self.sigla: str = ""
        self.nacionalidade = ""

    def get_database_name(self) -> str:
        return "empresa"

    def get_database_fields(self) -> list[str]:
        return ["nome", "sigla", "nacionalidade"]
