from parser.datetime_str_parser import DateTimeStrParser
from parser.now_parser import NowParser
from parser.timestamp_parser import TimestampParser


class ParserFactory(object):

    @staticmethod
    def get_correspond_parser(query_str):
        query_str = str(query_str).strip('"\' ')
        if query_str == u'now':
            parser = NowParser()
        else:
            try:
                ts = float(query_str)
                parser = TimestampParser(ts)
            except ValueError:
                dt_str = str(query_str)
                parser = DateTimeStrParser(dt_str)
        return parser
