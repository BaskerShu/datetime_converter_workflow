from dateutil import parser


class DateTimeStrParser:

    def __init__(self, dt_str):
        self.dt_str = dt_str

    def parse(self, tz):
        dt_str = self.dt_str
        d = parser.parse(dt_str).replace(tzinfo=tz)
        return d
