from flask import Blueprint, request, redirect, url_for, render_template
from app.services.despesas_service import (listar_despesas, calcular_total, inserir_despesa, excluir_despesa, buscar_despesa_por_id, atualizar_despesa)


main = Blueprint('main', __name__)


@main.route('/')
def home():
    despesas = listar_despesas()

    total = calcular_total()

    return render_template(
        'index.html',
        despesas = despesas,
        total = total
    )


@main.route('/nova', methods=['GET', 'POST'])
def nova_despesa():
    if request.method == 'POST':
        data = request.form['data']
        descricao = request.form['descricao']
        valor = request.form['valor']
        categoria = request.form['categoria']

        if not data or not descricao or not valor or not categoria:
            return 'Todos os campos são obrigatórios.'
        
        try:
            valor = float(valor)
        except ValueError:
            return 'Valor inválido.'
        
        inserir_despesa(data, descricao, valor, categoria)

        return redirect(url_for('main.home'))
    
    return render_template('nova.html')


@main.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_despesa(id):
    despesa = buscar_despesa_por_id(id)

    if despesa is None:
        return 'Despesa não encontrada.', 404
    
    if request.method == 'POST':
        data = request.form['data']
        descricao = request.form['descricao']
        valor = request.form['valor']
        categoria = request.form['categoria']

        if not data or not descricao or not valor or not categoria:
            return 'Todos os campos são obrigatórios.'
        
        try:
            valor = float(valor)
        except ValueError:
            return 'Valor inválido.'
        
        atualizar_despesa(id, data, descricao, valor, categoria)

        return redirect(url_for('main.home'))
    
    return render_template(
        'editar.html',
        despesa = despesa
    )


@main.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    excluir_despesa(id)
    return redirect(url_for('main.home'))
