# Backend - API Flask + SQLAlchemy

API de exemplo para demonstrar CRUD usando Flask, SQLAlchemy, Controllers, Services e Models.

## Como executar

Entre na pasta do backend:

```bash
cd backend
```

Crie e ative o ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie o arquivo `.env` com base no exemplo:

```bash
cp .env.example .env
```

Execute a API:

```bash
python app.py
```

A API ficará disponível em:

```text
http://127.0.0.1:5000
```

## Banco de dados

Por padrão, o projeto usa SQLite para facilitar o teste local:

```text
DATABASE_URL=sqlite:///escola.db
```

Para usar MySQL, execute o script:

```text
backend/database/create_database.sql
```

Depois altere o `.env` para:

```text
DATABASE_URL=mysql+pymysql://root:sua_senha@localhost:3306/escola_db
```

## Rotas da API

| Método | Rota | Descrição |
|---|---|---|
| GET | `/professores` | Lista todos os professores |
| GET | `/professores/<id>` | Busca um professor pelo id |
| GET | `/professores/por-disciplina?disciplina=Banco de Dados` | Busca professores ativos por disciplina usando Repository |
| POST | `/professores` | Cadastra um professor |
| PUT | `/professores/<id>` | Atualiza um professor |
| DELETE | `/professores/<id>` | Remove um professor |

## Caso de uso com Repository

Este projeto também possui um exemplo de consulta que não é CRUD básico:

```text
buscar_professores_por_disciplina
```

Fluxo do caso de uso:

```text
Controller -> Service -> Repository -> CALL sp_professores_por_disciplina -> MySQL
```

Rota:

```text
GET /professores/por-disciplina?disciplina=Banco de Dados
```

No MySQL, a procedure está no arquivo:

```text
backend/database/create_database.sql
```

Para facilitar testes locais com SQLite, o Repository possui uma consulta equivalente usando SQLAlchemy.

## Exemplo de JSON para cadastrar

```json
{
  "nome": "Ana Silva",
  "email": "ana@escola.com",
  "disciplina": "Banco de Dados"
}
```
