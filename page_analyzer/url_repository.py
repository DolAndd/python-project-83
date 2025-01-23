import psycopg2
from psycopg2.extras import RealDictCursor


class UrlRepository:
    def __init__(self, conn):
        self.conn = conn

