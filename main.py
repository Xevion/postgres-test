from psycopg2 import connect
from src.seed import main

if __name__ == '__main__':
    conn = connect(dbname='railway', user='postgres', password='8h9hxh5YeBwfqTCrxQQb',
                   host='containers-us-west-174.railway.app', port='7238')

    main(conn)
