# -*- coding: utf8 -*-


class BaseModel(object):
    def __init__(self) -> None:
        self.cod: int = 0

    def get_primary_key(self) -> str:
        return "cod"

    def get_database_name(self) -> str:
        return "base"

    def get_database_fields(self) -> list[str]:
        return ["cod"]

    def __repr__(self) -> str:
        return "%s - %s" % (self.get_database_name(), self.__dict__)
