# -*- coding: utf8 -*-

from copy import copy
from typing import Any
from model.base import BaseModel
from provider.connections.sqlite import Sqlite


class BaseDao(object):
    def __init__(self, conn: Sqlite) -> None:
        self.__conn: Sqlite = conn

    def insert(self, objeto: BaseModel) -> Any:
        setattr(objeto, objeto.get_primary_key(), self.__conn.get_new_id())

        sql: list[str] = [
            "insert into {1} ({0}, {2}) values ".format(
                objeto.get_primary_key(),
                objeto.get_database_name(),
                ", ".join(objeto.get_database_fields()),
            )
        ]

        fieldlist: list[str] = [str(getattr(objeto, objeto.get_primary_key()))]
        for field in objeto.get_database_fields():
            if type(getattr(objeto, field)) is str:
                fieldlist.append("'{0}'".format(getattr(objeto, field)))
                continue

            fieldlist.append(str(getattr(objeto, field)))

        sql.append("({0});".format(", ".join(fieldlist)))
        self.__conn.execute("".join(sql))
        return objeto

    def update(self, objeto: BaseModel):
        sql: list[str] = ["update {0} set ".format(objeto.get_database_name())]

        fieldlist: list[str] = []
        for field in objeto.get_database_fields():
            if type(getattr(objeto, field)) is str:
                fieldlist.append(
                    "{0} = '{1}'".format(field, str(getattr(objeto, field)))
                )
                continue

            fieldlist.append("{0} = {1}".format(field, str(getattr(objeto, field))))

        sql.append(", ".join(fieldlist))

        sql.append(
            " where {0} = {1};".format(
                objeto.get_primary_key(), getattr(objeto, objeto.get_primary_key())
            )
        )
        self.__conn.execute("".join(sql))
        return objeto

    def delete(self, objeto: BaseModel):
        sql = "delete from {0} where {1} = {2}".format(
            objeto.get_database_name(),
            objeto.get_primary_key(),
            getattr(objeto, objeto.get_primary_key()),
        )

        self.__conn.execute(sql)
        return objeto

    def get_all(self, objeto: BaseModel) -> list[BaseModel]:
        return self.get_by_filter(objeto, ["true"])

    def get_by_id(self, objeto: BaseModel, cod: int) -> BaseModel:
        return self.get_by_filter(
            objeto, ["{0} = {1}".format(objeto.get_primary_key(), cod)]
        )[0]

    def get_by_filter(self, objeto: BaseModel, where: list[str]) -> list[BaseModel]:
        sql = "select {2}, {0} from {1} where {3} order by {2};".format(
            ", ".join(objeto.get_database_fields()),
            objeto.get_database_name(),
            objeto.get_primary_key(),
            " ".join(where),
        )

        objeto_list: list[Any] = self.__conn.get_data(sql)

        fieldlist: list[str] = [objeto.get_primary_key()]
        fieldlist.extend(objeto.get_database_fields())
        result_list: list[BaseModel] = []

        for obj in objeto_list:
            objcopy = copy(objeto)
            for index, field in enumerate(fieldlist):
                setattr(objcopy, field, obj[index])

            result_list.append(objcopy)

        return result_list
