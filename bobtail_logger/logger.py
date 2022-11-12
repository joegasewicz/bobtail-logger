"""
Quick Start
===========
Installation::
    pip install bobtail-logger
Basic Usage::
    from bobtail_logger import BobtailLogger
    app = Bobtail(routes=routes)
    app.use(BobtailLogger())


"""
import logging
from datetime import datetime
from typing import Dict
from enum import Enum

from bobtail import AbstractMiddleware, Request, Response, Tail


class Colors(Enum):
    """
    You can use Colors enum to reference an ANSI  color code
    """
    RESET = "\033[0m"  # Black
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    YELLOW = "\033[93m"
    PINK = "\033[95m"
    CYAN = "\033[36m"
    PURPLE = "\033[35m"


class BobtailLogger(AbstractMiddleware):
    """
    BobtailLogger
    :kwargs:
    :key options: You can set the color oof the logs with the `color` key.
         For example::

            b = BobtailLogger(colors={"color": Colors.RED})

         Errors will always be displayed in `Color.RED`
    """

    _options: Dict = {
        "color": Colors.BLUE.value,
    }

    def __init__(self, **kwargs):
        try:
            self._options = {
                **self._options,
                **kwargs["options"],
            }
        except KeyError:
            pass

    def _color_suffix(self):
        return Colors.RESET.value

    def _color_prefix(self, color_code: str):
        return color_code

    def _get_req_datetime(self) -> str:
        d = datetime.now()
        date_time = f"{d.strftime('%d-%m-%y %H:%M:%S')}"
        return date_time

    def _display_color_unless_err(self, status: int):
        if status >= 400:
            return Colors.RED
        return self._color_prefix(self._options['color'])

    def run(self, req: Request, res: Response, tail: Tail) -> None:
        dt = self._get_req_datetime()
        method = req.method
        path = req.path
        status = res.status
        logging.getLogger("BobtailLogger")
        logging.basicConfig(
            format=f"{self._display_color_unless_err(status)}%(message)s {self._color_suffix()}",
            level=logging.INFO,
        )
        msg = f"[{dt}] {method} {path} {status}"
        logging.info(msg)
        tail(req, res)
