# encoding: utf-8

import os
import sys
from collections import namedtuple

from dateutil import tz
import time
from parser.factory import ParserFactory
from workflow import Workflow, ICON_CLOCK

# 获取时区
tz_str = os.environ.get('ALFRED_TZ')
tz = tz.gettz(tz_str) if tz_str else tz.tzlocal()


def process(wf):
    """ 主入口 """
    try:
        query_str = wf.args[0]  # 需要查询的时间参数
    except IndexError:
        query_str = 'now'
    dt = parse_query_str(query_str)
    if dt:
        datetime_items = serialize_datetime(dt)
        for item in datetime_items:
            wf.add_item(title=item.title,
                        subtitle=item.subtitle,
                        arg=item.arg,
                        valid=True,
                        icon=ICON_CLOCK)
    wf.send_feedback()


def parse_query_str(query_str):
    try:
        query_str_parser = ParserFactory.get_correspond_parser(query_str)
        dt = query_str_parser.parse(tz)
    except ValueError:
        dt = None
    return dt


def serialize_datetime(dt):
    Item = namedtuple(u'Item', u'title subtitle arg')
    date_ = dt.date()

    # 当前时间（时间戳和具体时间）
    datetime_timestamp, datetime_str = _get_timestamp_and_strftime(dt)
    date_timestamp, date_str = _get_timestamp_and_strftime(date_)
    datetime_items = [
        Item(title=datetime_timestamp, subtitle='datetime timestamp', arg=datetime_timestamp),
        Item(title=datetime_str, subtitle='datetime', arg=datetime_str),
        Item(title=date_timestamp, subtitle='date timestamp', arg=date_timestamp),
        Item(title=date_str, subtitle='date', arg=date_str),
    ]

    return datetime_items


def _get_timestamp_and_strftime(dt):
    format_ = "%Y-%m-%d %H:%M:%S"
    timestamp = str(int(time.mktime(dt.timetuple())))
    datetime_str = dt.strftime(format_)
    return timestamp, datetime_str


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(process))
