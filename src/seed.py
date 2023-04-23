import logging
import random

from contexttimer import Timer
from faker import Faker
from psycopg2._psycopg import connection

from src.sql import add_postings, add_accounts
from src.types import Posting, Account
from src.util import get_relative_date

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main(conn: connection, num_postings: int, num_accounts: int, num_filters: int) -> None:
    """A function for seeding the database with test data."""
    cur = conn.cursor()
    fake = Faker()

    try:
        with Timer() as t:
            postings = [Posting(name=fake.text(max_nb_chars=50), description=fake.text(max_nb_chars=200),
                                date=get_relative_date(-50, 100),
                                a=random.random() >= 0.5, b=random.randint(0, 100), c=random.uniform(0, 100)) for _ in
                        range(num_postings)]
            accounts = [Account(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email()) for _ in
                        range(num_accounts)]
        logger.debug(f"Generated {len(postings)} postings and {len(accounts)} accounts in {t.elapsed:.2f}s.")

        with Timer() as t:
            logger.debug(f"Adding {len(postings)} postings and {len(accounts)} accounts to database...")
            posting_ids = add_postings(cur, postings)
            logger.debug('Postings inserted.')
            account_ids = add_accounts(cur, accounts)
            logger.debug('Accounts inserted.')
        logger.debug(f'Done in {t.elapsed:.2f}s.')

        conn.commit()
    finally:
        cur.close()
