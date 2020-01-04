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
    datetime_items = []
    Item = namedtuple(u'Item', u'title subtitle arg')

    # first item
    item_value = str(int(time.mktime(dt.timetuple())))
    first_item = Item(title=item_value, subtitle='UTC Timestamp', arg=item_value)
    datetime_items.append(first_item)

    # Various formats
    formats = [
        # 1937-01-01 12:00:27
        ("%Y-%m-%d %H:%M:%S", ''),
        # 19 May 2002 15:21:36
        ("%d %b %Y %H:%M:%S", ''),
        # Sun, 19 May 2002 15:21:36
        ("%a, %d %b %Y %H:%M:%S", ''),
        # 1937-01-01T12:00:27
        ("%Y-%m-%dT%H:%M:%S", ''),
        # 1996-12-19T16:39:57-0800
        ("%Y-%m-%dT%H:%M:%S%z", ''),
    ]
    for format_, description in formats:
        item_value = dt.strftime(format_)
        item = Item(title=item_value, subtitle=description, arg=item_value)
        datetime_items.append(item)

    return datetime_items


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(process))
