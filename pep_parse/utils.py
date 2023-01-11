import datetime as dt

from .settings import DT_FORMAT

now = dt.datetime.now()
now_formatted = now.strftime(DT_FORMAT)