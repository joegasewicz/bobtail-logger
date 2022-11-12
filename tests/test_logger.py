from bobtail_logger import BobtailLogger, Colors
from bobtail.request import Request
from bobtail.response import Response


class TestBobtailLogger:

    def test_run(self, caplog):
        req = Request("/", "GET")
        res = Response()
        b = BobtailLogger()
        b.run(req, res, lambda rq, rs: None)
        logs = caplog.messages[0].split(" ")
        assert len(logs[0]) > 0
        assert len(logs[1]) > 0
        assert logs[2] == "GET"
        assert logs[3] == "/"
        assert logs[4] == "200"

    def test_run_set_color(self, caplog):
        req = Request("/hello", "POST")
        res = Response()
        b = BobtailLogger(colors={"color": Colors.RED})
        b.run(req, res, lambda rq, rs: None)
        logs = caplog.messages[0].split(" ")
        assert len(logs[0]) > 0
        assert len(logs[1]) > 0
        assert logs[2] == "POST"
        assert logs[3] == "/hello"
        assert logs[4] == "200"
