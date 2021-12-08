import dataclasses
import datetime as dt
from typing import Optional


@dataclasses.dataclass
class Scientist:
    full_name: str
    faculty: str
    cathedra: str
    laboratory: int
    post: str
    post_start: dt.date
    post_end: Optional[dt.date]

    @classmethod
    def empty(cls):
        return cls(
            full_name="",
            faculty="",
            cathedra="",
            laboratory=0,
            post="",
            post_start=dt.datetime.now().date(),
            post_end=None,
        )


@dataclasses.dataclass
class ScientistQuery:
    full_name: str
    faculty: str
    cathedra: str
    laboratory: str
    post: str

    @classmethod
    def empty(cls):
        return cls(
            full_name="",
            faculty="",
            cathedra="",
            laboratory="",
            post="",
        )
