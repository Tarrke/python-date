#!/usr/bin/env python3

"""A simple script to get the baby age"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

birthdate = datetime(2017, 12, 31)
now = datetime.now()

delta = now - birthdate

print("Baby is", delta.days, "days old.")

delta = relativedelta(now, birthdate)

print("Baby is", delta.months + delta.years*12, "months and", delta.days, "days old.")