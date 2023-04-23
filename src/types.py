from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Tuple


@dataclass
class Posting:
    name: str
    date: datetime
    description: str

    a: bool
    b: int
    c: float


@dataclass
class PostingFilter:
    creator: int
    name: str
    expires: datetime

    a: Optional[bool]
    b: Optional[Tuple[int, int]]
    c: Optional[Tuple[float, float]]


@dataclass
class Account:
    first_name: str
    last_name: str
    email: str
