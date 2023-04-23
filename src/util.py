import random
from datetime import datetime, timedelta


def logarithmic_randint(min: int, max: int) -> int:
    """Return a random integer between min and max, inclusive, with a logarithmic distribution."""
    # TODO: Implement
    return 0


def get_relative_date(min: int, max: int) -> datetime:
    """Return a random date between min and max days ago, inclusive."""
    return datetime.now() - timedelta(days=random.randint(min, max))
