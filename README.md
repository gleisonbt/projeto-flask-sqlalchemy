# Projeto Exemplo - CRUD com Flask + SQLAlchemy

Este repositório apresenta um exemplo simples de CRUD completo com:

- Backend em Flask;
- SQLAlchemy como ORM;
- Model herdando de `db.Model`;
- Controllers para receber requisições HTTP;
- Services organizados por caso de uso;
- Frontend simples em HTML, CSS e JavaScript consumindo a API;
- Script SQL para criação do banco MySQL;
- Exemplo de caso de uso com Repository chamando stored procedure.

## Estrutura do projeto

```text
nome-do-projeto/
├── frontend/
└── backend/
    ├── controllers/
    ├── models/
    ├── repositories/
    ├── services/
    └── database/
        └── create_database.sql
```

## Arquitetura usada no exemplo

```text
Frontend
   ↓
Controller
   ↓
Service
   ↓
Model
   ↓
Banco de Dados
```

## Funcionalidades implementadas

CRUD de Professores:

- Cadastrar professor;
- Listar professores;
- Buscar professor por id;
- Atualizar professor;
- Excluir professor.

Caso de uso com Repository:

- Buscar professores ativos por disciplina usando `ProfessorRepository`;
- No MySQL, o Repository chama a procedure `sp_professores_por_disciplina`;
- Controller e Service não chamam procedure diretamente.

## Como executar o backend

Entre na pasta do backend:

```bash
cd backend
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

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

Crie o arquivo `.env`:

```bash
cp .env.example .env
```

Execute o backend:

```bash
python app.py
```

A API ficará disponível em:

```text
http://127.0.0.1:5000
```

## Como executar o frontend

Em outro terminal, entre na pasta do frontend:

```bash
cd frontend
```

Execute um servidor local:

```bash
python -m http.server 5500
```

Acesse:

```text
http://127.0.0.1:5500
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

## Observação para os grupos

Este projeto serve como base de estudo. No projeto do grupo, a entidade `Professor` deve ser substituída ou complementada pelas Models definidas na modelagem de domínio entregue.

Cada funcionalidade completa deve ter:

```text
Tela no frontend
+
Rota na API
+
Controller
+
Service
+
Model
+
Persistência no banco de dados
```
