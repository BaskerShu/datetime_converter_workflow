from datetime import datetime


class NowParser:

    def parse(self, tz):
        d = datetime.now(tz=tz)
        return d
