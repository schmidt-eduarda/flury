# -*- coding: utf8 -*-

from model.base import BaseModel


class VooModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()

        self.origem: int = 0
        self.destino: int = 0
        self.empresa: int = 0
        self.aeronave: int = 0
        self.assentos: int = 0
        self.bagagem: float = 0
        self.natureza: str = ""
        self.datasaida: float = 0
        self.horasaida: float = 0
        self.passageiros: int = 0
        self.datachegada: float = 0
        self.horachegada: float = 0

    def get_database_name(self) -> str:
        return "voo"

    def get_database_fields(self) -> list[str]:
        return [
            "datasaida",
            "horasaida",
            "datachegada",
            "horachegada",
            "origem",
            "destino",
            "empresa",
            "aeronave",
            "assentos",
            "passageiros",
            "bagagem",
            "natureza",
        ]
