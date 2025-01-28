CREATE TABLE IF NOT EXISTS urls (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS url_checks (
    id SERIAL PRIMARY KEY,
    url_id integer NOT NULL,
    status_code integer,
    h1 TEXT,
    title TEXT,
    description TEXT,
    created_at DATE NOT NULL
);
