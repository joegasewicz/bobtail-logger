class BobtailLogger(AbstractMiddleware):

    def __init__(self):
        pass

    def init(self, req: Request, res: Response, tail: Tail) -> None:
        tail(req, res)
