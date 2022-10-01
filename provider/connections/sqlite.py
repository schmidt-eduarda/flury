# -*- coding: utf8 -*-

import sqlite3
from typing import Any
from provider.patterns.singleton import SingletonSample


@SingletonSample
class Sqlite(object):
    def __init__(self) -> None:
        self.__id: int = 0
        self.__cursor: sqlite3.Cursor = None
        self.__conn: sqlite3.Connection = None

    def connect(self) -> bool:
        try:
            self.__conn = sqlite3.connect(".\\db\\flury.sqlite")
            # self.__conn = sqlite3.connect(":memory:")
            self.__cursor = self.__conn.cursor()
        except Exception as erro:
            return False
        return True

    def get_new_id(self) -> int:
        self.__id += 1
        return self.__id

    def execute(self, sql) -> bool:
        try:
            self.connect()

            self.__cursor.execute(sql)
            self.__conn.commit()
        except Exception as erro:
            return False
        return True

    def get_data(self, sql) -> list[Any]:
        try:
            self.connect()
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except Exception as erro:
            return []


class DatabaseManager(object):
    def __init__(self, conn: Sqlite) -> None:
        self.__conn: Sqlite = conn

    def manage_tables(self) -> bool:
        table_list: list[str] = [
            "create table if not exists empresa (cod integer primary key autoincrement, nome text, sigla text, nacionalidade text);",
            "create table if not exists aeronave (cod integer primary key autoincrement, modelo text, assentos integer, limite_bagagem real);",
            "create table if not exists aeroporto (cod integer primary key autoincrement, nome text, sigla text, cidade text, estado text, pais text, continente text);",
            "create table if not exists voo (cod integer primary key autoincrement, datasaida real, horasaida real, datachegada real, horachegada real, origem integer, destino integer, empresa integer, aeronave integer, assentos integer, passageiros integer, bagagem real, natureza text);",
        ]

        try:
            for script in table_list:
                self.__conn.execute(script)
        except Exception as erro:
            return False

        return True
