# 📒 Registro de Despesas

Aplicação web desenvolvida em Flask para registro e visualização de despesas pessoais, com persistência em SQLite e deploy em produção no Render.

🔗 **Aplicação online:**  
https://registro-despesas-md0c.onrender.com

---

## ✨ Funcionalidades

- Cadastro de despesas (data, descrição, valor e categoria)
- Listagem das despesas cadastradas
- Cálculo automático do total de despesas
- Interface responsiva (desktop e mobile)
- Persistência de dados com SQLite
- Deploy em produção com Gunicorn e Render

---

## 🛠️ Stack utilizada

- Python
- Flask
- SQLite
- HTML (Jinja2)
- Gunicorn
- Render
- GitHub

---

## 📁 Estrutura do projeto

registro_despesas/

├── app.py

├── requirements.txt

├── .gitignore

├── database/

      └── despesas.db
    
└── templates/

      ├── base.html
    
      ├── index.html
    
      └── nova.html

> O banco de dados é criado automaticamente em runtime, caso não exista.

---

## ▶️ Como rodar o projeto localmente

1️⃣ Clone o repositório:

git clone https://github.com/seu-usuario/registro_despesas.git  
cd registro_despesas

2️⃣ Crie e ative o ambiente virtual:

python -m venv venv  

Windows:  
venv\Scripts\activate  

Linux / macOS:  
source venv/bin/activate  

3️⃣ Instale as dependências:

pip install -r requirements.txt

4️⃣ Execute a aplicação:

python app.py

A aplicação estará disponível em:  
http://127.0.0.1:5000

---

## ☁️ Deploy

O projeto está publicado em produção no **Render**, utilizando **Gunicorn** como servidor WSGI.

🔗 **URL pública:**  
https://registro-despesas-md0c.onrender.com

O deploy é realizado automaticamente a cada `git push` na branch `main`.

---

## ⚠️ Observação importante

Este projeto é um **MVP educacional**, desenvolvido com o objetivo de demonstrar:

- Estruturação de aplicações Flask
- Persistência de dados com SQLite
- Criação de rotas e formulários
- Deploy em ambiente de produção

A aplicação **não possui autenticação de usuários**, portanto os dados são públicos e podem ser alterados por qualquer visitante.

A implementação de autenticação, APIs e melhorias estruturais faz parte da evolução planejada do projeto.

---

## 🚀 Próximos passos planejados

- Refatoração da aplicação utilizando Flask Blueprints
- Migração do acesso ao banco para SQLAlchemy
- Criação de API REST
- Implementação de autenticação de usuários
- Controle de permissões e segurança

---

## 👨‍💻 Autor

Projeto desenvolvido por **José Polak**  
Como parte do processo de transição e formação em desenvolvimento backend com Python.
