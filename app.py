from flask import Flask
import sqlite3
from pathlib import Path


app = Flask(__name__)

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent

# Caminho do banco de dados
DB_PATH = BASE_DIR / 'database' / 'despesas.db'


def init_db():
    # Garante que a pasta database exista
    DB_PATH.parent.mkdir(exist_ok=True)

    # Conecta (ou cria) o banco
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS despesas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria TEXT NOT NULL
            )
        ''')

    conn.commit()
    conn.close()

# Inicializa o banco ao subir a aplicação
init_db()


# Rota principal
@app.route('/')
def home():
    return 'Projeto Registro de Despesas - base funcionando'

# Para execução local
if __name__ == '__main__':
    app.run(debug=True)
