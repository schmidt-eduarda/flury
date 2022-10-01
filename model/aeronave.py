# -*- coding: utf8 -*-

from model.base import BaseModel


class AeronaveModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()

        self.modelo: str = ""
        self.assentos: int = 0
        self.limite_bagagem = 0

    def get_database_name(self) -> str:
        return "aeronave"

    def get_database_fields(self) -> list[str]:
        return ["modelo", "assentos", "limite_bagagem"]
