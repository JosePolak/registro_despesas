import sqlite3
from pathlib import Path
from flask import current_app


def get_db_connection():
    db_path = Path(current_app.instance_path) / 'despesas.db'

    # garante que a pasta instance exista (evita problema no Render)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
