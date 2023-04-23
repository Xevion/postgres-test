from psycopg2._psycopg import cursor

from types import Account, Posting, PostingFilter


def add_account(cursor: cursor, data: Account) -> int:
    """Adds an account to the database."""
    cursor.execute('INSERT INTO Account'
                   '(first_name, last_name, email)'
                   'VALUES (%s, %s, %s)'
                   'RETURNING id',
                   (data.first_name, data.last_name, data.email))
    return cursor.fetchone()[0]


def add_posting(cursor: cursor, data: Posting) -> int:
    """Adds a posting to the database."""
    cursor.execute('INSERT INTO Posting'
                   '(name, date, description, a, b, c)'
                   'VALUES (%s, %s, %s, %s, %s, %s)'
                   'RETURNING id',
                   (data.name, data.date, data.description, data.a, data.b, data.c))
    return cursor.fetchone()[0]


def add_posting_filter(cursor: cursor, data: PostingFilter) -> int:
    """Adds a posting filter to the database."""
    b_lower, b_upper = data.b if data.b else (None, None)
    c_lower, c_upper = data.c if data.c else (None, None)
    cursor.execute('INSERT INTO PostingFilter'
                   '(creator, name, expires, a, b_lower, b_upper, c_lower, c_upper)'
                   'VALUES (%s, %s, %s, %s, %s, %s)'
                   'RETURNING id',
                   (data.creator, data.name, data.expires, data.a, b_lower, b_upper, c_lower, c_upper))
    return cursor.fetchone()[0]
