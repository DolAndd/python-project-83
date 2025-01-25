from psycopg2.extras import RealDictCursor
from datetime import date


class UrlRepository:
    def __init__(self, conn):
        self.conn = conn

    def find_id(self, id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM urls WHERE id = %s", (id,))
            return cur.fetchone()

    def get_content(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM urls ORDER BY created_at DESC, id DESC")
            return cur.fetchall()

    def save(self, url_data):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO urls (name, created_at) VALUES (%s, %s) RETURNING id",
                (url_data, date.today())
            )
            id = cur.fetchone()[0]
        self.conn.commit()
        return id

    def find_name(self, name):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM urls WHERE name = %s", (name,))
            return cur.fetchone()
