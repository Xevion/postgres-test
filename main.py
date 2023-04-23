from psycopg2 import connect
from src.seed import main

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    conn = connect(dbname='railway', user='postgres', password='8h9hxh5YeBwfqTCrxQQb',
                   host='containers-us-west-174.railway.app', port='7238')
    logger.info('Connected to database.')

    main(conn, 250, 1000, 500)
