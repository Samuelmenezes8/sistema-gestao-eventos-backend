# Sistema de Gestão de Eventos (Backend)

## Descrição do Projeto
Este repositório contém o backend de um sistema de gestão de eventos, construído com Django e Django REST Framework. O projeto foi desenvolvido para um portfólio pessoal com o objetivo de demonstrar habilidades em programação full stack.

O backend é responsável por gerir a lógica de negócio, o armazenamento de dados e a comunicação com a aplicação frontend.

## Funcionalidades
* **CRUD de Eventos:** Funcionalidades completas para criar, ler, atualizar e apagar eventos.
* **API RESTful:** Comunicação eficiente com a aplicação frontend através de uma API.

## Tecnologias Utilizadas
* **Python 3.11:** Linguagem de programação.
* **Django:** Framework web para o backend.
* **Django REST Framework:** Para a criação da API.
* **SQLite:** Banco de dados padrão do Django.

## Como Executar o Projeto
1.  **Clona o Repositório:**
    ```bash
    git clone [https://github.com/samuelmenezes8/sistema-gestao-eventos-backend.git](https://github.com/samuelmenezes8/sistema-gestao-eventos-backend.git)
    cd sistema-gestao-eventos-backend
    ```
2.  **Cria e Ativa o Ambiente Virtual:**
    * No Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
3.  **Instala as Dependências:**
    ```bash
    pip install django djangorestframework django-cors-headers
    ```
4.  **Faz as Migrações:**
    ```bash
    python manage.py makemigrations eventos
    python manage.py migrate
    ```
5.  **Inicia o Servidor:**
    ```bash
    python manage.py runserver
    ```
    A API estará disponível em `http://127.0.0.1:8000/api/eventos/`.

---

Depois de guardares o ficheiro `README.md`, envia-o para o GitHub.

```bash
git add README.md
git commit -m "docs: adiciona README.md para o backend"
git push origin main
