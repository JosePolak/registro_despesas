from flask import Flask, request, redirect, url_for
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


# Conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# Rota principal
@app.route('/')
def home():
    conn = get_db_connection()
    despesas = conn.execute('SELECT * FROM despesas ORDER BY data DESC').fetchall()
    conn.close()

    return str(despesas)


@app.route('/nova', methods=['GET', 'POST'])
def nova_despesa():
    if request.method == 'POST':
        data = request.form['data']
        descricao = request.form['descricao']
        valor = request.form['valor']
        categoria = request.form['categoria']
    
        # Validação simples
        if not data or not descricao or not valor or not categoria:
            return 'Todos os campos são obrigatórios'
        
        try:
            valor = float(valor)
        except ValueError:
            return 'Valor inválido.'
        
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO despesas (data, descricao, valor, categoria) VALUES (?, ?, ?, ?)', 
            (data, descricao, valor, categoria)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('home'))
    
    # GET
    return '''
        <h2>Nova Despesa</h2>
        <form method="post">
            Data: <input type="date" name="data"><br><br>
            Descrição: <input type="text" name="descricao"><br><br>
            Valor: <input type="text" name="valor"><br><br>
            Categoria: <input type="text" name="categoria"><br><br>
            <button type="submit">Salvar</button>
        </form>
    '''


# Para execução local
if __name__ == '__main__':
    app.run(debug=True)
