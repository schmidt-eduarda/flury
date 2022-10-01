# -*- coding: utf8 -*-

import sys

from provider.logger import Logger
from controller.main import MainControll
from provider.connections.sqlite import DatabaseManager, Sqlite


class Flury(object):
    def __init__(self, db: Sqlite) -> None:
        self.db = db

    def run(self) -> None:
        MainControll().run()
        return


if __name__ == "__main__":
    Logger.set_logger()
    DB: Sqlite = Sqlite.get_new_instance()
    DM: DatabaseManager = DatabaseManager(DB)

    if not (DB.connect() and DM.manage_tables()):
        sys.exit(0)

    Flury(DB).run()
