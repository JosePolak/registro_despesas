from app.db import get_db_connection


def listar_despesas():
    conn = get_db_connection()

    despesas = conn.execute(
        'SELECT * FROM despesas ORDER BY data DESC'
    ).fetchall()

    conn.close()
    return despesas


def calcular_total():
    conn = get_db_connection()

    total = conn.execute(
        'SELECT SUM(valor) FROM despesas'
    ).fetchone()[0]

    conn.close()
    return total


def inserir_despesa(data, descricao, valor, categoria):
    conn = get_db_connection()

    conn.execute(
        '''
        INSERT INTO despesas (data, descricao, valor, categoria)
        VALUES (?, ?, ?, ?)
        ''',
        (data, descricao, valor, categoria)
    )

    conn.commit()
    conn.close()
