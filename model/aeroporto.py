# -*- coding: utf8 -*-

from model.base import BaseModel


class AeroportoModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()

        self.nome: str = ""
        self.pais: str = ""
        self.sigla: str = ""
        self.cidade: str = ""
        self.estado: str = ""
        self.continente: str = ""

    def get_database_name(self) -> str:
        return "aeroporto"

    def get_database_fields(self) -> list[str]:
        return ["nome", "sigla", "cidade", "estado", "pais", "continente"]
