import re
from datetime import datetime, timedelta


class NowParser:
    regex_pattern = r'^now([-+])(\d+)$'

    def __init__(self, query_str):
        self.query_str = query_str

    def parse(self, tz):
        query_str = self.query_str
        dt_now = datetime.now(tz=tz)
        re_match = re.match(self.regex_pattern, query_str)
        if re_match:
            operator, num = re_match.groups()
            days_num = int(num)
            if operator == '-':
                dt = dt_now - timedelta(days=days_num)
                return dt
            elif operator == '+':
                dt = dt_now + timedelta(days=days_num)
                return dt
        else:
            return dt_now
