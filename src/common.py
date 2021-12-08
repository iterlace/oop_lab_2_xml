from typing import Optional

import datetime as dt


def str2date(raw: str, fmt: str = "%Y-%m-%d") -> Optional[dt.date]:
    if not raw.strip():
        return None

    date = dt.datetime.strptime(raw, fmt).date()
    return date
