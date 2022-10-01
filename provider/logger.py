# -*- coding: utf-8 -*-

import time
import logging
from typing import Callable
from datetime import datetime


class Logger(object):
    @classmethod
    def set_logger(cls):
        logging.basicConfig(
            encoding="utf-8",
            level=logging.DEBUG,
            datefmt="%d/%m/%Y %H:%M:%S",
            format="%(asctime)s:%(levelname)-8s:%(message)s",
            filename=".\\log\\flury_{}.log".format(datetime.now().strftime("%d_%m_%Y")),
        )

    @classmethod
    def trackmyfunctiontime(cls, funcao: Callable):
        def wrapper():
            logging.debug(
                "[{}] function starts at {}".format(
                    funcao.__name__, str(time.asctime())
                )
            )

            initime = time.time()
            funcao()

            logging.debug(
                "[{}] Tempo total de execução: {}".format(
                    funcao.__name__, str(time.time() - initime)
                )
            )

        return wrapper

    @classmethod
    def sampleloglevels(cls):
        logging.info("omg omg omg omg omg omg info")
        logging.error("omg omg omg omg omg omg error")
        logging.debug("omg omg omg omg omg omg debug")
        logging.warning("omg omg omg omg omg omg warning")
        logging.critical("omg omg omg omg omg omg critical")
