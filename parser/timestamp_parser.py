from datetime import datetime


class TimestampParser:

    def __init__(self, ts):
        self.ts = ts

    def parse(self, tz):
        ts = self.ts
        d = datetime.fromtimestamp(ts, tz=tz)
        return d
