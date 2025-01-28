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
            cur.execute("SELECT urls.id AS id, urls.name AS name, MAX(url_checks.created_at) AS created_at FROM urls LEFT JOIN url_checks ON urls.id = url_checks.url_id GROUP BY urls.id ORDER BY urls.created_at DESC, urls.id DESC")
            return cur.fetchall()

    def save_url(self, url_data):
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

    def get_url_check(self, url_id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, status_code, h1, title, description, created_at FROM url_checks WHERE url_id = %s ORDER BY created_at DESC, id DESC", (url_id,))
            return cur.fetchall()

    def save_url_check(self, url_id):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO url_checks (url_id, created_at) VALUES (%s, %s)",
                (url_id, date.today())
            )
        self.conn.commit()
