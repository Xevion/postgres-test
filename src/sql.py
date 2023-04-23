from typing import List

from psycopg2._psycopg import cursor as Cursor

from src.types import Account, Posting, PostingFilter


def add_account(cursor: Cursor, data: Account) -> int:
    """Adds an account to the database."""
    cursor.execute('INSERT INTO Account'
                   '(first_name, last_name, email)'
                   'VALUES (%s, %s, %s)'
                   'RETURNING id',
                   (data.first_name, data.last_name, data.email))
    return cursor.fetchone()[0]


def add_accounts(cursor: Cursor, data: List[Account]) -> List[int]:
    """Adds multiple accounts to the database."""
    cursor.executemany('INSERT INTO Account'
                       '(first_name, last_name, email)'
                       'VALUES (%s, %s, %s)'
                       'RETURNING id',
                       [(account.first_name, account.last_name, account.email) for account in data])
    return [id for (id,) in cursor.fetchall()]


def add_posting(cursor: Cursor, data: Posting) -> int:
    """Adds a posting to the database."""
    cursor.execute('INSERT INTO Posting'
                   '(name, date, description, a, b, c)'
                   'VALUES (%s, %s, %s, %s, %s, %s)'
                   'RETURNING id',
                   (data.name, data.date, data.description, data.a, data.b, data.c))
    return cursor.fetchone()[0]


def add_postings(cursor: Cursor, data: List[Posting]) -> List[int]:
    """Adds multiple postings to the database."""
    cursor.executemany('INSERT INTO Posting'
                       '(name, date, description, a, b, c)'
                       'VALUES (%s, %s, %s, %s, %s, %s)'
                       'RETURNING id',
                       [(posting.name, posting.date, posting.description, posting.a, posting.b, posting.c) for posting
                        in data])
    return [id for (id,) in cursor.fetchall()]


def add_posting_filter(cursor: Cursor, data: PostingFilter) -> int:
    """Adds a posting filter to the database."""
    b_lower, b_upper = data.b if data.b else (None, None)
    c_lower, c_upper = data.c if data.c else (None, None)
    cursor.execute('INSERT INTO PostingFilter'
                   '(creator, name, expires, a, b_lower, b_upper, c_lower, c_upper)'
                   'VALUES (%s, %s, %s, %s, %s, %s)'
                   'RETURNING id',
                   (data.creator, data.name, data.expires, data.a, b_lower, b_upper, c_lower, c_upper))
    return cursor.fetchone()[0]


def add_posting_filters(cursor: Cursor, data: List[PostingFilter]) -> List[int]:
    """Adds multiple posting filters to the database."""
    cursor.executemany('INSERT INTO PostingFilter'
                       '(creator, name, expires, a, b_lower, b_upper, c_lower, c_upper)'
                       'VALUES (%s, %s, %s, %s, %s, %s)'
                       'RETURNING id',
                       [(posting_filter.creator, posting_filter.name, posting_filter.expires, posting_filter.a,
                         posting_filter.b[0], posting_filter.b[1], posting_filter.c[0], posting_filter.c[1]) for
                        posting_filter in data])
    return [id for (id,) in cursor.fetchall()]


def get_account_ids(cur: Cursor):
    """Returns a list of all account IDs."""
    cur.execute('SELECT id FROM Account')
    return [id for (id,) in cur.fetchall()]
