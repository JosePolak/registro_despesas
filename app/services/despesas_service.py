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

    resultado = conn.execute(
        'SELECT SUM(valor) FROM despesas'
    ).fetchone()[0]

    conn.close()
    return resultado or 0


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


def excluir_despesa(despesa_id):
    conn = get_db_connection()

    conn.execute(
        'DELETE FROM despesas WHERE id = ?',
        (despesa_id,)
    )

    conn.commit()
    conn.close()
